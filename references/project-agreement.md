# Project agreement criteria

Read during kickoff/adoption or a material foundation change, before presenting unresolved choices. Use only the criteria relevant to the project. Reuse repository facts and prior decisions; ordinary implementation and resume do not need this reference.

## Required choices

Use available question tools or concise chat. Continue independent read-only discovery while waiting for answers.

### Documentation language

Before creating or rewriting project documentation, ask: **"Which language should project documentation use? English (default), your conversation language, or another language?"** The default is the suggested choice, not permission to skip the question. An explicit earlier answer such as "use the defaults" is sufficient; record it and do not ask again. If unanswered, defer documentation writes and dependent implementation.

Store prose in the selected language using UTF-8. Keep filenames, paths, commands, code identifiers, and canonical status codes unchanged. Conversation language and product UI language are separate choices; do not infer either from documentation language. Preserve existing documents' language unless a translation is requested; agree on scope when existing and selected languages differ.

### Backup policy

After inspection, offer relevant choices: **local snapshot**, **Git checkpoints**, **hybrid Git plus local/data snapshots**, or **another user-specified method**. Explain the actual coverage and tradeoff in one sentence each; recommend based on this project. Allow the user to explicitly decline backups and record the accepted limitations.

Agree on destination, included/excluded data, triggers, retention, restore method, and any remote upload/commit authority. Reuse an existing agreed policy. Read [backup-policy.md](backup-policy.md) when defining or executing backups. Do not begin project mutations, including replacing existing documentation, before the policy is decided and any required baseline is verified. For an empty project, record that there is no prior content to protect. If execution is unavailable, record the limitation and defer only work requiring that protection; policy text is not a completed backup.

### Project skill selection

Discover the current environment's available skill metadata. Propose the smallest useful set as a short table: exact skill name, why it fits this project, when it will be loaded, and whether available. Read full instructions only when needed for an actual task. Do not hardcode a universal skill catalog or load every suggested skill.

Ask the user to **approve, add, remove, or choose no optional skills** before using the proposed project set. Persist approved and declined choices, source identifiers/paths, and triggers in AGENTS.md. Existing explicit approval is enough; propose a delta only when the project's needs materially change. A selected skill is available for relevant tasks, not mandatory on every turn.

If host/system instructions already require a skill, disclose it separately with its reason; the optional selection cannot override those instructions. Do not install skills, enable integrations, or delegate to agents merely because they are listed. If a selected skill is unavailable, disclose the gap and offer the closest available workflow; get installation authority before installing it. Skill approval does not authorize publishing, messages, purchases, or other external effects.

## Scope and quality criteria

Infer facts from the repository; label unknowns and assumptions. Record decisions and rationale; unresolved decisions block only dependent tasks.

- Product outcome, target users, platforms, MVP scope, non-goals, constraints, and observable acceptance criteria. Distinguish prototype, internal tool, and production needs.
- Existing or chosen stack, runtime/package manager versions, lockfiles, key dependencies, module/data boundaries, external services, and deployment target. Preserve a suitable existing stack; do not force a framework or add dependencies without a concrete reason. Verify changing compatibility/support claims against primary documentation when needed.
- A small folder map with responsibilities, naming rules, generated/temporary output locations, and import/dependency boundaries. Create only directories needed now. Preserve framework conventions; propose disruptive cleanup separately. Keep secrets and build/cache artifacts out of version control.
- Reproducible setup, safe configuration examples, and actual build/lint/type/test commands with working directories. Mark untried commands as unverified. Add CI only when in scope; use the project's existing checks first.
- Security/data requirements tied to actual trust boundaries: secrets handling, authentication/authorization, input and upload validation, sensitive-data access/logging/retention, dependency risks, migrations, and recovery. Never store credentials or real sensitive records in Markdown. A full security audit or legal/compliance certification is a separate task.
- For user interfaces: core flows, success/error/empty/loading states, accessible input and keyboard use, focus and contrast, responsive/platform behavior, consistency with existing design, localization/RTL where relevant, and how these will be checked. Do not impose web/mobile checks on a CLI or backend.
- Risk-based verification and completion criteria: relevant checks, critical failure paths, manual/UI review where appropriate, and remaining limitations. A small reversible documentation change does not require an application test suite.
- For deployed services when relevant: environment separation, safe migrations, useful redacted diagnostics, rollback, and measurable performance/reliability expectations. Do not invent service targets or deployment authority.

Bundle independent unresolved choices with the language, backup, and skill proposal. Offer recommendations with tradeoffs; request follow-up only for consequential decisions that depend on an answer. Record confirmed facts, unknowns, and rationale without adding recurring approval gates for already-authorized work.
