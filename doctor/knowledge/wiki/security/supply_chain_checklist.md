# Supply Chain Security Checklist — AI Tools

> Checklist completo de segurança da cadeia de fornecimento para ferramentas de AI,
> com aplicação específica ao Doctor-AI. Actualizado: Junho 2026.

---

## Por que Supply Chain Security é Crítico em AI Tools

Agentes de AI têm uma superfície de ataque maior do que aplicações tradicionais:
- Executam código gerado dinamicamente
- Dependem de modelos externos (weights, APIs)
- Consomem dados de fontes não controladas
- Têm acesso ao filesystem e rede do utilizador

Uma dependência comprometida num agente de AI pode resultar em: exfiltração de dados,
execução de código malicioso, envenenamento de outputs académicos, ou acesso a credenciais.

---

## 1. Verificação de Dependências Python

### 1.1 Audit com pip-audit

```bash
# Instalar
pip install pip-audit

# Audit do projecto
pip-audit

# Audit com output JSON para CI
pip-audit --format json --output audit-report.json

# Audit de um requirements.txt específico
pip-audit -r requirements.txt

# Verificar apenas CVEs com score CVSS >= 7.0 (High/Critical)
pip-audit --format json | jq '.vulnerabilities[] | select(.fix_versions | length > 0)'
```

**Quando executar:** antes de cada release, e em CI/CD em cada PR.

### 1.2 Audit com safety

```bash
# Instalar
pip install safety

# Scan básico
safety check

# Scan com output JSON
safety check --json

# Scan de ficheiro de dependências
safety check -r pyproject.toml

# Integração com CI (falha o build se encontrar vulnerabilidades)
safety check --exit-code
```

### 1.3 Aplicação ao Doctor-AI

```bash
# Na raiz do repositório
cd /path/to/doctor-agent

# Verificar todas as dependências declaradas em pyproject.toml
pip-audit
safety check

# Dependências a verificar com atenção especial (acesso a rede/filesystem):
# - anthropic: API client — verificar changelog antes de actualizar
# - httpx: HTTP client — vulnerabilidades de SSRF conhecidas em versões antigas
# - beautifulsoup4 + lxml: parsing HTML — XSS/XXE se input não for sanitizado
# - scholarly: scraping Google Scholar — pode expor IP se sem proxy
```

---

## 2. Licenças — pip-licenses

```bash
# Instalar
pip install pip-licenses

# Listar todas as licenças
pip-licenses

# Output em formato tabela com homepage
pip-licenses --with-urls --format=markdown

# Verificar licenças incompatíveis com uso académico/comercial
pip-licenses --format=json | jq '.[] | select(.License | test("GPL|AGPL|LGPL"))'

# Licenças problemáticas para distribuição:
# - GPL v2/v3: copyleft forte — contamina o projecto inteiro
# - AGPL v3: copyleft de rede — problema para serviços web
# - LGPL: copyleft fraco — aceitável se usado como biblioteca dinâmica
# - Proprietary/Unknown: verificar manualmente
```

**Para o Doctor-AI:**
- Todas as dependências em `pyproject.toml` têm licenças permissivas (MIT, Apache 2.0, BSD)
- Verificar com `pip-licenses` após cada adição de dependência nova
- Manter registo em `docs/licenses.md`

---

## 3. Integridade de Modelos de AI

### 3.1 Verificação de checksums

Quando usar modelos locais (Ollama, HuggingFace, etc.):

```bash
# Calcular SHA-256 de um modelo depois de descarregar
sha256sum model.gguf

# Verificar contra o hash publicado pelo autor
echo "expected_hash  model.gguf" | sha256sum --check

# Para modelos HuggingFace — verificar via API
python3 -c "
from huggingface_hub import model_info
info = model_info('mistralai/Mistral-7B-v0.1')
print(info.sha)  # SHA do commit mais recente
"
```

### 3.2 Verificação de proveniência

```bash
# Verificar que um modelo no HuggingFace Hub tem:
# 1. Organização verificada (badge azul)
# 2. Model card completo com licença
# 3. Commits assinados (verificar no GitHub mirror)
# 4. Nenhuma file com extensão .py ou .sh no repositório (code injection vector)

# Para o Doctor-AI (usa Anthropic API):
# - Não há modelos locais a verificar
# - Verificar que a chave ANTHROPIC_API_KEY está em .env e não no código
# - Confirmar que .env está no .gitignore
grep -r "ANTHROPIC_API_KEY\|sk-ant-" --include="*.py" .  # deve retornar vazio
```

### 3.3 Política de actualização de modelos

