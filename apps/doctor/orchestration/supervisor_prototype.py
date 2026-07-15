"""
Supervisor pattern prototype for multi-section dissertation generation — PROPOSTA-RID-2.

Implements the Supervisor → Worker → Reviewer loop using Python 3.11+ stdlib only.
No LangGraph or external orchestration framework required.

Run as a module to see a live simulation:
    python -m doctor.orchestration.supervisor_prototype
"""

from __future__ import annotations

import random
import sys
from dataclasses import dataclass, field
from typing import Literal

# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------

Action = Literal["generate_section", "review_section", "retry", "complete", "abort"]


@dataclass
class SupervisorState:
    """Shared mutable state threaded through every node in the supervisor loop."""

    topic: str
    doc_type: str
    sections_todo: list[str]
    sections_done: list[str] = field(default_factory=list)
    sections_failed: list[str] = field(default_factory=list)
    current_section: str | None = None
    # Pending content awaiting review — keyed by section name
    pending_review: dict[str, str] = field(default_factory=dict)
    review_feedback: dict[str, str] = field(default_factory=dict)
    retry_counts: dict[str, int] = field(default_factory=dict)
    messages: list[str] = field(default_factory=list)
    iteration: int = 0
    max_iterations: int = 50

    # Derived helpers
    def log(self, msg: str) -> None:
        self.messages.append(msg)

    def all_done(self) -> bool:
        return set(self.sections_todo) <= set(self.sections_done)

    def has_abort_condition(self) -> bool:
        # Abort if more than half the sections are unrecoverably failed
        return len(self.sections_failed) > len(self.sections_todo) // 2

    def next_pending_section(self) -> str | None:
        """Return first section not yet done, failed, or in review."""
        in_review = set(self.pending_review.keys())
        done_or_failed = set(self.sections_done) | set(self.sections_failed)
        for s in self.sections_todo:
            if s not in done_or_failed and s not in in_review:
                return s
        return None


# ---------------------------------------------------------------------------
# Nodes
# ---------------------------------------------------------------------------

_MAX_RETRIES = 2


class SupervisorNode:
    """Decides what happens next based on the current state.

    Routing logic (no side effects):
      - If iteration limit reached → "abort"
      - If all sections done → "complete"
      - If abort condition met → "abort"
      - If there is content pending review → "review_section"
      - If there is a section to generate → "generate_section"
      - Otherwise → "complete" (nothing left to do)
    """

    def route(self, state: SupervisorState) -> Action:
        if state.iteration >= state.max_iterations:
            state.log(f"[Supervisor] Iteration limit {state.max_iterations} reached — aborting.")
            return "abort"

        if state.has_abort_condition():
            state.log(f"[Supervisor] Too many failed sections ({len(state.sections_failed)}) — aborting.")
            return "abort"

        if state.all_done():
            state.log("[Supervisor] All sections complete — finishing.")
            return "complete"

        if state.pending_review:
            state.log(f"[Supervisor] Content pending review: {list(state.pending_review.keys())}.")
            return "review_section"

        next_section = state.next_pending_section()
        if next_section:
            state.current_section = next_section
            state.log(f"[Supervisor] Dispatching generation for section: {next_section}.")
            return "generate_section"

        # Nothing pending and nothing failed — we must be done
        return "complete"


