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
- Follow these agreements directly during routine work. Load `project-foundation` only to establish/change foundation agreements, repair documents, or satisfy an explicit user/host request.
- On resume, use bounded reads of the current snapshot section in [PROJECT_STATUS.md](PROJECT_STATUS.md); locate relevant task/decision IDs and read those ranges as needed. Follow applicable nested instructions and inspect actual repository state before continuing.
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

{Authoring: For an explicit opt-out, replace the fields below with 1-2 lines recording the decision/date and recovery exposure. For an active policy, retain relevant coverage, authority, verification, and restore details or link to them. Remove this note.}

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
- Search for relevant sections/IDs before reading large files; exclude generated/dependency/backup output. Read full files when needed. Keep one source for each fact; link to detail.
- Prefer concise test/build output; preserve the actual exit status and result totals. Inspect relevant diagnostics on failure; do not let output filtering mask a failed check.
- At handoff, update PROJECT_STATUS.md with outcomes, evidence, limitations, and the next concrete action. Archive old completed history with verified links when the live file becomes unwieldy.
