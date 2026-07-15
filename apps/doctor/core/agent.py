"""
Loop principal do Doctor.
Streaming, tool use, memória persistente, auto-síntese de sessão.
"""

import os
from pathlib import Path

import anthropic

from doctor.core.identity import get_system_prompt
from doctor.core.tools import TOOL_DEFINITIONS, execute_tool
from doctor.knowledge.retriever import load_wiki_into_db, retrieve_relevant_context
from doctor.memory.db import init_db, create_session, log_observation
from doctor.memory.synthesis import build_memory_context, synthesize_session


DEFAULT_MODEL = "claude-sonnet-4-6"
DEFAULT_MAX_TOKENS = 8096
MAX_TOOL_ITERATIONS = 15  # Mais alto que Akita — dissertações requerem mais tool calls


class DoctorAgent:
    """
    Agente académico com especialidade em IST, ML/AI, Cloud e escrita científica.
    Suporta streaming, tool use, memória persistente e síntese de sessão.
    """

    def __init__(
        self,
        api_key: str | None = None,
        model: str | None = None,
        memory_dir: Path | None = None,
        project: str | None = None,
        doc_type: str | None = None,
        auto_synthesize: bool = True,
    ) -> None:
        self.client = anthropic.Anthropic(api_key=api_key or os.environ["ANTHROPIC_API_KEY"])
        self.model = model or os.environ.get("DOCTOR_MODEL", DEFAULT_MODEL)
        self.memory_dir = memory_dir or Path(
            os.path.expanduser(os.environ.get("DOCTOR_MEMORY_DIR", "~/.doctor"))
        )
        self.db_path = self.memory_dir / "doctor.db"
        self.project = project
        self.doc_type = doc_type  # "msc", "phd", "article", "bsc"
        self.auto_synthesize = auto_synthesize

        self.conversation: list[dict] = []
        self.session_id: str = ""
        self._initialized = False
        self._system_prompt: str = ""

    def initialize(self) -> None:
        """Inicializa base de dados, carrega wiki, cria sessão."""
        if self._initialized:
            return
        init_db(self.db_path)
        load_wiki_into_db(self.db_path)
        self.session_id = create_session(
            self.db_path,
            project=self.project,
            doc_type=self.doc_type,
        )
        self._initialized = True

    def _build_system_prompt(self, first_message: str = "") -> str:
        """Constrói o system prompt com memória académica e RAG injectados."""
        memory_context = build_memory_context(self.db_path, query=first_message)
        rag_context = retrieve_relevant_context(self.db_path, first_message)

        extra_parts: list[str] = []
        if memory_context:
            extra_parts.append(memory_context)
        if rag_context:
            extra_parts.append(f"## Conhecimento Académico Relevante\n\n{rag_context}")

        # Adicionar contexto do tipo de documento
        if self.doc_type:
            type_map = {
                "msc": "Dissertação de Mestrado IST",
                "phd": "Tese de Doutoramento IST",
                "bsc": "Trabalho de Licenciatura IST",
                "article": "Artigo Científico",
                "report": "Relatório Técnico IST",
            }
            dtype_name = type_map.get(self.doc_type, self.doc_type)
            extra_parts.append(f"## Contexto Actual\nTipo de documento: **{dtype_name}**")

        if self.project:
            extra_parts.append(f"Projecto/Dissertação: **{self.project}**")

        return get_system_prompt(extra_context="\n\n".join(extra_parts))

    def chat(self, user_message: str) -> str:
        """Envia mensagem e retorna resposta completa."""
        if not self._initialized:
            self.initialize()

        self.conversation.append({"role": "user", "content": user_message})
        log_observation(self.db_path, self.session_id, "user", user_message)

        if not self._system_prompt:
            self._system_prompt = self._build_system_prompt(user_message)

        response_text = self._run_turn(self._system_prompt)
        log_observation(self.db_path, self.session_id, "assistant", response_text)
        return response_text

    def chat_stream(self, user_message: str, callback) -> str:
        """Versão streaming: chama callback(chunk) para cada fragmento."""
        if not self._initialized:
            self.initialize()

        self.conversation.append({"role": "user", "content": user_message})
        log_observation(self.db_path, self.session_id, "user", user_message)

        if not self._system_prompt:
            self._system_prompt = self._build_system_prompt(user_message)

        response_text = self._run_turn(self._system_prompt, stream_callback=callback)
        log_observation(self.db_path, self.session_id, "assistant", response_text)
        return response_text

    def _run_turn(self, system_prompt: str, stream_callback=None) -> str:
        """Executa um turno completo com tool use em loop."""
        messages = list(self.conversation)
        iterations = 0

        while iterations < MAX_TOOL_ITERATIONS:
            if stream_callback is not None:
                text, stop_reason, content_blocks = self._stream_response(
                    system_prompt, messages, stream_callback
                )
                if stop_reason == "end_turn":
                    self.conversation.append({"role": "assistant", "content": content_blocks})
                    return text
                # tool_use durante streaming — recai para modo normal
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=DEFAULT_MAX_TOKENS,
                    system=system_prompt,
                    tools=TOOL_DEFINITIONS,
                    messages=messages,
                )
            else:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=DEFAULT_MAX_TOKENS,
                    system=system_prompt,
                    tools=TOOL_DEFINITIONS,
                    messages=messages,
                )

            if response.stop_reason == "end_turn":
                text = self._extract_text(response)
                self.conversation.append({"role": "assistant", "content": response.content})
                return text

            if response.stop_reason == "tool_use":
                tool_results = self._handle_tool_calls(response)
                messages.append({"role": "assistant", "content": response.content})
                messages.append({"role": "user", "content": tool_results})
                self.conversation = list(messages)
                iterations += 1
                continue

            text = self._extract_text(response)
            self.conversation.append({"role": "assistant", "content": response.content})
            return text

        return "[Doctor] Limite de iterações de ferramentas atingido."

    def _stream_response(self, system_prompt: str, messages: list, callback) -> tuple[str, str, list]:
        """Streaming com callback por chunk de texto."""
        full_text = ""
        content_blocks = []
        stop_reason = "end_turn"

        with self.client.messages.stream(
            model=self.model,
            max_tokens=DEFAULT_MAX_TOKENS,
            system=system_prompt,
            tools=TOOL_DEFINITIONS,
            messages=messages,
        ) as stream:
            for event in stream:
                event_type = getattr(event, "type", "")
                if event_type == "content_block_delta":
                    delta = getattr(event, "delta", None)
                    if delta and getattr(delta, "type", "") == "text_delta":
                        chunk = delta.text
                        full_text += chunk
                        callback(chunk)

            final = stream.get_final_message()
            stop_reason = final.stop_reason or "end_turn"
            content_blocks = list(final.content)

        return full_text, stop_reason, content_blocks

    def _handle_tool_calls(self, response: anthropic.types.Message) -> list[dict]:
        """Executa tool calls e retorna resultados."""
        tool_results = []
        for block in response.content:
            if block.type != "tool_use":
                continue
            result = execute_tool(
                tool_name=block.name,
                tool_input=block.input,
                db_path=self.db_path,
            )
            tool_results.append({
                "type": "tool_result",
                "tool_use_id": block.id,
                "content": result,
            })
            log_observation(
                self.db_path,
                self.session_id,
                "tool",
                f"{block.name}: {result[:200]}",
            )
        return tool_results

    @staticmethod
    def _extract_text(response: anthropic.types.Message) -> str:
        parts = []
        for block in response.content:
            if hasattr(block, "text"):
                parts.append(block.text)
        return "\n".join(parts)

    def end_session(self) -> str:
        """Finaliza sessão, sintetiza e persiste."""
        if not self._initialized or not self.session_id:
            return ""
        if not self.auto_synthesize:
            return ""
        return synthesize_session(
            client=self.client,
            db_path=self.db_path,
            session_id=self.session_id,
            project=self.project,
            doc_type=self.doc_type,
        )

    def get_session_id(self) -> str:
        return self.session_id

    def reset_conversation(self) -> None:
        self.conversation = []
