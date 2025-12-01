# Configuração de Email - Guia Completo

Este guia explica como configurar o sistema de notificação por email.

## Funcionalidades

O sistema envia emails automaticamente em duas situações:

1. **Notificação para Admin**: Quando um novo usuário se cadastra, o administrador recebe um email com os detalhes do cadastro
2. **Email de Boas-Vindas**: O novo usuário recebe um email de boas-vindas (opcional)

## Configuração Rápida

### 1. Copiar o arquivo de configuração

```bash
cp .env.example .env
```

### 2. Editar o arquivo .env

Abra o arquivo `.env` e configure suas credenciais:

```bash
# Habilitar envio de emails
EMAIL_ENABLED=true

# Configurações SMTP (exemplo com Gmail)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=seu_email@gmail.com
SMTP_PASSWORD=sua_senha_de_app

# Email do administrador
ADMIN_EMAIL=admin@example.com
```

### 3. Instalar dependência adicional (se necessário)

```bash
pip install python-dotenv
```

### 4. Modificar auth_system.py e api.py para usar .env

Adicione no início dos arquivos:

```python
from dotenv import load_dotenv
load_dotenv()  # Carrega variáveis do arquivo .env
```

## Configuração com Gmail

### Passo 1: Habilitar Autenticação de Dois Fatores

1. Acesse https://myaccount.google.com/security
2. Em "Como fazer login no Google", clique em "Verificação em duas etapas"
3. Siga as instruções para habilitar

### Passo 2: Gerar Senha de App

1. Acesse https://myaccount.google.com/apppasswords
2. Selecione "Email" como app
3. Selecione "Outro" como dispositivo e digite "Sistema de Autenticação"
4. Clique em "Gerar"
5. Copie a senha de 16 caracteres gerada

### Passo 3: Configurar no .env

```bash
EMAIL_ENABLED=true
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=seu_email@gmail.com
SMTP_PASSWORD=xxxx xxxx xxxx xxxx  # Senha de app de 16 caracteres
FROM_EMAIL=seu_email@gmail.com
FROM_NAME=Meu Sistema
ADMIN_EMAIL=admin@example.com
```

## Configuração com Outros Provedores

### Outlook/Hotmail

```bash
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
SMTP_USERNAME=seu_email@outlook.com
SMTP_PASSWORD=sua_senha
```

### Yahoo Mail

```bash
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
SMTP_USERNAME=seu_email@yahoo.com
SMTP_PASSWORD=sua_senha_de_app
```

Nota: Yahoo também requer senha de app. Gere em: https://login.yahoo.com/account/security

### ProtonMail

```bash
SMTP_SERVER=smtp.protonmail.com
SMTP_PORT=587
SMTP_USERNAME=seu_email@protonmail.com
SMTP_PASSWORD=sua_senha
```

### Servidor SMTP Próprio

```bash
SMTP_SERVER=smtp.seudominio.com
SMTP_PORT=587  # ou 465 para SSL
SMTP_USERNAME=seu_usuario
SMTP_PASSWORD=sua_senha
```

## Testando a Configuração

### Teste 1: Executar o módulo de email diretamente

```bash
python email_service.py
```

Este comando tentará enviar emails de teste. Se `EMAIL_ENABLED=false`, os emails não serão enviados mas você verá as mensagens de log.

### Teste 2: Registrar um usuário via API

```bash
curl -X POST http://localhost:5000/api/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "teste",
    "password": "senha123",
    "email": "teste@example.com",
    "role": "user"
  }'
```

Verifique se:
1. O admin recebeu email com os detalhes do cadastro
2. O usuário recebeu email de boas-vindas

## Tipos de Email Enviados

### 1. Notificação de Cadastro para Admin

**Quando é enviado**: Sempre que um novo usuário se registra

**Para quem**: Email definido em `ADMIN_EMAIL`

**Conteúdo**:
- Nome de usuário
- Email do novo usuário
- Papel/função atribuída
- Data e hora do cadastro

### 2. Email de Boas-Vindas

**Quando é enviado**: Quando um novo usuário se registra (se email foi fornecido)

**Para quem**: Email do novo usuário

**Conteúdo**:
- Mensagem de boas-vindas
- Confirmação dos dados de acesso
- Nome de usuário e email

### 3. Notificação de Login (Opcional)

Esta funcionalidade está implementada mas não ativa por padrão. Para ativar, adicione no endpoint de login:

```python
# No endpoint /api/login, após autenticação bem-sucedida
if email:
    email_service.send_login_notification(username, email, request.remote_addr)
```

## Desabilitando Emails

Para desabilitar temporariamente o envio de emails sem remover a configuração:

```bash
EMAIL_ENABLED=false
```

Com essa configuração, o sistema apenas registrará logs mas não enviará emails de fato.

## Solução de Problemas

### Erro: "SMTPAuthenticationError"

**Problema**: Credenciais incorretas ou autenticação bloqueada

**Solução**:
- Verifique se username e password estão corretos
- Para Gmail, certifique-se de usar senha de app, não a senha normal
- Verifique se a autenticação de dois fatores está habilitada (Gmail)

### Erro: "SMTPServerDisconnected"

