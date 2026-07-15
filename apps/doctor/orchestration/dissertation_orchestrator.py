"""
Dissertation generation orchestrator — PROPOSTA-RID-1.

Coordinates multi-section dissertation generation using the SectionDAG to
determine topological order and dependency readiness. Integrates with
BudgetTracker to enforce token budget with automatic warning and hard stop.

State is serialisable to JSON so an interrupted run can be resumed.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Literal

from doctor.core.budget import AgentBudget, BudgetExhaustedError, BudgetTracker, WARN_THRESHOLD
from doctor.core.section_dag import DocType, SectionDAG, build_dissertation_dag

# ---------------------------------------------------------------------------
# Token budget estimate per section type.
# Values are conservative upper bounds based on typical output size.
# ---------------------------------------------------------------------------

_SECTION_TOKEN_BUDGET: dict[str, int] = {
    "introduction": 8_000,
    "related_work": 12_000,
    "background": 10_000,
    "theoretical_framework": 10_000,
    "methodology": 10_000,
    "implementation": 8_000,
    "evaluation": 10_000,
    "contributions": 6_000,
    "results": 8_000,
    "discussion": 8_000,
    "future_work": 4_000,
    "conclusion": 5_000,
    "abstract": 2_000,
    "acknowledgements": 1_000,
}

_DEFAULT_SECTION_TOKEN_BUDGET = 6_000


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

TaskStatus = Literal["pending", "ready", "in_progress", "done", "failed"]


@dataclass
class DissertationTask:
    """Represents the generation task for a single dissertation section."""

    section: str
    status: TaskStatus
    dependencies: list[str]
    output_path: Path | None = None
    tokens_used: int = 0
    error: str | None = None

    def estimated_tokens(self) -> int:
        return _SECTION_TOKEN_BUDGET.get(self.section, _DEFAULT_SECTION_TOKEN_BUDGET)

    # ------------------------------------------------------------------
    # JSON serialisation — Path is not JSON-serialisable natively
    # ------------------------------------------------------------------

    def to_dict(self) -> dict:
        d = asdict(self)
        d["output_path"] = str(self.output_path) if self.output_path else None
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "DissertationTask":
        op = d.get("output_path")
        return cls(
            section=d["section"],
            status=d["status"],
            dependencies=d["dependencies"],
            output_path=Path(op) if op else None,
            tokens_used=d.get("tokens_used", 0),
            error=d.get("error"),
        )


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


class DissertationOrchestrator:
    """Stateful orchestrator for sequenced dissertation section generation.

    The orchestrator owns the task list (derived from the SectionDAG), tracks
    status transitions, enforces the token budget, and provides persistence so
    a failed run can be resumed.

    Lifecycle:
        1. ``build_plan()``          — derive tasks from DAG (call once).
        2. ``next_ready()``          — tasks whose deps are all done.
        3. Mark each task via        ``mark_done`` / ``mark_failed``.
        4. Repeat until              ``is_complete()`` or ``has_failed()``.
    """

    def __init__(
        self,
        topic: str,
        doc_type: str,
        project_dir: Path,
        budget_tokens: int = 100_000,
    ) -> None:
        _valid = {"bsc", "msc", "phd", "article"}
        if doc_type not in _valid:
            raise ValueError(f"doc_type must be one of {sorted(_valid)}, got {doc_type!r}")

        self.topic = topic
        self.doc_type = doc_type
        self.project_dir = project_dir
        self._budget_tracker = BudgetTracker(
            budget=AgentBudget(
                agent_name="dissertation_orchestrator",
                max_tokens=budget_tokens,
                max_tool_calls=200,  # not the primary constraint here
            )
        )
        self._tasks: list[DissertationTask] = []
        self._dag: SectionDAG | None = None

    # ------------------------------------------------------------------
    # Plan construction
    # ------------------------------------------------------------------

    def build_plan(self) -> list[DissertationTask]:
        """Build the ordered task list from the canonical SectionDAG.

        Returns tasks in topological order (root sections first).
        Calling this more than once replaces the previous plan.
        """
        self._dag = build_dissertation_dag(self.doc_type)
        order = self._dag.topological_order()

        # Extract deps for each section: a section's direct dependencies are
        # exactly the sections it is blocked on when no work has been done yet.
        all_blocked = self._dag.blocked_sections(set())
        deps_map: dict[str, list[str]] = {section: all_blocked.get(section, []) for section in order}

        self._tasks = [
            DissertationTask(
                section=section,
                status="pending",
                dependencies=deps_map[section],
            )
            for section in order
        ]

        # Mark root tasks (no deps) as immediately ready
        for task in self._tasks:
            if not task.dependencies:
                task.status = "ready"

        return list(self._tasks)

    # ------------------------------------------------------------------
    # State queries
    # ------------------------------------------------------------------

    def _task_by_section(self, section: str) -> DissertationTask:
        for t in self._tasks:
            if t.section == section:
                return t
        raise KeyError(f"No task for section {section!r}")

    def next_ready(self) -> list[DissertationTask]:
        """Return tasks whose every dependency is marked ``done`` and which are
        currently ``ready`` (not in_progress, done, or failed)."""
        done_sections = {t.section for t in self._tasks if t.status == "done"}
        ready: list[DissertationTask] = []
        for task in self._tasks:
            if task.status != "pending":
                continue
            if all(dep in done_sections for dep in task.dependencies):
                task.status = "ready"
                ready.append(task)
            elif task.status == "ready":
                ready.append(task)
        # Also include already-marked ready tasks
        ready = [t for t in self._tasks if t.status == "ready"]
        return ready

    def is_complete(self) -> bool:
        """True when every task has reached ``done`` status."""
        return bool(self._tasks) and all(t.status == "done" for t in self._tasks)

    def has_failed(self) -> bool:
        """True when at least one task has reached ``failed`` status."""
        return any(t.status == "failed" for t in self._tasks)

    def budget_exhausted(self) -> bool:
        return self._budget_tracker.is_exhausted()

    # ------------------------------------------------------------------
    # State transitions
    # ------------------------------------------------------------------

    def mark_in_progress(self, section: str) -> None:
        task = self._task_by_section(section)
        if task.status not in ("ready", "pending"):
            raise ValueError(
                f"Cannot mark {section!r} as in_progress from status {task.status!r}"
            )
        task.status = "in_progress"

    def mark_done(self, section: str, output_path: Path, tokens_used: int) -> None:
        """Record successful completion of a section.

        Updates the budget tracker and promotes any newly unblocked tasks to
        ``ready``. Raises ``BudgetExhaustedError`` if the hard token limit is hit.
        """
        task = self._task_by_section(section)
        task.status = "done"
        task.output_path = output_path
        task.tokens_used = tokens_used

        self._budget_tracker.consume_tokens(tokens_used)

        if self._budget_tracker.warn_if_above(WARN_THRESHOLD):
            msg = self._budget_tracker.warning_message()
            if msg:
                print(f"\n[BUDGET] {msg}")

        if self._budget_tracker.is_exhausted():
            self.save_state(self.project_dir / "orchestrator_state.json")
            raise BudgetExhaustedError("dissertation_orchestrator")

        # Promote newly unblocked tasks
        done_sections = {t.section for t in self._tasks if t.status == "done"}
        for t in self._tasks:
            if t.status == "pending" and all(dep in done_sections for dep in t.dependencies):
                t.status = "ready"

    def mark_failed(self, section: str, error: str) -> None:
        task = self._task_by_section(section)
        task.status = "failed"
        task.error = error

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    def progress_report(self) -> str:
        """Human-readable progress report with budget status."""
        if not self._tasks:
            return "No plan built yet. Call build_plan() first."

        total = len(self._tasks)
        done = sum(1 for t in self._tasks if t.status == "done")
        failed = sum(1 for t in self._tasks if t.status == "failed")
        in_progress = sum(1 for t in self._tasks if t.status == "in_progress")
        pending = sum(1 for t in self._tasks if t.status in ("pending", "ready"))
        pct = (done / total * 100) if total else 0.0

        tokens_used = self._budget_tracker.budget.used_tokens
        tokens_max = self._budget_tracker.budget.max_tokens
        token_pct = tokens_used / tokens_max * 100 if tokens_max else 0.0

        lines: list[str] = [
            f"Dissertation: {self.topic[:60]}",
            f"Type: {self.doc_type.upper()}  |  Sections: {total}",
            f"",
            f"Progress: {done}/{total} done ({pct:.0f}%)  "
            f"|  {in_progress} in-progress  |  {pending} pending  |  {failed} failed",
            f"Budget:   {tokens_used:,}/{tokens_max:,} tokens ({token_pct:.1f}%)",
            f"",
        ]

        status_icon = {"done": "v", "failed": "X", "in_progress": ">", "ready": "~", "pending": "."}
        for task in self._tasks:
            icon = status_icon.get(task.status, "?")
            dep_str = f"  deps: {task.dependencies}" if task.dependencies else ""
            token_str = f"  [{task.tokens_used:,} tok]" if task.tokens_used else ""
            err_str = f"  ERROR: {task.error}" if task.error else ""
            lines.append(f"  [{icon}] {task.section:<30}{dep_str}{token_str}{err_str}")

        return "\n".join(lines)

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save_state(self, path: Path) -> None:
        """Serialise orchestrator state to JSON for resumption after failure."""
        path.parent.mkdir(parents=True, exist_ok=True)
        state = {
            "topic": self.topic,
            "doc_type": self.doc_type,
            "project_dir": str(self.project_dir),
            "budget_tokens": self._budget_tracker.budget.max_tokens,
            "tokens_used": self._budget_tracker.budget.used_tokens,
            "tasks": [t.to_dict() for t in self._tasks],
        }
        path.write_text(json.dumps(state, indent=2), encoding="utf-8")

    @classmethod
    def load_state(cls, path: Path) -> "DissertationOrchestrator":
        """Restore an orchestrator from a previously saved JSON state file."""
        raw = json.loads(path.read_text(encoding="utf-8"))
        inst = cls(
            topic=raw["topic"],
            doc_type=raw["doc_type"],
            project_dir=Path(raw["project_dir"]),
            budget_tokens=raw["budget_tokens"],
        )
        inst._budget_tracker.consume_tokens(raw.get("tokens_used", 0))
        inst._tasks = [DissertationTask.from_dict(d) for d in raw["tasks"]]
        return inst


# ---------------------------------------------------------------------------
# High-level entry point
# ---------------------------------------------------------------------------


def orchestrate_dissertation(
    topic: str,
    doc_type: str,
    project_dir: Path,
    dry_run: bool = False,
) -> str:
    """Orchestrate full dissertation generation (or simulate in dry_run mode).

    Prints the execution plan to stdout and, when not dry_run, simulates the
    generation loop in dependency order with progress updates.

    Returns the final progress report string.
    """
    orchestrator = DissertationOrchestrator(topic, doc_type, project_dir)
    tasks = orchestrator.build_plan()

    # --- Print plan ---
    print(f"\nDissertation Plan — {doc_type.upper()}: {topic}\n")
    print(f"  {'Section':<30} {'Est. Tokens':>12}  Dependencies")
    print(f"  {'-'*30} {'-'*12}  {'-'*40}")
    total_estimated = 0
    for task in tasks:
        est = task.estimated_tokens()
        total_estimated += est
        deps = ", ".join(task.dependencies) if task.dependencies else "—"
        print(f"  {task.section:<30} {est:>12,}  {deps}")
    print(f"\n  Total estimated tokens: {total_estimated:,}")
    print(f"  Budget: {orchestrator._budget_tracker.budget.max_tokens:,} tokens\n")

    if dry_run:
        print("  [dry-run] Execution skipped.\n")
        return orchestrator.progress_report()

    # --- Simulate execution loop ---
    print("  Simulating execution...\n")
    import time

    iteration = 0
    max_iterations = len(tasks) * 3  # safety ceiling

    while not orchestrator.is_complete() and not orchestrator.has_failed() and iteration < max_iterations:
        iteration += 1
        ready = orchestrator.next_ready()
        if not ready:
            break

        # In real usage the orchestrator dispatches sub-agents concurrently.
        # Here we simulate sequential execution for demonstration.
        for task in ready:
            orchestrator.mark_in_progress(task.section)
            print(f"  > Generating: {task.section}...")
            simulated_tokens = task.estimated_tokens()
            out_path = project_dir / f"{task.section}.md"
            try:
                orchestrator.mark_done(task.section, out_path, simulated_tokens)
                print(f"    v Done: {task.section}  [{simulated_tokens:,} tokens]")
            except BudgetExhaustedError:
                print(f"\n  [BUDGET EXHAUSTED] State saved. Resume with load_state().\n")
                return orchestrator.progress_report()

    print()
    return orchestrator.progress_report()
