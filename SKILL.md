---
name: project-foundation
description: "Prepare or resume a software project with agreed documentation language, backup policy, skills, structure, and quality criteria; maintain AGENTS.md and PROJECT_STATUS.md. Use for project kickoff, adopting an existing project, or continuing work under these agreements. Do not restart onboarding for ordinary tasks in an already configured project."
license: MIT
metadata:
  author: "alidavodidev-lgtm"
  version: "1.0.0"
---

# Project Foundation

Establish durable project agreements, then use them throughout delivery. The user's instructions take precedence over this skill's guidelines. Match the process to project size; kickoff alone does not authorize building the application, reorganizing an existing repository, or publishing anything.

This is a portable Agent Skill: use the host's available file, search, shell, and question tools. If a suggested tool such as `rg` is unavailable, use its equivalent. Native invocation syntax varies; `project-foundation` is the skill name, not a universal slash/dollar command. No particular provider, plugin, network connection, or helper runtime is required for the core workflow.

## Choose the mode

- **Kickoff/adoption:** Agreements are missing or the user asks to establish them. Inspect first, ask for the decisions below, then create or merge the two core documents.
- **Resume:** Agreements exist. Read applicable AGENTS instructions and the current snapshot of PROJECT_STATUS.md, check actual repository state, and continue the authorized task. Do not repeat answered questions. Ask only about a consequential change or missing decision.
- **Repair:** Documents disagree with observed code or are incomplete. Preserve history, distinguish observations from assumptions, and reconcile only the affected sections. Never mark historical work verified merely because a document says it passed.

## 1. Inspect without changing the project

Locate the intended project root; ask if ambiguous. Inspect applicable parent/root/nested AGENTS.md and AGENTS.override.md files, host-native instructions such as CLAUDE.md or GEMINI.md when present, existing status documents, README, manifests, lockfiles, and top-level layout. Respect the host's instruction precedence; filenames do not have identical loading behavior across clients. For a Git repository, inspect branch, status, and relevant diff summaries. Use targeted discovery; do not print secrets, huge trees, dependencies, or generated output.

Identify what is already decided: product goal, users, platform, stack/versions, commands, structure, current work, user changes, data stores, deployment, and constraints. Do not run untrusted setup scripts during inspection. Do not initialize Git, install dependencies, move files, or overwrite documents at this stage.

## 2. Ask for language, backups, and skills

Ask in the user's conversation language. Use available question tools, otherwise ask concise questions in chat. Prepare concrete choices before asking for approval. Continue independent read-only discovery while waiting; silence is not agreement.

### Documentation language

Before creating or rewriting project documentation, ask: **"Which language should project documentation use? English (default), your conversation language, or another language?"** The default is the suggested choice, not permission to skip the question. An explicit earlier answer such as "use the defaults" is sufficient; record it and do not ask again. If unanswered, defer documentation writes and dependent implementation.

Store prose in the selected language using UTF-8. Keep filenames, paths, commands, code identifiers, and canonical status codes unchanged. Conversation language and product UI language are separate choices; do not infer either from documentation language. Preserve existing documents' language unless a translation is requested; agree on scope when existing and selected languages differ.

### Backup policy

After inspection, offer relevant choices: **local snapshot**, **Git checkpoints**, **hybrid Git plus local/data snapshots**, or **another user-specified method**. Explain the actual coverage and tradeoff in one sentence each; recommend based on this project. Allow the user to explicitly decline backups and record the accepted limitations.

Agree on destination, included/excluded data, triggers, retention, restore method, and any remote upload/commit authority. Reuse an existing agreed policy. Read [backup-policy.md](references/backup-policy.md) when defining or executing backups. Do not begin project mutations, including replacing existing documentation, before the policy is decided and any required baseline is verified. For an empty project, record that there is no prior content to protect. If execution is unavailable, record the limitation and defer only work requiring that protection; policy text is not a completed backup.

### Project skill selection

Discover the current environment's available skill metadata. Propose the smallest useful set as a short table: exact skill name, why it fits this project, when it will be loaded, and whether available. Read full instructions only when needed for an actual task. Do not hardcode a universal skill catalog or load every suggested skill.

