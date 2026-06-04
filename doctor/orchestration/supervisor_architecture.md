# Supervisor Architecture — Multi-Section Dissertation Generation

## Overview

The Supervisor pattern decouples routing intelligence from generation work.
A central Supervisor node inspects shared state after every action and decides
what happens next. Workers and Reviewers are stateless actors that receive a
task and return a result. The state object is the single source of truth.

---

## State Graph (ASCII Diagram)

```
                        ┌─────────────────────────────┐
                        │         SupervisorNode       │
                        │                             │
                        │  route(state) -> Action     │
                        └──────────────┬──────────────┘
                                       │
              ┌────────────────────────┼───────────────────────┐
              │                        │                       │
              v                        v                       v
   ┌──────────────────┐    ┌──────────────────────┐    ┌──────────────┐
   │   WorkerNode      │    │    ReviewerNode       │    │  Terminal    │
   │                  │    │                      │    │              │
   │ execute(state,   │    │ review(content,      │    │  complete    │
   │   section)       │    │   section)           │    │  abort       │
   │  -> (str, int)   │    │  -> (bool, str)      │    │              │
   └────────┬─────────┘    └──────────┬───────────┘    └──────────────┘
            │                         │
            │  content placed          │  approved → sections_done
            │  in pending_review       │  rejected → retry or fail
            │                         │
            └──────────> state <───────┘
                          │
                          │  (next iteration)
                          v
                   SupervisorNode.route()
```

**Edge conditions:**

| From        | Condition                           | To               |
|-------------|-------------------------------------|------------------|
| Supervisor  | pending_review not empty            | ReviewerNode     |
| Supervisor  | next section available              | WorkerNode       |
| Supervisor  | all sections done                   | complete         |
| Supervisor  | abort condition / iteration limit   | abort            |
| WorkerNode  | generation failure + retry budget   | Supervisor       |
| ReviewerNode| rejected + retry budget             | Supervisor (re-dispatch) |
| ReviewerNode| rejected + no retries               | sections_failed  |

---

## LangGraph Implementation (pseudocode)

```python
from langgraph.graph import StateGraph, END

# 1. Define typed state
class DissertationState(TypedDict):
    topic: str
    doc_type: str
    sections_todo: list[str]
    sections_done: list[str]
    sections_failed: list[str]
    current_section: str | None
    pending_review: dict[str, str]
    retry_counts: dict[str, int]
    iteration: int

# 2. Define node functions
def supervisor_node(state: DissertationState) -> DissertationState:
    """Pure function: inspect state, set current_section, return updated state."""
    ...

def worker_node(state: DissertationState) -> DissertationState:
    """Generate content for state["current_section"]; update pending_review."""
    section = state["current_section"]
    content = call_doctor_agent(state["topic"], section)
    return {**state, "pending_review": {**state["pending_review"], section: content}}

def reviewer_node(state: DissertationState) -> DissertationState:
    """Review all pending content; update sections_done / sections_failed."""
    ...

def route_supervisor(state: DissertationState) -> str:
    """Conditional edge: returns node name or END."""
    if state["iteration"] >= MAX_ITER:
        return END
    if all sections done:
        return END
    if state["pending_review"]:
        return "reviewer"
    if next_section_available(state):
        return "worker"
    return END

# 3. Build graph
graph = StateGraph(DissertationState)
graph.add_node("supervisor", supervisor_node)
graph.add_node("worker", worker_node)
graph.add_node("reviewer", reviewer_node)

graph.set_entry_point("supervisor")
graph.add_conditional_edges("supervisor", route_supervisor, {
    "worker":   "worker",
    "reviewer": "reviewer",
    END:        END,
})
graph.add_edge("worker",   "supervisor")
graph.add_edge("reviewer", "supervisor")

runnable = graph.compile()
final_state = runnable.invoke(initial_state)
```

Key LangGraph properties used:
- `StateGraph` — typed state dict threaded through all nodes
- `add_conditional_edges` — supervisor routing as a function returning node names
- `add_edge` — unconditional return to supervisor after each worker/reviewer step
- `compile()` — produces a `Runnable` compatible with LCEL

---

## Claude Agent SDK Implementation

With the Claude Agent SDK, the Supervisor becomes a parent agent that spawns
sub-agents for generation and review.

```python
import anthropic

client = anthropic.Anthropic()

def run_supervisor(topic: str, doc_type: str, sections: list[str]) -> dict:
    state = build_initial_state(topic, doc_type, sections)

    while not is_terminal(state):
        action = supervisor_route(state)

        if action == "generate":
            section = state["current_section"]
            # Spawn a Doctor sub-agent for this section
            result = client.messages.create(
                model="claude-opus-4-5",
                max_tokens=8192,
                system=build_worker_system_prompt(topic, doc_type),
                messages=[{"role": "user", "content": f"Write section: {section}"}],
            )
            content = result.content[0].text
            state["pending_review"][section] = content

        elif action == "review":
            for section, content in list(state["pending_review"].items()):
                result = client.messages.create(
                    model="claude-opus-4-5",
                    max_tokens=2048,
                    system=build_reviewer_system_prompt(),
                    messages=[{"role": "user", "content": f"Review:\n\n{content}"}],
                )
                approved, feedback = parse_review_response(result.content[0].text)
                update_state_after_review(state, section, approved, feedback)
                del state["pending_review"][section]

        state["iteration"] += 1

    return state
```

The Supervisor itself is not an agent — it is ordinary Python control flow.
Only the Workers and Reviewers are Claude API calls. This keeps routing logic
deterministic and testable without LLM inference cost.

---

## Trade-off Comparison

| Dimension            | Stdlib Prototype           | LangGraph               | Claude Agent SDK          |
|----------------------|---------------------------|-------------------------|---------------------------|
| External deps        | None                      | `langgraph`, `langchain`| `anthropic`               |
| State management     | Manual dataclass          | TypedDict + reducer     | Manual dict / dataclass   |
| Routing              | if/elif in Python         | `add_conditional_edges` | if/elif in Python         |
| Parallelism          | Sequential (trivially extended to asyncio) | Parallel branches via Send API | asyncio + gather  |
| Observability        | Custom log list           | LangSmith tracing       | Custom or Weave           |
| Streaming            | Not built-in              | `stream_mode`           | `stream=True`             |
| Resumability         | Serialize state to JSON   | Checkpointer (SQLite/Postgres) | Serialize state to JSON |
| Testability          | Pure functions, easy mock | Requires graph harness  | Requires API mock         |
| Learning curve       | Zero                      | Moderate                | Low                       |
| Production readiness | Prototype only            | Production-grade        | Production-grade          |

---

## When to Use Each Approach

**Stdlib prototype** — during architecture exploration, when you need to validate
the routing logic without any framework overhead. Ship this as a spike, not to
production.

**LangGraph** — when you need built-in persistence (checkpointing), streaming
intermediate state to a UI, parallel branch execution (multiple sections
concurrently), or LangSmith observability. Best when the graph structure is
complex and conditional edges would be unreadable as plain if/elif.

**Claude Agent SDK** — when the orchestration logic is straightforward but the
agents need long context, tool use, or multi-turn reasoning. The SDK gives you
direct control over every API call without framework abstractions. Prefer this
when the team already owns the infrastructure and does not want a new framework
dependency.

**Rule of thumb:** if you have more than 3 conditional routing paths or need
parallel section generation with independent checkpoints, reach for LangGraph.
If the graph is a simple Supervisor → Worker → Reviewer loop and you control
the infrastructure, the Agent SDK with manual state is sufficient.
