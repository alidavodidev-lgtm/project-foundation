---
name: project-foundation
description: "Establish or repair project agreements, AGENTS.md, and PROJECT_STATUS.md during kickoff, adoption, or changes to the project foundation. Routine implementation and resume use the recorded rules and current status directly; load this skill only for foundation changes, repair, or an explicit request."
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
- **Routine resume:** Existing AGENTS instructions and the current PROJECT_STATUS.md snapshot are sufficient. Check actual repository state and continue the authorized task without loading this skill or its references unless explicitly requested or required by the host. If already loaded, skip kickoff and reuse recorded choices.
- **Repair:** Documents disagree with observed code or are incomplete. Preserve history, distinguish observations from assumptions, and reconcile only the affected sections. Never mark historical work verified merely because a document says it passed.

## 1. Inspect without changing the project

Locate the intended project root; ask if ambiguous. Inspect applicable parent/root/nested AGENTS.md and AGENTS.override.md files, host-native instructions such as CLAUDE.md or GEMINI.md when present, existing status documents, README, manifests, lockfiles, and top-level layout. Respect the host's instruction precedence; filenames do not have identical loading behavior across clients. For a Git repository, inspect branch, status, and relevant diff summaries. Use targeted discovery; do not print secrets, huge trees, dependencies, or generated output.

Identify what is already decided: product goal, users, platform, stack/versions, commands, structure, current work, user changes, data stores, deployment, and constraints. Do not run untrusted setup scripts during inspection. Do not initialize Git, install dependencies, move files, or overwrite documents at this stage.

## 2. Agree on the foundation

For kickoff/adoption or a material agreement change, read [project-agreement.md](references/project-agreement.md) before presenting choices. It covers documentation language, backup protection, skill selection, and proportionate scope/quality criteria. Reuse recorded decisions. Bundle independent unresolved questions in the user's language with recommendations; follow up only on consequential dependencies. Silence is not approval. Resolve language, required backup protection, and material scope/architecture choices before dependent writes. Do not add recurring approval gates for routine authorized work.

## 3. Write the two core documents

Read and adapt [AGENTS.template.md](assets/AGENTS.template.md) and [PROJECT_STATUS.template.md](assets/PROJECT_STATUS.template.md) only when creating or restructuring these documents. Replace template slots with confirmed facts or explicit unknowns; omit irrelevant sections. Translate prose to the selected language. Do not copy template-authoring notes into the project.

**AGENTS.md owns stable rules:** purpose, document language, skills and triggers, stack/structure, commands, backup/restore policy, quality requirements, and how to resume/update status. Make these usable directly during routine work. Load `project-foundation` only for foundation changes, repair, or an explicit user/host request. Merge existing guidance; preserve unrelated rules, override files, and nested scopes. Do not create global instructions or weaken security rules. For an explicit backup opt-out, record the decision and recovery exposure in 1-2 lines; omit unused policy fields. Keep concrete coverage, authority, verification, and restore details for an active policy.

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

## 4. Work, verify, and leave a reliable handoff

At each task start, read applicable rules and the current snapshot; recheck actual files/Git state before trusting recorded state. Preserve user changes. Keep the task's acceptance criteria visible and execute the approved backup policy at its triggers before protected changes.

Update PROJECT_STATUS.md after a meaningful milestone, a material decision/blocker, a backup/recovery event, and before handing back or switching tasks. Record: timestamp with timezone/offset, task ID, outcome, affected paths or commit, relevant checks with actual results, limitations, and next action. Save evidence under a stable project-relative path or link to CI/commit; do not paste full logs. Distinguish passed, failed, not run, and unavailable. Associate verification with the revision or working-tree scope it actually checked. Never claim a check or backup ran when it did not.

Keep the current snapshot, phase/task table, and history consistent. Update AGENTS.md only when a stable agreement changes. At handoff, summarize what changed, validation, any required decision, and the next concrete step. If the request was kickoff only, stop after the agreed foundation is prepared.

## Context and token discipline

- Keep AGENTS.md proportional to the project (rough target: 80-140 lines, not a minimum or cap); reference deeper detail. Keep the snapshot near the top (rough target: 30-60 lines), with the next 1-3 actions. Omit empty or irrelevant fields.
- Read the snapshot section first using bounded ranges, not the whole status history. Locate section boundaries and relevant IDs with `rg -n` or equivalent, then read only needed ranges; do not assume a fixed line count contains the complete snapshot. Skip dependency/build/backup directories in ordinary searches. Read a full file when the task needs it.
- Load only the selected skill needed for the current task and its relevant references. Do not repeatedly load this skill's templates or backup guide on normal resume.
- Archive completed old history when it obscures active state; 200-250 lines is a warning, not a required threshold. Earlier separation is useful for frequent updates; small projects need no extra file. Retain active work, decisions, unresolved risks, latest evidence references, and an archive index. Verify moved content and links before removing live text; preserve meaningful history.
- Use concise test/build output when supported; retain exit status and result totals. Save verbose logs when needed and inspect relevant diagnostics on failure. Do not hide failures behind a successful output-filter command or rerun a check just to shorten its output.
- Batch independent reads and checks; reuse evidence until code, inputs, or the question changes. Do not rerun identical checks without a reason or sacrifice required verification to save tokens.
- Log concise facts and rationale, not raw tool output, repeated rules, or private reasoning. Record token/cost numbers only if measured by the environment; do not promise a fixed saving.

## Foundation completion

Before claiming setup complete, verify that language and backup choices are recorded; skill choices are confirmed; documents preserve existing rules; links/paths resolve; commands and verification are truthfully labeled; the roadmap has acceptance criteria; and an actionable next step exists. Report pending items explicitly. This is a review of the created foundation, not a claim that the product has passed security, accessibility, or production-readiness checks.