class WorkerNode:
    """Simulates section content generation.

    In production this node dispatches a Doctor sub-agent (or LangGraph worker)
    and returns the real generated content with actual token counts.
    """

    # Simulated failure rate to exercise retry logic
    _SIMULATED_FAILURE_RATE: float = 0.15

    def execute(self, state: SupervisorState, section: str) -> tuple[str, int]:
        """Simulate generating *section* content.

        Returns (content_placeholder, tokens_estimated).
        Raises RuntimeError on simulated generation failure.
        """
        if random.random() < self._SIMULATED_FAILURE_RATE:
            raise RuntimeError(f"Simulated generation failure for section '{section}'")

        content = (
            f"# {section.replace('_', ' ').title()}\n\n"
            f"[Placeholder content for {section} of '{state.topic}' "
            f"({state.doc_type.upper()}). "
            f"This section addresses the core aspects of the research topic "
            f"with appropriate academic rigour and citation density.]\n"
        )
        # Estimate tokens proportional to section type
        token_estimates: dict[str, int] = {
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
        tokens = token_estimates.get(section, 6_000)
        state.log(f"[Worker] Generated {section} ({tokens:,} tokens).")
        return content, tokens


class ReviewerNode:
    """Simulates academic quality review of generated section content.

    In production this invokes a dedicated review sub-agent or a structured
    Claude prompt that checks coherence, citation density, and depth.
    """

    _SIMULATED_REJECTION_RATE: float = 0.20

    def review(self, content: str, section: str) -> tuple[bool, str]:
        """Simulate reviewing *content* for section *section*.

        Returns (approved, feedback).
        """
        if random.random() < self._SIMULATED_REJECTION_RATE:
            feedback = (
                f"Section '{section}' requires revision: insufficient citation depth, "
                f"unclear contribution statement, or missing evaluation criteria."
            )
            return False, feedback

        return True, f"Section '{section}' meets academic standards."


# ---------------------------------------------------------------------------
# Supervisor loop
# ---------------------------------------------------------------------------


def run_supervisor_loop(
    topic: str,
    doc_type: str,
    sections: list[str] | None = None,
    max_iterations: int = 50,
) -> SupervisorState:
    """Execute the supervisor loop for the given topic and document type.

    *sections* defaults to the canonical section list for *doc_type* when not
    provided. The loop terminates on completion, abort, or ``max_iterations``.
    """
    from doctor.core.section_dag import build_dissertation_dag

    if sections is None:
        dag = build_dissertation_dag(doc_type)
        sections = dag.topological_order()

    state = SupervisorState(
        topic=topic,
        doc_type=doc_type,
        sections_todo=list(sections),
        max_iterations=max_iterations,
    )

    supervisor = SupervisorNode()
    worker = WorkerNode()
    reviewer = ReviewerNode()

    while True:
        state.iteration += 1
        action = supervisor.route(state)

        if action == "complete":
            state.log("[Loop] Dissertation complete.")
            break

        if action == "abort":
            state.log("[Loop] Aborting — unrecoverable state.")
            break

        if action == "generate_section":
            section = state.current_section
            assert section is not None, "Supervisor routed to generate_section without setting current_section"
            try:
                content, _tokens = worker.execute(state, section)
                state.pending_review[section] = content
            except RuntimeError as exc:
                retries = state.retry_counts.get(section, 0)
                if retries < _MAX_RETRIES:
                    state.retry_counts[section] = retries + 1
                    state.log(f"[Loop] Generation failed for {section} — retry {retries + 1}/{_MAX_RETRIES}.")
                else:
                    state.sections_failed.append(section)
                    state.log(f"[Loop] Section {section} failed permanently: {exc}")
            state.current_section = None

        elif action == "review_section":
            for section, content in list(state.pending_review.items()):
                approved, feedback = reviewer.review(content, section)
                state.review_feedback[section] = feedback
                del state.pending_review[section]

                if approved:
                    state.sections_done.append(section)
                    state.log(f"[Reviewer] Approved: {section}.")
                else:
                    retries = state.retry_counts.get(section, 0)
                    if retries < _MAX_RETRIES:
                        state.retry_counts[section] = retries + 1
                        state.log(
                            f"[Reviewer] Rejected {section} (retry {retries + 1}/{_MAX_RETRIES}): {feedback}"
                        )
                        # Put back into pending generation by ensuring it is not
                        # in done/failed — the supervisor will re-dispatch it.
                    else:
                        state.sections_failed.append(section)
                        state.log(f"[Reviewer] Section {section} failed review permanently: {feedback}")

    return state


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def _render_state(state: SupervisorState) -> None:
    width = 60
    print("=" * width)
    print(f"  Supervisor Loop — {state.doc_type.upper()}")
    print(f"  Topic: {state.topic[:50]}")
    print("=" * width)
    print(f"  Iterations:      {state.iteration}/{state.max_iterations}")
    print(f"  Sections done:   {len(state.sections_done)}/{len(state.sections_todo)}")
    print(f"  Sections failed: {len(state.sections_failed)}")
    print()

    print("  Section status:")
    for s in state.sections_todo:
        if s in state.sections_done:
            icon = "[v]"
        elif s in state.sections_failed:
            icon = "[X]"
        elif s in state.pending_review:
            icon = "[?]"  # in review
        else:
            icon = "[ ]"
        print(f"    {icon} {s}")

    print()
    print("  Event log:")
    for msg in state.messages:
        print(f"    {msg}")
    print("=" * width)


def main() -> None:
    random.seed(42)  # reproducible demo output

    topic = "Federated Learning para detecção de anomalias em redes IoT"
    doc_type = "msc"

    print(f"\nRunning supervisor prototype...")
    print(f"Topic:    {topic}")
    print(f"DocType:  {doc_type}\n")

    state = run_supervisor_loop(topic, doc_type, max_iterations=80)
    _render_state(state)

    outcome = "COMPLETE" if state.all_done() else ("PARTIAL" if state.sections_done else "FAILED")
    print(f"\n  Outcome: {outcome}")
    sys.exit(0 if outcome == "COMPLETE" else 1)


if __name__ == "__main__":
    main()
