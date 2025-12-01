# Guia de Segurança

Este documento descreve as práticas de segurança implementadas no sistema de autenticação.

## Melhorias de Segurança Implementadas

### 1. Hash de Senhas com bcrypt

- **Antes:** SHA-256 (inseguro - rápido demais para ataques de força bruta)
- **Agora:** bcrypt (seguro - lento e com salt automático)

```python
# Uso do bcrypt
password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
is_valid = bcrypt.checkpw(password.encode(), password_hash.encode())
```

### 2. Sistema de Redefinição de Senha Seguro

- Tokens criptograficamente seguros (`secrets.token_urlsafe(32)`)
- Tokens hasheados antes de armazenar (bcrypt)
- Expiração curta: 30 minutos
- Uso único: token invalidado após utilização
- Proteção contra enumeração de usuários

### 3. Remoção de Credenciais Hardcoded

- **Antes:** Usuários padrão sempre criados (admin/admin123, etc)
- **Agora:** Usuários de teste só são criados se `CREATE_DEFAULT_USERS=true`
- Por padrão, o sistema inicia em "modo seguro" sem usuários padrão

### 4. Variáveis de Ambiente

Todas as configurações sensíveis devem estar em variáveis de ambiente:

```bash
# Email
SMTP_USERNAME=seu_email@gmail.com
SMTP_PASSWORD=sua_senha_de_app
ADMIN_EMAIL=admin@example.com
EMAIL_ENABLED=true

# URLs
RESET_PASSWORD_URL=https://seu-dominio.com/reset-password.html

# Desenvolvimento
CREATE_DEFAULT_USERS=false  # NUNCA true em produção
```

## Práticas de Segurança

### Para Desenvolvimento

1. Copie `.env.example` para `.env`:
   ```bash
   cp .env.example .env
   ```

2. Configure as variáveis no `.env`

3. Para testes locais, habilite usuários padrão:
   ```bash
   echo "CREATE_DEFAULT_USERS=true" >> .env
   ```

### Para Produção

1. **NUNCA** commite o arquivo `.env`
2. Configure variáveis de ambiente no servidor/hosting
3. Use HTTPS obrigatoriamente
4. Configure `CREATE_DEFAULT_USERS=false` (padrão)
5. Use senhas fortes para contas administrativas
6. Configure CORS adequadamente
7. Monitore logs de autenticação
8. Implemente rate limiting (recomendado)

## Checklist de Segurança para Produção

- [ ] Arquivo `.env` está no `.gitignore`
- [ ] Variável `CREATE_DEFAULT_USERS` não está configurada (ou está como `false`)
- [ ] HTTPS está habilitado
- [ ] Certificado SSL válido
- [ ] CORS configurado apenas para domínios específicos
- [ ] Senhas de administradores são fortes (>12 caracteres, misto)
- [ ] Senhas de email/SMTP são "senhas de app" (não a senha principal)
- [ ] Logs de autenticação estão sendo monitorados
- [ ] Backups regulares do banco de dados
- [ ] Rate limiting implementado (recomendado)

## Endpoints de Segurança

### POST /api/forgot-password

Solicita redefinição de senha:

```json
{
  "username": "usuario"
}
```

**Características de Segurança:**
- Sempre retorna a mesma mensagem (evita enumeração)
- Token enviado apenas por email
- Não revela se o usuário existe

### POST /api/reset-password

Redefine senha com token:

```json
{
  "username": "usuario",
  "token": "token_recebido_por_email",
  "new_password": "nova_senha_forte"
}
```

**Características de Segurança:**
- Token deve ser válido e não expirado
- Token é invalidado após uso
- Senha deve atender requisitos mínimos

## Segurança de Email

### Gmail - Senhas de App

1. Ative autenticação de dois fatores
2. Acesse: https://myaccount.google.com/apppasswords
3. Gere uma senha de app
4. Use essa senha em `SMTP_PASSWORD`

**NUNCA** use sua senha principal do Gmail!

## Proteções Implementadas

1. **Contra Força Bruta:**
   - bcrypt é computacionalmente caro
   - Recomendado: adicionar rate limiting

2. **Contra Enumeração de Usuários:**
   - `/api/forgot-password` não revela se usuário existe

3. **Contra Replay Attacks:**
   - Tokens JWT têm expiração
   - Tokens de reset são de uso único

4. **Contra Timing Attacks:**
   - bcrypt.checkpw tem tempo constante

## Recomendações Futuras

1. **Rate Limiting:**
   ```python
   from flask_limiter import Limiter
   # Limite tentativas de login
   ```

2. **Autenticação de Dois Fatores (2FA):**
   - TOTP (Google Authenticator)
   - SMS (menos seguro)

3. **Auditoria de Segurança:**
   - Log de tentativas de login
   - Alertas de atividade suspeita

4. **Sessões Seguras:**
   - Refresh tokens
   - Revogação de tokens

5. **Validação de Senha Forte:**
   - Mínimo 8-12 caracteres
   - Letras maiúsculas e minúsculas
   - Números e caracteres especiais

## eReferências

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [bcrypt Documentation](https://pypi.org/project/bcrypt/)

---

**Última Atualização:** Dezembro 2025
**Autor:** Madson Aragão @ UFMG
