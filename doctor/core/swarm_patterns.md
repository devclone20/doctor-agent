# Claude Swarm Patterns — Doctor-Hacker-Rider Coordination

**Version:** 1.0 — June 2026  
**Context:** Doctor (writing agent), Hacker (security/research agent), Rider (orchestrator)  
**Reference:** claude-swarm, dsifry/metaswarm, open-multi-agent, anthropic-cookbook

---

## Overview

The Doctor-Hacker-Rider triad implements multi-agent coordination through four
canonical patterns drawn from the Claude Swarm and Metaswarm literature. Each pattern
is chosen based on task structure: whether subtasks are independent or sequential,
whether adversarial pressure improves output quality, and whether a supervisor needs
to maintain global state.

These patterns are encoded in Rider's orchestration logic. The pattern selection
algorithm is:

1. Are subtasks fully independent? → **Parallel Fan-out**
2. Does subtask B require output from subtask A? → **Sequential Chain**
3. Does the output benefit from challenge and counter-argument? → **Debate Mode**
4. Is the task too complex for a single agent but needs a coordinator? → **Supervisor-Worker**

---

## Pattern 1 — Sequential Chain

### Definition

Each agent's output is the next agent's input. The pipeline is linear.

```
Rider
  │
  ├─► Doctor (research + draft)
  │       │
  │       └─► output: draft_sections, citations
  │
  ├─► Hacker (security audit of any external sources used)
  │       │
  │       └─► output: verified_sources, risk_flags
  │
  └─► Doctor (final assembly with verified sources)
```

### When to use

- When each step produces artefacts that are strictly required by the next.
- Example: Doctor drafts methodology → Hacker verifies that cited tools/libraries
  have no known CVEs → Doctor incorporates the findings into the implementation
  section with appropriate caveats.
- Example: Hacker scans for leaked credentials in ingested documents → Doctor
  redacts and rewrites affected passages.

### Implementation notes

```python
# Rider dispatches sequentially, passing context forward
draft = await doctor.run(task="write methodology", context=project_doc)
audit = await hacker.run(task="verify sources", context=draft.citations)
final = await doctor.run(task="finalise methodology", context={**draft, **audit})
```

- Rider holds the shared `ProjectDocument` and passes the relevant slice to each agent.
- Token budget is allocated per step: Doctor gets 12 000 tokens for the draft,
  Hacker gets 5 000 for verification, Doctor gets 8 000 for the final pass.
- If any step fails a quality gate, Rider retries that step before advancing.

### Quality gate

The output of each agent is validated against the `ProjectDocument` schema before
being passed downstream. A malformed or empty output blocks the chain.

---

## Pattern 2 — Parallel Fan-out

### Definition

Rider decomposes the mission into N independent subtasks and dispatches all agents
simultaneously. Results are collected and synthesised by Rider.

```
                    Rider
                   /     \
                  /       \
           Doctor          Hacker
         (write intro)   (audit refs)
                  \       /
                   \     /
                    Rider
                (synthesise)
```

### When to use

- When subtasks share no data dependencies and can safely run concurrently.
- Example: Doctor writes the introduction section while Hacker audits the bibliography
  for retracted papers or suspicious sources. Neither task blocks the other.
- Example: Doctor drafts abstract + conclusion simultaneously (both depend only on
  already-completed sections).
- Example: Rider fans out section drafts across multiple Doctor instances when the
  document type allows parallel authorship (e.g., article with independent methodology
  and related-work sections).

### Implementation notes

```python
# Rider fans out to Doctor and Hacker in parallel
intro_task    = doctor.run(task="write introduction", context=project_doc)
audit_task    = hacker.run(task="audit bibliography", context=project_doc.bibliography)
intro, audit  = await asyncio.gather(intro_task, audit_task)
synthesis     = rider.synthesise([intro, audit])
```

- Each agent receives only the context slice it needs — not the full document.
  This conserves tokens and prevents cross-contamination of agent reasoning.
- The BudgetTracker for each agent is independent; Rider monitors all trackers
  and can cancel a slow agent if the overall mission budget is at risk.
