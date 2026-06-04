# OWASP Nettacker — Guia de Deployment para Contexto EIC IST

Documento de referência para uso de OWASP Nettacker em investigação e auditoria
no contexto do Departamento de Engenharia Informática e de Computadores (DEIC)
do Instituto Superior Técnico, Universidade de Lisboa.

---

## O que e o Nettacker

OWASP Nettacker e uma ferramenta de scan de redes e vulnerabilidades desenvolvida
pela OWASP Foundation. Executa:

- Descoberta de hosts e portos (port scanning)
- Detecao de servicos e versoes (service fingerprinting)
- Scan de vulnerabilidades conhecidas (CVE-based)
- Analise de certificados TLS/SSL
- Brute-force de credenciais (com autorizacao explícita)
- Recolha de informacao OSINT sobre dominios

Repositorio oficial: https://github.com/OWASP/Nettacker

---

## Instalacao

### Prerequisitos

```bash
# Python 3.11+ recomendado (mesmo que o doctor-agent)
python --version

# Instalar em virtualenv isolado — NAO misturar com o venv do doctor-agent
python -m venv ~/.venvs/nettacker
source ~/.venvs/nettacker/bin/activate
```

### Instalacao via pip (metodo recomendado)

```bash
pip install owasp-nettacker

# Verificar instalacao
nettacker --version
```

### Instalacao via Docker (recomendado para ambiente académico — isolamento total)

```bash
# Pull da imagem oficial OWASP
docker pull owasp/nettacker:latest

# Verificar digest antes de usar (boa pratica supply chain)
docker inspect owasp/nettacker:latest | grep -i digest

# Executar em modo interactivo com rede limitada ao host alvo
docker run --rm -it \
  --network host \
  owasp/nettacker:latest \
  --help
```

### Instalacao a partir do source (para contribuicao ou auditoria do proprio codigo)

```bash
git clone https://github.com/OWASP/Nettacker.git
cd Nettacker
pip install -r requirements.txt
python nettacker.py --help
```

---

## Interface Web (opcional)

O Nettacker tem uma interface web local para visualizacao de resultados:

```bash
# Iniciar interface web na porta 5000 (apenas localhost)
nettacker --start-api --api-host 127.0.0.1 --api-port 5000 --api-debug-mode

# Aceder em: http://127.0.0.1:5000
# Username/password definidos no ficheiro de configuracao ou via --api-username/--api-password
```

ATENCAO: Nunca expor a interface web a uma interface de rede publica. Usar apenas
em localhost ou atras de uma VPN de investigacao.

---

## Casos de uso em ambiente académico IST

### Caso 1: Auditoria de um servidor pessoal de investigacao

Contexto: tens uma VM no cluster de investigacao do DEIC (ou um servidor pessoal
no laboratorio) e queres verificar a sua superficie de ataque antes de o expor.

```bash
# Scan basico de portos e servicos
nettacker \
  --targets 192.168.1.100 \
  --scan-method port_scan \
  --output-file resultados-vm-investigacao.html \
  --graph d3_dynamic_tree_graph_lib

# Scan de certificados TLS (relevante para servicos HTTPS de investigacao)
nettacker \
  --targets meu-servidor.ist.utl.pt \
  --scan-method ssl_certificate \
  --output-file tls-audit.html

# Scan de vulnerabilidades web (apenas com autorizacao por escrito)
nettacker \
  --targets 192.168.1.100 \
  --scan-method all \
  --exclude-method brute_force \
  --output-file full-audit.json
```

### Caso 2: Verificacao de dependencias de rede de uma aplicacao deployada

Contexto: o doctor-agent e deployado num servidor e queres verificar que nao ha
portos desnecessários abertos.

```bash
# Scan cirurgico — apenas portos relevantes (80, 443, 22, 5432, 6379)
nettacker \
  --targets 10.0.0.50 \
  --scan-method port_scan \
  --custom-ports 22,80,443,5432,6379,8080,8443 \
  --output-file doctor-server-ports.txt
```

### Caso 3: Dissertacao / tese sobre segurança de redes (projecto de investigacao)

Contexto: dissertacao de mestrado ou doutoramento que inclui testes de penetracao
controlados. Requer autorizacao formal (ver seccao de consideracoes eticas).

```bash
# Scan completo num ambiente de laboratorio controlado (IP de uma VM de teste)
nettacker \
  --targets 10.0.0.0/24 \
  --scan-method all \
  --thread-number 10 \
  --timeout 15 \
  --log-in-file scan-dissertacao.log \
  --output-file dissertacao-resultados.json

# Exportar para CSV para analise estatistica na dissertacao
nettacker \
  --targets 10.0.0.100 \
  --scan-method vuln_scan \
  --output-file resultados.csv
```

### Caso 4: CTF (Capture the Flag) e ambientes de pratica

Para ambientes CTF (TryHackMe, HackTheBox, ambientes locais com VMs vulneráveis):

```bash
# Reconhecimento inicial num CTF
nettacker \
  --targets 10.10.10.50 \
  --scan-method port_scan,header_scan,cms_detection \
  --output-file ctf-recon.html

# Scan mais agressivo em ambiente CTF (nunca em producao)
nettacker \
  --targets 10.10.10.50 \
  --scan-method all \
  --thread-number 20 \
  --output-file ctf-full.json
```

