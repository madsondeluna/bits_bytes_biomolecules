#!/bin/bash

# Script de teste para API de Autenticação
# Este script testa todos os endpoints da API

echo "======================================================================"
echo "      Testes da API de Autenticação via Token JWT"
echo "======================================================================"
echo ""

BASE_URL="http://localhost:5000"

# Cores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Função para testar endpoints
test_endpoint() {
    local name=$1
    local method=$2
    local endpoint=$3
    local data=$4
    local headers=$5

    echo -e "${YELLOW}Testando: ${name}${NC}"
    echo "Endpoint: $method $endpoint"

    if [ -n "$data" ]; then
        echo "Dados: $data"
    fi

    if [ -n "$headers" ]; then
        response=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X $method "$BASE_URL$endpoint" \
            -H "Content-Type: application/json" \
            -H "$headers" \
            -d "$data")
    elif [ -n "$data" ]; then
        response=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X $method "$BASE_URL$endpoint" \
            -H "Content-Type: application/json" \
            -d "$data")
    else
        response=$(curl -s -w "\nHTTP_CODE:%{http_code}" -X $method "$BASE_URL$endpoint")
    fi

    http_code=$(echo "$response" | grep HTTP_CODE | cut -d':' -f2)
    body=$(echo "$response" | sed '/HTTP_CODE/d')

    if [ $http_code -ge 200 ] && [ $http_code -lt 300 ]; then
        echo -e "${GREEN}✓ Sucesso (HTTP $http_code)${NC}"
    else
        echo -e "${RED}✗ Falha (HTTP $http_code)${NC}"
    fi

    echo "Resposta:"
    echo "$body" | python3 -m json.tool 2>/dev/null || echo "$body"
    echo ""
    echo "----------------------------------------------------------------------"
    echo ""
}

# Variáveis para armazenar tokens
USER_TOKEN=""
ADMIN_TOKEN=""

# Teste 1: Endpoint raiz
test_endpoint "Endpoint Raiz" "GET" "/" "" ""

# Teste 2: Login com usuário comum
echo -e "${YELLOW}=== TESTE: Login com Usuário Comum ===${NC}"
response=$(curl -s -X POST "$BASE_URL/api/login" \
    -H "Content-Type: application/json" \
    -d '{"username":"user","password":"user123"}')
echo "$response" | python3 -m json.tool 2>/dev/null || echo "$response"
USER_TOKEN=$(echo "$response" | python3 -c "import sys, json; print(json.load(sys.stdin)['token'])" 2>/dev/null)
if [ -n "$USER_TOKEN" ]; then
    echo -e "${GREEN}✓ Token do usuário obtido${NC}"
else
    echo -e "${RED}✗ Falha ao obter token do usuário${NC}"
fi
echo ""
echo "----------------------------------------------------------------------"
echo ""

# Teste 3: Login com admin
echo -e "${YELLOW}=== TESTE: Login com Admin ===${NC}"
response=$(curl -s -X POST "$BASE_URL/api/login" \
    -H "Content-Type: application/json" \
    -d '{"username":"admin","password":"admin123"}')
echo "$response" | python3 -m json.tool 2>/dev/null || echo "$response"
ADMIN_TOKEN=$(echo "$response" | python3 -c "import sys, json; print(json.load(sys.stdin)['token'])" 2>/dev/null)
if [ -n "$ADMIN_TOKEN" ]; then
    echo -e "${GREEN}✓ Token do admin obtido${NC}"
else
    echo -e "${RED}✗ Falha ao obter token do admin${NC}"
fi
echo ""
echo "----------------------------------------------------------------------"
echo ""

# Teste 4: Login com credenciais inválidas
test_endpoint "Login com Credenciais Inválidas" "POST" "/api/login" \
    '{"username":"user","password":"senha_errada"}' ""

# Teste 5: Registrar novo usuário
test_endpoint "Registrar Novo Usuário" "POST" "/api/register" \
    '{"username":"testuser","password":"test123","email":"test@example.com","role":"user"}' ""

# Teste 6: Tentar registrar usuário existente
test_endpoint "Registrar Usuário Existente (deve falhar)" "POST" "/api/register" \
    '{"username":"testuser","password":"test123"}' ""

# Teste 7: Verificar token do usuário
if [ -n "$USER_TOKEN" ]; then
    test_endpoint "Verificar Token do Usuário" "GET" "/api/verify" "" \
        "Authorization: Bearer $USER_TOKEN"
