# Guia de Segurança - Sistema de Autenticação

## ALERTA IMPORTANTE

**NUNCA commite arquivos `.env` ou qualquer arquivo com credenciais no Git!**

## O Que Aconteceu

O GitGuardian detectou credenciais SMTP expostas no seu repositório. Isso acontece quando:
1. Arquivo `.env` é commitado acidentalmente
2. Credenciais são escritas diretamente no código
3. Tokens ou senhas aparecem em qualquer arquivo versionado

## Correção Imediata

### 1. Remover arquivo .env do Git

```bash
# Remover do tracking (mantém arquivo localmente)
git rm --cached auth/.env

# Commit a remoção
git add .gitignore
git commit -m "Remove sensitive .env file and add .gitignore"
git push
```

### 2. TROCAR TODAS AS CREDENCIAIS EXPOSTAS

**CRÍTICO:** Se suas credenciais foram expostas no Git, você DEVE trocá-las imediatamente:

#### A. Senha de App do Gmail

1. Acesse: https://myaccount.google.com/apppasswords
2. **REVOGUE** a senha de app antiga
3. Gere uma **NOVA** senha de app
4. Atualize no arquivo `.env` local (que NÃO está mais no Git)

#### B. Chaves Secretas

```bash
# Gerar novas chaves aleatórias
python3 -c "import secrets; print(secrets.token_hex(32))"
```

Atualize `SECRET_KEY` e `JWT_SECRET_KEY` no `.env`

### 3. Verificar Histórico do Git

**IMPORTANTE:** Mesmo removendo o arquivo, ele ainda existe no histórico do Git!

#### Opção A: Limpar Histórico (Recomendado se repositório é privado ou novo)

```bash
# ATENÇÃO: Isso reescreve o histórico! Use com cuidado!

# Instalar git-filter-repo
pip install git-filter-repo

# Remover arquivo do histórico completo
git filter-repo --path auth/.env --invert-paths --force

# Force push (CUIDADO: só faça se souber o que está fazendo)
git push origin --force --all
```

#### Opção B: Aceitar e Seguir em Frente

Se você já trocou todas as credenciais, pode simplesmente continuar. As credenciais antigas no histórico não funcionam mais.

## Estrutura de Segurança Correta

### Arquivos que DEVEM estar no Git:

```
✓ .env.example          # Template SEM credenciais reais
✓ .gitignore            # Lista de arquivos a ignorar
✓ *.py (código)         # Código fonte
✓ README.md             # Documentação
✓ requirements.txt      # Dependências
```

### Arquivos que NÃO DEVEM estar no Git:

```
✗ .env                  # NUNCA! Contém credenciais reais
✗ secrets.json          # NUNCA!
✗ credentials.txt       # NUNCA!
✗ *.pem, *.key          # NUNCA!
✗ Qualquer arquivo com senhas
```

## Configuração Segura

### 1. Desenvolvimento Local

**Arquivo: `auth/.env` (NÃO no Git)**

```bash
EMAIL_ENABLED=true
SMTP_USERNAME=madsondeluna@gmail.com
SMTP_PASSWORD=xxxx xxxx xxxx xxxx  # Senha de app
ADMIN_EMAIL=madsondeluna@gmail.com
SECRET_KEY=chave_secreta_aqui
JWT_SECRET_KEY=outra_chave_aqui
```

### 2. Produção (Heroku, Railway, etc.)

**NÃO use arquivo .env!** Configure variáveis de ambiente direto na plataforma:

#### Heroku:
```bash
heroku config:set EMAIL_ENABLED=true
heroku config:set SMTP_USERNAME=madsondeluna@gmail.com
heroku config:set SMTP_PASSWORD=sua_senha_de_app
heroku config:set ADMIN_EMAIL=madsondeluna@gmail.com
heroku config:set SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
heroku config:set JWT_SECRET_KEY=$(python3 -c "import secrets; print(secrets.token_hex(32))")
```

#### Railway/Render:
Use a interface web para adicionar variáveis de ambiente.

### 3. Verificar antes de Commitar

**SEMPRE execute antes de fazer commit:**

```bash
# Verificar se .env está no staging
git status

# Se .env aparecer, REMOVA:
git reset HEAD auth/.env

# Verificar o que será commitado
git diff --cached

# Se ver credenciais, PARE e remova!
```

## Boas Práticas de Segurança

### 1. Usar Variáveis de Ambiente

❌ **ERRADO:**
```python
SMTP_PASSWORD = "minha_senha_123"
```

✅ **CORRETO:**
```python
import os
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
```

### 2. Validar .gitignore

```bash
# Testar se .env está sendo ignorado
git check-ignore -v auth/.env

# Deve retornar:
# .gitignore:2:.env    auth/.env
```

