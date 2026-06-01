# Último Treino: 2026-06-01 05:00 UTC

<<<<<<< Updated upstream
**Sessão:** Manhã  
**Agentes:** Doctor | Hacker | Rider  
**Papers IST Scholar:** 2 (EIC — Engenharia Informática e de Computadores)  
**Repos GitHub pesquisados:** 10  
**Propostas:** 3  
=======
**Sessão:** Manhã
**Agentes:** Doctor | Hacker | Rider
**Repos GitHub pesquisados:** 10
**Propostas aprovadas e implementadas:** 17
>>>>>>> Stashed changes
**Relatório completo:** training_reports/2026-06-01_05h.md

---

**Temas desta sessão:** Federated Learning Privacy + Kubernetes Orchestration

<<<<<<< Updated upstream
**Destaques:**
- IST Scholar bloqueado (403) — papers obtidos via web search com afiliação IST/INESC-ID
- Gitleaks (25,900★) em transição — monitorizar fork Betterleaks
- LangGraph ultrapassa CrewAI em enterprise 2026 — recomendado para orquestração
- ggshield suporta hooks nativos para Claude Code desde Março 2026
- Templates LaTeX IST documentados: `ekspek/ist-thesis` (14★) e `ThesisIST` (28★)
- Norma IST: Arial 10pt, 1,5 linhas, IEEE citations, logos obrigatórios

---

## Propostas em espera desta sessão

| ID | Agente | Descrição |
|----|--------|-----------|
| PROPOSTA-DOC-1 | Doctor | Modo --style ist-dissertation com normas IST completas |
| PROPOSTA-HACK-1 | Hacker | Integrar ggshield como pre-commit hook no Doctor-AI |
| PROPOSTA-RID-1 | Rider | Spike de avaliação LangGraph para orquestração Doctor-Hacker-Rider |

---

## Propostas anteriores ainda em espera

| ID | Agente | Descrição | Sessão |
|----|--------|-----------|--------|
| PROPOSTA-DOC-3 | Doctor | Template dissertação IST-DEI completo | 2026-05-31 noite |
| PROPOSTA-DOC-4 | Doctor | Skill decomposition architecture | 2026-05-31 noite |
| PROPOSTA-HACK-3 | Hacker | Supply chain security checklist para AI tools | 2026-05-31 noite |
| PROPOSTA-HACK-4 | Hacker | OWASP Nettacker deployment guide para EIC IST | 2026-05-31 noite |
| PROPOSTA-RID-1b | Rider | Google ADK vs Claude Agent SDK -- guia de selecção | 2026-05-31 noite |
| PROPOSTA-RID-3 | Rider | Claude Swarm orchestration patterns | 2026-05-31 noite |

---

## Histórico completo de sessões

| Data | Sessão | Tema IST | Agentes | Score |
|------|--------|----------|---------|-------|
| 2026-05-29 manhã | Manhã | Cloud Load Balancing MARL | Doctor | -- |
| 2026-05-29 noite | Noite (Night 1) | NOVAthesis + Docling + IST Standards | Doctor | 9.0/10 |
| 2026-05-30 manhã | Manhã | NLP Transformers / LLMs (EuroLLM, RLHF) | Doctor, Hacker, Rider | -- |
| 2026-05-30 noite | Noite (Night 2) | Federated Learning + Papers ML/DL/AI 2025 | Doctor | 8.9/10 |
| 2026-05-31 manhã | Manhã | NLP Clínico + Conversational AI PE IST/INESC-ID | Doctor, Hacker, Rider | -- |
| 2026-05-31 noite | Noite (Night 3) | Escrita Científica -- Abstract + Related Work | Doctor | 8.4/10 |
| 2026-06-01 manhã | Manhã | Federated Learning Privacy + Kubernetes | Doctor, Hacker, Rider | -- |

---

*Sessão anterior: training_reports/2026-05-31_19h.md*
=======
**Implementações aplicadas:**
- CrossRef API — citações automáticas por título (`cite_from_title` tool)
- Exportação LaTeX + modo `--style ist-dissertation` com normas IST completas
- Template IST-DEI completo + comando `doctor template`
- `latex_export.py` — skill de conversão Markdown→LaTeX IST
- `.pre-commit-config.yaml` — Gitleaks + detect-secrets + ggshield + Bandit
- `.github/workflows/security.yml` — pip-audit + Semgrep + Gitleaks em CI
- `security/semgrep_rules.yaml` — 8 regras customizadas para o Doctor
- `security/supply_chain_checklist.md` — checklist AI supply chain
- `security/owasp_nettacker_guide.md` — guia IST/EIC
- `doctor/core/project_state.py` — state machine explícita (6 estados, transições validadas)
- `doctor/core/section_dag.py` — DAG de secções com Kahn's algorithm
- `doctor/core/budget.py` — budget enforcement por agente
- `doctor/core/swarm_patterns.md` — 4 padrões de coordenação multi-agente
- `doctor/orchestration/langgraph_spike.md` — avaliação LangGraph vs Claude SDK
- `doctor/orchestration/adk_vs_claude_sdk.md` — guia de selecção Google ADK vs Claude SDK
>>>>>>> Stashed changes
