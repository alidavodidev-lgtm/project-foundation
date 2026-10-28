# AGENTS template authoring notes

Adapt the content below to the project and selected documentation language. Replace braces, omit irrelevant sections, and remove these authoring notes. Preserve existing instructions. This is an outline, not a mandate to create new tooling.

---

# Project agreements

## Purpose and scope

- Product outcome and users: {confirmed outcome and users}
- Platforms and delivery level: {platforms; prototype/internal/production}
- In scope / non-goals: {boundaries}
- Acceptance overview: {observable success criteria; link to details}

## Documentation and continuation

- Documentation language: {confirmed language}; UTF-8. Conversation/UI language: {separate choices if relevant}.
- Follow these agreements throughout work. Use the `project-foundation` skill when available to prepare or resume the project and maintain its status; otherwise follow the rules recorded here.
- On resume, read the current snapshot in [PROJECT_STATUS.md](PROJECT_STATUS.md), relevant task entries, and applicable nested instructions; inspect actual repository state before continuing.
- Keep stable rules here and changing progress in PROJECT_STATUS.md. Update progress at milestones, meaningful decisions/blockers, and handoff. Keep verification and backup claims tied to actual evidence.
- Read referenced documents only when relevant. Preserve full meaningful history in linked archives; do not load archives by default.

## Approved skills

| Skill / source | Trigger and purpose | Selection / availability |
| --- | --- | --- |
| {exact name and source/path} | {when useful} | {approved/declined/host-required; available/unavailable} |

Approval: {user decision and date; reference if needed}. Load skills only for their triggers. Propose additions/removals when needs change. Installation and external actions require their own applicable authority.

## Stack and structure

- Stack and tool versions: {observed or agreed versions; constraints}
- Package manager / lockfile: {tools and paths}
- Structure: {small folder map with responsibilities and dependency boundaries}
- Naming / conventions: {project-specific rules or link}
- Generated and temporary output: {locations and ignore rules}
- Configuration: {safe example paths and required variable names; no values for secrets}

## Commands and verification

| Purpose | Working directory | Command | Evidence / verification state |
| --- | --- | --- | --- |
| {setup/build/lint/typecheck/test/run as applicable} | {relative path} | `{actual command}` | {verified reference or unverified} |

- Completion requires: {acceptance criteria and relevant checks for this project}.
- Report checks as passed, failed, not run, or unavailable, with relevant revision/scope. Do not report planned checks as executed.
- Preserve user changes; keep implementation scoped to the authorized task.

## Backup and recovery agreement

- Method and approval: {local/Git/hybrid/custom/explicitly declined; decision date}
- Coverage: {source, untracked/ignored assets, documents, data stores as applicable}
- Exclusions and remaining exposure: {regenerable artifacts and data outside coverage}
- Destination and access: {approved location/provider; privacy/encryption requirements; no credentials}
- Triggers: {baseline, milestones, protected changes; frequency if agreed}
- Retention: {count/age; whether pruning is authorized}
- Execution authority: {local copies, commits, remote uploads; their limits}
- Verification: {inventory/hash/readability checks; Git coverage checks; restore drill if required}
- Restore: {concrete safe procedure or runbook link; first restore to a separate location}
- On failure: {retry limit and what work depends on protection}
- Record backup results and references in PROJECT_STATUS.md. A plan or Git status alone is not a completed backup.

## Security and data

{Project-specific trust boundaries and required controls: secrets/configuration, authentication and authorization, validation, sensitive-data logging/retention, dependencies, migrations and rollback. Omit non-applicable requirements.}

## UI/UX and accessibility

{For a UI: critical flows/states, existing visual conventions, responsive/platform behavior, keyboard/focus/input requirements, localization/RTL, and relevant verification. Omit for projects without a UI.}

## Delivery and context discipline

- {Environment, deployment, migration, diagnostics, and performance expectations when relevant.}
- Use targeted reads and bounded output. Keep one source for each fact; link to detailed docs instead of duplicating them.
- At handoff, update PROJECT_STATUS.md with outcomes, evidence, limitations, and the next concrete action. Archive old completed history with verified links when the live file becomes unwieldy.
