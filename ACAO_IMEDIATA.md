# AÇÃO IMEDIATA - Segurança das Credenciais

## GitGuardian detectou credenciais expostas!

### O que foi feito automaticamente:

✅ Arquivo `.env` removido do Git (mas mantido localmente)
✅ `.gitignore` criado para prevenir futuros commits acidentais
✅ Documentação de segurança criada ([SECURITY.md](SECURITY.md))

---

## O QUE VOCÊ PRECISA FAZER AGORA (URGENTE):

### 1. TROCAR SUA SENHA DE APP DO GMAIL (Imediato!)

Como a senha foi exposta no Git, você DEVE trocá-la:

**Passo a passo:**

1. Acesse: https://myaccount.google.com/apppasswords

2. **REVOGUE** a senha de app atual:
   - Procure por "Sistema de Autenticação" ou a senha que você criou
   - Clique em "Remover" ou "Revogar"

3. **GERE UMA NOVA** senha de app:
   - Clique em "Gerar"
   - App: Email
   - Dispositivo: Outro (digite "Sistema de Autenticação")
   - Copie a nova senha de 16 caracteres

4. **ATUALIZE** o arquivo `.env` local:
   ```bash
   # Edite o arquivo
   nano auth/.env

   # Ou use seu editor preferido
   code auth/.env
   ```

   Atualize a linha:
   ```
   SMTP_PASSWORD=xxxx xxxx xxxx xxxx  # Coloque a NOVA senha aqui
   ```

### 2. GERAR NOVAS CHAVES SECRETAS

```bash
# Gerar nova SECRET_KEY
python3 -c "import secrets; print('SECRET_KEY=' + secrets.token_hex(32))"

# Gerar nova JWT_SECRET_KEY
python3 -c "import secrets; print('JWT_SECRET_KEY=' + secrets.token_hex(32))"

# Copie os valores e atualize no arquivo auth/.env
```

### 3. COMMITAR AS MUDANÇAS DE SEGURANÇA

```bash
# Adicionar arquivos de segurança
git add .gitignore SECURITY.md WEBSITE_AUTH.md ACAO_IMEDIATA.md

# Adicionar novas páginas
git add docs/cadastro.html docs/login.html docs/dashboard.html

# Adicionar sistema de autenticação e email
git add auth/auth_system.py auth/api.py auth/email_service.py
git add auth/client_example.py auth/test_api.sh
git add auth/requirements.txt auth/.env.example
git add auth/EMAIL_SETUP.md auth/CONFIGURAR_EMAIL.md auth/README.md

# Adicionar mudança na página de exercícios
git add docs/exercises.html

# Commit
git commit -m "Security: Remove .env from Git and add authentication system

- Remove sensitive .env file from version control
- Add .gitignore to prevent future credential leaks
- Implement JWT token-based authentication system
- Add email notification service for new user registrations
- Create user registration, login, and dashboard pages
- Update exercises page with real API authentication
- Add comprehensive security documentation"

# Push
git push origin main
```

### 4. VERIFICAR SE .ENV NÃO ESTÁ MAIS NO GIT

```bash
# Verificar status
git status

# O arquivo auth/.env NÃO deve aparecer
# Se aparecer, algo deu errado!
```

---

## CHECKLIST DE SEGURANÇA

Marque quando completar:

- [ ] Revogou senha de app antiga do Gmail
- [ ] Gerou nova senha de app do Gmail
- [ ] Atualizou `SMTP_PASSWORD` no arquivo `auth/.env` local
- [ ] Gerou nova `SECRET_KEY`
- [ ] Gerou nova `JWT_SECRET_KEY`
- [ ] Atualizou as chaves no arquivo `auth/.env` local
- [ ] Executou os comandos git acima
- [ ] Verificou que `.env` não aparece no `git status`
- [ ] Fez push das mudanças

---

## VERIFICAÇÃO FINAL

Após fazer tudo acima, verifique:

```bash
# 1. Arquivo .env está sendo ignorado?
git check-ignore -v auth/.env
# Deve retornar: .gitignore:2:.env    auth/.env

# 2. .env não está no repositório?
git ls-files | grep .env
# Não deve retornar nada

# 3. .gitignore foi commitado?
git ls-files | grep .gitignore
# Deve retornar: .gitignore
```

---

## SE VOCÊ ESTIVER EM PRODUÇÃO

Se você já fez deploy da aplicação (Heroku, Railway, etc):

```bash
# Atualizar variáveis de ambiente em produção
# Exemplo para Heroku:

heroku config:set SMTP_PASSWORD=nova_senha_aqui
heroku config:set SECRET_KEY=nova_chave_aqui
heroku config:set JWT_SECRET_KEY=nova_chave_jwt_aqui
```

---

## HISTÓRICO DO GIT

**IMPORTANTE:** O arquivo `.env` ainda existe no histórico do Git (commits anteriores).

### Opção 1: Aceitar e Seguir em Frente (Recomendado)

Como você já trocou todas as credenciais, as senhas antigas no histórico não funcionam mais. É seguro continuar.

### Opção 2: Limpar Histórico (Avançado)

⚠️ **CUIDADO:** Isso reescreve o histórico e pode causar problemas se outras pessoas têm clones do repositório!

```bash
# Instalar ferramenta
pip install git-filter-repo

# Remover .env do histórico COMPLETO
git filter-repo --path auth/.env --invert-paths --force

# Force push (apaga histórico remoto)
git push origin --force --all
git push origin --force --tags
```

**Nota:** Se você escolher a Opção 2, avise qualquer pessoa que tenha clone do repositório para fazer:
```bash
git fetch origin
git reset --hard origin/main
```

---

## PRÓXIMOS PASSOS

Depois de completar tudo acima:

1. ✅ Suas credenciais estão seguras
2. ✅ `.env` nunca mais será commitado
3. ✅ Sistema de autenticação funcionando
4. ✅ Emails de notificação configurados

**Teste o sistema:**

```bash
# Iniciar API
cd auth/
python api.py

# Em outro terminal, testar
curl http://localhost:5000/

# Acessar as páginas
# - cadastro: http://localhost:8000/cadastro.html
# - login: http://localhost:8000/login.html
# - exercícios: http://localhost:8000/exercises.html
```

---

## DÚVIDAS?

Consulte:
- [SECURITY.md](SECURITY.md) - Guia completo de segurança
- [WEBSITE_AUTH.md](WEBSITE_AUTH.md) - Como funciona o sistema de autenticação
- [auth/EMAIL_SETUP.md](auth/EMAIL_SETUP.md) - Configuração de email

---

## RESUMO EXECUTIVO

| Ação | Status | Urgência |
|------|--------|----------|
| Trocar senha Gmail | ⏳ PENDENTE | 🔴 CRÍTICA |
| Gerar novas chaves | ⏳ PENDENTE | 🔴 CRÍTICA |
| Commitar mudanças | ⏳ PENDENTE | 🟡 ALTA |
| Limpar histórico | ⏳ OPCIONAL | 🟢 BAIXA |

---

**⏰ TEMPO ESTIMADO TOTAL: 10-15 minutos**

**Boa sorte! Qualquer dúvida, consulte a documentação.**