- Wave structure: Fan-out tasks form a single "wave" in the orchestration board.
  All must pass quality gates before the next wave fires.

### Quality gate

Rider checks that fan-out results are non-conflicting before synthesis. Conflicts
(e.g., Doctor and Hacker disagree on a source's validity) are escalated to
Debate Mode (Pattern 3) rather than silently resolved.

---

## Pattern 3 — Debate Mode

### Definition

Two agents are given the same artefact and asked to argue opposite positions.
Rider acts as judge, synthesising the strongest points from each side.

```
        ┌─────────────────────────────────────────┐
        │              Rider (judge)               │
        └────────┬────────────────────┬────────────┘
                 │                    │
          Doctor (proponent)    Hacker (adversary)
         "This methodology     "The cited tool has
          is sound because..."   a known exploit in
                                 version 3.x..."
                 │                    │
        ┌────────┴────────────────────┴────────────┐
        │          Rider synthesises:               │
        │  - Accepts Doctor's methodology           │
        │  - Accepts Hacker's version constraint    │
        │  - Revises section with constraint noted  │
        └───────────────────────────────────────────┘
```

### When to use

- When output quality benefits from adversarial pressure.
- Example: Doctor proposes a research methodology → Hacker argues against every
  assumption to find weaknesses → Rider synthesises a hardened methodology that
  addresses the identified weaknesses.
- Example: Doctor writes a security section in the dissertation → Hacker challenges
  each claim → Rider accepts only claims that survived challenge.
- Example: Choosing between two architectural approaches — Doctor argues for A,
  Hacker argues for B, Rider decides.

### Implementation notes

```python
# Each agent receives the same artefact with opposing instructions
proponent = doctor.run(
    task="defend this methodology",
    context=draft_methodology,
    instruction="argue why this approach is correct and complete"
)
adversary = hacker.run(
    task="challenge this methodology",
    context=draft_methodology,
    instruction="find every weakness, assumption, and gap"
)
pro_result, adv_result = await asyncio.gather(proponent, adversary)
final = rider.adjudicate(pro_result, adv_result, original=draft_methodology)
```

- Rider's adjudication is not averaging — it is principled selection. Claims that
  survive adversarial challenge are accepted; claims that do not are revised or
  removed.
- Debate Mode should be bounded: maximum 2 rounds before Rider makes a final
  decision. Infinite debate loops are treated as an escalation trigger.
- Both agents consume from separate BudgetTrackers; the combined cost must still
  fit within the mission budget.

### Quality gate

The synthesis must resolve every point raised by the adversary. An unresolved
challenge is a gate failure; Rider must either address it or document it as a
known limitation.

---

## Pattern 4 — Supervisor-Worker

### Definition

Rider acts as a stateful supervisor that maintains the global `ProjectDocument`
and dispatches workers (Doctor, Hacker) for atomic subtasks. Workers never
communicate directly with each other — all coordination passes through Rider.

```
┌──────────────────────────────────────────────────────────────────┐
│                      RIDER (supervisor)                           │
│                                                                   │
│   ProjectDocument state machine                                   │
│   SectionDAG (topological order + blocked sections)              │
│   BudgetTracker per worker                                        │
│                                                                   │
│   dispatch_queue: [(section, agent, context), ...]               │
└──────┬─────────────────────────────────────────────┬─────────────┘
       │                                             │
  Doctor worker                               Hacker worker
  (writes one section                         (audits one source
   at a time, returns                          at a time, returns
   completed section)                          verified flag)
       │                                             │
       └────────────────────────────────────────────┘
                           │
                    Rider updates state:
                    - transition(doc, new_state)
                    - marks section complete
                    - unblocks dependent sections
                    - schedules next wave
```

### When to use

- For full dissertation or multi-chapter document generation.
- When the task requires maintaining consistent state across many agent invocations.
- When the Rider needs to enforce the SectionDAG ordering: a section cannot be
  marked complete until its dependencies are at least `parcial`.
- When recovery from partial failure must preserve completed work — Rider can
  checkpoint the `ProjectDocument` after each section and resume from the last
  checkpoint if an agent fails.

### Implementation notes

```python
class RiderSupervisor:
    def __init__(self, doc: ProjectDocument) -> None:
        self.doc = doc
        self.dag = build_dissertation_dag(doc.doc_type)
        self.trackers: dict[str, BudgetTracker] = {
            "doctor": BudgetTracker(AgentBudget.for_agent("doctor")),
            "hacker": BudgetTracker(AgentBudget.for_agent("hacker")),
        }

    async def run(self) -> ProjectDocument:
        while not self.dag.is_complete(self._completed_sections()):
            ready = self.dag.ready_sections(self._completed_sections())
            for section in ready:
                agent  = self._assign_agent(section)
                result = await agent.run(task=f"write {section}", context=self.doc)
                self.doc = self._apply_result(self.doc, section, result)
                save_project(self.doc, checkpoint_path(self.doc.id))
        return transition(self.doc, ProjectState.EM_REVISAO)

    def _completed_sections(self) -> set[str]:
        return {
            name for name, data in self.doc.sections.items()
            if data.get("state") == "completo"
        }

    def _assign_agent(self, section: str) -> Agent:
        # Security-sensitive sections (e.g., threat model) go to Hacker.
        security_sections = {"threat_model", "security_analysis", "risk_assessment"}
        return hacker if section in security_sections else doctor
```

- Checkpointing after each section is non-optional. Full document generation can
  span many agent calls; a crash without checkpoints loses all work.
- The dispatch queue is derived from `SectionDAG.ready_sections()` at each iteration,
  not computed once at the start. This allows the queue to adapt if a section
  transitions to `bloqueado` mid-execution.
- BudgetTracker exhaustion for a worker agent causes Rider to pause that worker's
  queue, synthesise what has been done, and report to the user before continuing.

### Quality gate

After all sections are written, Rider runs Doctor and Hacker in Debate Mode on the
full draft before transitioning to `EM_REVISAO`. This final adversarial pass catches
inconsistencies introduced across independently-written sections.

---

## Pattern Selection Matrix

| Condition | Pattern |
|-----------|---------|
| Steps A → B → C (strict order) | Sequential Chain |
| Steps A, B, C (fully independent) | Parallel Fan-out |
| Output needs challenge/hardening | Debate Mode |
| Complex stateful multi-step task | Supervisor-Worker |
| Mix of sequential and parallel | Supervisor-Worker with fan-out waves |

---

## Token Budget by Pattern

| Pattern | Doctor tokens | Hacker tokens | Rider overhead | Total (est.) |
|---------|--------------|---------------|----------------|-------------|
| Sequential Chain | 20 000–40 000 | 10 000–20 000 | 5 000 | 35 000–65 000 |
| Parallel Fan-out | 12 000–20 000 | 8 000–15 000 | 3 000 | 23 000–38 000 |
| Debate Mode | 15 000–25 000 | 15 000–25 000 | 8 000 | 38 000–58 000 |
| Supervisor-Worker | 80 000–100 000 | 30 000–50 000 | 20 000 | 130 000–170 000 |

Rider enforces these via `BudgetTracker`. When the combined budget of a pattern
exceeds the mission budget, Rider falls back to Sequential Chain (lowest overhead)
and flags the reduction in the Mission Plan.

---

## Error Handling and Recovery

All four patterns follow the same failure recovery ladder:

1. **Agent timeout / empty output** → Retry once with a more specific prompt.
2. **Quality gate failure** → Retry with the gate criteria appended to the prompt.
3. **Two consecutive failures** → Escalate: reassign to the other agent if capable.
4. **Persistent failure** → Replan: Rider rebuilds the task DAG and selects a
   simpler pattern (e.g., Supervisor-Worker degrades to Sequential Chain).
5. **Mission-level failure** → Abort: Rider saves current `ProjectDocument` state,
   prints Final Synthesis Board with ABORT verdict, and reports root cause.

No pattern has a path from failure to success that bypasses quality gates.
