# PROJECT_STATUS template authoring notes

Translate prose to the selected language; keep status codes and identifiers stable. Replace braces and remove these notes. Create only phases/tasks that represent this project. This file and its linked archives together preserve the meaningful work history.

---

# Project status

## Current snapshot

- Updated: {ISO-8601 timestamp with timezone/offset}
- Objective / current scope: {short statement}
- Current phase and task: {IDs, statuses, immediate focus}
- Repository state: {branch/commit if available; relevant uncommitted changes; or no Git}
- Last meaningful outcome: {what actually changed}
- Latest verification: {check, outcome, checked revision/scope, evidence link; or not run}
- Latest backup: {artifact/commit reference, time, coverage verification; or none with reason}
- Active blockers / risks / decisions needed: {items with IDs or none}
- Next actions: {1-3 concrete actions with dependencies}

## Roadmap and tasks

Status codes: `pending`, `in_progress`, `blocked`, `done`, `skipped`.

| Phase ID | Outcome / acceptance criteria | Status | Dependencies / evidence |
| --- | --- | --- | --- |
| P00 | {foundation prepared with confirmed choices, working links, and review evidence} | {status} | {references} |
| {phase ID} | {project-specific deliverable and observable acceptance} | {status} | {dependencies or completion evidence} |

| Task ID | Phase | Task / acceptance criteria | Status | Dependencies / evidence / owner if useful |
| --- | --- | --- | --- | --- |
| T001 | P00 | {concrete task with observable completion} | {status} | {references} |

Use `done` only with acceptance evidence; for `blocked`, state cause and unblock action; for `skipped`, state reason. Keep unknown future work coarse until it can be planned responsibly.

## Decisions and approvals

| ID / date | Decision and rationale | Approval / assumptions | Consequences / supersedes |
| --- | --- | --- | --- |
| D001 / {date} | Documentation language: {language} | {user choice} | {scope of translated or existing docs} |
| D002 / {date} | Backup: {method or explicitly declined} | {user choice} | Policy in [AGENTS.md](AGENTS.md) |
| D003 / {date} | Project skills: {selection summary} | {user approval} | Registry in [AGENTS.md](AGENTS.md) |

Link to a separate decision record only when alternatives and rationale need substantial detail.

## Risks, blockers, and open questions

| ID | Issue / impact | State | Mitigation or unblock action | Owner if known |
| --- | --- | --- | --- | --- |
| {ID} | {specific issue} | {open/resolved/accepted} | {concrete action or decision} | {owner or unknown} |

## Work history and verification

Newest entries first. Keep concise entries for every meaningful step, phase transition, material failure, or recovery. Summarize tool output; link to evidence.

### {timestamp with offset} — {task ID}: {outcome}

- Result and affected paths/revision: {observed changes}
- Checks: {command/check, working directory, outcome, checked scope/revision, evidence location; or not run and why}
- Backup/recovery: {artifact/commit reference, coverage and verification result; when relevant}
- Decision or failed approach: {what matters for future work and why; omit if none}
- Remaining limitation / next action: {concrete continuation}

## History archives and supporting documents

{Project-relative links with date ranges and brief scope. Keep active decisions, risks, roadmap, and latest evidence references in the live file. No archive is needed at kickoff.}