**Problema**: Problemas de conexão com o servidor SMTP

**Solução**:
- Verifique se o servidor e porta estão corretos
- Verifique sua conexão com a internet
- Alguns provedores bloqueiam conexões SMTP em redes públicas

### Erro: "Connection refused"

**Problema**: Porta ou servidor incorretos

**Solução**:
- Verifique se está usando a porta correta (587 para TLS, 465 para SSL)
- Tente porta alternativa

### Emails não chegam

**Possíveis causas**:
1. **Caixa de spam**: Verifique a pasta de spam/lixo eletrônico
2. **Configurações de segurança**: Alguns provedores bloqueiam emails de servidores desconhecidos
3. **Limite de envio**: Você pode ter atingido o limite de envio diário do provedor

### Emails demoram muito para chegar

**Solução**:
- Normal: Emails podem levar alguns segundos a minutos
- Se demorar mais de 5 minutos, verifique os logs do servidor
- Considere usar serviços de email transacional (SendGrid, Mailgun, etc.)

## Melhores Práticas para Produção

### 1. Use Serviços de Email Transacional

Para produção, recomendamos usar serviços especializados:

- **SendGrid**: https://sendgrid.com
- **Mailgun**: https://www.mailgun.com
- **Amazon SES**: https://aws.amazon.com/ses/
- **Postmark**: https://postmarkapp.com

Vantagens:
- Melhor entregabilidade
- Não cai em spam
- Analytics e tracking
- Maiores limites de envio
- Suporte a templates

### 2. Configuração com SendGrid (exemplo)

```bash
SMTP_SERVER=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USERNAME=apikey
SMTP_PASSWORD=sua_api_key_do_sendgrid
```

### 3. Nunca Commite Credenciais

Adicione `.env` ao `.gitignore`:

```bash
echo ".env" >> .gitignore
```

### 4. Use Variáveis de Ambiente em Produção

Em servidores de produção (Heroku, AWS, etc), configure as variáveis de ambiente diretamente no painel de controle, não use arquivo `.env`.

### 5. Implemente Fila de Emails

Para melhor performance, use filas (Celery, RQ) para enviar emails em background:

```python
# Exemplo com Celery
@celery.task
def send_registration_email(username, email, role):
    email_service.send_registration_notification_to_admin(username, email, role)
    if email:
        email_service.send_welcome_email(username, email)
```

### 6. Monitoramento

- Configure logs para rastrear emails enviados
- Implemente alertas para falhas de envio
- Monitore taxa de abertura e cliques (se usar serviço transacional)

## Templates de Email Personalizados

Os templates de email estão em [email_service.py](email_service.py). Para personalizar:

1. Localize a função desejada (ex: `send_welcome_email`)
2. Modifique o conteúdo HTML em `html_content`
3. Modifique o conteúdo texto em `text_content`

Exemplo de personalização:

```python
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Seus estilos CSS aqui */
    </style>
</head>
<body>
    <h1>Bem-vindo {username}!</h1>
    <p>Seu conteúdo personalizado aqui</p>
</body>
</html>
"""
```

## Variáveis de Ambiente - Referência Completa

| Variável | Obrigatório | Padrão | Descrição |
|----------|-------------|---------|-----------|
| EMAIL_ENABLED | Não | false | Habilita/desabilita envio de emails |
| SMTP_SERVER | Sim | smtp.gmail.com | Servidor SMTP |
| SMTP_PORT | Sim | 587 | Porta SMTP (587 para TLS, 465 para SSL) |
| SMTP_USERNAME | Sim | - | Usuário para autenticação SMTP |
| SMTP_PASSWORD | Sim | - | Senha para autenticação SMTP |
| FROM_EMAIL | Não | SMTP_USERNAME | Email remetente |
| FROM_NAME | Não | Sistema de Autenticação | Nome do remetente |
| ADMIN_EMAIL | Sim | - | Email do administrador para receber notificações |

## Suporte

Se encontrar problemas:

1. Verifique os logs do servidor
2. Teste a conexão SMTP manualmente
3. Consulte a documentação do seu provedor de email
4. Verifique se não há firewall bloqueando a porta SMTP

## Exemplos de Código

### Enviar email personalizado

```python
from email_service import EmailService

email = EmailService()

# Email customizado
message = email._create_message(
    to_email="usuario@example.com",
    subject="Assunto do Email",
    html_content="<h1>Conteúdo HTML</h1>",
    text_content="Conteúdo em texto"
)

email._send_email(message)
```

### Adicionar novo tipo de notificação

```python
# No arquivo email_service.py

def send_password_reset_email(self, username: str, email: str, reset_link: str) -> bool:
    """Envia email com link de redefinição de senha"""
    subject = "Redefinir sua senha"

    html_content = f"""
    <html>
        <body>
            <h1>Olá {username}</h1>
            <p>Clique no link abaixo para redefinir sua senha:</p>
            <a href="{reset_link}">Redefinir Senha</a>
        </body>
    </html>
    """

    message = self._create_message(email, subject, html_content)
    return self._send_email(message)
```

---

Para mais informações, consulte o [README.md](README.md) principal.
