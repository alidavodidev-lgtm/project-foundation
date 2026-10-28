# Project Foundation

**Give your next AI session a project it can understand.**

[![Validate](https://github.com/alidavodidev-lgtm/project-foundation/actions/workflows/validate.yml/badge.svg)](https://github.com/alidavodidev-lgtm/project-foundation/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-2563eb.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-open_standard-059669.svg)](https://agentskills.io/specification)

[فارسی](README.fa.md) · [Installation](docs/installation.md) · [Example](docs/example.md) · [Compatibility](docs/compatibility.md)

Project Foundation is a portable **Agent Skill** for starting and continuing software projects with clear agreements, recoverable work, and an honest record of progress.

Ask your agent to use it. It inspects the project, asks the important questions, and maintains two useful documents:

| Document | What it remembers |
| --- | --- |
| **AGENTS.md** | Stable rules: stack, structure, approved skills, backups, security, UX, and verification. |
| **PROJECT_STATUS.md** | Living context: phases, tasks, decisions, evidence, blockers, work history, and the next step. |

Your existing code and rules are preserved. Additional documents appear when they have a real purpose. The core workflow is Markdown-only: no API key, MCP server, or runtime dependency.

## Start in one minute

For a local Codex setup, clone into the personal skills directory. This installs the skill for your projects on this machine; it does not automatically start a project or sync to cloud agents.

```bash
git clone https://github.com/alidavodidev-lgtm/project-foundation.git ~/.agents/skills/project-foundation
```

In Codex:

```text
Use $project-foundation to prepare this project before implementation.
```

In Claude Code, install into `~/.claude/skills/project-foundation` and invoke `/project-foundation`. Antigravity, Gemini CLI, Cursor, and Copilot have their own discovery and invocation rules. Follow the [installation guide](docs/installation.md) for your client and operating system. Keep one copy per client discovery scope to avoid duplicate names. These routes follow vendor documentation; see [what has actually been validated](docs/validation.md).

## What happens before implementation

1. **Inspect first.** Understand the repository, instructions, existing changes, and constraints.
2. **Choose the documentation language.** English is suggested; you make the choice. Product UI and conversation language stay separate.
3. **Choose a recovery plan.** Local snapshots, Git checkpoints, a hybrid, your existing service, or an explicit opt-out. Coverage and restore steps are recorded.
4. **Choose the project skills.** Review a relevant shortlist, then approve, add, remove, or decline optional skills. Nothing is installed just because it is suggested.
5. **Agree on the foundation.** Scope, acceptance criteria, stack, folders, security/data handling, UI/UX where relevant, and appropriate checks.
6. **Create or merge the documents.** Protect existing work and finish with a concrete next action.

```text
Inspect → Agree → Protect → Document → Implement → Verify → Update
                                      ↑                    │
                                      └──── Next session ──┘
```

## Built for work that continues

- **New or existing projects.** Adopt the current stack and conventions before proposing changes.
- **Approvals that persist.** Answer once; revisit only when the decision changes.
- **Backups with evidence.** A policy, a Git status, and a successful recovery point are different things.
- **Useful progress history.** Record meaningful work, failed approaches that matter, check results, and exact next actions.
- **Security and UX in context.** Apply relevant requirements to the actual product, rather than pasting a universal checklist.
- **Smaller startup context.** Stable rules stay short; current status comes first; older history is linked and archived. No fixed token-saving claim.
- **One source of truth.** Client adapters point to shared rules; they do not duplicate the whole project manual.

To resume:

```text
Use project-foundation to resume this project. Read the current snapshot,
check the actual working tree, and continue the next authorized task.
Reuse the language, backup, and skill choices already recorded.
```

For an example of the questions and resulting documents, read the [illustrated walkthrough](docs/example.md).

## Compatible by design, explicit about evidence

The skill uses the [open Agent Skills format](https://agentskills.io/specification): a SKILL.md entry point, on-demand references, and adaptable templates. The workflow uses ordinary file/search/question tools rather than provider-specific APIs.

Installation routes are documented for **Codex, Claude Code, Google Antigravity, Gemini CLI, Cursor, and GitHub Copilot**. This is a format and documentation compatibility claim, not a claim that every client, model, version, or cloud surface has been tested. See the [compatibility matrix](docs/compatibility.md).

Agents still need project file access and the relevant execution permissions. This skill guides behavior; it does not enforce permissions, schedule backups, run a security certification, or guarantee a model follows every instruction.

## What's inside

```text
SKILL.md                      Portable workflow
agents/openai.yaml            Optional Codex UI metadata
assets/                       Adaptable AGENTS and status templates
references/                   Backup and client-context procedures
docs/                         Install, compatibility, example, validation
scripts/check_package.py      Maintainer-only package checks
.github/workflows/            Automated package validation
```

The maintainer tooling is optional. Agents do not need Python to use the skill.

## Contribute

Useful contributions include a reproducible client compatibility report, a clearer workflow, a new language guide, or a fix for a real project failure. Start with [CONTRIBUTING.md](CONTRIBUTING.md). For defects and ideas, [open an issue](https://github.com/alidavodidev-lgtm/project-foundation/issues).

If this makes your project easier to continue, a star helps others find it.

Released under the [MIT License](LICENSE). Product names belong to their respective owners; this is an independent community project.
