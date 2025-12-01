# Sistema de Autenticação do Website

Este documento explica como funciona o sistema de autenticação integrado entre o website (GitHub Pages) e a API de autenticação.

## Arquitetura

```
┌─────────────────────────┐
│   GitHub Pages          │
│  (Frontend Estático)    │
│                         │
│  - cadastro.html        │
│  - login.html           │
│  - dashboard.html       │
│  - exercises.html       │
└───────────┬─────────────┘
            │
            │ HTTP/HTTPS
            │ (Fetch API)
            ▼
┌─────────────────────────┐
│   API Flask             │
│  (Backend Dinâmico)     │
│                         │
│  - /api/register        │
│  - /api/login           │
│  - /api/verify          │
│  - /api/profile         │
└─────────────────────────┘
```

## Páginas Criadas

### 1. Página de Cadastro (`cadastro.html`)

**URL:** https://madsondeluna.github.io/bits_bytes_biomolecules/cadastro.html

**Funcionalidades:**
- Formulário de cadastro de novo usuário
- Validação de senha em tempo real (força da senha)
- Verificação de senhas coincidentes
- Envio de dados para API `/api/register`
- Redirecionamento automático para login após cadastro bem-sucedido

**Campos:**
- Nome de usuário (obrigatório, mínimo 3 caracteres)
- Email (obrigatório)
- Senha (obrigatório, mínimo 6 caracteres)
- Confirmação de senha (obrigatório)
- Tipo de usuário (seleção: usuário, pesquisador, estudante)

### 2. Página de Login (`login.html`)

**URL:** https://madsondeluna.github.io/bits_bytes_biomolecules/login.html

**Funcionalidades:**
- Formulário de login
- Opção "Lembrar-me" (salva username localmente)
- Integração com API `/api/login`
- Armazenamento de token JWT no localStorage
- Redirecionamento para dashboard após login bem-sucedido

### 3. Dashboard (`dashboard.html`)

**URL:** https://madsondeluna.github.io/bits_bytes_biomolecules/dashboard.html

**Funcionalidades:**
- Verificação automática de autenticação (requer token válido)
- Exibição de informações do usuário
- Cards de acesso rápido:
  - Exercícios práticos
  - Tutorial de tradução
  - Perfil do usuário
- Botão de logout
- Avatar com inicial do nome do usuário

**Proteção:**
- Se não houver token válido, redireciona para `login.html`

### 4. Página de Exercícios Atualizada (`exercises.html`)

**URL:** https://madsondeluna.github.io/bits_bytes_biomolecules/exercises.html

**Modificações:**
- Substituiu autenticação hardcoded por autenticação via API
- Login através de overlay modal
- Verificação de token JWT ao carregar a página
- Link para criar conta
- Botão de logout

## Fluxo de Autenticação

### Fluxo de Cadastro

```
1. Usuário acessa cadastro.html
   ↓
2. Preenche formulário
   ↓
3. Frontend valida dados (senha forte, emails coincidentes, etc)
   ↓
4. Frontend envia POST /api/register
   ↓
5. API cria usuário e envia emails:
   - Email para admin (madsondeluna@gmail.com) com notificação
   - Email para usuário com boas-vindas
   ↓
6. Usuário é redirecionado para login.html
```

### Fluxo de Login

```
1. Usuário acessa login.html ou exercises.html
   ↓
2. Insere credenciais
   ↓
3. Frontend envia POST /api/login
   ↓
4. API valida credenciais e retorna:
   {
     "token": "jwt_token_aqui",
     "user": {
       "username": "...",
       "role": "...",
       "email": "..."
     }
   }
   ↓
5. Frontend salva token e dados do usuário:
   - sessionStorage.setItem('authToken', token)
   - sessionStorage.setItem('user', JSON.stringify(user))
   ↓
6. Usuário acessa conteúdo protegido
```

### Verificação de Token

```
Quando página protegida carrega:
   ↓
1. Verifica se há token no sessionStorage
   ↓
2. Se há token, envia GET /api/verify
   Headers: { Authorization: "Bearer <token>" }
   ↓
3. API valida token
   ↓
4. Se válido: mostra conteúdo
   Se inválido: redireciona para login
```

## Configuração da API

### Para Desenvolvimento Local

1. **Iniciar a API:**
```bash
cd auth/
python api.py
```

A API rodará em `http://localhost:5000`

2. **Configurar CORS:**

A API já está configurada com CORS habilitado para aceitar requisições do GitHub Pages.

### Para Produção

1. **Hospedar a API em um servidor:**

Opções populares:
- **Heroku:** https://www.heroku.com
- **Railway:** https://railway.app
- **Render:** https://render.com
- **PythonAnywhere:** https://www.pythonanywhere.com
- **AWS EC2 / DigitalOcean / etc**

2. **Atualizar URL da API nas páginas:**

Nos arquivos:
- `cadastro.html`
- `login.html`
- `exercises.html`

Altere:
```javascript
const API_URL = 'http://localhost:5000';
```

Para:
```javascript
const API_URL = 'https://sua-api.herokuapp.com';
```

3. **Configurar HTTPS:**

