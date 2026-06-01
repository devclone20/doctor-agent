# Google ADK vs. Claude Agent SDK — Comparação para Doctor-Hacker-Rider

> Análise comparativa estruturada para decidir qual SDK adoptar (ou como combinar)
> no sistema multi-agente Doctor-Hacker-Rider.
> Data: Junho 2026

---

## Visão Geral

| | Google ADK | Claude Agent SDK |
|---|---|---|
| **Fornecedor** | Google DeepMind / Google Cloud | Anthropic |
| **Versão** | 1.x (GA desde Q1 2026) | 0.54+ (anthropic Python SDK) |
| **Modelo base** | Gemini 2.0/2.5 (suporta outros via LiteLLM) | Claude 3.5/4.x |
| **Linguagem** | Python, Java (preview) | Python, TypeScript |
| **Licença** | Apache 2.0 | MIT |
| **Repositório** | https://github.com/google/adk-python | https://github.com/anthropics/anthropic-sdk-python |

---

## Google ADK (Agent Development Kit)

### O que é

Framework da Google para construir agentes de AI com integração nativa com o ecossistema
Google Cloud: Vertex AI, BigQuery, Cloud Functions, Google Search grounding.

### Arquitectura core

```python
from google.adk.agents import Agent
from google.adk.tools import google_search, code_execution

# Definir um agente com ferramentas
research_agent = Agent(
    name="research_agent",
    model="gemini-2.0-flash",
    instruction="Fazes pesquisa académica...",
    tools=[google_search, code_execution],
)

# Sub-agentes (multi-agent nativo)
orchestrator = Agent(
    name="orchestrator",
    model="gemini-2.5-pro",
    instruction="Coordenas os agentes especializados...",
    sub_agents=[research_agent, security_agent],
)

# Executar
from google.adk.runners import Runner
runner = Runner(agent=orchestrator)
response = runner.run("Revê a segurança do meu deployment e escreve o capítulo 5")
```

### Features relevantes

| Feature | ADK | Detalhe |
|---|---|---|
| Multi-agent nativo | Sim | `sub_agents` como primeiro cidadão |
| Streaming | Sim | `runner.run_streaming()` |
| Tool calling | Sim | Google tools + custom Python functions |
| Code execution | Sim | Sandbox nativo (não precisa de Bash tool) |
| Google Search grounding | Sim | Resultados web verificados com fontes |
| Memory | Sim | `SessionService` + `MemoryService` |
| Evaluation | Sim | `AgentEvaluator` built-in |
| Vertex AI deployment | Sim | Deploy directo para Vertex AI Agent Engine |
| Multi-modal | Sim | Texto, imagem, áudio, vídeo (Gemini native) |
| Live API (áudio/vídeo real-time) | Sim | Único no mercado |

### Limitações

- **Lock-in Google.** Code execution e grounding são Google-proprietary.
- **Gemini preferido.** Outros modelos suportados via LiteLLM, mas com menos features.
- **Ecossistema jovem.** ADK GA desde Q1 2026 — menos battle-tested que o Anthropic SDK.
- **Documentação.** Boa qualidade mas exemplos maioritariamente focados em Google Cloud.
- **GDPR/privacidade.** Dados passam por Google Cloud — considerar para projectos académicos com dados sensíveis.

---

## Claude Agent SDK (Anthropic)

### O que é

O SDK oficial Python da Anthropic para interagir com a API Claude. Não é um "agent SDK"
no sentido de CrewAI ou ADK — é um cliente de API com primitivos para tool use,
computer use, e streaming. O padrão de agentes é construído pelo utilizador sobre estes primitivos.

### Arquitectura de agentes (padrão actual Doctor-Hacker-Rider)

```python
import anthropic

client = anthropic.Anthropic()

# Definir ferramentas para o Rider invocar
tools = [
    {
        "name": "call_doctor",
        "description": "Invocar o Doctor para tarefas académicas",
        "input_schema": {
            "type": "object",
            "properties": {
                "task": {"type": "string", "description": "Tarefa académica a executar"},
                "context": {"type": "string", "description": "Contexto do projecto"}
            },
            "required": ["task"]
        }
    },
    {
        "name": "call_hacker",
        "description": "Invocar o Hacker para tarefas de segurança e infra",
        "input_schema": {
            "type": "object",
            "properties": {
                "task": {"type": "string"},
            },
            "required": ["task"]
        }
    }
]

def rider_orchestrate(user_request: str) -> str:
    """Rider como orquestrador via tool_use."""
    messages = [{"role": "user", "content": user_request}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            system=RIDER_SYSTEM_PROMPT,
            tools=tools,
            messages=messages,
        )

        if response.stop_reason == "end_turn":
            return response.content[0].text

        if response.stop_reason == "tool_use":
            tool_call = next(b for b in response.content if b.type == "tool_use")
            tool_result = _execute_tool(tool_call.name, tool_call.input)

            messages.append({"role": "assistant", "content": response.content})
            messages.append({
                "role": "user",
                "content": [{"type": "tool_result", "tool_use_id": tool_call.id, "content": tool_result}]
            })
```

### Features relevantes

