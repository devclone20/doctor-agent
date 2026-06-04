# LangGraph vs Claude Agent SDK — Spike Técnico

**Tipo:** Avaliação arquitectural (ADR-draft)  
**Data:** Junho 2026  
**Contexto:** Orquestração Doctor-Hacker-Rider no projecto doctor-agent  
**Autor:** Rider (Senior Orchestration Agent v2.0)

---

## Resumo executivo

LangGraph oferece um modelo de programação de grafos explícito, stateful e
com checkpointing nativo — o que o torna adequado para orquestração de workflows
longos com estado persistente. O Claude Agent SDK oferece integração nativa com
modelos Anthropic, simplicidade de setup e um modelo de subagente com `Agent()`
que funciona bem para delegation patterns.

**Recomendação:** Claude Agent SDK para a implementação actual do Rider.
Reavaliar LangGraph se o projecto precisar de workflows com mais de 10 nós,
Human-in-the-loop blocking, ou persistência de estado cross-session com
replay de eventos.

---

## 1. Arquitectura de grafo proposta (LangGraph)

Se o Rider fosse implementado em LangGraph, o grafo seria:

```
                    START
                      │
              ┌───────▼────────┐
              │  intake_node   │  — parse mission, classify pattern
              └───────┬────────┘
                      │
              ┌───────▼────────┐
              │   plan_node    │  — build task DAG, print mission board
              └───────┬────────┘
                      │
            ┌─────────┴──────────┐
            │   conditional edge  │
            │  (pattern router)   │
            └──┬──────────┬───────┘
               │          │
       ┌───────▼──┐  ┌────▼──────────┐
       │ parallel │  │  sequential   │
       │ fan-out  │  │    chain      │
       └───────┬──┘  └────┬──────────┘
               │          │
        ┌──────▼──────────▼──────┐
        │   quality_gate_node    │  — blocking check
        └──────────┬─────────────┘
                   │
          ┌────────▼────────┐
          │  synthesis_node │  — final board + GO/ABORT
          └────────┬────────┘
                   │
                  END
```

Nós principais:

| Nó | Tipo | Responsabilidade |
|----|------|-----------------|
| `intake_node` | Regular | Parse da missão, identificação do padrão |
| `plan_node` | Regular | Construção do task DAG, output do mission board |
| `doctor_node` | Agent | Invoca o agente Doctor com contexto delimitado |
| `hacker_node` | Agent | Invoca o agente Hacker com contexto delimitado |
| `quality_gate_node` | Conditional | Avalia critérios de gate; retorna `pass` ou `retry` |
| `synthesis_node` | Regular | Agrega resultados, decide GO/NEEDS WORK/ABORT |

Estado partilhado (TypedDict):

```python
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages

class RiderState(TypedDict):
    mission: str
    pattern: str                        # "sequential" | "fanout" | "debate" | "supervisor"
    project_doc: dict                   # serialised ProjectDocument
    wave_results: dict[str, dict]       # agent_name → result
    gates_passed: list[str]
    retry_counts: dict[str, int]
    messages: Annotated[list, add_messages]
    verdict: str | None                 # "GO" | "NEEDS_WORK" | "ABORT"
```

---

## 2. Vantagens de LangGraph

### 2.1 Estado explícito e checkpointing nativo

LangGraph persiste o estado do grafo após cada nó através do `MemorySaver` ou
`PostgresSaver`. Num workflow de dissertação que pode durar horas, isto significa
que uma falha no nó 7 de 15 não perde o trabalho anterior — o grafo retoma a
partir do checkpoint.

```python
from langgraph.checkpoint.memory import MemorySaver

checkpointer = MemorySaver()
graph = workflow.compile(checkpointer=checkpointer)

# Retomar após falha:
config = {"configurable": {"thread_id": project_id}}
graph.invoke({"mission": "..."}, config=config)
```

### 2.2 Human-in-the-loop (interrupt_before / interrupt_after)

LangGraph suporta interrupção do grafo para aprovação humana antes de nós críticos.
Para o workflow do Rider, isto permite pausar antes de `synthesis_node` e apresentar
o draft ao utilizador para aprovação antes do output final.

```python
graph = workflow.compile(
    checkpointer=checkpointer,
    interrupt_before=["synthesis_node"]
)
```

### 2.3 Streaming de eventos

