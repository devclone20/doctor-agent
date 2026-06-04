"""
State machine for dissertation project documents.

Encodes the valid lifecycle of a ProjectDocument as an explicit finite state
machine with validated transitions. Inspired by LangGraph's node/edge model
but implemented as pure stdlib Python — zero external dependencies.

RID-1: projecto.json com state machine explícita.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any


# ---------------------------------------------------------------------------
# States
# ---------------------------------------------------------------------------


class ProjectState(str, Enum):
    """Lifecycle states for a dissertation project document.

    Ordering reflects the natural progression of academic writing:
      draft → investigation → writing → review → approved → exported.
    """

    RASCUNHO = "RASCUNHO"           # initial draft, topic defined
    EM_INVESTIGACAO = "EM_INVESTIGACAO"  # literature search in progress
    ESCRITA = "ESCRITA"             # sections being written
    EM_REVISAO = "EM_REVISAO"       # submitted for supervisor review
    APROVADO = "APROVADO"           # supervisor approved
    EXPORTADO = "EXPORTADO"         # final PDF/document generated and delivered


# ---------------------------------------------------------------------------
# Transition table
# ---------------------------------------------------------------------------

VALID_TRANSITIONS: dict[ProjectState, list[ProjectState]] = {
    ProjectState.RASCUNHO: [
        ProjectState.EM_INVESTIGACAO,
    ],
    ProjectState.EM_INVESTIGACAO: [
        ProjectState.ESCRITA,
        ProjectState.RASCUNHO,          # back to draft if topic changes
    ],
    ProjectState.ESCRITA: [
        ProjectState.EM_REVISAO,
        ProjectState.EM_INVESTIGACAO,   # back if gaps found during writing
    ],
    ProjectState.EM_REVISAO: [
        ProjectState.APROVADO,
        ProjectState.ESCRITA,           # revisions requested
    ],
    ProjectState.APROVADO: [
        ProjectState.EXPORTADO,
    ],
    ProjectState.EXPORTADO: [],         # terminal state
}


# ---------------------------------------------------------------------------
# Domain error
# ---------------------------------------------------------------------------


class InvalidTransitionError(ValueError):
    """Raised when a requested state transition is not in VALID_TRANSITIONS."""

    def __init__(
        self,
        current: ProjectState,
        requested: ProjectState,
        allowed: list[ProjectState],
    ) -> None:
        allowed_labels = [s.value for s in allowed]
        super().__init__(
            f"Cannot transition from {current.value!r} to {requested.value!r}. "
            f"Allowed targets: {allowed_labels or ['none — terminal state']}"
        )
        self.current = current
        self.requested = requested
        self.allowed = allowed


# ---------------------------------------------------------------------------
# Document model
# ---------------------------------------------------------------------------


@dataclass
class ProjectDocument:
    """Represents a single dissertation/research project in its current state.

    Sections is a free-form dict keyed by section name (e.g. "introduction",
    "methodology") whose values are dicts with at minimum a "state" key
    ("vazio" | "parcial" | "completo" | "bloqueado") and optional "content".
    """

    id: str
    title: str
    topic: str
    doc_type: str                       # "msc" | "phd" | "bsc" | "article"
    state: ProjectState
    sections: dict[str, dict[str, Any]] = field(default_factory=dict)
    created_at: datetime = field(
        default_factory=lambda: datetime.now(tz=timezone.utc)
    )
    updated_at: datetime = field(
        default_factory=lambda: datetime.now(tz=timezone.utc)
    )

    # Convenience -------------------------------------------------------------

    def is_terminal(self) -> bool:
        """True when no further transitions are possible."""
        return not VALID_TRANSITIONS[self.state]

    def allowed_next_states(self) -> list[ProjectState]:
        return VALID_TRANSITIONS[self.state]


# ---------------------------------------------------------------------------
# Transition function (pure)
# ---------------------------------------------------------------------------


def transition(doc: ProjectDocument, new_state: ProjectState) -> ProjectDocument:
    """Validate and apply a state transition, returning an updated document.

    Returns a *new* ProjectDocument instance — the original is unchanged.
    Raises InvalidTransitionError if the transition is not permitted.
    """
    allowed = VALID_TRANSITIONS[doc.state]
    if new_state not in allowed:
        raise InvalidTransitionError(doc.state, new_state, allowed)

    return ProjectDocument(
        id=doc.id,
        title=doc.title,
        topic=doc.topic,
        doc_type=doc.doc_type,
        state=new_state,
        sections=doc.sections,
        created_at=doc.created_at,
        updated_at=datetime.now(tz=timezone.utc),
    )


# ---------------------------------------------------------------------------
# Serialisation helpers
# ---------------------------------------------------------------------------

_ISO_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"


def _to_dict(doc: ProjectDocument) -> dict[str, Any]:
    raw = asdict(doc)
    raw["state"] = doc.state.value
    raw["created_at"] = doc.created_at.isoformat()
    raw["updated_at"] = doc.updated_at.isoformat()
    return raw


def _from_dict(data: dict[str, Any]) -> ProjectDocument:
    data = dict(data)
    data["state"] = ProjectState(data["state"])
    data["created_at"] = datetime.fromisoformat(data["created_at"])
    data["updated_at"] = datetime.fromisoformat(data["updated_at"])
    return ProjectDocument(**data)


def load_project(path: Path) -> ProjectDocument:
    """Deserialise a ProjectDocument from a JSON file at *path*.

    Raises FileNotFoundError if the file does not exist.
    Raises ValueError if the JSON is malformed or contains an unknown state.
    """
    raw = json.loads(path.read_text(encoding="utf-8"))
    return _from_dict(raw)


def save_project(doc: ProjectDocument, path: Path) -> None:
    """Serialise *doc* to JSON and write it to *path*, creating parent dirs."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_to_dict(doc), indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
