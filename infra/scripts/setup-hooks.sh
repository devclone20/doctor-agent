#!/usr/bin/env bash
# setup-hooks.sh — Instala e configura os pre-commit hooks do doctor-agent
#
# Uso:
#   chmod +x scripts/setup-hooks.sh
#   ./scripts/setup-hooks.sh
#
# O que faz:
#   1. Verifica que pre-commit está instalado (instala se não estiver)
#   2. Instala os hooks definidos em .pre-commit-config.yaml
#   3. Verifica que ggshield está autenticado (avisa se não estiver)
#   4. Corre um check inicial em todos os ficheiros staged

set -euo pipefail

YELLOW='\033[1;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
RESET='\033[0m'

info()    { echo -e "${GREEN}[INFO]${RESET} $*"; }
warning() { echo -e "${YELLOW}[WARN]${RESET} $*"; }
error()   { echo -e "${RED}[ERROR]${RESET} $*"; exit 1; }

# ── 1. Verificar que estamos na raiz do repositório ────────────────────────
if [[ ! -f ".pre-commit-config.yaml" ]]; then
    error "Corre este script a partir da raiz do repositório (onde está .pre-commit-config.yaml)"
fi

# ── 2. Instalar pre-commit ─────────────────────────────────────────────────
if ! command -v pre-commit &>/dev/null; then
    info "pre-commit não encontrado. A instalar..."
    pip install pre-commit
else
    info "pre-commit encontrado: $(pre-commit --version)"
fi

# ── 3. Instalar ggshield ───────────────────────────────────────────────────
if ! command -v ggshield &>/dev/null; then
    info "ggshield não encontrado. A instalar..."
    pip install ggshield
else
    info "ggshield encontrado: $(ggshield --version)"
fi

# ── 4. Verificar autenticação ggshield ────────────────────────────────────
info "A verificar autenticação GitGuardian..."
if ! ggshield auth status &>/dev/null; then
    warning "ggshield não está autenticado."
    warning "Para activar a detecção de secrets, corre:"
    warning "  ggshield auth login"
    warning "Ou define a variável GITGUARDIAN_API_KEY no teu ambiente."
    warning ""
    warning "Podes obter uma API key gratuita em: https://dashboard.gitguardian.com/"
    warning ""
    warning "Os hooks vão ser instalados mas ggshield vai falhar até estares autenticado."
else
    info "ggshield autenticado."
fi

# ── 5. Instalar os hooks no .git/hooks/ ───────────────────────────────────
info "A instalar hooks em .git/hooks/..."
pre-commit install
pre-commit install --hook-type commit-msg

info "Hooks instalados com sucesso."

# ── 6. Actualizar os repos dos hooks para a versão mais recente ───────────
info "A actualizar hooks para versões mais recentes..."
pre-commit autoupdate

# ── 7. Correr check inicial (opcional — comenta se for lento) ─────────────
info "A correr check inicial em todos os ficheiros..."
pre-commit run --all-files || {
    warning "Alguns checks falharam. Revê o output acima e corrige os problemas."
    warning "Isto é normal na primeira instalação — os formatadores aplicam fixes automáticos."
    warning "Corre 'git add -u && pre-commit run --all-files' novamente para confirmar."
}

echo ""
info "Setup concluído."
info "A partir de agora, os hooks correm automaticamente antes de cada 'git commit'."
info ""
info "Comandos úteis:"
info "  pre-commit run --all-files    # correr todos os hooks manualmente"
info "  pre-commit run ggshield       # correr só o ggshield"
info "  pre-commit uninstall          # remover os hooks"
info "  ggshield auth login           # autenticar no GitGuardian"
