# Google ADK vs Claude Agent SDK — Guia de Selecção Técnica

**Tipo:** Architecture Decision Record (ADR-002)  
**Data:** Junho 2026  
**Contexto:** doctor-agent — orquestração Doctor-Hacker-Rider  
**Status:** ACCEPTED

---

## Resumo executivo

O Google Agent Development Kit (ADK) e o Claude Agent SDK são os dois frameworks
de agentes mais relevantes em 2026 para multi-agent coordination em Python. A
escolha entre eles não é de performance — ambos são adequados em termos de
latência e throughput para o caso de uso do doctor-agent. É uma escolha de
modelo de programação, ecossistema, e alinhamento com os modelos de linguagem
escolhidos.

**Decisão: Claude Agent SDK** para o doctor-agent.  
**Usar Google ADK quando:** os requisitos incluem integração com o Google Cloud
stack (Vertex AI, Gemini, Cloud Run, BigQuery), ou quando o modelo de programação
baseado em eventos do ADK for materialmente mais adequado ao workflow.

---

## 1. Modelo de programação

### Claude Agent SDK

O Claude Agent SDK não é um framework de agentes no sentido tradicional — é um
cliente Python para a API Anthropic com suporte a `tools`, streaming, e `Messages`.
A orquestração é código Python puro; não existe um grafo, não existe um runtime.

```python
# Um "agente" no Claude SDK é uma função que chama client.messages.create()
from anthropic import Anthropic

client = Anthropic()

def doctor_agent(task: str, context: str) -> str:
    response = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=12_000,
        system=DOCTOR_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"{task}\n\nContext:\n{context}"}],
    )
    return response.content[0].text
```

Vantagens:
- Código Python completamente standard — sem runtime, sem framework magic
- Fácil de testar (mock `client.messages.create`)
- Sem overhead conceptual: um agente é uma função
- Debugging trivial com qualquer Python debugger

Desvantagens:
- Sem modelo de estado automático — o programador gere o estado explicitamente
- Sem routing de mensagens entre agentes — tem de ser implementado
- Sem ferramentas de observabilidade out-of-the-box

### Google ADK

O Google ADK tem um modelo baseado em `Agent` classes com `Runner`, `Session`, e
`InvocationContext`. Os agentes comunicam via `Events` e o framework gere o ciclo
de vida da invocação.

```python
from google.adk.agents import Agent, LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

doctor_agent = LlmAgent(
    name="doctor",
    model="gemini-2.5-pro",
    description="Academic writing specialist",
    instruction=DOCTOR_SYSTEM_PROMPT,
    tools=[write_section_tool, search_references_tool],
)

runner = Runner(
    agent=doctor_agent,
    app_name="doctor-agent",
    session_service=InMemorySessionService(),
)

session = await runner.session_service.create_session(app_name="doctor-agent", user_id="u1")

async for event in runner.run_async(
    user_id="u1",
    session_id=session.id,
    new_message=types.Content(role="user", parts=[types.Part(text=task)]),
):
    if event.is_final_response():
        result = event.content.parts[0].text
```

Vantagens:
- Session management automático com persistência de histórico de mensagens
- Modelo de multi-agent nativo: `AgentTool` permite um agente invocar outro
- Integração nativa com Vertex AI e Google Cloud services
- `SequentialAgent`, `ParallelAgent`, `LoopAgent` como primitivas declarativas

Desvantagens:
- Acoplamento forte a Gemini/Google Cloud (mudar de modelo é não trivial)
- Verbosidade: hello world é 3x mais código que no Claude SDK
- Maturidade em 2026: ADK 1.x estabilizou a API mas tem breaking changes frequentes
  entre minor versions
- Runtime próprio torna debugging mais opaco

---

## 2. Suporte a Tools

### Claude Agent SDK

Tools são definidos como JSON schemas e passados em `tools=[...]` na chamada
`messages.create()`. O modelo retorna `tool_use` blocks que o programador
executa manualmente num loop.

```python
tools = [
    {
        "name": "save_section",
        "description": "Save a completed section to the project document",
        "input_schema": {
            "type": "object",
            "properties": {
                "section_name": {"type": "string"},
                "content": {"type": "string"},
                "state": {"type": "string", "enum": ["parcial", "completo"]},
            },
            "required": ["section_name", "content", "state"],
        },
    }
]

# Agentic loop (implementado pelo programador)
messages = [{"role": "user", "content": task}]
while True:
    response = client.messages.create(model="claude-opus-4-5", tools=tools, messages=messages)
    if response.stop_reason == "end_turn":
        break
    if response.stop_reason == "tool_use":
        tool_result = execute_tool(response.content)
        messages.append({"role": "assistant", "content": response.content})
        messages.append({"role": "user", "content": tool_result})
```

O agentic loop é explícito — o programador controla quando parar, o que executar,
e como tratar erros de tool. Isto é uma vantagem quando a lógica de negócio do
loop é complexa (e.g., BudgetTracker a cada iteração).

### Google ADK

