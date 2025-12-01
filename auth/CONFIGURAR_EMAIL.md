# Como Configurar seu Email para Receber Notificações

Olá Madson! Este guia vai te ajudar a configurar o sistema para receber emails quando novos usuários se cadastrarem.

## Passo 1: Gerar Senha de App do Gmail

1. **Acesse a página de segurança do Google:**
   - Vá para: https://myaccount.google.com/security

2. **Habilitar Autenticação de Dois Fatores** (se ainda não estiver habilitada):
   - Clique em "Verificação em duas etapas"
   - Siga as instruções para habilitar

3. **Gerar uma Senha de App:**
   - Vá para: https://myaccount.google.com/apppasswords
   - Ou procure por "Senhas de app" na página de segurança
   - Selecione "Email" como app
   - Selecione "Outro" como dispositivo
   - Digite: "Sistema de Autenticação"
   - Clique em "Gerar"
   - **Copie a senha de 16 caracteres** que aparecer (será algo como: xxxx xxxx xxxx xxxx)

## Passo 2: Configurar o arquivo .env

O arquivo `.env` já foi criado com seu email. Você só precisa adicionar a senha de app:

1. Abra o arquivo `.env` no diretório `auth/`

2. Localize a linha:
   ```
   SMTP_PASSWORD=COLOQUE_SUA_SENHA_DE_APP_AQUI
   ```

3. Substitua por:
   ```
   SMTP_PASSWORD=xxxx xxxx xxxx xxxx
   ```
   (cole a senha de 16 caracteres que você copiou)

4. Habilite o envio de emails mudando:
   ```
   EMAIL_ENABLED=false
   ```
   Para:
   ```
   EMAIL_ENABLED=true
   ```

5. Salve o arquivo

## Passo 3: Testar a Configuração

### Teste 1: Testar o serviço de email

```bash
cd auth/
python email_service.py
```

Você deverá ver mensagens de log. Se tudo estiver correto, você receberá emails de teste em madsondeluna@gmail.com

### Teste 2: Testar com a API

1. Inicie o servidor:
```bash
python api.py
```

2. Em outro terminal, registre um usuário de teste:
```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "usuario_teste",
    "password": "senha123",
    "email": "teste@example.com",
    "role": "user"
  }'
```

3. Verifique seu email (madsondeluna@gmail.com). Você deve receber:
   - Email de notificação sobre o novo cadastro

## Exemplo de Email que Você Receberá

Quando um novo usuário se cadastrar, você receberá um email assim:

**Assunto:** Novo Cadastro: usuario_teste

**Conteúdo:**
```
Novo Usuário Cadastrado

Olá Administrador,

Um novo usuário acabou de se cadastrar no sistema.

Detalhes do Cadastro:
- Nome de usuário: usuario_teste
- Email: teste@example.com
- Papel/Função: user
- Data/Hora: 01/12/2025 às 15:30:00

Este é um email automático de notificação.
```

## Arquivo .env Final

Seu arquivo `.env` deve ficar assim (com sua senha de app real):

```bash
# Habilitar envio de emails
EMAIL_ENABLED=true

# Configurações SMTP
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=madsondeluna@gmail.com
SMTP_PASSWORD=sua_senha_de_app_de_16_caracteres_aqui

# Emails
FROM_EMAIL=madsondeluna@gmail.com
FROM_NAME=Sistema de Autenticação - Bits Bytes Biomolecules
ADMIN_EMAIL=madsondeluna@gmail.com
```

## Solução de Problemas

### Erro: "SMTPAuthenticationError"

**Causa:** Senha incorreta ou autenticação de dois fatores não habilitada

**Solução:**
1. Verifique se você usou a senha de app (16 caracteres), não a senha normal do Gmail
2. Certifique-se de que a autenticação de dois fatores está habilitada
3. Gere uma nova senha de app se necessário

### Emails não chegam

**Verifique:**
1. Caixa de spam/lixo eletrônico
2. Verifique se EMAIL_ENABLED=true
3. Verifique os logs do servidor para erros

### Desabilitar temporariamente

Se quiser desabilitar temporariamente as notificações:

```bash
EMAIL_ENABLED=false
```

O sistema continuará funcionando normalmente, mas não enviará emails.

## Próximos Passos

Depois de configurado, toda vez que um novo usuário se registrar através da API, você receberá automaticamente um email em **madsondeluna@gmail.com** com os detalhes do cadastro!

---

**Dúvidas?** Consulte o arquivo [EMAIL_SETUP.md](EMAIL_SETUP.md) para mais detalhes técnicos.
