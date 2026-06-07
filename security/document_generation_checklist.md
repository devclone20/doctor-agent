# Checklist de Segurança — Geração de Documentos

> Aplicável a todos os outputs do Doctor Agent: python-docx, LaTeX, PDF, Markdown.
> Verificar antes de entregar qualquer documento gerado ao utilizador.

---

## 1. python-docx

### XML Injection
- [ ] Nenhum conteúdo de utilizador é inserido directamente em XML raw (`.element.xml`)
- [ ] Usar exclusivamente a API python-docx (`paragraph.add_run()`, `table.add_row()`) — nunca manipular `._element` com strings de utilizador
- [ ] Campos de merge (`«field»`) validados contra lista de campos permitidos antes do merge
- [ ] Nenhum conteúdo HTML é passado sem sanitização a `python-docx-html` ou equivalente

### Path Traversal
- [ ] Caminhos de ficheiros de imagem validados com `pathlib.Path.resolve()` e confirmados dentro do directório de trabalho autorizado
- [ ] Nomes de ficheiro de output sanitizados: remover `../`, `/`, `\`, caracteres nulos
- [ ] Templates `.docx` carregados apenas de paths explícitos hard-coded ou lista de permitidos — nunca de input de utilizador

### Metadata
- [ ] `doc.core_properties.author` não expõe nome de utilizador do sistema (`os.getlogin()`)
- [ ] `doc.core_properties.last_modified_by` limpo ou definido como valor neutro antes de entrega
- [ ] Remover propriedades custom que possam conter paths internos ou tokens

### Macros VBA
- [ ] Nenhum template `.docm` é usado ou gerado
- [ ] Verificar que ficheiros `.docx` de template recebidos externamente não contêm streams `vbaProject.bin` (inspecionar com `zipfile` — rejeitar se presente)

### Links Externos
- [ ] URLs inseridas no documento validadas contra allowlist de domínios ou esquemas (`https://` apenas)
- [ ] Nenhuma URL de utilizador é inserida sem validação de origem
- [ ] Hiperlinks com `rel="noopener"` quando o formato suporta (HTML export)

---

## 2. LaTeX

### Command Injection
- [ ] `\write18` ausente em todo o output gerado — verificar com `check_latex_shell_escape()`
- [ ] `\immediate\write` com paths de utilizador bloqueado
- [ ] `\input{}` e `\include{}` apenas com paths literais hard-coded — nunca interpolação de input de utilizador
- [ ] `\def`, `\newcommand`, `\renewcommand` com conteúdo de utilizador bloqueado (podem redefinir comandos de segurança)
- [ ] `\catcode` não presente em output gerado (altera tokenização — vector de injecção)

### Path Traversal em \includegraphics
- [ ] Paths em `\includegraphics{}` validados como relativos e dentro do directório do projecto
- [ ] Nenhum path absoluto (`/etc/`, `C:\`) em comandos de inclusão de ficheiros
- [ ] Extensões de imagem restritas a: `.pdf`, `.png`, `.jpg`, `.eps`

### Shell Escape
- [ ] Compilação sempre sem `--shell-escape` (ou `-shell-escape`)
- [ ] Usar `get_safe_latex_preamble()` que exclui pacotes que requerem shell escape: `minted`, `epstopdf` (modo auto), `svg` (modo inkscape), `gnuplottex`
- [ ] Se `minted` for absolutamente necessário: isolar compilação em sandbox sem acesso à rede

### Ficheiros Auxiliares com Dados Sensíveis
- [ ] `.log` — pode conter paths completos do sistema; não enviar ao utilizador
- [ ] `.aux` — pode conter títulos, autores, referências antes de publicação; tratar como confidencial
- [ ] `.synctex.gz` — contém paths do sistema de ficheiros; nunca incluir em arquivo de entrega
- [ ] Limpar directório de build antes de entregar: enviar apenas `.pdf` final

---

## 3. Geração por IA

### Hallucinated Credentials
- [ ] Output do modelo revisto para: padrões de API key (`sk-...`, `Bearer ...`, `ghp_...`, tokens JWT)
- [ ] DOIs e ISBNs verificados — o modelo alucina referências bibliográficas com DOIs plausíveis mas inválidos
- [ ] Nomes de pessoas reais em contextos negativos ou fictícios — risco de difamação
- [ ] Emails e números de telefone gerados por IA removidos se não verificados

### PII em Exemplos Gerados
- [ ] Exemplos de código sem nomes reais, emails reais, números reais de identificação
- [ ] Datasets de exemplo gerados com dados sintéticos — nunca PII real interpolada de contexto de sessão
- [ ] Histórico de conversa não incluído acidentalmente em outputs de documento

### API Keys em Código Exemplo
- [ ] Snippets de código com placeholders explícitos: `YOUR_API_KEY`, `<TOKEN>` — nunca valores reais
- [ ] Verificar que variáveis de ambiente do processo não foram interpoladas no output
- [ ] `.env` do projecto nunca referenciado ou incluído em output

### Dados de Treino Expostos
- [ ] Output não reproduz verbatim blocos extensos de texto com copyright (>50 palavras de uma fonte)
- [ ] Código gerado que replica implementações proprietárias flagrante: identificar e alertar utilizador

---

## 4. Validação Pré-Entrega

Steps obrigatórios antes de entregar qualquer documento gerado ao utilizador:

```
1. sanitize_latex_content(content)       — se LaTeX
2. check_latex_shell_escape(content)     — rejeitar se lista não vazia
3. Scan de padrões de credenciais no output final
4. Verificar limites de tamanho (abstract ≤250 words, etc.)
5. Confirmar que nenhum path interno do servidor está no output
6. Se .docx: verificar ausência de vbaProject.bin
7. Log de auditoria: timestamp, tipo de documento, hash SHA-256 do output
```

### Scan de Credenciais (regex mínimo)
```python
import re

CREDENTIAL_PATTERNS = [
    r"sk-[A-Za-z0-9]{32,}",           # OpenAI API key
    r"ghp_[A-Za-z0-9]{36}",           # GitHub PAT
    r"Bearer\s+[A-Za-z0-9\-._~+/]+=*",# Bearer token
    r"eyJ[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+\.[A-Za-z0-9\-_]+",  # JWT
    r"AKIA[0-9A-Z]{16}",              # AWS Access Key
]
```

---

## 5. IST Específico

### Declaração de Integridade Académica
- [ ] Documento final contém Declaração de Honra assinada (não gerada por IA — assinatura manual obrigatória)
- [ ] Nenhuma secção apresenta trabalho de terceiros sem citação IEEE correcta
- [ ] Self-plagiarism verificado se o autor tem trabalho publicado anteriormente

### AI Disclosure (IST 2026)
- [ ] `aidisclose` preenchida com: ferramenta usada, finalidade específica, secções afectadas
- [ ] Declaração em conformidade com Despacho IST 2026 (verificar número oficial)
- [ ] Orientador notificado e aprovou o uso de IA declarado

### Dados de Investigação Protegidos
- [ ] Dados de parceiros industriais ou institucionais não incluídos em exemplos sem autorização
- [ ] Resultados experimentais preliminares não publicados não expostos em metadados do documento
- [ ] Acordo de confidencialidade (NDA) verificado antes de incluir dados de parceiros em apêndices

---

*Checklist gerada por Doctor Agent · Hacker Skill — Security Review*
*Referências: OWASP Top 10, LaTeX Security Guide (Volker RW Schaa), python-docx docs*
