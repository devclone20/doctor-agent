"""
Interface abstracta para o orquestrador de dissertações — PROPOSTA-RID-1.

Define OrchestratorProtocol como um typing.Protocol, garantindo que qualquer
backend (stdlib, LangGraph, ou futuro) seja substituível sem alterar os callers.

A factory create_orchestrator() é o único ponto de entrada que os callers
(CLI, agente) devem usar — nunca instanciar DissertationOrchestrator directamente.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal, Protocol, runtime_checkable


# ---------------------------------------------------------------------------
# Protocol
# ---------------------------------------------------------------------------

@runtime_checkable
class OrchestratorProtocol(Protocol):
    """
    Contrato público do orquestrador de dissertações.

    Qualquer implementação (stdlib, LangGraph, ou futura) deve satisfazer
    este contrato. O Protocol é runtime_checkable para facilitar testes.

    Lifecycle canónico:
        plan = orch.build_plan(topic, doc_type)
        while not orch.is_complete():
            for task in orch.next_ready():
                try:
                    output = generate(task)
                    orch.mark_done(task["section"], output.path, output.tokens)
                except Exception as exc:
                    orch.mark_failed(task["section"], str(exc))
        print(orch.progress_report())
    """

    def build_plan(self) -> list:
        """
        Constrói o plano de geração: lista de tasks em ordem topológica.

        topic e doc_type são fornecidos via factory (create_orchestrator).
        Deve ser chamado exactamente uma vez antes de qualquer outro método.
        Retorna a lista de tasks para inspeção (o estado interno é idêntico).
        """
        ...

    def next_ready(self) -> list:
        """
        Retorna tasks cujas dependências estão todas concluídas e que ainda
        não foram iniciadas ou marcadas como done/failed.
        """
        ...

    def mark_done(self, section: str, output_path: Path, tokens: int) -> None:
        """
        Regista a conclusão bem-sucedida de uma secção.

        Actualiza o tracker de budget e promove tasks desbloqueadas para ready.
        Pode lançar BudgetExhaustedError se o limite de tokens for atingido.
        """
        ...

    def mark_failed(self, section: str, error: str) -> None:
        """Regista falha numa secção com a mensagem de erro."""
        ...

    def progress_report(self) -> str:
        """Retorna relatório legível do estado actual da geração."""
        ...

    def is_complete(self) -> bool:
        """True quando todas as secções estão em estado done."""
        ...

    def save_state(self, path: Path) -> None:
        """Serializa o estado do orquestrador para um ficheiro JSON."""
        ...

    @classmethod
    def load_state(cls, path: Path) -> "OrchestratorProtocol":
        """Restaura um orquestrador a partir de um ficheiro JSON previamente guardado."""
        ...


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

def create_orchestrator(
    backend: Literal["stdlib", "langgraph"] = "stdlib",
    *,
    topic: str,
    doc_type: str,
    project_dir: Path,
    budget_tokens: int = 100_000,
) -> OrchestratorProtocol:
    """
    Factory para instanciar o orquestrador correcto com base no backend.

    Parameters
    ----------
    backend:
        "stdlib"    — implementação pura Python (DissertationOrchestrator).
                      Pronto para produção.
        "langgraph" — reservado para integração futura com LangGraph.
                      Lança NotImplementedError com instruções claras.
    topic:
        Tema da dissertação.
    doc_type:
        Tipo de documento: "bsc", "msc", "phd", "article".
    project_dir:
        Directório onde os ficheiros gerados e o estado serão guardados.
    budget_tokens:
        Limite máximo de tokens para toda a geração. Default: 100 000.

    Returns
    -------
    OrchestratorProtocol
        Instância pronta a usar. Chamada seguinte deve ser build_plan().

    Raises
    ------
    NotImplementedError
        Se backend="langgraph" (não implementado — aguarda decisão arquitectural).
    ValueError
        Se backend for um valor desconhecido.
    """
    if backend == "stdlib":
        from doctor.orchestration.dissertation_orchestrator import DissertationOrchestrator

        return DissertationOrchestrator(
            topic=topic,
            doc_type=doc_type,
            project_dir=project_dir,
            budget_tokens=budget_tokens,
        )

    if backend == "langgraph":
        raise NotImplementedError(
            "O backend LangGraph ainda não está implementado.\n"
            "\n"
            "Consulta doctor/orchestration/langgraph_spike.md para o racional de adopção.\n"
            "Para usar o orquestrador em produção, passa backend='stdlib' (default).\n"
            "\n"
            "Quando LangGraph for adoptado:\n"
            "  1. Criar doctor/orchestration/langgraph_orchestrator.py\n"
            "  2. Implementar OrchestratorProtocol nessa classe\n"
            "  3. Instanciar aqui e remover este NotImplementedError"
        )

    raise ValueError(
        f"Backend desconhecido: {backend!r}. "
        "Valores suportados: 'stdlib', 'langgraph'."
    )


# ---------------------------------------------------------------------------
# Convenience: load existing state without knowing the backend
# ---------------------------------------------------------------------------

def load_orchestrator_state(state_path: Path) -> OrchestratorProtocol:
    """
    Restaura um orquestrador a partir de um ficheiro de estado JSON.

    Usa sempre o backend stdlib — o estado JSON foi gerado por DissertationOrchestrator
    e é agnóstico ao backend futuro.

    Raises
    ------
    FileNotFoundError
        Se state_path não existir.
    """
    if not state_path.exists():
        raise FileNotFoundError(f"Ficheiro de estado não encontrado: {state_path}")

    from doctor.orchestration.dissertation_orchestrator import DissertationOrchestrator

    return DissertationOrchestrator.load_state(state_path)