| Feature | Claude SDK | Detalhe |
|---|---|---|
| Tool calling | Sim | `tool_use` nativo, bem testado |
| Streaming | Sim | `client.messages.stream()` |
| Computer use | Sim | Screenshot + click + type (único no mercado) |
| Extended thinking | Sim | `thinking` blocks para raciocínio profundo |
| Prompt caching | Sim | `cache_control` — reduz custo em 90% em system prompts longos |
| Structured output | Sim | Via JSON schema em `tool_use` |
| Multi-modal | Sim | Texto + imagem (sem áudio/vídeo nativo) |
| Context window | 200K tokens | Maior da indústria para texto |
| Multi-agent | Manual | Sem primitivo nativo — implementado via tools |
| Memory | Manual | Sem `SessionService` — implementado pelo utilizador |
| Evaluation | Manual | Sem `AgentEvaluator` — implementar com pytest |
| Vertex AI | Não | Disponível via Amazon Bedrock ou Anthropic directo |

### Limitações

- **Multi-agent manual.** Sem primitivo nativo para sub-agents — o programador implementa o loop.
- **Sem grounding nativo.** Web search requer tool custom (DuckDuckGo, Tavily, etc.).
- **Sem code sandbox nativo.** Execução de código requer Bash tool ou E2B.
- **Python only.** TypeScript disponível mas menos maduro.

---

## Comparação Directa por Dimensão

### Integração com ferramentas existentes no Doctor-Agent

| Ferramenta | ADK | Claude SDK |
|---|---|---|
| `httpx` (pesquisa CrossRef) | Via custom tool | Via Bash tool ou custom tool |
| `python-docx` (geração .docx) | Via code_execution (sandbox) | Via Bash tool (execução local) |
| `rich` (CLI output) | Não integrado | Funciona directamente |
| `scholarly` (Google Scholar) | Via custom tool | Via custom tool |
| arXiv / Semantic Scholar | Via Google Search grounding (indirecto) | Via custom tool (directo) |

**Vantagem Claude SDK:** as tools existentes no Doctor funcionam sem modificação.
**Vantagem ADK:** code_execution sandbox evita execução de código não-confiado na máquina local.

### Casos de uso ideais

| Caso de uso | Melhor opção | Razão |
|---|---|---|
| Dissertação académica (Doctor) | Claude SDK | Context 200K, extended thinking, prompt caching |
| Análise de segurança (Hacker) | Ambos equivalentes | Nenhum tem vantagem clara |
| Web search em tempo real | ADK | Google Search grounding com fontes verificadas |
| Geração de código executável | ADK | Code execution sandbox nativo |
| Orquestração complexa (Rider) | ADK | Sub-agents como primeiro cidadão |
| Computer use (automação de UI) | Claude SDK | Computer use exclusivo do Claude |
| Custo em volume | Claude SDK | Prompt caching reduz drasticamente o custo |
| Multimodal (áudio/vídeo) | ADK | Gemini native live API |

### Curva de aprendizagem

| SDK | Para alguém com Python + LLM básico | Para especialista |
|---|---|---|
| Claude SDK | 1–2 dias (tool_use loop) | 1 semana (computer use, caching avançado) |
| ADK | 2–3 dias (Runner + Agent + tools) | 2 semanas (Vertex deployment, SessionService) |

### Ecossistema e comunidade

| Dimensão | ADK | Claude SDK |
|---|---|---|
| GitHub stars | ~8K (Junho 2026) | ~12K (Junho 2026) |
| Documentação | Boa — developer.google.com/adk | Excelente — docs.anthropic.com |
| Exemplos de código | Muitos (Google focus) | Muitos (geral) |
| Community (Discord/Slack) | Google Developers Discord | Anthropic Discord (activo) |
| Stack Overflow | Poucos Q&A (novo) | Muitos Q&A |

---

## Recomendação para o Contexto Doctor-Hacker-Rider

**Adoptar: Claude Agent SDK como primário. Google ADK como opcional para casos específicos.**

### Justificação

**Manter Claude SDK como primário porque:**
1. Doctor, Hacker, e Rider já estão escritos como system prompts Claude — migrar requer reescrever tudo
2. O context window de 200K é crítico para dissertações longas (o doctor.md sozinho tem >1800 linhas)
3. Prompt caching reduz o custo de carregar o `doctor.md` em cada chamada em ~90%
4. Extended thinking para problemas de arquitectura complexos (sem equivalente no ADK)
5. Computer use (único) para automação de tarefas que requerem UI

**Considerar ADK como complemento se:**
- Precisar de web search grounded com fontes verificadas (Google Search grounding)
- Quiser deploy em Vertex AI Agent Engine para exposição pública
- O sistema crescer para 6+ agentes com estado persistente

**Nunca migrar completamente para ADK porque:**
- Lock-in Google Cloud para features core (grounding, code execution)
- Os system prompts do Doctor são optimizados para o comportamento do Claude
- Prompt caching não tem equivalente no ADK/Gemini com o mesmo custo-benefício

### Arquitectura híbrida (se necessário)

```python
# Rider como hub com acesso a ambos os modelos
import anthropic
import google.generativeai as genai

def rider_decide_model(task: str) -> str:
    """Rider usa o modelo mais adequado para cada subtarefa."""
    if _needs_web_search(task):
        # ADK / Gemini para search grounded
        return _call_gemini_with_search(task)
    elif _needs_long_context(task):
        # Claude para contexto longo (dissertações)
        return _call_claude(task)
    else:
        # Claude por defeito (melhor instruction following)
        return _call_claude(task)
```