O ADK abstrai o agentic loop no `Runner`. Tools são funções Python decoradas:

```python
from google.adk.tools import FunctionTool

def save_section(section_name: str, content: str, state: str) -> dict:
    """Save a completed section to the project document."""
    # implementation
    return {"status": "saved"}

doctor_agent = LlmAgent(
    name="doctor",
    model="gemini-2.5-pro",
    tools=[FunctionTool(func=save_section)],
    ...
)
```

O ADK invoca as tools automaticamente quando o modelo as pede. Isto é mais conciso
mas menos controlável: não é trivial injectar lógica entre tool call e tool result
(e.g., actualizar o BudgetTracker).

**Veredicto tools:** Claude SDK ganha para workflows com lógica de controlo
complexa entre tool calls. ADK ganha para prototipagem rápida com tools simples.

---

## 3. Streaming

### Claude Agent SDK

```python
with client.messages.stream(
    model="claude-opus-4-5",
    max_tokens=12_000,
    system=DOCTOR_SYSTEM,
    messages=messages,
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)

    # Acesso a usage após stream completo
    final = stream.get_final_message()
    tokens_used = final.usage.input_tokens + final.usage.output_tokens
```

Streaming com acesso a usage no final — essencial para o BudgetTracker.

### Google ADK

O ADK emite `Event` objects durante a execução. Eventos de streaming de texto são
`ContentEvent` com `partial=True`. O acesso a token counts é via a resposta final.

```python
async for event in runner.run_async(...):
    if hasattr(event, "content") and event.content:
        for part in event.content.parts:
            if part.text:
                print(part.text, end="", flush=True)
```

**Veredicto streaming:** Equivalente para o caso de uso do doctor-agent. O Claude
SDK tem uma API ligeiramente mais ergonómica para text streaming.

---

## 4. Memory

### Claude Agent SDK

Sem memória persistente out-of-the-box. O programador gere o histórico de mensagens
explicitamente no array `messages`. Para persistência cross-session, usa uma base de
dados externa.

Para o doctor-agent, o `ProjectDocument` (serializado via `save_project`) serve como
a memória persistente do agente. Cada agente recebe o slice do documento relevante.

### Google ADK

O ADK tem `SessionService` com implementações `InMemorySessionService` e
`DatabaseSessionService`. A session persiste o histórico completo de mensagens
automaticamente.

```python
# Retomar sessão existente
session = await session_service.get_session(app_name="doctor-agent", session_id=existing_id)
```

