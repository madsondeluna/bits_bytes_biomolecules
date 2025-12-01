#!/usr/bin/env python3
"""
Sistema de Autenticação via Token JWT
Implementação de login e validação de usuários usando tokens JWT
"""

import jwt
import datetime
import hashlib
import secrets
from typing import Optional, Dict, Any
from functools import wraps
from flask import Flask, request, jsonify

# Configurações
SECRET_KEY = secrets.token_hex(32)  # Chave secreta para assinar tokens
TOKEN_EXPIRATION_HOURS = 24  # Tempo de expiração do token em horas
ALGORITHM = "HS256"  # Algoritmo de criptografia


class User:
    """Classe para representar um usuário"""

    def __init__(self, username: str, password_hash: str, role: str = "user", email: str = ""):
        self.username = username
        self.password_hash = password_hash
        self.role = role
        self.email = email
        self.created_at = datetime.datetime.utcnow()
        self.last_login = None

    def to_dict(self) -> Dict[str, Any]:
        """Converte o usuário para dicionário (sem a senha)"""
        return {
            "username": self.username,
            "role": self.role,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "last_login": self.last_login.isoformat() if self.last_login else None
        }


class AuthManager:
    """Gerenciador de autenticação e tokens"""

    def __init__(self, secret_key: str = SECRET_KEY):
        self.secret_key = secret_key
        # Base de dados simulada (em produção, use um banco de dados real)
        self.users: Dict[str, User] = {}

        # Criar alguns usuários de exemplo
        self._create_default_users()

    def _create_default_users(self):
        """Cria usuários padrão para demonstração"""
        # Usuário admin
        self.create_user("admin", "admin123", "admin", "admin@example.com")
        # Usuário comum
        self.create_user("user", "user123", "user", "user@example.com")
        # Usuário pesquisador
        self.create_user("researcher", "research123", "researcher", "researcher@example.com")

    @staticmethod
    def hash_password(password: str) -> str:
        """Cria um hash da senha usando SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()

    def create_user(self, username: str, password: str, role: str = "user", email: str = "") -> bool:
        """
        Cria um novo usuário

        Args:
            username: Nome de usuário
            password: Senha em texto plano
            role: Papel do usuário (user, admin, researcher, etc.)
            email: Email do usuário

        Returns:
            True se o usuário foi criado com sucesso, False caso contrário
        """
        if username in self.users:
            return False

        password_hash = self.hash_password(password)
        self.users[username] = User(username, password_hash, role, email)
        return True

    def authenticate(self, username: str, password: str) -> Optional[str]:
        """
        Autentica um usuário e retorna um token JWT

        Args:
            username: Nome de usuário
            password: Senha em texto plano

        Returns:
            Token JWT se a autenticação for bem-sucedida, None caso contrário
        """
        user = self.users.get(username)

        if not user:
            return None

        password_hash = self.hash_password(password)

        if password_hash != user.password_hash:
            return None

        # Atualizar último login
        user.last_login = datetime.datetime.utcnow()

        # Gerar token JWT
        token = self.generate_token(username, user.role)
        return token

    def generate_token(self, username: str, role: str) -> str:
        """
        Gera um token JWT para o usuário

        Args:
            username: Nome de usuário
            role: Papel do usuário

        Returns:
            Token JWT assinado
        """
        payload = {
            "username": username,
            "role": role,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRATION_HOURS),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, self.secret_key, algorithm=ALGORITHM)
        return token

    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """
        Verifica e decodifica um token JWT

        Args:
            token: Token JWT a ser verificado

        Returns:
            Payload do token se for válido, None caso contrário
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[ALGORITHM])
            return payload
        except jwt.ExpiredSignatureError:
            return None  # Token expirado
        except jwt.InvalidTokenError:
            return None  # Token inválido

    def get_user(self, username: str) -> Optional[User]:
        """Retorna informações do usuário"""
        return self.users.get(username)

    def change_password(self, username: str, old_password: str, new_password: str) -> bool:
        """
        Altera a senha de um usuário

        Args:
            username: Nome de usuário
            old_password: Senha antiga
            new_password: Nova senha

        Returns:
            True se a senha foi alterada com sucesso, False caso contrário
        """
        user = self.users.get(username)

        if not user:
            return False

        old_password_hash = self.hash_password(old_password)

        if old_password_hash != user.password_hash:
            return False

        user.password_hash = self.hash_password(new_password)
        return True

    def delete_user(self, username: str) -> bool:
        """Remove um usuário"""
        if username in self.users:
            del self.users[username]
            return True
        return False

    def list_users(self) -> list:
        """Lista todos os usuários (sem senhas)"""
        return [user.to_dict() for user in self.users.values()]


