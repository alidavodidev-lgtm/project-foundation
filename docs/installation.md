# Install Project Foundation

The core skill is a folder named `project-foundation` containing SKILL.md, references, and assets. Git is convenient for installation; alternatively download the repository ZIP, extract it, and copy the folder into your client's skill directory. A ZIP download may extract as `project-foundation-main`; rename the installed skill folder to `project-foundation`.

Review the files before use. Clone/copy only into a destination that does not already exist; preserve and compare an existing installation rather than overwriting it. Do not install the same skill into several locations scanned by one client.

## Local personal installation

Choose the destination for **your client**:

| Client | Personal skill directory containing the project-foundation folder | Official source |
| --- | --- | --- |
| Codex | `~/.agents/skills/` | [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | `~/.claude/skills/` | [Skills](https://code.claude.com/docs/en/skills) |
| Google Antigravity | `~/.gemini/config/skills/` | [Migration and locations](https://antigravity.google/docs/migration/workflows-to-skills/) |
| Gemini CLI | `~/.gemini/skills/` | [Getting started](https://geminicli.com/docs/cli/tutorials/skills-getting-started/) |
| Cursor | `~/.cursor/skills/` or shared `~/.agents/skills/` | [Skills](https://cursor.com/docs/skills) |
| GitHub Copilot | Surface-dependent; documented personal paths include `~/.copilot/skills/` and `~/.agents/skills/` | [Skills](https://docs.github.com/en/copilot/concepts/customizations/agent-skills) |

These are local-machine paths. Personal skills do not automatically reach cloud sessions, remote workspaces, teammates, or managed environments. Check your surface's documented setup and trust requirements. See [compatibility](compatibility.md).

### macOS / Linux

Example for Codex; substitute the destination from the table for another client:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/alidavodidev-lgtm/project-foundation.git ~/.agents/skills/project-foundation
```

### Windows PowerShell

Example for Codex; `$HOME` is read as the normal user-home variable and is not reassigned:

```powershell
$skillParent = Join-Path $HOME '.agents\skills'
New-Item -ItemType Directory -Path $skillParent -Force | Out-Null
git clone https://github.com/alidavodidev-lgtm/project-foundation.git (Join-Path $skillParent 'project-foundation')
```

For Claude Code, use `.claude\skills` as the parent path; for other clients, use their documented directory. No administrator rights are needed for ordinary file copies or clones into your home folder.

## Share within a project

Copy the skill into a supported project directory, for example `.agents/skills/project-foundation/` for Codex/Antigravity or `.claude/skills/project-foundation/` for Claude Code. Cursor also documents `.cursor/skills/`, Gemini CLI `.gemini/skills/`, and Copilot `.github/skills/` with surface-specific alternatives. See the official sources above.

For a copy rather than a nested Git checkout, copy SKILL.md, LICENSE, assets/, references/, and optional agents/ metadata; preserve the folder name. Review the copy and commit the skill content with your project if you want teammates to receive it. This does not install it into a separate hosted account. Maintainer docs and validation tooling are optional for using the skill.

## Invoke and verify discovery

- **Codex:** type `$project-foundation` or select it in the skill picker. If a new skill does not appear, restart the client.
- **Claude Code:** type `/project-foundation`; the exact command can be prefixed in plugin or same-name installations. Check the skills menu.
- **Antigravity / Cursor:** select `project-foundation` from the client's skill or slash-command UI.
- **Gemini CLI:** check `/skills list`; use `/skills reload` after adding files, then ask it to use the skill.
- **Copilot / other hosts:** use the host's skill picker or ask it to use `project-foundation` and confirm it can read SKILL.md. Do not assume dollar/slash syntax is universal.

Use this first request in any client that can access the files:

```text
Use the project-foundation skill to prepare this project before implementation.
Ask for my documentation language, backup method, and proposed project skills.
Preserve existing files and rules. Do not start application implementation yet.
```

The first run should ask for documentation language (English suggested), present a concrete backup choice and relevant skill shortlist, and wait for decisions before dependent work. It then establishes the agreed documents. If it cannot find the skill, supply the actual installed SKILL.md path and ask it to read that file.

## Keep project agreements available

Skill discovery and persistent project instructions are separate. AGENTS.md is the shared rules document. The skill checks whether the active client loads it, using a small native adapter when needed. Read the [client-context reference](../references/client-context.md) for the available routes and fallback resume prompt. Keep one canonical rules document rather than copies for every client.

## Update or remove

For a Git clone you have not modified, inspect its status, then use `git pull --ff-only` from that skill directory. If you changed the skill locally, compare/merge your changes first. Recheck client discovery after an update. Back up any local modifications before removing or replacing the installed folder. Removing a skill does not remove the AGENTS.md or PROJECT_STATUS.md it created in your projects.
