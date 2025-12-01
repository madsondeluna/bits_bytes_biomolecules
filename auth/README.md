# Sistema de Autenticação via Token JWT

Sistema completo de autenticação baseado em tokens JWT (JSON Web Tokens) para aplicações Python/Flask.

## Características

- Autenticação via token JWT
- Registro e gestão de usuários
- Diferentes níveis de acesso (roles)
- Proteção de rotas com decorators
- Alteração de senha
- Validação de tokens
- API RESTful completa
- Exemplos de uso incluídos
- **Notificações por email** (novo usuário cadastrado)

## Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

## Instalação

1. **Clone ou navegue até o diretório:**
```bash
cd auth/
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **(Opcional) Configure notificações por email:**

Veja [EMAIL_SETUP.md](EMAIL_SETUP.md) para instruções detalhadas.

Resumo rápido:
```bash
# Copiar arquivo de configuração
cp .env.example .env

# Editar .env com suas credenciais SMTP
# EMAIL_ENABLED=true
# SMTP_USERNAME=seu_email@gmail.com
# SMTP_PASSWORD=sua_senha_de_app
# ADMIN_EMAIL=admin@example.com
```

## Uso Rápido

### 1. Iniciar o Servidor da API

```bash
python api.py
```

O servidor estará rodando em `http://localhost:5000`

### 2. Usar o Cliente de Exemplo

Em outro terminal:

```bash
python client_example.py
```

### 3. Testar Diretamente

```bash
python auth_system.py
```

## Estrutura do Projeto

```
auth/
├── auth_system.py      # Sistema de autenticação e gerenciamento de usuários
├── api.py              # API REST Flask com endpoints
├── email_service.py    # Serviço de notificação por email
├── client_example.py   # Exemplos de uso do cliente
├── test_api.sh         # Script de testes da API
├── requirements.txt    # Dependências do projeto
├── .env.example        # Exemplo de configuração de variáveis de ambiente
├── EMAIL_SETUP.md      # Guia de configuração de email
└── README.md           # Esta documentação
```

## Usuários Padrão

O sistema vem com três usuários pré-configurados:

| Username   | Password     | Role       |
|------------|--------------|------------|
| admin      | admin123     | admin      |
| user       | user123      | user       |
| researcher | research123  | researcher |

**IMPORTANTE:** Altere essas credenciais em produção!

## API Endpoints

### Autenticação

#### POST `/api/login`
Faz login e obtém um token JWT.

**Request:**
```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response (200 OK):**
```json
{
  "message": "Login bem-sucedido",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "username": "admin",
    "role": "admin",
    "email": "admin@example.com",
    "created_at": "2025-12-01T10:30:00",
    "last_login": "2025-12-01T15:45:00"
  }
}
```

#### POST `/api/register`
Registra um novo usuário.

**Request:**
```json
{
  "username": "newuser",
  "password": "securepass123",
  "email": "newuser@example.com",
  "role": "user"
}
```

**Response (201 Created):**
```json
{
  "message": "Usuário criado com sucesso",
  "user": {
    "username": "newuser",
    "role": "user",
    "email": "newuser@example.com"
  }
}
```

#### GET `/api/verify`
Verifica se um token é válido.

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "valid": true,
  "user": {
    "username": "admin",
    "role": "admin"
  }
}
```

### Rotas Protegidas (Requerem Token)

#### GET `/api/profile`
Obtém o perfil do usuário autenticado.

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "user": {
    "username": "admin",
    "role": "admin",
    "email": "admin@example.com",
    "created_at": "2025-12-01T10:30:00",
    "last_login": "2025-12-01T15:45:00"
  }
}
```

#### POST `/api/change-password`
Altera a senha do usuário autenticado.

**Headers:**
```
Authorization: Bearer <token>
```

**Request:**
```json
{
  "old_password": "oldpass123",
  "new_password": "newpass456"
}
```

**Response (200 OK):**
```json
{
  "message": "Senha alterada com sucesso"
}
```

#### GET `/api/protected`
Rota de exemplo que requer autenticação.

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "message": "Acesso autorizado à rota protegida!",
  "user": "admin",
  "role": "admin"
}
```

### Rotas Admin (Requerem Token + Role Admin)

#### GET `/api/users`
Lista todos os usuários (apenas admin).

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "users": [
    {
      "username": "admin",
      "role": "admin",
      "email": "admin@example.com",
      "created_at": "2025-12-01T10:30:00",
      "last_login": "2025-12-01T15:45:00"
    },
    {
      "username": "user",
      "role": "user",
      "email": "user@example.com",
      "created_at": "2025-12-01T11:00:00",
      "last_login": null
    }
  ]
}
```

#### DELETE `/api/users/<username>`
Deleta um usuário (apenas admin).

**Headers:**
```
Authorization: Bearer <token>
```

**Response (200 OK):**
```json
{
  "message": "Usuário deletado com sucesso"
}
```

## Exemplos de Código

### Exemplo 1: Login Básico

```python
import requests

# Fazer login
response = requests.post('http://localhost:5000/api/login', json={
    'username': 'admin',
    'password': 'admin123'
})

data = response.json()
token = data['token']
print(f"Token: {token}")
```

### Exemplo 2: Acessar Rota Protegida

```python
import requests

token = "seu_token_aqui"

