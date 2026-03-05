# Gibbs Agent Development Team

Dieses Repository dient als Workspace für das autonome Entwicklungsteam unter der Leitung von Gibbs (OpenClaw).

## 🤖 Das Team

| Rolle | Agent Name | Modell | Aufgabe |
|---|---|---|---|
| **Project Lead** | Gibbs | `google/gemini-3-pro-preview` | Orchestrierung, User-Kommunikation, GitHub Management. |
| **Architect** | `architect` | `ollama/mistral-nemo:12b` | Analysiert Requirements, erstellt `ARCHITECTURE.md`, wählt Tech-Stack. |
| **Developer** | `coder` | `ollama/qwen2.5-coder:7b` | Schreibt Code basierend auf Architektur-Plänen. |
| **QA Engineer** | `tester` | `ollama/llama3.1:latest` | Schreibt Tests, prüft Code-Qualität, meldet Bugs. |

## 🔄 Workflow

1.  **Ticket:** User erstellt ein Issue in GitHub (Label: `idea`).
2.  **Analysis:** Gibbs liest Issue, weist `architect` zu.
3.  **Design:** Architect erstellt Design-Docs (PR oder Commit).
4.  **Implementation:** Gibbs weist `coder` zu. Coder schreibt Code.
5.  **Review:** Gibbs weist `tester` zu. Tester prüft.
6.  **Merge:** Wenn QA 🟢, merged Gibbs den Code.

## 🛠 Tools

*   **Language:** Python (Primary), Node.js (Secondary).
*   **CI:** GitHub Actions.
*   **Docs:** Markdown.