```markdown
## Política de Actualização — Doctor-AI

1. **Anthropic API**: actualizar `anthropic` SDK apenas após ler o changelog completo
2. **Novo modelo disponível** (ex.: claude-opus-5): testar em ambiente de staging
   antes de actualizar o modelo em produção
3. **Registo de versões**: manter `docs/model-versions.md` com a versão do modelo
   em uso, data de adopção, e razão da mudança
4. **Rollback**: manter a versão anterior do SDK em requirements-pinned.txt
```

---

## 4. Política de Actualização de Dependências

### 4.1 Categorias de actualização

| Categoria | Urgência | Processo |
|---|---|---|
| Patch com CVE crítico (CVSS ≥ 9.0) | Imediata (24h) | Actualizar, testar, release |
| Patch com CVE alto (CVSS 7.0–8.9) | 1 semana | Actualizar, testar, release |
| Patch sem CVE | Mensal | Batch update |
| Minor version | Trimestral | Testar em branch |
| Major version | Semestral | Análise de breaking changes |

### 4.2 Dependabot / Renovate (recomendado)

```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 5
    reviewers:
      - "doctor-agent-maintainers"
    labels:
      - "dependencies"
      - "security"
```

---

## 5. SBOM — Software Bill of Materials

### 5.1 Gerar SBOM com CycloneDX

```bash
# Instalar
pip install cyclonedx-bom

# Gerar SBOM em formato JSON (CycloneDX v1.4)
cyclonedx-py environment --output-format json --output-file sbom.json

# Gerar SBOM em formato XML
cyclonedx-py environment --output-format xml --output-file sbom.xml

# Para o Doctor-AI: gerar SBOM a cada release
# Incluir sbom.json no release assets do GitHub
```

### 5.2 Estrutura do SBOM Doctor-AI

```json
{
  "bomFormat": "CycloneDX",
  "specVersion": "1.4",
  "version": 1,
  "metadata": {
    "component": {
      "name": "doctor-agent",
      "version": "1.0.0",
      "type": "application"
    }
  },
  "components": [
    {
      "name": "anthropic",
      "version": ">=0.54.0",
      "type": "library",
      "licenses": [{"license": {"id": "MIT"}}],
      "purl": "pkg:pypi/anthropic"
    }
    // ... todas as dependências
  ]
}
```

### 5.3 Verificar SBOM com grype

```bash
# Instalar grype (Anchore)
brew install anchore/grype/grype

# Scan do SBOM gerado
grype sbom:./sbom.json

# Scan directo do ambiente Python
grype dir:.

# Output apenas vulnerabilidades High/Critical
grype sbom:./sbom.json --fail-on high
```

---

## 6. Checklist Completo — Doctor-AI Específico

### Antes de cada commit

- [ ] `grep -r "sk-ant-\|ANTHROPIC_API_KEY=" --include="*.py" .` — retorna vazio
- [ ] `.env` está em `.gitignore` e não foi staged (`git status` não mostra `.env`)
- [ ] Nenhuma credencial ou token hardcoded no código

### Antes de cada release

- [ ] `pip-audit` — zero vulnerabilidades High/Critical
- [ ] `safety check` — zero issues
- [ ] `pip-licenses` — zero licenças GPL/AGPL incompatíveis
- [ ] SBOM gerado e incluído nos release assets
- [ ] Changelog actualizado com dependências modificadas

### Mensalmente

- [ ] Verificar CVEs nas 5 dependências de maior risco: `anthropic`, `httpx`, `lxml`, `requests`, `scholarly`
- [ ] Actualizar dependências com patches de segurança
- [ ] Revisar `.env.example` — remover campos desnecessários

### Quando adicionar uma nova dependência

- [ ] Verificar CVEs conhecidos: `pip-audit --dry-run <pacote>`
- [ ] Verificar licença: `pip show <pacote>` → campo License
- [ ] Verificar maintainers: PyPI page → maintainers activos? Últimos commits há quanto tempo?
- [ ] Verificar downloads semanais (>10K/semana = mainstream)
- [ ] Verificar se existe alternativa já no projecto que cobre o caso de uso

---

## 7. Recursos e Referências

- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)
- [pip-audit](https://github.com/pypa/pip-audit) — ferramenta oficial PyPA
- [safety](https://github.com/pyupio/safety) — alternativa popular
- [CycloneDX Python](https://github.com/CycloneDX/cyclonedx-python) — geração de SBOM
- [grype](https://github.com/anchore/grype) — scanner de vulnerabilidades por SBOM
- [SLSA Framework](https://slsa.dev/) — Supply-chain Levels for Software Artifacts
- [NIST SSDF](https://csrc.nist.gov/Projects/ssdf) — Secure Software Development Framework
