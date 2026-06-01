# OWASP Nettacker — Guia para EIC IST

> Guia de deployment do OWASP Nettacker no contexto do Departamento de Engenharia
> Informática e de Computadores (EIC/DEI) do Instituto Superior Técnico, Lisboa.
> Para uso em projectos de dissertação ou investigação com componente de segurança.
>
> **Aviso legal:** usar Nettacker apenas em sistemas para os quais tens autorização
> explícita. No contexto IST, isso significa: a tua própria máquina, VMs de laboratório
> que te foram atribuídas, ou sistemas da dissertação com aprovação do orientador.
> Nunca executar scans na rede IST sem autorização dos DSI/NREN.

---

## O que é o OWASP Nettacker

OWASP Nettacker é um framework de automated network attack and scanning em Python,
desenvolvido pela OWASP Foundation. Características relevantes para o contexto académico:

- Scanner de vulnerabilidades de rede + web
- Framework extensível com módulos (scan, attack, brute, fuzz)
- Output em JSON, HTML, CSV — integrável em pipelines de análise
- Open source (Apache 2.0) — auditável
- Activamente mantido (repositório: https://github.com/OWASP/Nettacker)

**Casos de uso em dissertações EIC IST:**
- Avaliação de segurança de sistemas implementados na dissertação
- Benchmark de vulnerabilidades em infraestrutura cloud (AWS/GCP/Azure VMs da dissertação)
- Validação de controlos de segurança implementados
- Geração de dados para análise em dissertações de segurança

---

## 1. Instalação

### Via pip (recomendado para desenvolvimento)

```bash
# Criar ambiente virtual isolado
python3 -m venv .venv-nettacker
source .venv-nettacker/bin/activate

# Instalar Nettacker
pip install owasp-nettacker

# Verificar instalação
nettacker --version
```

### Via Docker (recomendado para produção/CI)

```bash
# Pull da imagem oficial
docker pull owasp/nettacker

# Executar com Docker
docker run -it --rm \
  -v $(pwd)/output:/tmp/output \
  owasp/nettacker \
  --targets 192.168.1.1 \
  --scan-module port_scan \
  --report-path /tmp/output/report.html

# Verificar integridade da imagem (supply chain)
docker pull owasp/nettacker@sha256:<digest-publicado>
```

### Via código-fonte (para desenvolvimento de módulos)

```bash
git clone https://github.com/OWASP/Nettacker.git
cd Nettacker

# Verificar integridade
git log --oneline -5  # confirmar commits recentes

pip install -r requirements.txt
python3 nettacker.py --help
```

---

## 2. Configuração de Scan Profiles para Infraestrutura Académica

### Perfil 1: Scan Básico de Rede (tua máquina/VM de dissertação)

```bash
# Scan de portos abertos numa VM de dissertação
nettacker \
  --targets 10.0.0.1 \
  --scan-module port_scan \
  --ports 22,80,443,8080,8443,3000,5000,6379,5432,27017 \
  --report-path ./reports/port_scan.html \
  --report-type html \
  --verbose

# Scan de range de portos (desenvolvimento local)
nettacker \
  --targets 127.0.0.1 \
  --scan-module port_scan \
  --ports 1-10000 \
  --threads 50 \
  --report-path ./reports/localhost_scan.json \
  --report-type json
```

### Perfil 2: Scan de Vulnerabilidades Web (aplicação web da dissertação)

```bash
# Scan de vulnerabilidades num servidor web de teste
nettacker \
  --targets http://localhost:8080 \
  --scan-module http_options_enabled,http_cors,ssl_expired,ssl_weak_cipher \
  --report-path ./reports/web_vuln_scan.html \
  --report-type html

# Scan SSL/TLS (se a tua dissertação expõe HTTPS)
nettacker \
  --targets yourdomain.example.com \
  --scan-module ssl_expired,ssl_weak_cipher,ssl_certificate_hostname \
  --report-path ./reports/ssl_scan.html
```

### Perfil 3: Scan de Infraestrutura Cloud (VMs da dissertação)

```bash
# Para uma VM em AWS/GCP/Azure da dissertação
# Substituir TARGET pelo IP da tua instância

TARGET="YOUR_VM_IP"

nettacker \
  --targets $TARGET \
  --scan-module \
    port_scan,\
    ssh_brute,\
    http_options_enabled,\
    http_cors,\
    apache_version,\
    nginx_version \
  --ports 22,80,443,8080,5000 \
  --threads 20 \
  --timeout 10 \
  --report-path ./reports/cloud_vm_scan_$(date +%Y%m%d).html \
  --report-type html

# IMPORTANTE: ssh_brute — usar apenas com credenciais de teste conhecidas
# Para evitar lockout, configurar --delay entre tentativas
```

### Perfil 4: Scan Orientado para Dissertação de Segurança

```bash
# Scan abrangente para dissertações com componente de segurança
# Executar numa VM de teste isolada — NUNCA na rede IST sem autorização

nettacker \
  --targets 192.168.100.0/24 \
  --scan-module \
    port_scan,\
    http_options_enabled,\
    http_cors,\
    ssl_expired,\
    ssl_weak_cipher,\
    ftp_anonymous \
  --report-path ./reports/full_scan.json \
  --report-type json \
  --log-in-file ./logs/nettacker.log \
  --verbose
```

---

## 3. Módulos Relevantes por Caso de Uso

| Módulo | Descrição | Caso de uso IST |
|---|---|---|
| `port_scan` | Enumerar portos abertos | Inventário de serviços da dissertação |
| `http_options_enabled` | Detectar HTTP methods perigosos (PUT, DELETE) | APIs REST implementadas |
| `http_cors` | Verificar CORS mal configurado | Frontend + API da dissertação |
| `ssl_expired` | Certificados SSL expirados | Deployments com HTTPS |
| `ssl_weak_cipher` | Cifras SSL fracas (RC4, DES, etc.) | Segurança de comunicações |
| `ssl_certificate_hostname` | Mismatch de hostname no certificado | Deployment cloud |
| `apache_version` | Versão Apache exposta | Servidores web de dissertação |
| `nginx_version` | Versão nginx exposta | Servidores web de dissertação |
| `ftp_anonymous` | FTP anónimo habilitado | Servidores de ficheiros |
| `ssh_brute` | Brute force SSH | Auditoria de autenticação (VM de teste) |
| `telnet_weak_password` | Telnet com password fraca | IoT/dispositivos de teste |

---

## 4. Interpretar os Resultados

### Estrutura do relatório JSON

```json
{
  "scan_results": [
    {
      "target": "10.0.0.1",
      "module": "port_scan",
      "port": 22,
      "status": "open",
      "service": "ssh",
      "banner": "SSH-2.0-OpenSSH_8.9p1",
      "severity": "info",
      "description": "SSH port open"
    },
    {
      "target": "10.0.0.1",
      "module": "ssl_weak_cipher",
      "port": 443,
      "status": "vulnerable",
      "severity": "high",
      "description": "RC4 cipher suite enabled",
      "recommendation": "Disable RC4 and use TLS 1.3 only"
    }
  ]
}
```

### Níveis de severidade e acção recomendada

| Severidade | CVSS Range | Acção recomendada | Prazo |
|---|---|---|---|
| **Critical** | 9.0–10.0 | Fix imediato | 24h |
| **High** | 7.0–8.9 | Fix urgente | 1 semana |
| **Medium** | 4.0–6.9 | Fix no próximo sprint | 1 mês |
| **Low** | 0.1–3.9 | Fix quando possível | Próximo release |
| **Info** | 0.0 | Documentar, não necessariamente fix | — |

### Resultados comuns em projectos de dissertação EIC

**Portos abertos inesperados:**
- `5432` (PostgreSQL) ou `27017` (MongoDB) abertos ao exterior — fechar com firewall
- `6379` (Redis) sem autenticação — configurar `requirepass`
- `8080` (dev server) acessível publicamente — usar proxy reverso ou restringir IP

**Vulnerabilidades web frequentes:**
- `http_cors` — `Access-Control-Allow-Origin: *` — restringir ao domínio do frontend
- `http_options_enabled` — método DELETE/PUT exposto — desactivar no reverse proxy
- `ssl_weak_cipher` — TLS 1.0/1.1 habilitado — forçar TLS 1.2 mínimo (TLS 1.3 preferido)

---

## 5. Integração com Workflow de Segurança da Dissertação

### 5.1 Integração em CI/CD (GitHub Actions)

```yaml
# .github/workflows/security-scan.yml
name: Security Scan

on:
  push:
    branches: [main, develop]
  schedule:
    - cron: '0 2 * * 1'  # Segundas-feiras às 2h

jobs:
  nettacker-scan:
    runs-on: ubuntu-latest
    services:
      app:
        image: your-app-image
        ports:
          - 8080:8080

    steps:
      - uses: actions/checkout@v4

      - name: Install Nettacker
        run: pip install owasp-nettacker

      - name: Run security scan
        run: |
          nettacker \
            --targets 127.0.0.1 \
            --scan-module port_scan,http_options_enabled,http_cors \
            --ports 8080 \
            --report-path ./security-report.json \
            --report-type json

      - name: Check for high/critical issues
        run: |
          python3 -c "
          import json, sys
          with open('security-report.json') as f:
              results = json.load(f)
          issues = [r for r in results.get('scan_results', [])
                    if r.get('severity') in ('high', 'critical')]
          if issues:
              print(f'FAIL: {len(issues)} high/critical issues found')
              for i in issues:
                  print(f'  - {i[\"module\"]}: {i[\"description\"]}')
              sys.exit(1)
          print('OK: No high/critical issues found')
          "

      - name: Upload scan report
        uses: actions/upload-artifact@v4
        with:
          name: security-scan-report
          path: security-report.json
```

### 5.2 Script de scan rápido para desenvolvimento local

```bash
#!/usr/bin/env bash
# scripts/security-scan-local.sh
# Uso: ./scripts/security-scan-local.sh [TARGET_IP]

TARGET=${1:-"127.0.0.1"}
REPORT_DIR="./security-reports"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p "$REPORT_DIR"

echo "=== OWASP Nettacker Security Scan ==="
echo "Target: $TARGET"
echo "Report: $REPORT_DIR/scan_${DATE}.html"
echo ""

nettacker \
  --targets "$TARGET" \
  --scan-module port_scan,http_options_enabled,http_cors,ssl_expired \
  --report-path "$REPORT_DIR/scan_${DATE}.html" \
  --report-type html \
  --verbose

echo ""
echo "=== Scan concluído. Abrir relatório: ==="
echo "open $REPORT_DIR/scan_${DATE}.html"
```

### 5.3 Documentar resultados na dissertação

Quando usar Nettacker como parte da avaliação de segurança na dissertação:

```markdown
## 5.X Avaliação de Segurança

A segurança da implementação foi avaliada com o OWASP Nettacker vX.Y [REF],
um framework de scanning de vulnerabilidades de rede da OWASP Foundation.

### Setup de avaliação
- **Ferramenta:** OWASP Nettacker vX.Y
- **Target:** VM de teste com IP 10.0.0.X (isolada da rede de produção)
- **Módulos activos:** port_scan, http_cors, ssl_expired, http_options_enabled
- **Data:** YYYY-MM-DD

### Resultados

| Severidade | Quantidade | Issues identificados |
|---|---|---|
| Critical | 0 | — |
| High | 1 | SSL TLS 1.0 habilitado |
| Medium | 2 | HTTP OPTIONS exposto; versão nginx visível |
| Low | 3 | ... |

### Medidas correctivas aplicadas
[Descrever os fixes implementados após o scan]
```

---

## 6. Referências

- [OWASP Nettacker GitHub](https://github.com/OWASP/Nettacker)
- [OWASP Nettacker Docs](https://owasp.org/www-project-nettacker/)
- [OWASP Top 10 2021](https://owasp.org/Top10/)
- [CWE/SANS Top 25](https://cwe.mitre.org/top25/)
- [DSI IST — Segurança Informática](https://si.tecnico.ulisboa.pt) — para pedidos de autorização de scans na rede IST
