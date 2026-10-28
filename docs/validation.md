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

No all-client runtime certification, measured token-saving percentage, actual project backup, or security/accessibility audit is claimed. Vendor-documented integration routes are recorded separately in [compatibility](compatibility.md).

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
| Resume | Existing choices/status; actual worktree differs from the snapshot | No repeated onboarding; state is reconciled against files; next authorized task continues and status records actual checks. |
| Client switch | Same project opened in a client with different context discovery | Existing native files survive; shared rules load through supported behavior or one minimal adapter; limitation is disclosed if unverified. |
| History growth | Status contains old completed work plus an active blocker | Old history moves to a linked archive without loss; active state and evidence references remain accessible; links resolve. |
| Backend scope | A CLI or service with no UI | No forced responsive/web-design phase or unnecessary UI tooling. |

For new compatibility claims, include a fresh-session resume trial as well as discovery and kickoff. A successful install alone is insufficient.