LangGraph emite eventos granulares (`on_node_start`, `on_node_end`, `on_tool_call`)
que permitem ao Rider actualizar o Live Status Board em tempo real sem polling.

```python
async for event in graph.astream_events(input, config, version="v2"):
    if event["event"] == "on_node_end":
        update_status_board(event["name"], event["data"]["output"])
```

### 2.4 Paralelismo declarativo

A edges paralelas (`add_conditional_edges` com múltiplos targets) permitem fan-out
declarativo sem asyncio manual.

### 2.5 Visualização do grafo

`graph.get_graph().draw_mermaid()` gera o diagrama do workflow automaticamente —
útil para debugging e documentação.

---

## 3. Desvantagens de LangGraph

### 3.1 Dependência pesada

LangGraph puxa `langchain-core` e um ecossistema de dependências. O `doctor-agent`
usa hoje zero dependências externas nos módulos core — adicionar LangGraph muda
esse invariante fundamentalmente.

```
langgraph==0.2.x
├── langchain-core>=0.3
│   ├── pydantic>=2
│   ├── tenacity
│   └── ... (20+ transitive deps)
```

### 3.2 Overhead conceptual para workflows simples

Para o padrão Sequential Chain com 3 agentes (Doctor → Hacker → Doctor), LangGraph
é arquitecturalmente correcto mas verboso em relação ao que seria necessário. O
mesmo workflow em Claude Agent SDK é ~40 linhas vs ~120 em LangGraph.

### 3.3 Acoplamento ao ecossistema LangChain

LangGraph está acoplado ao modelo de `messages` do LangChain (`HumanMessage`,
`AIMessage`, `ToolMessage`). Integrar com a API Anthropic directamente (como o
Claude Agent SDK faz) requer um wrapper ou o uso do `langchain-anthropic` adapter,
que tem lag de versão face ao SDK oficial.

### 3.4 Maturidade em 2026

LangGraph v0.2 estabilizou as APIs mas o modelo de `send()` para fan-out dinâmico
(mapa de agentes) ainda tem edge cases documentados nos issues do repositório.
Para produção, a API do Claude Agent SDK é mais estável e tem SLA de suporte
garantido pela Anthropic.

### 3.5 Debugging de grafos complexos

Quando um grafo tem 15+ nós e múltiplas conditional edges, o stack trace de um
erro de nó é difícil de seguir. O Claude Agent SDK tem um modelo de debugging mais
directo (python stack traces normais).

---

## 4. Claude Agent SDK — características relevantes

### 4.1 `Agent()` e subagentes nativos

```python
from anthropic import Anthropic
client = Anthropic()

# Subagente com budget controlado
response = client.messages.create(
    model="claude-opus-4-5",
    max_tokens=12_000,
    system=doctor_system_prompt,
    messages=[{"role": "user", "content": task_context}]
)
```

O SDK não tem um modelo de subagente explícito — a "orquestração" é código Python
normal que chama `client.messages.create()` para cada agente. Isto é uma vantagem
(sem magia) e uma desvantagem (sem checkpointing automático).

### 4.2 Streaming nativo

```python
with client.messages.stream(...) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

Suporte para streaming parcial de texto — útil para o Rider mostrar progresso
do agente em tempo real sem esperar pelo response completo.

### 4.3 Tool use

O SDK tem suporte nativo a `tools` com JSON schema validation. O Rider pode
definir `transition_state`, `mark_section_complete`, `check_budget` como tools
que os agentes invocam directamente.

### 4.4 Sem estado automático

O Claude Agent SDK não persiste estado entre chamadas. O Rider tem de gerir o
`ProjectDocument` explicitamente (via `save_project` / `load_project`) e passar
o contexto relevante em cada chamada.

---

## 5. POC mínimo em pseudocódigo Python

### 5.1 LangGraph (Sequential Chain, Doctor → Hacker → Doctor)

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    project_doc: dict
    draft: str
    audit: dict
    final: str

def doctor_draft_node(state: State) -> State:
    draft = call_anthropic(
        system=DOCTOR_SYSTEM,
        prompt=f"Write methodology for: {state['project_doc']['topic']}",
        max_tokens=12_000,
    )
    return {**state, "draft": draft}

def hacker_audit_node(state: State) -> State:
    audit = call_anthropic(
        system=HACKER_SYSTEM,
        prompt=f"Audit sources in this draft:\n{state['draft']}",
        max_tokens=5_000,
    )
    return {**state, "audit": audit}

def doctor_finalise_node(state: State) -> State:
    final = call_anthropic(
        system=DOCTOR_SYSTEM,
        prompt=f"Revise draft using audit findings:\n{state['draft']}\nAudit: {state['audit']}",
        max_tokens=8_000,
    )
    return {**state, "final": final}

workflow = StateGraph(State)
workflow.add_node("doctor_draft", doctor_draft_node)
workflow.add_node("hacker_audit", hacker_audit_node)
workflow.add_node("doctor_finalise", doctor_finalise_node)
workflow.set_entry_point("doctor_draft")
workflow.add_edge("doctor_draft", "hacker_audit")
workflow.add_edge("hacker_audit", "doctor_finalise")
workflow.add_edge("doctor_finalise", END)

graph = workflow.compile(checkpointer=MemorySaver())
result = graph.invoke({"project_doc": project_doc})
```