### 3. Pre-commit Hooks

Instale um hook para prevenir commits de credenciais:

```bash
pip install pre-commit

# Criar .pre-commit-config.yaml
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: check-added-large-files
      - id: detect-private-key
      - id: check-yaml

  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.4.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
EOF

# Instalar hooks
pre-commit install
```

### 4. Scanning de Segurança

Use ferramentas para detectar credenciais:

```bash
# GitGuardian CLI
pip install ggshield
ggshield scan repo .

# TruffleHog
docker run -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/madsondeluna/bits_bytes_biomolecules
```

## Checklist de Segurança

Antes de cada commit:

- [ ] Arquivo `.env` NÃO está sendo commitado
- [ ] `.gitignore` está configurado corretamente
- [ ] Nenhuma senha ou token no código
- [ ] Variáveis sensíveis vêm de `os.environ.get()`
- [ ] `.env.example` não contém credenciais reais
- [ ] Executei `git status` e verifiquei os arquivos

## Rotação de Credenciais

**Recomendação:** Troque suas credenciais periodicamente:

### Gmail - Senha de App

1. Revogue senha antiga
2. Gere nova senha
3. Atualize `.env` local
4. Atualize variáveis de ambiente em produção

### Frequência recomendada:
- **Desenvolvimento:** A cada 3 meses
- **Produção:** A cada 1-2 meses
- **Se expostas:** IMEDIATAMENTE

## Monitoramento

### GitHub Secret Scanning

O GitHub automaticamente escaneia repositórios públicos. Se detectar credenciais:

1. Você receberá um alerta
2. **Ação imediata:** Troque a credencial
3. Remova do histórico (se possível)
4. Verifique logs para acessos suspeitos

### GitGuardian

- Monitora repositórios em tempo real
- Alerta sobre credenciais expostas
- Dashboard: https://dashboard.gitguardian.com

## Resposta a Incidentes

Se credenciais foram expostas:

### Passo 1: Avaliar Impacto (Imediato)
- [ ] Que credenciais foram expostas?
- [ ] Por quanto tempo estiveram expostas?
- [ ] O repositório é público ou privado?

### Passo 2: Conter (Imediato - primeiras 2 horas)
- [ ] Trocar TODAS as credenciais expostas
- [ ] Revogar tokens/senhas antigas
- [ ] Verificar logs de acesso para atividades suspeitas

### Passo 3: Remediar (24 horas)
- [ ] Remover credenciais do Git
- [ ] Adicionar `.gitignore` apropriado
- [ ] Limpar histórico (se possível)
- [ ] Implementar pre-commit hooks

### Passo 4: Prevenir (1 semana)
- [ ] Revisar todos os repositórios
- [ ] Treinar time sobre segurança
- [ ] Implementar scanning automático
- [ ] Documentar lições aprendidas

## Recursos Adicionais

### Ferramentas Recomendadas

1. **git-secrets** (AWS)
   ```bash
   git clone https://github.com/awslabs/git-secrets.git
   cd git-secrets && make install
   git secrets --install
   ```

2. **Talisman**
   ```bash
   curl https://thoughtworks.github.io/talisman/install.sh > install.sh
   chmod +x install.sh
   ./install.sh
   ```

3. **GitGuardian**
   - Website: https://www.gitguardian.com
   - Dashboard: https://dashboard.gitguardian.com

### Leitura Recomendada

- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [12 Factor App](https://12factor.net/)

## Suporte

Se você acidentalmente expôs credenciais:

1. **NÃO entre em pânico**
2. Siga os passos de "Resposta a Incidentes" acima
3. Troque as credenciais IMEDIATAMENTE
4. Se precisar de ajuda, abra uma issue (sem incluir credenciais!)

---

## Resumo: Ação Imediata

Se você está lendo isso porque o GitGuardian alertou:

```bash
# 1. Trocar credenciais AGORA
# - Gmail: Revogar senha de app e gerar nova
# - Gerar novas SECRET_KEY e JWT_SECRET_KEY

# 2. Remover .env do Git (se ainda não fez)
git rm --cached auth/.env
git add .gitignore
git commit -m "Security: Remove .env and add .gitignore"
git push

# 3. Verificar que .gitignore está funcionando
git status  # .env NÃO deve aparecer

# 4. Atualizar .env local com novas credenciais
# (Edite auth/.env com as novas credenciais)

# 5. Se em produção, atualizar variáveis de ambiente
heroku config:set SMTP_PASSWORD=nova_senha_aqui
```

**Pronto! Suas credenciais estão seguras agora.**

---

**Autor:** Madson Aragão @ UFMG
**Última atualização:** Dezembro 2025
