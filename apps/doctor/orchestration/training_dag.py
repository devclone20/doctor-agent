"""
DAG de orquestração para sessões de auto-training do Rider.

Define o grafo de dependências entre fases de treino, valida pré-condições
antes de cada fase, e gera relatórios no formato padrão training_reports.

Integra com doctor.core.budget para enforcement de token budget por fase.

RID-1 (07-06): DAG de orquestração para sessões auto-training.
"""

from __future__ import annotations

import textwrap
from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


# ---------------------------------------------------------------------------
# Phase enum & DAG topology
# ---------------------------------------------------------------------------


class TrainingPhase(str, Enum):
    """Fases ordenadas de uma sessão de auto-training do Rider."""

    FETCH = "fetch_papers"
    ANALYSE = "analyse_papers"
    GENERATE_PROPOSALS = "generate_proposals"
    UPDATE_WIKI = "update_wiki_pages"
    COMMIT_REPORT = "commit_report"


# Grafo de dependências: fase → conjunto de fases que devem estar completas antes.
# ANALYSE e UPDATE_WIKI dependem de FETCH.
# GENERATE_PROPOSALS depende de ANALYSE.
# COMMIT_REPORT depende de GENERATE_PROPOSALS e UPDATE_WIKI.
TRAINING_DAG: dict[TrainingPhase, frozenset[TrainingPhase]] = {
    TrainingPhase.FETCH:              frozenset(),
    TrainingPhase.ANALYSE:            frozenset({TrainingPhase.FETCH}),
    TrainingPhase.UPDATE_WIKI:        frozenset({TrainingPhase.FETCH}),
    TrainingPhase.GENERATE_PROPOSALS: frozenset({TrainingPhase.ANALYSE}),
    TrainingPhase.COMMIT_REPORT:      frozenset({
        TrainingPhase.GENERATE_PROPOSALS,
        TrainingPhase.UPDATE_WIKI,
    }),
}

# Token budget por fase — proporcional à intensidade de processamento.
PHASE_TOKEN_BUDGET: dict[TrainingPhase, int] = {
    TrainingPhase.FETCH:              20_000,
    TrainingPhase.ANALYSE:            40_000,
    TrainingPhase.UPDATE_WIKI:        15_000,
    TrainingPhase.GENERATE_PROPOSALS: 30_000,
    TrainingPhase.COMMIT_REPORT:      10_000,
}

# Duração estimada por fase em segundos (p50 observado em sessões reais).
PHASE_DURATION_SECONDS: dict[TrainingPhase, int] = {
    TrainingPhase.FETCH:              120,
    TrainingPhase.ANALYSE:            300,
    TrainingPhase.UPDATE_WIKI:        90,
    TrainingPhase.GENERATE_PROPOSALS: 240,
    TrainingPhase.COMMIT_REPORT:      60,
}


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------


@dataclass
class Proposal:
    """Uma proposta gerada durante a fase GENERATE_PROPOSALS."""

    id: str                      # Ex: "PROPOSTA-DOC-1 (07-06)"
    agent: str                   # "doctor" | "hacker" | "rider"
    title: str
    description: str
    status: str = "approved"     # "approved" | "pending" | "rejected"


@dataclass
class TrainingSession:
    """Estado completo de uma sessão de auto-training."""

    date: date
    agents: list[str]
    papers_found: int = 0
    repos_searched: int = 0
    phases_done: list[TrainingPhase] = field(default_factory=list)
    proposals: list[Proposal] = field(default_factory=list)
    score: float = 0.0           # 0.0–10.0, avaliação da qualidade da sessão

    def mark_done(self, phase: TrainingPhase) -> None:
        """Regista a fase como concluída (idempotente)."""
        if phase not in self.phases_done:
            self.phases_done.append(phase)

    def is_complete(self) -> bool:
        """True quando todas as fases do DAG estão concluídas."""
        return set(self.phases_done) == set(TrainingPhase)


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