### 5.2 Claude Agent SDK (Sequential Chain, equivalente)

```python
from anthropic import Anthropic
from doctor.core.budget import BudgetTracker, AgentBudget
from doctor.core.project_state import save_project

client = Anthropic()

def run_sequential_chain(project_doc: ProjectDocument) -> str:
    doctor_tracker = BudgetTracker(AgentBudget.for_agent("doctor"))
    hacker_tracker = BudgetTracker(AgentBudget.for_agent("hacker"))

    # Step 1: Doctor drafts
    r1 = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=12_000,
        system=DOCTOR_SYSTEM,
        messages=[{"role": "user", "content": f"Write methodology: {project_doc.topic}"}],
    )
    doctor_tracker.consume_tokens(r1.usage.input_tokens + r1.usage.output_tokens)
    draft = r1.content[0].text

    # Step 2: Hacker audits
    r2 = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=5_000,
        system=HACKER_SYSTEM,
        messages=[{"role": "user", "content": f"Audit sources:\n{draft}"}],
    )
    hacker_tracker.consume_tokens(r2.usage.input_tokens + r2.usage.output_tokens)
    audit = r2.content[0].text

    # Step 3: Doctor finalises
    r3 = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=8_000,
        system=DOCTOR_SYSTEM,
        messages=[{"role": "user", "content": f"Revise:\n{draft}\nAudit:\n{audit}"}],
    )
    doctor_tracker.consume_tokens(r3.usage.input_tokens + r3.usage.output_tokens)

    # Checkpoint
    save_project(project_doc, checkpoint_path(project_doc.id))

    return r3.content[0].text
```

### Comparação de LOC e complexidade

| Dimensão | LangGraph | Claude Agent SDK |
|---------|-----------|-----------------|
| LOC para Sequential Chain 3 nós | ~80 | ~45 |
| LOC para Fan-out 2 agentes | ~60 | ~35 (asyncio.gather) |
| Checkpointing | automático | manual (2 linhas) |
| Dependências adicionadas | 20+ | 0 |
| Debugging | LangSmith ou raw | Python standard |
| Streaming granular | sim (eventos) | sim (text_stream) |

---

## 6. Recomendação final

**Decisão: Claude Agent SDK para o Rider actual.**

Justificação:

1. **Zero dependências adicionais.** Os módulos `project_state.py`, `section_dag.py`
   e `budget.py` são stdlib puro. Adicionar LangGraph quebraria este invariante
   sem benefício proporcional para os workflows actuais (≤5 agentes, ≤4 waves).

2. **Checkpointing é trivial com `save_project`.** A persistência de estado que o
   LangGraph oferece automaticamente é replicável em 2 linhas usando o `ProjectDocument`
   + `save_project`. Não justifica o peso de `langchain-core`.

3. **O modelo de programação Python explícito é mais fácil de auditar.** O Rider é
   um agente de segurança e qualidade — o seu próprio código deve ser transparente.
   LangGraph graphs com conditional edges são difíceis de auditar para um revisor externo.

4. **Reavaliar quando:**
   - O número de agentes no Rider cresce para 10+
   - É necessário Human-in-the-loop blocking no meio de um workflow (não apenas no início/fim)
   - É necessário replay de eventos para debugging de produção
   - O workflow precisa de persistir estado entre sessões de utilizadores distintos
     (cross-session, não cross-call dentro da mesma sessão)

**ADR status:** ACCEPTED — implementar com Claude Agent SDK.  
**Review trigger:** quando qualquer uma das condições de reavaliação acima se tornar requisito.