---

## Opcoes mais relevantes

| Opcao | Descricao | Exemplo |
|---|---|---|
| `--targets` | IP, range CIDR, ou hostname | `192.168.1.0/24` |
| `--scan-method` | Modulo(s) a executar | `port_scan,ssl_certificate` |
| `--exclude-method` | Excluir modulos | `brute_force` |
| `--thread-number` | Threads paralelas (default: 100) | `--thread-number 10` |
| `--timeout` | Timeout por host em segundos | `--timeout 10` |
| `--output-file` | Ficheiro de output | `results.html` |
| `--graph` | Visualizacao de grafo (HTML) | `d3_dynamic_tree_graph_lib` |
| `--log-in-file` | Guardar log num ficheiro | `scan.log` |
| `--custom-ports` | Portos especificos | `22,80,443,8080` |
| `--start-api` | Iniciar interface web local | — |

### Modulos disponiveis (seleccao relevante)

```bash
# Listar todos os modulos
nettacker --show-all-modules

# Modulos mais usados em auditoria académica:
# port_scan          — descoberta de portos TCP/UDP
# ssl_certificate    — validade, cifras fracas, HSTS
# header_scan        — headers de segurança HTTP (CSP, HSTS, X-Frame-Options)
# cms_detection      — WordPress, Joomla, Drupal
# subdomain_scan     — enumeracao de subdomínios
# vuln_scan          — vulnerabilidades conhecidas (CVE)
# http_options_scan  — metodos HTTP perigosos (PUT, DELETE, TRACE)
```

---

## Consideracoes eticas para uso em investigacao

### Regra fundamental

OWASP Nettacker so deve ser usado em sistemas que controlasou para os quais
tens autorizacao ESCRITA e EXPLICITA do proprietario.

Em contexto académico IST, "eu sou aluno de LEIC/MEIC" nao e autorizacao.

### O que e permitido sem autorizacao adicional

- VMs locais criadas por ti (VirtualBox, VMware, QEMU)
- Ambientes de laboratorio fornecidos pelo proprio docente para a disciplina
- Plataformas de pratica: TryHackMe (maquinas atribuidas a ti), HackTheBox (lab machines)
- O teu proprio servidor/VPS
- Redes de teste completamente isoladas (sem saida para internet ou rede IST)

### O que requer autorizacao formal

- Qualquer host na rede IST (eduroam, rede de laboratorios, rede de investigacao)
- Servidores de projectos de investigacao partilhados
- Infraestrutura de outros grupos de investigacao ou departamentos
- Qualquer host na internet, mesmo que "abandonado" ou "publico"

### Processo de autorizacao formal para dissertacoes IST

1. Redigir um documento descrevendo: alvo, metodologia, ferramentas, periodo de testes
2. Obter assinatura do orientador de dissertacao
3. Submeter ao DEIC/DSI para aprovacao (dependendo do alvo)
4. Guardar copia da autorizacao durante e apos os testes
5. Concordar com o Regulamento de Utilizacao de Recursos Informaticos IST

### Impacto dos scans e responsabilidade

- Scans de portos geram trafico mensuravel — podem ser detectados por IDS/IPS
- Scans de vulnerabilidades podem crashar servicos frageis — avisar o responsavel
- Brute-force pode triggerar lockout de contas — usar apenas com autorizacao explícita
- Os logs de scan ficam nos servidores alvo — assume que o teu scan e rastreavel

### Referencias legais (Portugal)

- Lei do Cibercrime (Lei n.° 109/2009, de 15 de setembro) — artigo 7 (acesso ilegitimo)
- RGPD — se o scan recolher dados pessoais
- Regulamentos de Utilizacao de Recursos Informaticos da ULisboa

---

## Integracao com o workflow do doctor-agent

O doctor-agent pode usar o Nettacker como parte de uma dissertacao sobre segurança
de redes. Exemplo de workflow:

```
1. Definir alvo e obter autorizacao
2. Executar scan com Nettacker → output JSON
3. O Doctor analisa o JSON e gera relatorio académico estruturado
4. O Doctor cita CVEs relevantes usando search_academic("CVE-XXXX-YYYY impact")
5. Relatorio final em LaTeX/Markdown via write_file
```

Exemplo de prompt para o Doctor:

```
"Analisa o ficheiro scan-results.json gerado pelo Nettacker e redige
a seccao 4.2 (Avaliacao de Vulnerabilidades) da minha dissertacao,
citando os CVEs encontrados com referencias IEEE. Usa os dados reais
do scan para suportar as conclusoes."
```

---

## Recursos adicionais

- Documentacao oficial: https://github.com/OWASP/Nettacker/wiki
- OWASP Testing Guide (metodologia de testes): https://owasp.org/www-project-web-security-testing-guide/
- TryHackMe — pratica legal e etica: https://tryhackme.com
- HackTheBox — pratica legal e etica: https://hackthebox.com
- CVE Database: https://cve.mitre.org
- NVD (National Vulnerability Database): https://nvd.nist.gov
- Regulamento DSI ULisboa: https://si.ulisboa.pt (interno)
