# Prompt de Auto-Training — Doctor / Hacker / Rider

## Tarefa

Realiza o treino diário dos agentes Doctor, Hacker e Rider.

### 1. Pesquisa GitHub (usar WebSearch + WebFetch)

Pesquisa os seguintes temas e recolhe os top repos com +1k stars, activos nos últimos 3 meses:

**Para Doctor (académico / escrita científica):**
- `python-docx academic report generator site:github.com`
- `latex dissertation template IST site:github.com`
- `scientific writing AI agent site:github.com`
- `citation formatter IEEE python site:github.com`

**Para Hacker (segurança):**
- `OWASP security scanner python site:github.com`
- `secrets detection git pre-commit site:github.com`
- `static analysis security python site:github.com`
- `dependency audit vulnerability python site:github.com`

**Para Rider (orquestrador):**
- `multi-agent orchestration python site:github.com`
- `task planning AI agents site:github.com`
- `agent swarm coordination site:github.com`

### 2. Cross-training

Para cada par de agentes, identificar:
- Que padrões do Hacker podem tornar o Doctor mais seguro?
- Que técnicas de orquestração do Rider podem melhorar o Doctor?
- Que conhecimento académico do Doctor pode enriquecer relatórios do Rider?

### 3. Relatório

Gerar um ficheiro `.md` estruturado com:
```
# Relatório de Treino — {DATA} {HORA}

## Resumo
- X repos novos encontrados
- Y actualizações propostas
- Z insights de cross-training

## Doctor — Actualizações
### Repos encontrados
...
### Padrões extraídos
...
### Diffs propostos (a aprovar)
...

## Hacker — Actualizações
...

## Rider — Actualizações
...

## Cross-training Insights
...
```

### 4. Push para GitHub
Fazer commit do relatório para `aigenesis20/doctor-ai20/training_reports/YYYY-MM-DD_HHh.md`