# Instância global do gerenciador de autenticação
auth_manager = AuthManager()


def token_required(f):
    """
    Decorator para proteger rotas que requerem autenticação

    Uso:
        @app.route('/protected')
        @token_required
        def protected_route(current_user):
            return f"Hello {current_user['username']}"
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # O token pode vir no header Authorization
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]  # Format: "Bearer <token>"
            except IndexError:
                return jsonify({"message": "Token format inválido"}), 401

        # Ou pode vir como parâmetro
        if not token and 'token' in request.args:
            token = request.args.get('token')

        if not token:
            return jsonify({"message": "Token ausente"}), 401

        # Verificar o token
        payload = auth_manager.verify_token(token)

        if not payload:
            return jsonify({"message": "Token inválido ou expirado"}), 401

        return f(payload, *args, **kwargs)

    return decorated


def role_required(required_role: str):
    """
    Decorator para proteger rotas que requerem um papel específico

    Uso:
        @app.route('/admin')
        @token_required
        @role_required('admin')
        def admin_route(current_user):
            return "Admin only"
    """
    def decorator(f):
        @wraps(f)
        def decorated(current_user, *args, **kwargs):
            if current_user.get('role') != required_role:
                return jsonify({"message": f"Acesso negado. Papel '{required_role}' necessário"}), 403
            return f(current_user, *args, **kwargs)
        return decorated
    return decorator


if __name__ == "__main__":
    # Demonstração do sistema de autenticação
    print("=== Sistema de Autenticação via Token JWT ===\n")

    # Listar usuários padrão
    print("Usuários disponíveis:")
    for user in auth_manager.list_users():
        print(f"  - {user['username']} ({user['role']})")

    print("\n--- Teste de Autenticação ---")

    # Tentar login com credenciais corretas
    print("\n1. Login com credenciais corretas:")
    token = auth_manager.authenticate("admin", "admin123")
    if token:
        print(f"   ✓ Login bem-sucedido!")
        print(f"   Token: {token[:50]}...")

        # Verificar token
        print("\n2. Verificando token:")
        payload = auth_manager.verify_token(token)
        if payload:
            print(f"   ✓ Token válido!")
            print(f"   Usuário: {payload['username']}")
            print(f"   Papel: {payload['role']}")
            print(f"   Expira em: {datetime.datetime.fromtimestamp(payload['exp'])}")
    else:
        print("   ✗ Login falhou")

    # Tentar login com credenciais incorretas
    print("\n3. Login com credenciais incorretas:")
    token = auth_manager.authenticate("admin", "senha_errada")
    if token:
        print("   ✓ Login bem-sucedido!")
    else:
        print("   ✗ Login falhou (esperado)")

    # Criar novo usuário
    print("\n4. Criando novo usuário:")
    success = auth_manager.create_user("testuser", "test123", "user", "test@example.com")
    if success:
        print("   ✓ Usuário criado com sucesso!")
        token = auth_manager.authenticate("testuser", "test123")
        if token:
            print(f"   ✓ Login com novo usuário bem-sucedido!")

    # Alterar senha
    print("\n5. Alterando senha:")
    success = auth_manager.change_password("testuser", "test123", "newpass123")
    if success:
        print("   ✓ Senha alterada com sucesso!")
        token = auth_manager.authenticate("testuser", "newpass123")
        if token:
            print("   ✓ Login com nova senha bem-sucedido!")

    print("\n=== Demonstração concluída ===")