Para workflows que precisam de referenciar interacções anteriores (e.g., "na sessão
anterior dissemos que o deadline era X"), o ADK tem uma vantagem clara.

**Veredicto memory:** ADK ganha para workflows com necessidade de histórico de
conversação cross-session. Para o doctor-agent (onde a memória relevante é o
`ProjectDocument`, não o histórico de mensagens), a vantagem é marginal.

---

## 5. Multi-agent Coordination

### Claude Agent SDK

Multi-agent é código Python puro. Rider invoca Doctor e Hacker como funções:

```python
async def parallel_fanout(project_doc: ProjectDocument) -> tuple[str, str]:
    doctor_task = asyncio.create_task(doctor_agent(task_a, serialize(project_doc)))
    hacker_task = asyncio.create_task(hacker_agent(task_b, serialize(project_doc)))
    return await asyncio.gather(doctor_task, hacker_task)
```

Sem primitivas de coordenação — tudo é `asyncio`. Isto é simples e previsível.

### Google ADK

O ADK tem primitivas nativas de multi-agent:

```python
from google.adk.agents import SequentialAgent, ParallelAgent

pipeline = SequentialAgent(
    name="rider",
    sub_agents=[doctor_agent, hacker_agent],
)

# Ou em paralelo:
pipeline = ParallelAgent(
    name="rider",
    sub_agents=[doctor_agent, hacker_agent],
)
```

`AgentTool` permite um agente invocar outro como tool call — útil para o padrão
Supervisor-Worker onde o Rider decide em runtime qual agente chamar.

```python
from google.adk.tools.agent_tool import AgentTool

rider_agent = LlmAgent(
    name="rider",
    model="gemini-2.5-pro",
    tools=[AgentTool(agent=doctor_agent), AgentTool(agent=hacker_agent)],
)
```

**Veredicto multi-agent:** ADK tem primitivas mais expressivas. Para o Rider com
os 4 padrões definidos em `swarm_patterns.md`, o ADK pouparia ~30% de código de
coordenação. Mas o acoplamento a Gemini é o custo.

---

## 6. Pricing Considerations (2026)

### Claude Agent SDK

- Pagamento por tokens: `claude-opus-4-5` custa ~$15/M input tokens, ~$75/M output tokens
- Sem custo de infraestrutura do SDK (é um cliente HTTP simples)
- Token budget controlado via `BudgetTracker` — custo previsível

### Google ADK

- O ADK em si é open source e gratuito
- Modelos: `gemini-2.5-pro` via Vertex AI custa ~$1.25/M input, ~$10/M output
  (com contexto até 1M tokens — significativo para dissertações longas)
- Hosting no Google Cloud (Cloud Run, etc.) tem custo adicional
- Para processamento de documentos longos (dissertações de 100+ páginas),
  a janela de contexto de 1M tokens do Gemini é uma vantagem real

**Veredicto pricing:** Para volumes baixos (protótipo, uso pessoal), Claude SDK
tem custo mais previsível. Para volume alto com documentos longos, Gemini via ADK
pode ser mais económico graças à janela de contexto maior (menos chunking necessário).

---

## 7. Maturidade em 2026

### Claude Agent SDK

- API estável desde 2024, sem breaking changes major em 2025/2026
- Documentação excelente, exemplos abundantes no `anthropic-cookbook`
- SLA de suporte garantido pela Anthropic
- `claude-opus-4-5` é o modelo mais capaz disponível em 2026 para raciocínio complexo

### Google ADK

- ADK 1.0 lançado em Abril 2025 (Google Cloud Next '25)
- Breaking changes entre 0.x e 1.x foram significativos
- Em Junho 2026: ADK 1.x estável mas ainda com evolução rápida da API
- Ecosystem de exemplos crescendo mas menos maduro que o Anthropic cookbook
- `gemini-2.5-pro` com thinking mode é competitivo em raciocínio mas tem
  comportamento mais imprevisível em tool use complexo vs Claude

**Veredicto maturidade:** Claude SDK ganha em estabilidade e previsibilidade de API.

---

## 8. Comparação sumária

| Dimensão | Claude Agent SDK | Google ADK |
|---------|-----------------|-----------|
| Modelo de programação | Python puro, sem framework | Runtime + Agent classes |
| Dependências | `anthropic` (1 pkg) | `google-adk` + `google-genai` + deps |
| Agentic loop | Explícito (controlado) | Implícito (automático) |
| Multi-agent primitives | asyncio manual | SequentialAgent, ParallelAgent, AgentTool |
| Session/memory | Manual (ProjectDocument) | Automático (SessionService) |
| Streaming | sim, ergonómico | sim, via Events |
| Tool use control | Total | Parcial (ADK gere o loop) |
| Integração cloud | Agnóstico | Google Cloud nativo |
| Janela de contexto | 200k tokens (Opus 4) | 1M tokens (Gemini 2.5 Pro) |
| Custo (baixo volume) | Previsível | Previsível |
| Custo (alto volume, docs longos) | Maior (janela menor) | Menor (janela maior) |
| Maturidade API | Alta | Média-alta |
| Debugging | Trivial | Moderado |
| Observabilidade | Manual ou Langfuse | Cloud Trace integrado |

---

## 9. Conclusão — Quando usar cada um no contexto doctor-agent

### Usar Claude Agent SDK quando:

- O projecto usa modelos Anthropic (Claude) — sem necessidade de adaptadores
- O agentic loop precisa de lógica de controlo custom entre tool calls
  (e.g., BudgetTracker a cada iteração, quality gate blocking)
- A equipa prefere código Python explícito e auditável sem framework magic
- O deployment é agnóstico de cloud (não há dependência de Google Cloud)
- A janela de contexto de 200k tokens é suficiente (documentos até ~150 páginas)
- A estabilidade de API é crítica (zero downtime por breaking changes do framework)

**Este é o caso do doctor-agent actual.** Implementar com Claude Agent SDK.

### Usar Google ADK quando:

- O projecto já está no Google Cloud stack (Vertex AI, Cloud Run, BigQuery)
- Os documentos a processar têm mais de 150 páginas e a janela de 1M tokens
  do Gemini elimina a necessidade de chunking
- O modelo preferido é Gemini (e.g., por custo ou disponibilidade regional)
- É necessário session management automático com histórico de conversação
  cross-session sem implementar infraestrutura de base de dados
- As primitivas declarativas `SequentialAgent`/`ParallelAgent` mapeiam
  directamente para os padrões de orquestração do Rider (poupança de código)

### Trigger de reavaliação:

Se o doctor-agent crescer para processar dissertações de 200+ páginas em contexto
único (sem chunking), o custo de token do Claude SDK pode tornar o Gemini via ADK
mais atractivo. Reavaliar quando o custo mensal de API ultrapassar €500/mês.

---

## ADR Summary

```
ADR-002: Framework de agentes — Claude Agent SDK vs Google ADK
Status: ACCEPTED
Context: Selecção de framework para orquestração Doctor-Hacker-Rider
Decision: Claude Agent SDK
Consequences:
  - Zero dependências de framework nos módulos core
  - Agentic loop explícito (mais código, mais controlo)
  - Acoplamento a modelos Anthropic
  - Janela de contexto limitada a 200k tokens por chamada
Alternatives considered:
  - Google ADK: rejeitado por acoplamento a Google Cloud e maturidade de API
  - LangGraph: rejeitado por peso de dependências (ver ADR-001 / langgraph_spike.md)
  - OpenAI Agents SDK: rejeitado por não suportar modelos Anthropic nativamente
```