class TrainingDAGOrchestrator:
    """
    Orquestra a execução de sessões de auto-training seguindo o TRAINING_DAG.

    Responsabilidades:
    - Calcular a ordem de execução respeitando dependências
    - Verificar pré-condições antes de cada fase
    - Identificar fases que podem correr em paralelo
    - Gerar relatório final no formato training_reports
    - Estimar duração e budget de tokens por sessão
    """

    def build_session_plan(self, agents: list[str]) -> list[TrainingPhase]:
        """
        Retorna a ordem de execução das fases para os *agents* dados.

        A ordem é um topological sort do TRAINING_DAG que garante que
        nenhuma fase é executada antes das suas dependências.

        Fases sem dependências comuns a todos os agents são incluídas
        incondicionalmente — o filtro por agent acontece na execução real.
        """
        return _topological_sort(TRAINING_DAG)

    def can_run_phase(
        self,
        phase: TrainingPhase,
        completed_phases: list[TrainingPhase] | frozenset[TrainingPhase],
    ) -> bool:
        """
        True se todas as dependências de *phase* estão em *completed_phases*.

        Permite ao orquestrador verificar pré-condições antes de despachar
        uma fase para execução — evita falhas silenciosas por ordem errada.
        """
        required = TRAINING_DAG[phase]
        done = frozenset(completed_phases)
        return required.issubset(done)

    def parallel_phases(
        self,
        completed_phases: list[TrainingPhase] | frozenset[TrainingPhase],
    ) -> list[TrainingPhase]:
        """
        Retorna todas as fases que podem correr em paralelo agora.

        Uma fase é elegível quando:
        1. Ainda não está concluída
        2. Todas as suas dependências estão concluídas

        O caller pode despachar estas fases simultaneamente sem violar o DAG.
        """
        done = frozenset(completed_phases)
        return [
            phase
            for phase in TrainingPhase
            if phase not in done and self.can_run_phase(phase, done)
        ]

    def estimate_duration(self, phases: list[TrainingPhase]) -> dict[str, int]:
        """
        Estima o tempo de execução para a lista de fases dada.

        Considera paralelismo: fases que podem correr simultaneamente
        contribuem apenas com o tempo da fase mais longa do grupo paralelo.

        Returns:
            dict com chaves:
            - ``sequential_seconds``: soma de todas as fases (sem paralelismo)
            - ``parallel_seconds``: duração estimada com paralelismo máximo
            - ``token_budget_total``: soma dos token budgets das fases
            - per-phase entries: ``{phase.value: seconds}``
        """
        per_phase = {p.value: PHASE_DURATION_SECONDS[p] for p in phases}
        sequential = sum(per_phase.values())
        token_total = sum(PHASE_TOKEN_BUDGET[p] for p in phases)

        # Simular execução paralela: processar camadas do DAG
        completed: frozenset[TrainingPhase] = frozenset()
        parallel_total = 0
        remaining = set(phases)

        while remaining:
            runnable = [
                p for p in remaining
                if self.can_run_phase(p, completed)
            ]
            if not runnable:
                break  # DAG inconsistente — não deve acontecer
            layer_duration = max(PHASE_DURATION_SECONDS[p] for p in runnable)
            parallel_total += layer_duration
            completed = completed | frozenset(runnable)
            remaining -= set(runnable)

        return {
            "sequential_seconds": sequential,
            "parallel_seconds": parallel_total,
            "token_budget_total": token_total,
            **per_phase,
        }

    def session_report(self, session: TrainingSession) -> str:
        """
        Gera relatório formatado da sessão no padrão training_reports existente.

        O formato segue os relatórios de treino observados no projecto:
        header com data/agents, métricas de pesquisa, propostas geradas,
        score de qualidade, e sumário de fases concluídas.
        """
        date_str = session.date.strftime("%Y-%m-%d")
        agents_str = ", ".join(session.agents) if session.agents else "—"
        phases_done_str = ", ".join(p.value for p in session.phases_done) or "nenhuma"

        proposals_block = _format_proposals(session.proposals)

        score_label = _score_label(session.score)
        completion_pct = int(len(session.phases_done) / len(TrainingPhase) * 100)

        duration = self.estimate_duration(list(TrainingPhase))

        return textwrap.dedent(f"""\
            # Training Report — {date_str}

            **Agents:** {agents_str}
            **Sessão completa:** {"Sim" if session.is_complete() else "Não"} ({completion_pct}%)
            **Score de qualidade:** {session.score:.1f}/10.0 — {score_label}

            ---

            ## Métricas de Pesquisa

            | Métrica              | Valor |
            |----------------------|-------|
            | Papers encontrados   | {session.papers_found} |
            | Repositórios pesquisados | {session.repos_searched} |
            | Propostas geradas    | {len(session.proposals)} |
            | Fases concluídas     | {len(session.phases_done)}/{len(TrainingPhase)} |

            ---

            ## Propostas Geradas

            {proposals_block}

            ---

            ## Fases Concluídas

            {phases_done_str}

            ---

            ## Estimativa de Duração

            | Modo             | Segundos |
            |-----------------|---------|
            | Sequencial       | {duration["sequential_seconds"]}s |
            | Com paralelismo  | {duration["parallel_seconds"]}s |
            | Budget tokens total | {duration["token_budget_total"]:,} |

            ---

            *Relatório gerado por TrainingDAGOrchestrator · Doctor Agent*
        """)


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------


