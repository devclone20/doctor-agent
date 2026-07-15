"""
DAG of sections for dissertation/research documents.

Models the dependency graph between academic sections so that the Rider agent
can determine the correct writing order, surface parallelism, and detect when
all required sections are complete.

RID-2: DAG de secções com detecção de dependências.
"""

from __future__ import annotations

from collections import deque
from typing import Literal


# ---------------------------------------------------------------------------
# Canonical section dependencies
# ---------------------------------------------------------------------------

DocType = Literal["msc", "phd", "bsc", "article"]

# Each key is a section name; its value is the list of sections that must be
# at least partially written before this section can be completed.
# Sections not listed as keys are dependency-free (they may be started any time).
SECTION_DEPENDENCIES: dict[str, dict[str, list[str]]] = {
    "bsc": {
        "background": ["introduction"],
        "methodology": ["background"],
        "results": ["methodology"],
        "discussion": ["results"],
        "conclusion": ["discussion"],
        "abstract": ["conclusion"],
    },
    "msc": {
        "related_work": ["introduction"],
        "background": ["introduction"],
        "methodology": ["background"],
        "implementation": ["methodology"],
        "evaluation": ["implementation"],
        "discussion": ["evaluation"],
        "conclusion": ["discussion"],
        "abstract": ["conclusion"],
        "acknowledgements": [],
    },
    "phd": {
        "related_work": ["introduction"],
        "background": ["introduction"],
        "theoretical_framework": ["background"],
        "methodology": ["theoretical_framework"],
        "implementation": ["methodology"],
        "evaluation": ["implementation"],
        "contributions": ["evaluation"],
        "discussion": ["contributions", "evaluation"],
        "conclusion": ["discussion"],
        "future_work": ["conclusion"],
        "abstract": ["conclusion"],
        "acknowledgements": [],
    },
    "article": {
        "related_work": ["introduction"],
        "methodology": ["introduction"],
        "results": ["methodology"],
        "discussion": ["results"],
        "conclusion": ["discussion"],
        "abstract": ["conclusion"],
    },
}


# ---------------------------------------------------------------------------
# SectionDAG
# ---------------------------------------------------------------------------


class CycleError(ValueError):
    """Raised when a cycle is detected in the section dependency graph."""


class SectionDAG:
    """Directed acyclic graph representing section writing dependencies.

    Nodes are section names (strings).
    A directed edge A → B means "B depends on A" (A must be written first).
    """

    def __init__(self) -> None:
        # adjacency: section → set of sections that depend on it
        self._deps: dict[str, set[str]] = {}   # section → its direct dependencies
        self._nodes: set[str] = set()

    # ------------------------------------------------------------------
    # Mutation
    # ------------------------------------------------------------------

    def add_section(self, name: str, deps: list[str] | None = None) -> None:
        """Register a section with optional dependencies.

        If *deps* is empty or None the section is a root node (no prerequisites).
        """
        if deps is None:
            deps = []
        self._nodes.add(name)
        self._deps[name] = set(deps)
        for dep in deps:
            self._nodes.add(dep)
            if dep not in self._deps:
                self._deps[dep] = set()

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def topological_order(self) -> list[str]:
        """Return sections in the order they should be written (Kahn's algorithm).

        Raises CycleError if the graph contains a cycle.
        """
        in_degree: dict[str, int] = {n: 0 for n in self._nodes}
        for node in self._nodes:
            for dep in self._deps.get(node, set()):
                in_degree[dep]   # ensure key exists — deps are already nodes
                in_degree[node]  # no-op, already initialised
        # rebuild in_degree correctly
        in_degree = {n: 0 for n in self._nodes}
        for node in self._nodes:
            for dep in self._deps.get(node, set()):
                # dep must come before node → dep has no extra in-degree here;
                # node's in-degree increases because dep is a prerequisite
                in_degree[node] += 0  # counted below via reverse pass
        # in_degree[v] = number of sections v depends on
        in_degree = {n: len(self._deps.get(n, set())) for n in self._nodes}

        queue: deque[str] = deque(
            sorted(n for n, d in in_degree.items() if d == 0)
        )
        order: list[str] = []

        # Build reverse map: dep → sections that have dep as prerequisite
        reverse: dict[str, list[str]] = {n: [] for n in self._nodes}
        for node in self._nodes:
            for dep in self._deps.get(node, set()):
                reverse[dep].append(node)

        while queue:
            node = queue.popleft()
            order.append(node)
            for dependent in sorted(reverse.get(node, [])):
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)

        if len(order) != len(self._nodes):
            cycle_nodes = self._nodes - set(order)
            raise CycleError(
                f"Cycle detected involving sections: {sorted(cycle_nodes)}"
            )
        return order

    def independent_groups(self) -> list[list[str]]:
        """Return sections grouped by their earliest possible writing wave.

        Each group is a list of sections that can be written in parallel
        (all their dependencies belong to earlier groups).
        """
        in_degree = {n: len(self._deps.get(n, set())) for n in self._nodes}
        reverse: dict[str, list[str]] = {n: [] for n in self._nodes}
        for node in self._nodes:
            for dep in self._deps.get(node, set()):
                reverse[dep].append(node)

        groups: list[list[str]] = []
        remaining = dict(in_degree)

        while remaining:
            wave = sorted(n for n, d in remaining.items() if d == 0)
            if not wave:
                cycle_nodes = set(remaining.keys())
                raise CycleError(
                    f"Cycle detected involving sections: {sorted(cycle_nodes)}"
                )
            groups.append(wave)
            for node in wave:
                del remaining[node]
                for dependent in reverse.get(node, []):
                    if dependent in remaining:
                        remaining[dependent] -= 1

        return groups

    def is_complete(self, completed: set[str]) -> bool:
        """True when every registered section is present in *completed*."""
        return self._nodes <= completed

    def blocked_sections(self, completed: set[str]) -> dict[str, list[str]]:
        """Return sections that cannot be started yet, mapped to their missing deps."""
        blocked: dict[str, list[str]] = {}
        for node in self._nodes:
            if node in completed:
                continue
            missing = [d for d in self._deps.get(node, set()) if d not in completed]
            if missing:
                blocked[node] = sorted(missing)
        return blocked

    def ready_sections(self, completed: set[str]) -> list[str]:
        """Return sections whose dependencies are all satisfied but are not yet done."""
        return sorted(
            node
            for node in self._nodes
            if node not in completed
            and all(dep in completed for dep in self._deps.get(node, set()))
        )


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------


def build_dissertation_dag(doc_type: str) -> SectionDAG:
    """Construct the canonical SectionDAG for a given document type.

    *doc_type* must be one of: "bsc", "msc", "phd", "article".
    Raises ValueError for unknown document types.
    """
    if doc_type not in SECTION_DEPENDENCIES:
        known = list(SECTION_DEPENDENCIES.keys())
        raise ValueError(
            f"Unknown doc_type {doc_type!r}. Known types: {known}"
        )

    dag = SectionDAG()
    dep_map = SECTION_DEPENDENCIES[doc_type]

    # Register all sections, including those that appear only as dependencies
    all_sections: set[str] = set(dep_map.keys())
    for deps in dep_map.values():
        all_sections.update(deps)

    for section in sorted(all_sections):
        dag.add_section(section, dep_map.get(section, []))

    return dag
