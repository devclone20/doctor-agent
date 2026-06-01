# Claude Swarm — Padrões de Orquestração

> Padrões de orquestração para sistemas multi-agente com Claude, aplicados ao contexto
> Doctor-Hacker-Rider. Cada padrão inclui diagrama, descrição, e exemplo de configuração.

---

## O que é Claude Swarm

Claude Swarm é uma abordagem de orquestração onde múltiplos agentes Claude
especializados colaboram para resolver tarefas complexas. Cada agente tem:
- Um system prompt especializado (a sua "skill")
- Um conjunto de tools disponíveis
- Um papel definido no workflow

A "swarm" não é um produto Anthropic específico — é um padrão de arquitectura
que usa os primitivos do Anthropic SDK: `tool_use`, `subagents`, e `context passing`.

---

## Padrão 1: Hub-and-Spoke (Rider como Hub)

### Diagrama

```
                    ┌────────┐
          ┌────────▶│ Doctor │────────┐
          │         └────────┘        │
          │                           ▼
    ┌─────┴──────┐              ┌──────────┐
    │   Rider    │◀─────────────│  output  │
    │   (Hub)    │              └──────────┘
    └─────┬──────┘
          │         ┌────────┐
          └────────▶│ Hacker │────────┐
                    └────────┘        │
                                      ▼
                               ┌──────────┐
                               │  output  │
                               └──────────┘
```

### Descrição

O Rider é o único ponto de entrada. Recebe o pedido do utilizador, decide qual
especialista invocar, e sintetiza os outputs numa resposta final coerente.

- **Rider:** orquestrador, nunca executa tarefas especializadas directamente
- **Doctor:** invocado pelo Rider via tool_use para tarefas académicas
- **Hacker:** invocado pelo Rider via tool_use para segurança/infra

### Quando usar

- Pedidos mistos ("revê a segurança e escreve o capítulo de avaliação")
- O utilizador não sabe qual agente é mais adequado
- Necessidade de síntese coerente de múltiplos outputs

### Configuração

```python
import anthropic
from typing import Any

client = anthropic.Anthropic()

# System prompts carregados dos ficheiros .md
RIDER_PROMPT = open("rider.md").read()
DOCTOR_PROMPT = open("doctor.md").read()
HACKER_PROMPT = open("hacker.md").read()


def call_doctor(task: str, context: str = "") -> str:
    """Invocar o Doctor como sub-agente."""
    messages = [{"role": "user", "content": f"{context}\n\n{task}" if context else task}]
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system=DOCTOR_PROMPT,
        messages=messages,
    )
    return response.content[0].text


def call_hacker(task: str, context: str = "") -> str:
    """Invocar o Hacker como sub-agente."""
    messages = [{"role": "user", "content": f"{context}\n\n{task}" if context else task}]
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system=HACKER_PROMPT,
        messages=messages,
    )
    return response.content[0].text


# Tools que o Rider pode invocar
RIDER_TOOLS = [
    {
        "name": "call_doctor",
        "description": "Invocar o Doctor para tarefas académicas: dissertações, artigos, citações, pesquisa científica, formatação Word/LaTeX.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task": {"type": "string", "description": "Tarefa académica detalhada"},
                "context": {"type": "string", "description": "Contexto do projecto (opcional)"}
            },
            "required": ["task"]
        }
    },
    {
        "name": "call_hacker",
        "description": "Invocar o Hacker para tarefas de segurança, infra, DevSecOps, análise de vulnerabilidades.",
        "input_schema": {
            "type": "object",
            "properties": {
                "task": {"type": "string", "description": "Tarefa de segurança/infra detalhada"},
                "context": {"type": "string", "description": "Contexto técnico (opcional)"}
            },
            "required": ["task"]
        }
    }
]


def hub_and_spoke(user_request: str) -> str:
    """
    Padrão Hub-and-Spoke: Rider como hub central.
    O Rider decide quais especialistas invocar e sintetiza os resultados.
    """
    messages = [{"role": "user", "content": user_request}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            system=RIDER_PROMPT,
            tools=RIDER_TOOLS,
            messages=messages,
        )

        # Acumular na conversa
        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            # Rider concluiu — extrair texto final
            return next(b.text for b in response.content if hasattr(b, "text"))

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type != "tool_use":
                    continue
                if block.name == "call_doctor":
                    result = call_doctor(block.input["task"], block.input.get("context", ""))
                elif block.name == "call_hacker":
                    result = call_hacker(block.input["task"], block.input.get("context", ""))
                else:
                    result = f"Tool {block.name} não reconhecida"

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })

            messages.append({"role": "user", "content": tool_results})
```

---

## Padrão 2: Pipeline (Doctor → Hacker → Rider em Sequência)

### Diagrama