Ask the user to **approve, add, remove, or choose no optional skills** before using the proposed project set. Persist approved and declined choices, source identifiers/paths, and triggers in AGENTS.md. Existing explicit approval is enough; propose a delta only when the project's needs materially change. A selected skill is available for relevant tasks, not mandatory on every turn.

If host/system instructions already require a skill, disclose it separately with its reason; the optional selection cannot override those instructions. Do not install skills, enable integrations, or delegate to agents merely because they are listed. If a selected skill is unavailable, disclose the gap and offer the closest available workflow; get installation authority before installing it. Skill approval does not authorize publishing, messages, purchases, or other external effects.

## 3. Establish a proportionate project agreement

Infer facts from the repository and existing requirements. Ask only unresolved questions that change the outcome; offer a recommendation with its tradeoff. Bundle related questions instead of producing a long interview. Resolve scope and material stack/architecture choices before scaffolding.

Record the following as applicable; label unknowns and assumptions rather than inventing answers:

- Product outcome, target users, platforms, MVP scope, non-goals, constraints, and observable acceptance criteria. Distinguish prototype, internal tool, and production needs.
- Existing or chosen stack, runtime/package manager versions, lockfiles, key dependencies, module/data boundaries, external services, and deployment target. Preserve a suitable existing stack; do not force a framework or add dependencies without a concrete reason. Verify changing compatibility/support claims against primary documentation when needed.
- A small folder map with responsibilities, naming rules, generated/temporary output locations, and import/dependency boundaries. Create only directories needed now. Preserve framework conventions; propose disruptive cleanup separately. Keep secrets and build/cache artifacts out of version control.
- Reproducible setup, safe configuration examples, and actual build/lint/type/test commands with working directories. Mark untried commands as unverified. Add CI only when in scope; use the project's existing checks first.
- Security/data requirements tied to actual trust boundaries: secrets handling, authentication/authorization, input and upload validation, sensitive-data access/logging/retention, dependency risks, migrations, and recovery. Never store credentials or real sensitive records in Markdown. A full security audit or legal/compliance certification is a separate task.
- For user interfaces: core flows, success/error/empty/loading states, accessible input and keyboard use, focus and contrast, responsive/platform behavior, consistency with existing design, localization/RTL where relevant, and how these will be checked. Do not impose web/mobile checks on a CLI or backend.
- Risk-based verification and completion criteria: relevant checks, critical failure paths, manual/UI review where appropriate, and remaining limitations. A small reversible documentation change does not require an application test suite.
- For deployed services when relevant: environment separation, safe migrations, useful redacted diagnostics, rollback, and measurable performance/reliability expectations. Do not invent service targets or deployment authority.

Use a compact proposal and one combined confirmation where possible. Do not introduce recurring approval gates for routine work already authorized. Record material decisions and their rationale; unresolved consequential decisions remain visible and block only dependent tasks.

## 4. Write the two core documents

Read and adapt [AGENTS.template.md](assets/AGENTS.template.md) and [PROJECT_STATUS.template.md](assets/PROJECT_STATUS.template.md) only when creating or restructuring these documents. Replace template slots with confirmed facts or explicit unknowns; omit irrelevant sections. Translate prose to the selected language. Do not copy template-authoring notes into the project.

**AGENTS.md owns stable rules:** project purpose, document language, skills and triggers, stack/structure, safe commands, backup/restore policy, quality/security/UI requirements, and how to resume/update status. Include a short instruction to use the `project-foundation` skill when available for ongoing work and to follow the recorded agreements when it is unavailable. Keep stable operational rules directly usable without reloading this skill on every small task. Merge existing guidance carefully; preserve unrelated rules, override files, and nested scopes. Do not create global instructions or weaken existing security rules.

For the active client, check whether AGENTS.md will actually load in a fresh session. If it needs a native bridge, read [client-context.md](references/client-context.md), then add or merge the smallest project-local pointer/import as part of the agreed foundation. Do not create adapters for every vendor, duplicate rules, import the entire status history into startup context, or change global client settings. If native persistence cannot be verified, give an explicit resume prompt and label the limitation.

