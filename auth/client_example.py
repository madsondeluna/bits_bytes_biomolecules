#!/usr/bin/env python3
"""
Exemplo de Cliente para API de Autenticação
Demonstra como fazer requisições para a API de autenticação
"""

import requests
import json

# URL base da API
BASE_URL = "http://localhost:5000"


class AuthClient:
    """Cliente para interagir com a API de autenticação"""

    def __init__(self, base_url: str = BASE_URL):
        self.base_url = base_url
        self.token = None
        self.user = None

    def login(self, username: str, password: str) -> bool:
        """
        Faz login na API

        Args:
            username: Nome de usuário
            password: Senha

        Returns:
            True se o login foi bem-sucedido, False caso contrário
        """
        url = f"{self.base_url}/api/login"
        payload = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 200:
                data = response.json()
                self.token = data['token']
                self.user = data['user']
                print(f"✓ Login bem-sucedido como {username}")
                print(f"  Token: {self.token[:50]}...")
                return True
            else:
                print(f"✗ Login falhou: {response.json().get('message', 'Erro desconhecido')}")
                return False

        except requests.exceptions.RequestException as e:
            print(f"✗ Erro de conexão: {e}")
            return False

    def register(self, username: str, password: str, email: str = "", role: str = "user") -> bool:
        """
        Registra um novo usuário

        Args:
            username: Nome de usuário
            password: Senha
            email: Email (opcional)
            role: Papel do usuário (opcional)

        Returns:
            True se o registro foi bem-sucedido, False caso contrário
        """
        url = f"{self.base_url}/api/register"
        payload = {
            "username": username,
            "password": password,
            "email": email,
            "role": role
        }

        try:
            response = requests.post(url, json=payload)

            if response.status_code == 201:
                data = response.json()
                print(f"✓ Usuário {username} criado com sucesso")
                return True
            else:
                print(f"✗ Registro falhou: {response.json().get('message', 'Erro desconhecido')}")
                return False

        except requests.exceptions.RequestException as e:
            print(f"✗ Erro de conexão: {e}")
            return False

    def verify_token(self) -> bool:
        """
        Verifica se o token atual é válido

        Returns:
            True se o token é válido, False caso contrário
        """
        if not self.token:
            print("✗ Nenhum token disponível")
            return False

        url = f"{self.base_url}/api/verify"
        headers = {"Authorization": f"Bearer {self.token}"}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                print(f"✓ Token válido para usuário {data['user']['username']}")
                return True
            else:
                print(f"✗ Token inválido: {response.json().get('message', 'Erro desconhecido')}")
                return False

        except requests.exceptions.RequestException as e:
            print(f"✗ Erro de conexão: {e}")
            return False

    def get_profile(self) -> dict:
        """
        Obtém o perfil do usuário autenticado

        Returns:
            Dicionário com os dados do usuário ou None em caso de erro
        """
        if not self.token:
            print("✗ Você precisa fazer login primeiro")
            return None

        url = f"{self.base_url}/api/profile"
        headers = {"Authorization": f"Bearer {self.token}"}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                print("✓ Perfil obtido com sucesso:")
                print(json.dumps(data['user'], indent=2))
                return data['user']
            else:
                print(f"✗ Erro ao obter perfil: {response.json().get('message', 'Erro desconhecido')}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"✗ Erro de conexão: {e}")
            return None

    def change_password(self, old_password: str, new_password: str) -> bool:
        """
        Altera a senha do usuário autenticado

        Args:
            old_password: Senha antiga
            new_password: Nova senha

        Returns:
            True se a senha foi alterada com sucesso, False caso contrário
        """
        if not self.token:
            print("✗ Você precisa fazer login primeiro")
            return False

        url = f"{self.base_url}/api/change-password"
        headers = {"Authorization": f"Bearer {self.token}"}
        payload = {
            "old_password": old_password,
            "new_password": new_password
        }

        try:
            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                print("✓ Senha alterada com sucesso")
                return True
            else:
                print(f"✗ Erro ao alterar senha: {response.json().get('message', 'Erro desconhecido')}")
                return False

        except requests.exceptions.RequestException as e:
            print(f"✗ Erro de conexão: {e}")
            return False

    def access_protected_route(self) -> bool:
        """
        Acessa uma rota protegida

        Returns:
            True se o acesso foi bem-sucedido, False caso contrário
        """
        if not self.token:
            print("✗ Você precisa fazer login primeiro")
            return False

        url = f"{self.base_url}/api/protected"
        headers = {"Authorization": f"Bearer {self.token}"}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                print(f"✓ {data['message']}")
                return True
            else:
                print(f"✗ Acesso negado: {response.json().get('message', 'Erro desconhecido')}")
                return False

        except requests.exceptions.RequestException as e:
            print(f"✗ Erro de conexão: {e}")
            return False

    def list_users(self) -> list:
        """
        Lista todos os usuários (requer permissão de admin)

        Returns:
            Lista de usuários ou None em caso de erro
        """
        if not self.token:
            print("✗ Você precisa fazer login primeiro")
            return None

        url = f"{self.base_url}/api/users"
        headers = {"Authorization": f"Bearer {self.token}"}

        try:
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                print(f"✓ Lista de usuários ({len(data['users'])} usuários):")
                for user in data['users']:
                    print(f"  - {user['username']} ({user['role']})")
                return data['users']
            else:
                print(f"✗ Erro ao listar usuários: {response.json().get('message', 'Erro desconhecido')}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"✗ Erro de conexão: {e}")
            return None


def main():
    """Demonstração do cliente de autenticação"""
    print("=" * 80)
    print("Cliente de Autenticação - Exemplo de Uso")
    print("=" * 80)

    client = AuthClient()

    # Teste 1: Login com usuário comum
    print("\n--- Teste 1: Login com usuário comum ---")
    if client.login("user", "user123"):
        client.verify_token()
        client.get_profile()
        client.access_protected_route()

    # Teste 2: Registrar novo usuário
    print("\n--- Teste 2: Registrar novo usuário ---")
    client.register("newuser", "newpass123", "newuser@example.com", "user")

    # Teste 3: Login com novo usuário
    print("\n--- Teste 3: Login com novo usuário ---")
    if client.login("newuser", "newpass123"):
        client.get_profile()

    # Teste 4: Alterar senha
    print("\n--- Teste 4: Alterar senha ---")
    if client.change_password("newpass123", "supersecret456"):
        # Fazer login com nova senha
        print("\nFazendo login com nova senha...")
        client.login("newuser", "supersecret456")

    # Teste 5: Login como admin
    print("\n--- Teste 5: Login como admin ---")
    if client.login("admin", "admin123"):
        client.list_users()

    # Teste 6: Tentar login com credenciais inválidas
    print("\n--- Teste 6: Login com credenciais inválidas ---")
    client.login("user", "senha_errada")

    # Teste 7: Tentar acessar rota protegida sem token
    print("\n--- Teste 7: Acessar rota protegida sem token ---")
    client2 = AuthClient()
    client2.access_protected_route()

    print("\n" + "=" * 80)
    print("Demonstração concluída!")
    print("=" * 80)


if __name__ == "__main__":
    main()