```
User ──▶ Doctor ──────────▶ Hacker ──────────▶ Rider ──▶ User
         │                  │                  │
         │ (draft +         │ (draft +         │ (final
         │  research)        │  security        │  document)
         │                  │  review)         │
         ▼                  ▼                  ▼
      academic           security           synthesis
      output             annotations        + format
```

### Descrição

Cada agente processa sequencialmente o output do anterior. Sem ciclos.
Adequado quando as fases são bem separadas e o output de cada fase é
input determinístico da seguinte.

### Quando usar

- Dissertação com revisão de segurança do deployment (Doctor escreve, Hacker revê, Rider formata)
- Workflow de paper: Doctor draft → Hacker verifica claims técnicos de segurança → Rider exporta
- Tarefas onde a ordem de execução é fixa e conhecida antecipadamente

### Configuração

```python
def pipeline(user_request: str) -> dict[str, str]:
    """
    Padrão Pipeline: execução sequencial Doctor → Hacker → Rider.
    Cada agente recebe o output do anterior como contexto.
    """
    # Fase 1: Doctor produz o draft académico
    doctor_output = call_doctor(
        task=user_request,
        context=""
    )

    # Fase 2: Hacker revê o output do Doctor (segurança/técnico)
    hacker_output = call_hacker(
        task=f"Revê o seguinte conteúdo técnico e identifica problemas de segurança, imprecisões técnicas, ou vulnerabilidades nos sistemas descritos:\n\n{doctor_output}",
        context=f"Pedido original: {user_request}"
    )

    # Fase 3: Rider sintetiza e formata o resultado final
    rider_synthesis_prompt = f"""
Pedido original do utilizador: {user_request}

Output do Doctor (conteúdo académico):
{doctor_output}

Revisão do Hacker (segurança e técnica):
{hacker_output}

Sintetiza estes dois outputs num documento final coerente, incorporando as
correcções do Hacker no texto do Doctor onde aplicável.
"""
    final_response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system=RIDER_PROMPT,
        messages=[{"role": "user", "content": rider_synthesis_prompt}],
    )

    return {
        "doctor_output": doctor_output,
        "hacker_review": hacker_output,
        "final": final_response.content[0].text,
    }
```

---

## Padrão 3: Parallel (Múltiplos Agentes em Simultâneo)

### Diagrama

```
                    ┌────────┐
          ┌────────▶│ Doctor │────────┐
          │         └────────┘        │
          │                           ▼
User ──▶ Rider                   ┌─────────┐ ──▶ User
          │                      │ Reducer │
          │         ┌────────┐   │ (Rider) │
          └────────▶│ Hacker │───▶         │
                    └────────┘   └─────────┘
```

### Descrição

Doctor e Hacker executam em paralelo sobre o mesmo pedido. O Rider (como reducer)
recebe ambos os outputs e sintetiza a resposta final. Reduz a latência total quando
as tarefas são independentes.

### Quando usar

- Análise de um documento: Doctor revê estrutura académica, Hacker revê segurança técnica
- Geração de relatório: Doctor escreve texto, Hacker escreve secção de segurança — ambos independentes
- Research: Doctor pesquisa papers, Hacker pesquisa CVEs — sobre temas paralelos

### Configuração

```python
import concurrent.futures
from typing import NamedTuple


class ParallelResult(NamedTuple):
    doctor: str
    hacker: str
    synthesis: str


def parallel(user_request: str) -> ParallelResult:
    """
    Padrão Parallel: Doctor e Hacker executam concorrentemente.
    ThreadPoolExecutor — seguro para I/O bound (chamadas API).
    """
    # Decompor o pedido em subtarefas paralelas
    decompose_response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=512,
        system=RIDER_PROMPT,
        messages=[{
            "role": "user",
            "content": f"Decompõe este pedido em duas subtarefas independentes: uma para o Doctor (académica) e uma para o Hacker (segurança/técnica). Pedido: {user_request}\n\nResponde em JSON: {{\"doctor_task\": \"...\", \"hacker_task\": \"...\"}}"
        }],
    )

    import json
    tasks = json.loads(decompose_response.content[0].text)
    doctor_task = tasks.get("doctor_task", user_request)
    hacker_task = tasks.get("hacker_task", user_request)

    # Executar em paralelo
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        doctor_future = executor.submit(call_doctor, doctor_task)
        hacker_future = executor.submit(call_hacker, hacker_task)

        doctor_output = doctor_future.result()
        hacker_output = hacker_future.result()

    # Rider sintetiza
    synthesis_response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        system=RIDER_PROMPT,
        messages=[{
            "role": "user",
            "content": f"""
Pedido original: {user_request}

Output do Doctor: {doctor_output}

Output do Hacker: {hacker_output}

Sintetiza numa resposta final coerente.
"""
        }],
    )

    return ParallelResult(
        doctor=doctor_output,
        hacker=hacker_output,
        synthesis=synthesis_response.content[0].text,
    )
```

---

