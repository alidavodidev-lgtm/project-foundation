# Contributing

Small, evidence-backed improvements are welcome. Start with an issue for a significant workflow change; a focused correction can go straight to a pull request.

## What makes a useful contribution

- A real project situation, the observed failure, and the smallest general correction.
- A client compatibility report with version, platform, install route, and kickoff/resume evidence.
- A clear translation or example that preserves the same decisions and authorization boundaries.
- A fix that removes duplicated instructions or unnecessary context loading.

Keep the portable workflow independent of a single vendor's tools. Add client-specific guidance in the appropriate reference or documentation. Avoid turning one project's preference into a universal requirement or adding approvals to routine authorized work.

## Validate locally

Python is needed only for maintainer checks, not to use the skill. From the repository root, use Python 3.12+ in a virtual environment:

```bash
python -m venv .venv
# Activate .venv with the command appropriate for your shell.
python -m pip install -r requirements-dev.txt
python -m skills_ref.cli validate "$PWD"
python scripts/check_package.py
```

Use the activated environment's Python executable. The pinned `skills-ref` package exposes this module entry point (its executable is named `agentskills`). Pass the full current-directory path: version 0.1.1 does not resolve `.` before checking the directory name. `$PWD` works in Bash and PowerShell. On systems where the command is `python3`, substitute it as appropriate. The folder containing SKILL.md should be named `project-foundation`; if a ZIP or fork uses another folder name, rename the extracted folder before validation.

Package checks cover the specification, YAML metadata, bundled references, and local documentation links. They do not prove agent behavior. For changed decision logic, run relevant [behavioral scenarios](docs/validation.md) in a disposable workspace and report what was actually observed. Do not report a manual walkthrough as an end-to-end client test.

## Pull requests

Describe the user-visible problem, resulting behavior, and validation. Update examples and compatibility claims if they change. Keep version metadata and release notes aligned when preparing a release. Do not include API keys, personal paths, private project files, real user data, or raw conversation history in an issue, fixture, or PR.

By contributing, you agree that your contributions may be distributed under the repository's [MIT License](LICENSE). This is not a request to transfer copyright.
