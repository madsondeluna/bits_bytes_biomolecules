#!/usr/bin/env python3
"""
API REST para Sistema de Autenticação
Endpoints para login, registro, validação de token e gestão de usuários
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from auth_system import auth_manager, token_required, role_required
from email_service import email_service

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir requisições de diferentes origens


@app.route('/', methods=['GET'])
def index():
    """Endpoint raiz com informações da API"""
    return jsonify({
        "message": "API de Autenticação via Token JWT",
        "version": "1.0.0",
        "endpoints": {
            "POST /api/login": "Fazer login e obter token",
            "POST /api/register": "Registrar novo usuário",
            "GET /api/verify": "Verificar validade do token",
            "GET /api/profile": "Obter perfil do usuário (requer token)",
            "POST /api/change-password": "Alterar senha (requer token)",
            "GET /api/users": "Listar todos os usuários (requer admin)",
            "DELETE /api/users/<username>": "Deletar usuário (requer admin)",
            "GET /api/protected": "Rota protegida de exemplo (requer token)"
        }
    }), 200


@app.route('/api/login', methods=['POST'])
def login():
    """
    Endpoint de login

    Request Body:
        {
            "username": "string",
            "password": "string"
        }

    Response:
        {
            "message": "Login bem-sucedido",
            "token": "jwt_token_string",
            "user": {
                "username": "string",
                "role": "string",
                "email": "string"
            }
        }
    """
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"message": "Username e password são obrigatórios"}), 400

    username = data['username']
    password = data['password']

    # Autenticar usuário
    token = auth_manager.authenticate(username, password)

    if not token:
        return jsonify({"message": "Credenciais inválidas"}), 401

    # Obter informações do usuário
    user = auth_manager.get_user(username)

    return jsonify({
        "message": "Login bem-sucedido",
        "token": token,
        "user": user.to_dict()
    }), 200


@app.route('/api/register', methods=['POST'])
def register():
    """
    Endpoint de registro de novo usuário

    Request Body:
        {
            "username": "string",
            "password": "string",
            "email": "string",
            "role": "string" (opcional, padrão: "user")
        }

    Response:
        {
            "message": "Usuário criado com sucesso",
            "user": {
                "username": "string",
                "role": "string",
                "email": "string"
            }
        }
    """
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"message": "Username e password são obrigatórios"}), 400

    username = data['username']
    password = data['password']
    email = data.get('email', '')
    role = data.get('role', 'user')

    # Criar usuário
    success = auth_manager.create_user(username, password, role, email)

    if not success:
        return jsonify({"message": "Usuário já existe"}), 409

    user = auth_manager.get_user(username)

    # Enviar notificação por email para o admin
    try:
        email_service.send_registration_notification_to_admin(username, email, role)
    except Exception as e:
        print(f"[ERRO] Falha ao enviar email de notificação: {e}")

    # Enviar email de boas-vindas para o novo usuário (opcional)
    if email:
        try:
            email_service.send_welcome_email(username, email)
        except Exception as e:
            print(f"[ERRO] Falha ao enviar email de boas-vindas: {e}")

    return jsonify({
        "message": "Usuário criado com sucesso",
        "user": user.to_dict()
    }), 201


@app.route('/api/verify', methods=['GET'])
def verify_token():
    """
    Endpoint para verificar validade do token

    Headers:
        Authorization: Bearer <token>

    Response:
        {
            "valid": true,
            "user": {
                "username": "string",
                "role": "string"
            }
        }
    """
    token = None

    if 'Authorization' in request.headers:
        auth_header = request.headers['Authorization']
        try:
            token = auth_header.split(" ")[1]
        except IndexError:
            return jsonify({"valid": False, "message": "Token format inválido"}), 400

    if not token:
        return jsonify({"valid": False, "message": "Token ausente"}), 400

    payload = auth_manager.verify_token(token)

    if not payload:
        return jsonify({"valid": False, "message": "Token inválido ou expirado"}), 401

    return jsonify({
        "valid": True,
        "user": {
            "username": payload['username'],
            "role": payload['role']
        }
    }), 200


@app.route('/api/profile', methods=['GET'])
@token_required
def get_profile(current_user):
    """
    Endpoint para obter perfil do usuário autenticado

    Headers:
        Authorization: Bearer <token>

    Response:
        {
            "user": {
                "username": "string",
                "role": "string",
                "email": "string",
                "created_at": "string",
                "last_login": "string"
            }
        }
    """
    user = auth_manager.get_user(current_user['username'])

    if not user:
        return jsonify({"message": "Usuário não encontrado"}), 404

    return jsonify({"user": user.to_dict()}), 200


@app.route('/api/change-password', methods=['POST'])
@token_required
def change_password(current_user):
    """
    Endpoint para alterar senha do usuário autenticado

    Headers:
        Authorization: Bearer <token>

    Request Body:
        {
            "old_password": "string",
            "new_password": "string"
        }

    Response:
        {
            "message": "Senha alterada com sucesso"
        }
    """
    data = request.get_json()

    if not data or not data.get('old_password') or not data.get('new_password'):
        return jsonify({"message": "old_password e new_password são obrigatórios"}), 400

    old_password = data['old_password']
    new_password = data['new_password']
    username = current_user['username']

    success = auth_manager.change_password(username, old_password, new_password)

    if not success:
        return jsonify({"message": "Senha antiga incorreta"}), 401

    return jsonify({"message": "Senha alterada com sucesso"}), 200


@app.route('/api/users', methods=['GET'])
@token_required
@role_required('admin')
def list_users(current_user):
    """
    Endpoint para listar todos os usuários (apenas admin)

    Headers:
        Authorization: Bearer <token>

    Response:
        {
            "users": [
                {
                    "username": "string",
                    "role": "string",
                    "email": "string",
                    "created_at": "string",
                    "last_login": "string"
                }
            ]
        }
    """
    users = auth_manager.list_users()
    return jsonify({"users": users}), 200


@app.route('/api/users/<username>', methods=['DELETE'])
@token_required
@role_required('admin')
def delete_user(current_user, username):
    """
    Endpoint para deletar um usuário (apenas admin)

    Headers:
        Authorization: Bearer <token>

    Response:
        {
            "message": "Usuário deletado com sucesso"
        }
    """
    # Não permitir deletar a si mesmo
    if username == current_user['username']:
        return jsonify({"message": "Você não pode deletar sua própria conta"}), 403

    success = auth_manager.delete_user(username)

    if not success:
        return jsonify({"message": "Usuário não encontrado"}), 404

    return jsonify({"message": "Usuário deletado com sucesso"}), 200


@app.route('/api/protected', methods=['GET'])
@token_required
def protected_route(current_user):
    """
    Exemplo de rota protegida que requer autenticação

    Headers:
        Authorization: Bearer <token>

    Response:
        {
            "message": "Acesso autorizado",
            "user": "string"
        }
    """
    return jsonify({
        "message": "Acesso autorizado à rota protegida!",
        "user": current_user['username'],
        "role": current_user['role']
    }), 200


@app.route('/api/admin-only', methods=['GET'])
@token_required
@role_required('admin')
def admin_only_route(current_user):
    """
    Exemplo de rota que requer papel de admin

    Headers:
        Authorization: Bearer <token>

    Response:
        {
            "message": "Acesso admin autorizado",
            "user": "string"
        }
    """
    return jsonify({
        "message": "Bem-vindo à área administrativa!",
        "user": current_user['username']
    }), 200


@app.errorhandler(404)
def not_found(error):
    """Handler para rotas não encontradas"""
    return jsonify({"message": "Endpoint não encontrado"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handler para erros internos"""
    return jsonify({"message": "Erro interno do servidor"}), 500


if __name__ == '__main__':
    print("=" * 80)
    print("API de Autenticação via Token JWT")
    print("=" * 80)
    print("\nUsuários padrão disponíveis:")
    print("  - admin / admin123 (admin)")
    print("  - user / user123 (user)")
    print("  - researcher / research123 (researcher)")
    print("\nServidor rodando em: http://localhost:5000")
    print("Documentação: http://localhost:5000")
    print("=" * 80)
    print("\nPressione CTRL+C para parar o servidor\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