## Padrão 4: Recursive (Agentes que Lançam Sub-Agentes)

### Diagrama

```
User ──▶ Rider
              │
              ▼
           Doctor
              │
              ├──▶ Doctor-Research (sub-agente)
              │         │
              │         └──▶ CrossRef API
              │
              └──▶ Doctor-Review (sub-agente)
                        │
                        └──▶ Doctor-Research (recursivo, se necessário)
```

### Descrição

Um agente principal pode invocar sub-agentes do mesmo tipo para tarefas mais específicas.
O Doctor pode lançar um sub-Doctor para pesquisa enquanto escreve, ou para rever uma
secção específica sem perder o contexto global.

Útil para tarefas que requerem decomposição dinâmica não conhecida antecipadamente.

### Quando usar

- Dissertação longa: cada capítulo processado por uma instância Doctor separada
- Research extensiva: múltiplos sub-agentes pesquisam subtemas em paralelo
- Revisão recursiva: um agente revê o output de outro agente do mesmo tipo

### Configuração

```python
def recursive_doctor(task: str, depth: int = 0, max_depth: int = 2) -> str:
    """
    Doctor recursivo: pode invocar sub-Doctors para subtarefas.
    max_depth previne recursão infinita.
    """
    if depth >= max_depth:
        # Fallback: executar sem sub-agentes
        return call_doctor(task)

    # Tools para o Doctor invocar sub-Doctors
    sub_doctor_tools = [
        {
            "name": "research_subtopic",
            "description": "Pesquisar um subtópico específico com um sub-agente especializado",
            "input_schema": {
                "type": "object",
                "properties": {
                    "subtopic": {"type": "string", "description": "Subtópico a pesquisar"},
                    "num_papers": {"type": "integer", "description": "Número de papers a encontrar", "default": 10}
                },
                "required": ["subtopic"]
            }
        },
        {
            "name": "review_section",
            "description": "Invocar um sub-Doctor para rever uma secção específica",
            "input_schema": {
                "type": "object",
                "properties": {
                    "section_text": {"type": "string", "description": "Texto da secção a rever"},
                    "criteria": {"type": "string", "description": "Critérios de revisão"}
                },
                "required": ["section_text"]
            }
        }
    ]

    messages = [{"role": "user", "content": task}]

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=8192,
            system=DOCTOR_PROMPT,
            tools=sub_doctor_tools,
            messages=messages,
        )

        messages.append({"role": "assistant", "content": response.content})

        if response.stop_reason == "end_turn":
            return next(b.text for b in response.content if hasattr(b, "text"))

        if response.stop_reason == "tool_use":
            tool_results = []
            for block in response.content:
                if block.type != "tool_use":
                    continue

                if block.name == "research_subtopic":
                    # Sub-Doctor para pesquisa — recursivo com depth+1
                    sub_task = f"Pesquisa {block.input['num_papers']} papers sobre: {block.input['subtopic']}"
                    result = recursive_doctor(sub_task, depth=depth + 1, max_depth=max_depth)

                elif block.name == "review_section":
                    # Sub-Doctor para revisão
                    sub_task = f"Revê esta secção: {block.input['section_text']}\nCritérios: {block.input.get('criteria', 'padrão IST')}"
                    result = recursive_doctor(sub_task, depth=depth + 1, max_depth=max_depth)

                else:
                    result = f"Tool {block.name} não reconhecida"

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })

            messages.append({"role": "user", "content": tool_results})
```

---

## Guia de Selecção de Padrão

```
Qual é a natureza do pedido?
│
├── Pedido misto ou incerto → Hub-and-Spoke
│   (o utilizador não sabe qual agente precisa)
│
├── Fases bem definidas e sequenciais → Pipeline
│   (ex.: escreve → revê segurança → formata)
│
├── Tarefas independentes → Parallel
│   (ex.: pesquisa papers E analisa vulnerabilidades em simultâneo)
│
└── Tarefa complexa com decomposição dinâmica → Recursive
    (ex.: dissertação completa onde cada capítulo requer pesquisa própria)
```

---

## Considerações de Performance e Custo

| Padrão | Latência | Custo de tokens | Complexidade |
|---|---|---|---|
| Hub-and-Spoke | Média (sequencial com routing) | Médio (Rider overhead) | Baixa |
| Pipeline | Alta (completamente sequencial) | Alto (contexto cresce) | Baixa |
| Parallel | Baixa (I/O concurrent) | Alto (múltiplas chamadas) | Média |
| Recursive | Variável (depth-dependent) | Muito alto (sem max_depth) | Alta |

**Optimizações transversais:**
- Usar `cache_control` nos system prompts longos (doctor.md, hacker.md) — reduz custo em ~90%
- Definir `max_tokens` conservadoramente em sub-agentes (não todos precisam de 8192 tokens)
- Limitar `max_depth` no padrão Recursive (2–3 é suficiente para a maioria dos casos)
