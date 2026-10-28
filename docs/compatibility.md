# Compatibility and evidence

Documentation reviewed: **2026-10-28**. Client releases and discovery paths can change. Follow the linked vendor documentation for your actual version and deployment surface.

## Portable core

The package follows the [Agent Skills specification](https://agentskills.io/specification): standard name/description/license/metadata frontmatter, a Markdown workflow, relative references, and templates. It does not use proprietary tool names, hooks, dynamic shell interpolation, tool-approval extensions, or a provider-specific dependency for its core behavior. `agents/openai.yaml` is optional Codex UI metadata; other clients can ignore it.

The portability claim concerns the package format and workflow. A compatible client still needs file access, an interactive way to collect decisions, and suitable execution permissions. Markdown guidance cannot enforce a backup, override host rules, or ensure identical behavior across models.

## Documented routes

| Client | Skill format / install route | Project rule persistence | Evidence level |
| --- | --- | --- | --- |
| Codex | Agent Skills; personal/project `.agents/skills` | AGENTS.md | Vendor documentation; package structurally validated |
| Claude Code | Agent Skills; `.claude/skills` | AGENTS.md in supported configurations; CLAUDE.md import when needed | Vendor documentation; runtime not tested |
| Google Antigravity | Agent Skills; project `.agents/skills`, personal `.gemini/config/skills` | AGENTS.md | Vendor documentation; runtime not tested |
| Gemini CLI | Agent Skills; `.gemini/skills` and documented alias | GEMINI.md import or configured AGENTS.md | Vendor documentation; runtime not tested |
| Cursor | Agent Skills; `.cursor/skills` or `.agents/skills` | Check active client rules/context; add a minimal pointer if needed | Vendor documentation; runtime not tested |
| GitHub Copilot | Agent Skills; directories depend on CLI/IDE/cloud surface | Check that surface's repository instructions; pointer if needed | Vendor documentation; runtime not tested |
| Other file-capable assistants | Manually read SKILL.md and its relevant resources | Explicitly read AGENTS.md and current status at each new session | Manual workflow fallback; not native integration certification |

No claim is made that every AI product, plain web chat, model, version, or cloud environment is supported. Unsupported skill discovery may still allow a manually loaded workflow when file access exists.

## Primary sources

- [Codex skills](https://learn.chatgpt.com/docs/build-skills) and [AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
- [Claude Code skills](https://code.claude.com/docs/en/skills) and [memory / AGENTS.md loading](https://code.claude.com/docs/en/memory).
- [Antigravity skills migration and paths](https://antigravity.google/docs/migration/workflows-to-skills/) and [rules](https://antigravity.google/docs/rules/).
- [Gemini CLI skills](https://geminicli.com/docs/cli/tutorials/skills-getting-started/) and [GEMINI.md imports](https://geminicli.com/docs/cli/gemini-md/).
- [Cursor skills](https://cursor.com/docs/skills).
- [GitHub Copilot skills](https://docs.github.com/en/copilot/concepts/customizations/agent-skills).

## Help establish tested compatibility

An end-to-end compatibility report should include client/version, operating system, personal/project install path, model if relevant, discovery result, kickoff choices, produced files, fresh-session resume result, and any failure. Use a disposable project with no credentials or private data. A screenshot of a skill name in a menu establishes discovery, not correct backup or resume behavior.

See [validation](validation.md) for checks that are reproducible today and scenarios to run before strengthening claims.
