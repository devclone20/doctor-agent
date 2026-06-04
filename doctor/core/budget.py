"""
Token and tool-call budget enforcement for Rider sub-agents.

Provides hard limits and early-warning thresholds so that no sub-agent can
silently exhaust context. The Rider orchestrator creates one BudgetTracker per
dispatched agent and checks it after every significant operation.

RID-3: Budget enforcement + Claude Swarm patterns.
"""

from __future__ import annotations

from dataclasses import dataclass, field


# ---------------------------------------------------------------------------
# Per-agent defaults
# ---------------------------------------------------------------------------

#: Default budgets keyed by agent name.
#: max_tokens  — approximate context tokens the agent may consume.
#: max_tool_calls — number of tool invocations (Bash, Read, Write, Edit, …).
AGENT_DEFAULTS: dict[str, dict[str, int]] = {
    "doctor": {
        "max_tokens": 100_000,
        "max_tool_calls": 20,
    },
    "hacker": {
        "max_tokens": 50_000,
        "max_tool_calls": 15,
    },
    "rider": {
        "max_tokens": 200_000,
        "max_tool_calls": 50,
    },
    # Additional specialist agents inherit rider-scale budgets by default.
    "architect": {
        "max_tokens": 80_000,
        "max_tool_calls": 20,
    },
    "engineer": {
        "max_tokens": 80_000,
        "max_tool_calls": 30,
    },
    "designer": {
        "max_tokens": 60_000,
        "max_tool_calls": 20,
    },
    "validator": {
        "max_tokens": 50_000,
        "max_tool_calls": 15,
    },
    "qa": {
        "max_tokens": 60_000,
        "max_tool_calls": 25,
    },
    "ingestor": {
        "max_tokens": 40_000,
        "max_tool_calls": 30,
    },
}

_DEFAULT_BUDGET: dict[str, int] = {
    "max_tokens": 50_000,
    "max_tool_calls": 20,
}

WARN_THRESHOLD: float = 0.80   # emit warning above this fraction
BLOCK_THRESHOLD: float = 1.00  # hard stop at 100 %


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


@dataclass
class AgentBudget:
    """Immutable budget configuration for a single agent invocation."""

    agent_name: str
    max_tokens: int
    used_tokens: int = 0
    max_tool_calls: int = 20
    used_tool_calls: int = 0

    @classmethod
    def for_agent(cls, agent_name: str) -> "AgentBudget":
        """Create an AgentBudget using the registered defaults for *agent_name*.

        Falls back to ``_DEFAULT_BUDGET`` for unknown agents.
        """
        defaults = AGENT_DEFAULTS.get(agent_name, _DEFAULT_BUDGET)
        return cls(
            agent_name=agent_name,
            max_tokens=defaults["max_tokens"],
            max_tool_calls=defaults["max_tool_calls"],
        )


# ---------------------------------------------------------------------------
# Tracker
# ---------------------------------------------------------------------------