# Acessar rota protegida
response = requests.get(
    'http://localhost:5000/api/profile',
    headers={'Authorization': f'Bearer {token}'}
)

print(response.json())
```

### Exemplo 3: Registrar Novo Usuário

```python
import requests

# Registrar novo usuário
response = requests.post('http://localhost:5000/api/register', json={
    'username': 'newuser',
    'password': 'securepass123',
    'email': 'newuser@example.com',
    'role': 'user'
})

print(response.json())
```

### Exemplo 4: Criar Rota Protegida Customizada

```python
from flask import Flask
from auth_system import token_required, role_required

app = Flask(__name__)

@app.route('/api/my-protected-route')
@token_required
def my_protected_route(current_user):
    return {
        "message": f"Olá {current_user['username']}!",
        "data": "Dados sensíveis aqui"
    }

@app.route('/api/admin-only-route')
@token_required
@role_required('admin')
def admin_only_route(current_user):
    return {
        "message": "Área administrativa",
        "admin": current_user['username']
    }
```

## Segurança

### Boas Práticas Implementadas

1. **Hash de Senhas**: Senhas são armazenadas usando SHA-256
2. **Tokens JWT**: Autenticação stateless com tokens assinados
3. **Expiração de Tokens**: Tokens expiram após 24 horas
4. **Validação de Entrada**: Validação de dados em todos os endpoints
5. **CORS**: Configurado para permitir requisições cross-origin
6. **Separação de Roles**: Diferentes níveis de acesso

### Recomendações para Produção

**ATENÇÃO**: Este é um exemplo educacional. Para produção:

1. **Use um banco de dados real** (PostgreSQL, MySQL, MongoDB)
2. **Use bcrypt ou argon2** para hash de senhas (não SHA-256)
3. **Armazene SECRET_KEY em variáveis de ambiente**
4. **Implemente rate limiting** para prevenir ataques de força bruta
5. **Use HTTPS** em produção
6. **Adicione logs de auditoria**
7. **Implemente refresh tokens**
8. **Configure CORS adequadamente** (não use `*` em produção)
9. **Adicione validação de força de senha**
10. **Implemente 2FA (autenticação de dois fatores)**

## Testes com cURL

### Login
```bash
curl -X POST http://localhost:5000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'
```

### Verificar Token
```bash
curl -X GET http://localhost:5000/api/verify \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

### Obter Perfil
```bash
curl -X GET http://localhost:5000/api/profile \
  -H "Authorization: Bearer SEU_TOKEN_AQUI"
```

### Listar Usuários (Admin)
```bash
curl -X GET http://localhost:5000/api/users \
  -H "Authorization: Bearer TOKEN_DO_ADMIN"
```

## Configuração Avançada

### Alterar Tempo de Expiração do Token

Em [auth_system.py](auth_system.py:13):
```python
TOKEN_EXPIRATION_HOURS = 24  # Altere para o valor desejado
```

### Alterar Chave Secreta

Em [auth_system.py](auth_system.py:12):
```python
SECRET_KEY = "sua_chave_secreta_aqui"
```

**Melhor prática**: Use variáveis de ambiente:
```python
import os
SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'fallback_key')
```

### Adicionar Novos Roles

```python
# Criar usuário com role personalizada
auth_manager.create_user("scientist", "pass123", "scientist", "sci@example.com")

# Proteger rota com role personalizada
@app.route('/api/science-data')
@token_required
@role_required('scientist')
def science_data(current_user):
    return {"data": "Dados científicos"}
```

## Troubleshooting

### Erro: "Token inválido ou expirado"
- Verifique se o token não expirou (24h por padrão)
- Certifique-se de incluir "Bearer " antes do token no header

### Erro: "ModuleNotFoundError: No module named 'jwt'"
- Instale as dependências: `pip install -r requirements.txt`

### Erro: "Address already in use"
- Outra aplicação está usando a porta 5000
- Altere a porta em `api.py`: `app.run(port=5001)`

### Erro de CORS
- Certifique-se de que flask-cors está instalado
- Verifique a configuração de CORS em `api.py`

## Diagrama de Fluxo

```
┌─────────────┐
│   Cliente   │
└──────┬──────┘
       │
       │ 1. POST /api/login
       │    {username, password}
       ▼
┌─────────────┐
│  API Flask  │
└──────┬──────┘
       │
       │ 2. Validar credenciais
       ▼
┌─────────────┐
│ AuthManager │
└──────┬──────┘
       │
       │ 3. Gerar token JWT
       │
       ▼
┌─────────────┐
│   Cliente   │ ◄── Token JWT
└──────┬──────┘
       │
       │ 4. GET /api/protected
       │    Header: Authorization: Bearer <token>
       ▼
┌─────────────┐
│  API Flask  │
└──────┬──────┘
       │
       │ 5. Verificar token
       ▼
┌─────────────┐
│ AuthManager │ ◄── Token válido?
└──────┬──────┘
       │
       │ 6. Retornar dados protegidos
       ▼
┌─────────────┐
│   Cliente   │ ◄── Dados
└─────────────┘
```

## Contribuindo

Sinta-se livre para contribuir com melhorias:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto é fornecido como exemplo educacional. Use por sua conta e risco.

## Autor

Criado por Madson Aragão @ UFMG

## Suporte

Para dúvidas ou problemas, abra uma issue no repositório.

---

**Se este projeto foi útil, considere dar uma estrela!**