fi

# Teste 8: Obter perfil do usuário
if [ -n "$USER_TOKEN" ]; then
    test_endpoint "Obter Perfil do Usuário" "GET" "/api/profile" "" \
        "Authorization: Bearer $USER_TOKEN"
fi

# Teste 9: Acessar rota protegida
if [ -n "$USER_TOKEN" ]; then
    test_endpoint "Acessar Rota Protegida" "GET" "/api/protected" "" \
        "Authorization: Bearer $USER_TOKEN"
fi

# Teste 10: Tentar acessar rota protegida sem token
test_endpoint "Acessar Rota Protegida Sem Token (deve falhar)" "GET" "/api/protected" "" ""

# Teste 11: Tentar acessar rota protegida com token inválido
test_endpoint "Acessar Rota Protegida Com Token Inválido (deve falhar)" "GET" "/api/protected" "" \
    "Authorization: Bearer token_invalido_12345"

# Teste 12: Listar usuários (como admin)
if [ -n "$ADMIN_TOKEN" ]; then
    test_endpoint "Listar Usuários (como Admin)" "GET" "/api/users" "" \
        "Authorization: Bearer $ADMIN_TOKEN"
fi

# Teste 13: Tentar listar usuários sem ser admin
if [ -n "$USER_TOKEN" ]; then
    test_endpoint "Listar Usuários Sem Ser Admin (deve falhar)" "GET" "/api/users" "" \
        "Authorization: Bearer $USER_TOKEN"
fi

# Teste 14: Acessar rota admin-only (como admin)
if [ -n "$ADMIN_TOKEN" ]; then
    test_endpoint "Acessar Rota Admin (como Admin)" "GET" "/api/admin-only" "" \
        "Authorization: Bearer $ADMIN_TOKEN"
fi

# Teste 15: Tentar acessar rota admin-only sem ser admin
if [ -n "$USER_TOKEN" ]; then
    test_endpoint "Acessar Rota Admin Sem Ser Admin (deve falhar)" "GET" "/api/admin-only" "" \
        "Authorization: Bearer $USER_TOKEN"
fi

# Teste 16: Alterar senha
if [ -n "$USER_TOKEN" ]; then
    test_endpoint "Alterar Senha do Usuário" "POST" "/api/change-password" \
        '{"old_password":"user123","new_password":"newpass456"}' \
        "Authorization: Bearer $USER_TOKEN"

    # Teste 17: Login com nova senha
    echo -e "${YELLOW}=== TESTE: Login com Nova Senha ===${NC}"
    response=$(curl -s -X POST "$BASE_URL/api/login" \
        -H "Content-Type: application/json" \
        -d '{"username":"user","password":"newpass456"}')
    echo "$response" | python3 -m json.tool 2>/dev/null || echo "$response"
    http_code=$(echo "$response" | python3 -c "import sys, json; print('success' if 'token' in json.load(sys.stdin) else 'fail')" 2>/dev/null)
    if [ "$http_code" == "success" ]; then
        echo -e "${GREEN}✓ Login com nova senha bem-sucedido${NC}"
    else
        echo -e "${RED}✗ Falha ao fazer login com nova senha${NC}"
    fi
    echo ""
    echo "----------------------------------------------------------------------"
    echo ""
fi

# Teste 18: Deletar usuário (como admin)
if [ -n "$ADMIN_TOKEN" ]; then
    test_endpoint "Deletar Usuário (como Admin)" "DELETE" "/api/users/testuser" "" \
        "Authorization: Bearer $ADMIN_TOKEN"
fi

# Teste 19: Tentar deletar usuário que não existe
if [ -n "$ADMIN_TOKEN" ]; then
    test_endpoint "Deletar Usuário Inexistente (deve falhar)" "DELETE" "/api/users/usuario_que_nao_existe" "" \
        "Authorization: Bearer $ADMIN_TOKEN"
fi

# Teste 20: Endpoint não encontrado
test_endpoint "Endpoint Não Encontrado (404)" "GET" "/api/endpoint-que-nao-existe" "" ""

echo ""
echo "======================================================================"
echo "                    Testes Concluídos!"
echo "======================================================================"
echo ""
echo -e "${GREEN}✓${NC} = Sucesso"
echo -e "${RED}✗${NC} = Falha"
echo ""
echo "Para executar novamente: bash test_api.sh"
echo ""
