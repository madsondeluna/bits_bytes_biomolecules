#!/usr/bin/env python3
"""
Sistema de Autenticação via Token JWT
Implementação de login e validação de usuários usando tokens JWT
"""

import jwt
import datetime
import secrets
import bcrypt
from typing import Optional, Dict, Any, List
from functools import wraps
from flask import Flask, request, jsonify

# Configurações
SECRET_KEY = secrets.token_hex(32)  # Chave secreta para assinar tokens
TOKEN_EXPIRATION_HOURS = 24  # Tempo de expiração do token em horas
ALGORITHM = "HS256"  # Algoritmo de criptografia


class PasswordResetToken:
    """Classe para representar um token de redefinição de senha"""

    def __init__(self, username: str, token: str, expires_at: datetime.datetime):
        self.username = username
        self.token_hash = bcrypt.hashpw(token.encode(), bcrypt.gensalt()).decode()
        self.expires_at = expires_at
        self.used = False

    def is_valid(self, token: str) -> bool:
        """Verifica se o token é válido"""
        if self.used:
            return False
        if datetime.datetime.utcnow() > self.expires_at:
            return False
        return bcrypt.checkpw(token.encode(), self.token_hash.encode())

    def mark_as_used(self):
        """Marca o token como usado"""
        self.used = True


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
        # Armazenamento de tokens de redefinição de senha
        self.reset_tokens: Dict[str, PasswordResetToken] = {}

        # Criar alguns usuários de exemplo APENAS se variável de ambiente permitir
        import os
        if os.getenv('CREATE_DEFAULT_USERS', 'false').lower() == 'true':
            self._create_default_users()

    def _create_default_users(self):
        """Cria usuários padrão para demonstração - APENAS PARA DESENVOLVIMENTO"""
        # Usuário admin
        self.create_user("admin", "admin123", "admin", "admin@example.com")
        # Usuário comum
        self.create_user("user", "user123", "user", "user@example.com")
        # Usuário pesquisador
        self.create_user("researcher", "research123", "researcher", "researcher@example.com")

    @staticmethod
    def hash_password(password: str) -> str:
        """Cria um hash da senha usando bcrypt (seguro para senhas)"""
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        """Verifica se a senha corresponde ao hash"""
        return bcrypt.checkpw(password.encode(), password_hash.encode())

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

        if not self.verify_password(password, user.password_hash):
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

        if not self.verify_password(old_password, user.password_hash):
            return False

        user.password_hash = self.hash_password(new_password)
        return True

    def create_password_reset_token(self, username: str) -> Optional[str]:
        """
        Cria um token de redefinição de senha

        Args:
            username: Nome de usuário

        Returns:
            Token de redefinição se o usuário existir, None caso contrário
        """
        user = self.users.get(username)

        if not user:
            return None

        # Gerar token criptograficamente seguro
        token = secrets.token_urlsafe(32)

        # Token expira em 30 minutos
        expires_at = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

        # Armazenar token
        self.reset_tokens[username] = PasswordResetToken(username, token, expires_at)

        return token

    def reset_password_with_token(self, username: str, token: str, new_password: str) -> bool:
        """
        Redefine a senha usando um token de redefinição

        Args:
            username: Nome de usuário
            token: Token de redefinição
            new_password: Nova senha

        Returns:
            True se a senha foi redefinida com sucesso, False caso contrário
        """
        user = self.users.get(username)

        if not user:
            return False

        reset_token = self.reset_tokens.get(username)

        if not reset_token:
            return False

        if not reset_token.is_valid(token):
            return False

        # Redefinir senha
        user.password_hash = self.hash_password(new_password)

        # Marcar token como usado
        reset_token.mark_as_used()

        return True

    def cleanup_expired_tokens(self):
        """Remove tokens de redefinição expirados"""
        now = datetime.datetime.utcnow()
        expired = [
            username for username, token in self.reset_tokens.items()
            if token.expires_at < now or token.used
        ]
        for username in expired:
            del self.reset_tokens[username]

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