**IMPORTANTE:** O GitHub Pages usa HTTPS. Sua API também deve usar HTTPS para evitar erros de mixed content.

## Exemplo de Deploy no Heroku

### Passo 1: Criar arquivos necessários

**Procfile:**
```
web: gunicorn --chdir auth api:app
```

**requirements.txt** (já existe em `auth/requirements.txt`)
```
Flask==3.0.0
PyJWT==2.8.0
Flask-CORS==4.0.0
gunicorn==21.2.0
```

**runtime.txt:**
```
python-3.11.0
```

### Passo 2: Deploy

```bash
# Login no Heroku
heroku login

# Criar app
heroku create sua-api-biomoleculas

# Configurar variáveis de ambiente
heroku config:set EMAIL_ENABLED=true
heroku config:set SMTP_USERNAME=madsondeluna@gmail.com
heroku config:set SMTP_PASSWORD=sua_senha_de_app
heroku config:set ADMIN_EMAIL=madsondeluna@gmail.com

# Deploy
git add .
git commit -m "Add auth API"
git push heroku main
```

### Passo 3: Testar

```bash
# Testar API
curl https://sua-api-biomoleculas.herokuapp.com/

# Atualizar URL nos arquivos HTML
# E fazer commit no GitHub
```

## Segurança

### Tokens JWT

- **Expiração:** Tokens expiram em 24 horas
- **Armazenamento:** Tokens são armazenados no `sessionStorage` (mais seguro que localStorage)
- **Validação:** Cada requisição protegida valida o token

### HTTPS

- GitHub Pages: HTTPS automático
- API: Deve usar HTTPS em produção

### CORS

- API configurada para aceitar requisições do domínio do GitHub Pages
- Em produção, configure CORS para aceitar apenas seu domínio

### Senhas

- Nunca armazenadas em plain text
- Hash SHA-256 (para produção, usar bcrypt)

## Testando Localmente

### 1. Iniciar API

```bash
cd auth/
python api.py
```

### 2. Servir Website Localmente

```bash
cd docs/
python -m http.server 8000
```

### 3. Acessar

- Website: http://localhost:8000
- API: http://localhost:5000

### 4. Testar Fluxo Completo

1. Acesse http://localhost:8000/cadastro.html
2. Crie uma conta
3. Verifique o console da API para ver a notificação de cadastro
4. Faça login em http://localhost:8000/login.html
5. Acesse o dashboard
6. Tente acessar os exercícios

## Solução de Problemas

### Erro: CORS

**Sintoma:** Console mostra erro de CORS

**Solução:**
- Certifique-se de que a API está rodando
- Verifique se Flask-CORS está instalado
- Em `api.py`, certifique-se de que `CORS(app)` está configurado

### Erro: "Failed to fetch"

**Sintoma:** Não consegue conectar à API

**Soluções:**
1. Verifique se a API está rodando
2. Verifique a URL da API nos arquivos HTML
3. Abra o console do navegador para ver erro detalhado

### Token Expirado

**Sintoma:** Usuário é deslogado automaticamente

**Solução:** Normal, tokens expiram em 24h. Usuário deve fazer login novamente.

### Email não chega

**Sintoma:** Não recebe email após cadastro

**Soluções:**
1. Verifique `EMAIL_ENABLED=true` no `.env`
2. Verifique credenciais SMTP
3. Verifique pasta de spam
4. Veja console da API para mensagens de erro

## Próximos Passos

### Melhorias Sugeridas

1. **Recuperação de Senha:**
   - Adicionar endpoint `/api/forgot-password`
   - Enviar email com link de recuperação

2. **Verificação de Email:**
   - Enviar email de confirmação após cadastro
   - Só ativar conta após verificação

3. **Perfil do Usuário:**
   - Página para editar informações
   - Upload de foto de perfil

4. **Histórico de Progresso:**
   - Salvar progresso nos exercícios
   - Estatísticas de uso

5. **Refresh Tokens:**
   - Implementar refresh tokens para não forçar re-login após 24h

6. **2FA:**
   - Autenticação de dois fatores

## Usuários de Teste

**⚠️ MODO DESENVOLVIMENTO APENAS**

Para testar rapidamente em ambiente de desenvolvimento, configure a variável de ambiente:

```bash
export CREATE_DEFAULT_USERS=true
```

Isso criará os seguintes usuários de teste:

| Username   | Password     | Role       |
|------------|--------------|------------|
| admin      | admin123     | admin      |
| user       | user123      | user       |
| researcher | research123  | researcher |

**🔒 IMPORTANTE PARA PRODUÇÃO:**
- Por padrão, esses usuários **NÃO** são criados (modo seguro)
- NUNCA configure `CREATE_DEFAULT_USERS=true` em produção
- Em produção, crie usuários apenas através do endpoint `/api/register`

## Suporte

Para dúvidas ou problemas:
- Consulte o [README.md](auth/README.md) da API
- Consulte o [EMAIL_SETUP.md](auth/EMAIL_SETUP.md) para configuração de email
- Abra uma issue no GitHub

---

**Autor:** Madson Aragão @ UFMG
**Data:** Dezembro 2025
