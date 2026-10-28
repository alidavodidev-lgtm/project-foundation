# A small project, from kickoff to handoff

This is an **illustrative example**, not a transcript of a real execution or evidence that a backup/test ran. Names, outputs, and decisions below demonstrate the intended workflow.

## Request

```text
Use project-foundation before building my bookmark API.
It is an internal service. Keep the existing Python stack.
Do not implement endpoints during kickoff.
```

The agent inspects the repository without changing it, then asks which language the documentation should use. The user chooses English. It proposes appropriate backup coverage and a short list drawn from the skills actually available in that environment.

The user chooses local snapshots to an approved folder outside the repository, and approves a relevant implementation skill while declining an optional full security scan. The agent records the choice; an unavailable skill is not silently installed. It clarifies the API's acceptance criteria and protects existing work according to the agreed policy before changing documents.

## Resulting AGENTS.md excerpt

```markdown
# Project agreements

## Scope

Internal bookmark API using the existing Python stack.
MVP: create, list, and delete the current user's bookmarks.
Public sharing and browser extensions are outside this phase.

## Continuation

Documentation language: English; UTF-8.
Read the current snapshot in PROJECT_STATUS.md at task start.
Use project-foundation when available; reuse agreed choices.

## Recovery

Local snapshots before disruptive edits and at phase completion.
Use the approved destination outside the repository.
Include source, project documents, and relevant untracked assets.
Exclude caches and secrets. Datastore recovery needs its own export.
Verify contents and record the artifact reference after execution.

## Quality

Preserve existing ownership checks. A user cannot delete another
user's bookmark. Record actual verification results before handoff.
```

A real AGENTS.md also records the exact approved destination, restore procedure, retention/authority, selected skill names and triggers, observed commands, and relevant stack/folder details. The excerpt omits these rather than fabricating a real backup path or tool result.

## Resulting PROJECT_STATUS.md excerpt

```markdown
# Project status

## Current snapshot

- Current phase: P01 / pending — bookmark operations.
- Latest outcome: project agreements prepared.
- Verification: application checks not run; kickoff changed documentation.
- Next action: inspect the existing authorization path for task T101.

## Roadmap

| Phase | Acceptance criteria | Status |
| --- | --- | --- |
| P00 | Choices confirmed; documents reviewed; links resolve | done |
| P01 | Users can create, list, and delete their own bookmarks | pending |
| P02 | Ownership and failure-path checks pass | pending |
```

In a real status document, `P00 / done` links to the actual agreement and review evidence, and the latest backup field references the verified artifact or states the agreed limitation. Kickoff completion does not imply P01 or P02 is complete.

## Next session

```text
Use project-foundation to resume. Read AGENTS.md and the current
PROJECT_STATUS.md snapshot, check the working tree, and continue T101.
```

The agent reuses the language, backup, and skill choices. It checks current files rather than trusting stale status, performs only the authorized work, runs relevant checks, and records what actually happened. Old history is archived with links when needed; it is not erased.