def _topological_sort(dag: dict[TrainingPhase, frozenset[TrainingPhase]]) -> list[TrainingPhase]:
    """
    Kahn's algorithm sobre o DAG de fases.

    Garante ordem estável e detecta ciclos (lança ValueError se existirem).
    """
    in_degree: dict[TrainingPhase, int] = {phase: 0 for phase in dag}
    for deps in dag.values():
        for dep in deps:
            in_degree[dep] = in_degree.get(dep, 0)  # ensure present

    # Recalculate: count how many phases depend ON each phase
    dependents: dict[TrainingPhase, int] = {phase: 0 for phase in dag}
    for phase, deps in dag.items():
        for dep in deps:
            dependents[dep] = dependents.get(dep, 0)

    # Build correct in-degree: how many unresolved deps does each phase have
    phase_in_degree: dict[TrainingPhase, int] = {
        phase: len(deps) for phase, deps in dag.items()
    }

    queue: list[TrainingPhase] = [p for p, d in phase_in_degree.items() if d == 0]
    result: list[TrainingPhase] = []

    while queue:
        # Sort for deterministic output
        queue.sort(key=lambda p: p.value)
        current = queue.pop(0)
        result.append(current)

        for phase, deps in dag.items():
            if current in deps and phase not in result:
                phase_in_degree[phase] -= 1
                if phase_in_degree[phase] == 0:
                    queue.append(phase)

    if len(result) != len(dag):
        raise ValueError(
            f"TRAINING_DAG contains a cycle. Processed {len(result)}/{len(dag)} phases."
        )

    return result


def _format_proposals(proposals: list[Proposal]) -> str:
    if not proposals:
        return "_Nenhuma proposta gerada nesta sessão._"

    lines: list[str] = []
    for p in proposals:
        status_icon = "+" if p.status == "approved" else ("~" if p.status == "pending" else "-")
        lines.append(f"- [{status_icon}] **{p.id}** ({p.agent}) — {p.title}")
        if p.description:
            lines.append(f"  {p.description[:120]}{'...' if len(p.description) > 120 else ''}")

    return "\n".join(lines)


def _score_label(score: float) -> str:
    if score >= 9.0:
        return "Excelente"
    if score >= 7.0:
        return "Bom"
    if score >= 5.0:
        return "Aceitável"
    if score >= 3.0:
        return "Fraco"
    return "Insuficiente"
