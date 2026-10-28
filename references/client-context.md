# Project instructions across clients

Read only when establishing project-local persistence or switching clients. AGENTS.md remains the source of stable rules; PROJECT_STATUS.md remains the source of changing state. Discovery and settings vary by version and deployment surface. Check the actual client's loaded context; these are documented integration routes, not a record of end-to-end testing.

## Shared procedure

Inspect existing native instruction files before adding anything. Preserve their rules and precedence. Prefer an existing supported AGENTS.md loader. Otherwise, add the smallest local import or instruction to read AGENTS.md at project start. Translate prose to the agreed documentation language; preserve syntax. Report the adapter path and how to verify it. Never create both an import and a second full copy of the same rules.

Do not import PROJECT_STATUS.md wholesale into always-loaded context. AGENTS.md already tells the agent to read its current snapshot and relevant entries on resume. If the host cannot load instructions persistently, use the explicit resume prompt at the end of this reference.

## Client routes

- **Codex:** Use project AGENTS.md directly, preserving applicable override/nested scopes. Follow the host's actual instruction hierarchy. See [official instructions documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- **Claude Code:** Recent versions can load AGENTS.md directly, but an existing CLAUDE.md or session settings can change that. Where needed, add `@AGENTS.md` to the project-root CLAUDE.md, retaining its other content. Relative import paths resolve from the importing file, so `.claude/CLAUDE.md` needs `@../AGENTS.md` instead. Verify with the client's context/memory view. See [official memory documentation](https://code.claude.com/docs/en/memory).
- **Gemini CLI:** If the workspace already loads AGENTS.md via its context configuration, reuse it. Otherwise add `@./AGENTS.md` to a root GEMINI.md. Preserve other content. Verify with `/memory show`; reload with `/memory reload` if needed. See [official context documentation](https://geminicli.com/docs/cli/gemini-md/).
- **Google Antigravity:** The documented rules system supports project AGENTS.md directly. Reuse it; inspect the active Rules/context UI before adding another file. See [official rules documentation](https://antigravity.google/docs/rules/).
- **Cursor, Copilot, and other clients:** Check the active surface/version's AGENTS.md support first. If needed, merge a brief instruction into the client's existing project-level rules: "At the start of work, read and follow AGENTS.md, then read the current snapshot and relevant tasks in PROJECT_STATUS.md." Use the client's documented format and scope, not an invented import syntax. This is an instruction to read files, not proof the host injects their contents. Verify in a fresh session, or use the explicit prompt below.

## Explicit resume fallback

```text
Read and follow the project's AGENTS.md and applicable native instructions.
Read the current snapshot and relevant tasks in PROJECT_STATUS.md.
Use bounded section reads; locate relevant task IDs before reading details.
Check the actual working tree, then continue the next authorized task.
Reuse recorded choices. Load project-foundation only for foundation changes,
document repair, or an explicit user/host request.
```

Skills require a client with local file access to maintain project files; a chat-only model cannot provide that behavior merely by reading the skill text. Instructions guide the agent; they are not a sandbox or a scheduler.