**PROJECT_STATUS.md owns changing state:** current snapshot first, phases/tasks and their acceptance criteria, dependencies, status, significant decisions, evidence, risks/blockers, backup references, work history, and exact next actions. The project roadmap lives here unless an established tracker already owns it; link to that tracker rather than maintaining conflicting copies.

Use stable IDs and status codes `pending`, `in_progress`, `blocked`, `done`, `skipped`. For `blocked`, include cause and unblock action; for `skipped`, include reason. `done` requires the stated acceptance evidence. Treat kickoff completion separately from product completion. Avoid unsupported progress percentages or estimates.

Do not fabricate historical stages. Mark inherited claims as reported/unverified; use Git or other evidence if reconstructing history. Record every meaningful completed step and phase transition, including failed approaches that affect future work; do not transcribe every tool call or the conversation.

### Additional Markdown files: create on demand

Default to the two core documents. Explain proposed additions and reuse existing equivalents:

| File | Create when it has a distinct purpose |
| --- | --- |
| README.md | Humans need durable setup/run/test instructions; link from AGENTS instead of repeating them. |
| docs/ARCHITECTURE.md | Module, data, or deployment boundaries need more explanation than a short map. |
| docs/decisions/NNNN-topic.md | A consequential, hard-to-reverse decision needs alternatives and rationale. |
| SECURITY.md | A project needs maintained security policy or vulnerability reporting guidance; never invent a reporting contact. |
| docs/RUNBOOK.md | Deployment, recovery, or operations need executable procedures. |
| docs/DESIGN.md | A UI needs reusable design rules, flows, accessibility, or localization specifications. |
| docs/history/PROJECT_STATUS-YYYY-MM.md | Older status history needs archiving to keep startup context small. |

Do not create empty placeholder files or a second parallel roadmap/changelog just to look professional. Keep one owner for each fact and use links elsewhere.

## 5. Work, verify, and leave a reliable handoff

At each task start, read applicable rules and the current snapshot; recheck actual files/Git state before trusting recorded state. Preserve user changes. Keep the task's acceptance criteria visible and execute the approved backup policy at its triggers before protected changes.

Update PROJECT_STATUS.md after a meaningful milestone, a material decision/blocker, a backup/recovery event, and before handing back or switching tasks. Record: timestamp with timezone/offset, task ID, outcome, affected paths or commit, relevant checks with actual results, limitations, and next action. Save evidence under a stable project-relative path or link to CI/commit; do not paste full logs. Distinguish passed, failed, not run, and unavailable. Associate verification with the revision or working-tree scope it actually checked. Never claim a check or backup ran when it did not.

Keep the current snapshot, phase/task table, and history consistent. Update AGENTS.md only when a stable agreement changes. At handoff, summarize what changed, validation, any required decision, and the next concrete step. If the request was kickoff only, stop after the agreed foundation is prepared.

## Context and token discipline

- Keep AGENTS.md compact (rough target: 80-140 lines, not a cap); reference deeper detail. Keep the current status snapshot near the top (rough target: 30-60 lines), with the next 1-3 concrete actions.
- Read the snapshot and relevant task/decision entries on resume, not the entire history. Use `rg` and bounded file reads. Skip dependency/build/backup directories in ordinary searches.
- Load only the selected skill needed for the current task and its relevant references. Do not repeatedly load this skill's templates or backup guide on normal resume.
- When status becomes unwieldy (roughly 200-250 lines), move completed old history into dated files; retain active work, decisions, unresolved risks, latest evidence references, and an archive index. Verify archive content and links before removing moved text from the live file. Preserve the full meaningful history across live and archived files.
- Batch independent reads and checks; reuse evidence until code, inputs, or the question changes. Do not rerun identical checks without a reason or sacrifice required verification to save tokens.
- Log concise facts and rationale, not raw tool output, repeated rules, or private reasoning. Record token/cost numbers only if measured by the environment; do not promise a fixed saving.

## Foundation completion

Before claiming setup complete, verify that language and backup choices are recorded; skill choices are confirmed; documents preserve existing rules; links/paths resolve; commands and verification are truthfully labeled; the roadmap has acceptance criteria; and an actionable next step exists. Report pending items explicitly. This is a review of the created foundation, not a claim that the product has passed security, accessibility, or production-readiness checks.