@dataclass
class BudgetTracker:
    """Tracks consumption of tokens and tool calls against a fixed budget.

    All mutating methods return ``self`` so call-chains are possible.

    Usage::

        tracker = BudgetTracker(AgentBudget.for_agent("doctor"))
        tracker.consume_tokens(1_500)
        tracker.consume_tool_call()
        if tracker.is_exhausted():
            raise BudgetExhaustedError(tracker.budget.agent_name)
    """

    budget: AgentBudget
    _warnings_emitted: list[str] = field(default_factory=list, repr=False)

    # ------------------------------------------------------------------
    # Mutation
    # ------------------------------------------------------------------

    def consume_tokens(self, n: int) -> "BudgetTracker":
        """Record *n* tokens as consumed. Negative values are silently ignored."""
        if n > 0:
            self.budget = _replace_budget(
                self.budget, used_tokens=self.budget.used_tokens + n
            )
        return self

    def consume_tool_call(self) -> "BudgetTracker":
        """Record one tool call as consumed."""
        self.budget = _replace_budget(
            self.budget, used_tool_calls=self.budget.used_tool_calls + 1
        )
        return self

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def remaining_tokens(self) -> int:
        """Number of tokens still available (floored at 0)."""
        return max(0, self.budget.max_tokens - self.budget.used_tokens)

    def remaining_tool_calls(self) -> int:
        """Number of tool calls still available (floored at 0)."""
        return max(0, self.budget.max_tool_calls - self.budget.used_tool_calls)

    def token_usage_percent(self) -> float:
        """Token consumption as a fraction in [0.0, ∞)."""
        if self.budget.max_tokens == 0:
            return 1.0
        return self.budget.used_tokens / self.budget.max_tokens

    def tool_usage_percent(self) -> float:
        """Tool-call consumption as a fraction in [0.0, ∞)."""
        if self.budget.max_tool_calls == 0:
            return 1.0
        return self.budget.used_tool_calls / self.budget.max_tool_calls

    def is_exhausted(self) -> bool:
        """True when tokens *or* tool calls have reached their limit."""
        return (
            self.budget.used_tokens >= self.budget.max_tokens
            or self.budget.used_tool_calls >= self.budget.max_tool_calls
        )

    def warn_if_above(self, threshold: float = WARN_THRESHOLD) -> bool:
        """Return True and record a warning if any dimension exceeds *threshold*.

        Warnings are deduplicated — the same threshold triggers at most once per
        dimension per tracker instance.
        """
        triggered = False

        for dimension, used, maximum in (
            ("tokens", self.budget.used_tokens, self.budget.max_tokens),
            ("tool_calls", self.budget.used_tool_calls, self.budget.max_tool_calls),
        ):
            pct = used / maximum if maximum else 1.0
            key = f"{dimension}:{threshold:.2f}"
            if pct >= threshold and key not in self._warnings_emitted:
                self._warnings_emitted.append(key)
                triggered = True

        return triggered

    def usage_percent(self) -> dict[str, float]:
        """Return a dict with ``tokens`` and ``tool_calls`` usage percentages."""
        return {
            "tokens": round(self.token_usage_percent() * 100, 1),
            "tool_calls": round(self.tool_usage_percent() * 100, 1),
        }

    def status_bar(self) -> str:
        """Compact single-line status for embedding in the orchestration board."""
        t_pct = self.token_usage_percent()
        c_pct = self.tool_usage_percent()

        def bar(pct: float, width: int = 10) -> str:
            filled = min(int(pct * width), width)
            return "█" * filled + "░" * (width - filled)

        t_bar = bar(t_pct)
        c_bar = bar(c_pct)
        agent = self.budget.agent_name
        return (
            f"{agent:12s} | tokens [{t_bar}] {t_pct*100:5.1f}%"
            f"  calls [{c_bar}] {c_pct*100:5.1f}%"
        )

    def warning_message(self) -> str | None:
        """Human-readable warning if above WARN_THRESHOLD, else None."""
        t_pct = self.token_usage_percent()
        c_pct = self.tool_usage_percent()
        agent = self.budget.agent_name

        if t_pct >= BLOCK_THRESHOLD or c_pct >= BLOCK_THRESHOLD:
            return (
                f"BUDGET EXHAUSTED for agent '{agent}': "
                f"tokens {self.budget.used_tokens:,}/{self.budget.max_tokens:,} "
                f"({t_pct*100:.1f}%), "
                f"tool calls {self.budget.used_tool_calls}/{self.budget.max_tool_calls} "
                f"({c_pct*100:.1f}%). "
                "Synthesise completed work and stop."
            )
        if t_pct >= WARN_THRESHOLD or c_pct >= WARN_THRESHOLD:
            return (
                f"BUDGET WARNING for agent '{agent}': "
                f"tokens at {t_pct*100:.1f}% "
                f"({self.remaining_tokens():,} remaining), "
                f"tool calls at {c_pct*100:.1f}% "
                f"({self.remaining_tool_calls()} remaining). "
                "Begin synthesising — budget is nearly exhausted."
            )
        return None


# ---------------------------------------------------------------------------
# Budget-exhausted error
# ---------------------------------------------------------------------------


class BudgetExhaustedError(RuntimeError):
    """Raised by callers that enforce hard budget limits."""

    def __init__(self, agent_name: str) -> None:
        super().__init__(
            f"Agent '{agent_name}' has exhausted its budget. "
            "Cannot dispatch further work until the budget is reset or increased."
        )
        self.agent_name = agent_name


# ---------------------------------------------------------------------------
# Internal helper — simulate dataclass replace without importing copy
# ---------------------------------------------------------------------------


def _replace_budget(b: AgentBudget, **overrides: int) -> AgentBudget:
    """Return a new AgentBudget with *overrides* applied."""
    return AgentBudget(
        agent_name=b.agent_name,
        max_tokens=overrides.get("max_tokens", b.max_tokens),
        used_tokens=overrides.get("used_tokens", b.used_tokens),
        max_tool_calls=overrides.get("max_tool_calls", b.max_tool_calls),
        used_tool_calls=overrides.get("used_tool_calls", b.used_tool_calls),
    )
