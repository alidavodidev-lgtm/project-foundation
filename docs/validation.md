# Validation and behavioral scenarios

## What the automated checks establish

From a configured maintainer environment, run:

```bash
python -m skills_ref.cli validate "$PWD"
python scripts/check_package.py
```

The reference validator checks the Agent Skills frontmatter and naming. The package checker also checks string metadata, the declared license file, YAML parseability, Codex prompt naming, and local Markdown file-link targets outside fenced examples and output templates. It does not fetch external URLs, validate Markdown anchor fragments, or prove agent behavior. The CI workflow runs both commands with read-only repository permissions.

## Initial release evidence

Local release checks on **2026-10-28** passed with Python 3.12:

| Check | Observed result |
| --- | --- |
| Bundled skill-creator validator | Passed |
| `python -m skills_ref.cli validate` with the absolute skill directory | Passed against skills-ref 0.1.1 |
| `python scripts/check_package.py` | Specification, metadata, YAML, and local file targets passed |
| Disposable negative fixtures | Missing link, escaping link, malformed YAML, and missing declared license were rejected; restoring the fixture returned a clean result |

GitHub Actions exposes fresh results for each published revision. These are package checks, not a completed end-to-end trial in each client.

No all-client runtime certification, measured end-to-end token-saving percentage, actual project backup, or security/accessibility audit is claimed. Vendor-documented integration routes are recorded separately in [compatibility](compatibility.md).

## Updated 1.0.0 static context measurement

On **2026-10-29**, Python 3.14 and `tiktoken` 0.14.0 counted UTF-8 text with line endings normalized to LF. The baseline is `SKILL.md` at commit `61d40f4`; the candidate is the updated 1.0.0 entry point, including frontmatter.

| Encoding | Baseline entry point | Updated entry point | Reduction |
| --- | --- | --- | --- |
| `o200k_base` | 2,948 | 2,069 | 29.8% |
| `cl100k_base` | 2,963 | 2,078 | 29.9% |

This measures file contents, not a complete conversation, actual client loading, caching, billing, or task quality. Detailed language/backup/skill/scope criteria moved to an on-demand agreement reference. Kickoff reads that reference too, so the smaller entry point does not imply lower total kickoff input. Routine continuation should load neither file unless needed or explicitly requested; it still reads the project rules and relevant current state.

To reproduce, read the baseline with `git show 61d40f4:SKILL.md`, read the current entry point as UTF-8, normalize CRLF to LF, and count each string with `len(tiktoken.get_encoding(encoding).encode(text))`. The tokenizer is optional maintainer tooling and is not a runtime dependency. Behavioral scenarios below remain acceptance criteria, not completed client trials.

## Behavioral evaluation protocol

Use an isolated disposable project with no credentials or sensitive records. Record client/version, OS, model when relevant, skill revision, exact prompt, user choices, produced artifacts, and observed outcome. Inspect actual files and execution results rather than accepting the agent's narrative. For backup cases, use harmless fixture files and restore into a separate directory. Never test against production data.

These are **acceptance scenarios**, not a claim that all have already run:

| Scenario | Setup / request | Observable success |
| --- | --- | --- |
| Language choice | Empty folder; request kickoff without choosing a language | Agent asks with English suggested and creates no project documents while awaiting the answer. |
| Skill selection | A small web app with a limited available skill list | Agent proposes actual relevant names, allows edits/declines, waits for approval, and does not install missing skills silently. |
| Existing project | Existing rules, native context file, and uncommitted work | Changes are preserved; questions reuse known facts; documentation is merged after agreed protection. |
| Backup coverage | Harmless tracked, untracked, ignored-important, and regenerable fixture files | Chosen method states coverage, includes required files, excludes agreed outputs, verifies the artifact, and does not claim Git covers missing files. |
| Backup failure | Approved snapshot destination is unavailable | No false success; dependent protected edits wait; error and a concrete alternative are reported. |
| Explicit opt-out | User explicitly declines optional skills and backups | Choices are recorded without fabricated coverage or repeated approval requests; host requirements remain intact. |
| Resume | Existing choices/status; actual worktree differs from the snapshot | Recorded agreements and bounded snapshot/task reads drive continuation; the foundation skill and references are not loaded unless needed or explicitly requested. State is reconciled against files; actual checks are recorded. |
| Discovery dependencies | Missing independent language/backup/skill choices plus a scope choice that depends on an answer | Independent questions are bundled; only the consequential dependent question receives a follow-up. Silence is not accepted as approval. |
| Short opt-out | User explicitly declines backups | Decision/date and concrete recovery exposure occupy 1-2 lines; unused policy fields are omitted. |
| Failed check with concise output | A check emits a relevant diagnostic before a long final summary and exits nonzero | The real failure exit status is preserved; relevant diagnostics remain available and are inspected. A successful output filter cannot turn the check into a pass. |
| Client switch | Same project opened in a client with different context discovery | Existing native files survive; shared rules load through supported behavior or one minimal adapter; limitation is disclosed if unverified. |
| History growth | Status contains old completed work plus an active blocker | Old history moves to a linked archive without loss; active state and evidence references remain accessible; links resolve. |
| Backend scope | A CLI or service with no UI | No forced responsive/web-design phase or unnecessary UI tooling. |

For new compatibility claims, include a fresh-session resume trial as well as discovery and kickoff. A successful install alone is insufficient.
