"""Read-only maintainer checks; not required to use the skill."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from skills_ref import validate


def prose_lines(text: str):
    """Skip fenced examples, whose links may describe generated project files."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s*(`{3,}|~{3,})(.*)$", line)
        if marker:
            run, suffix = marker.groups()
            if fence is None:
                fence = (run[0], len(run))
            elif run[0] == fence[0] and len(run) >= fence[1] and not suffix.strip():
                fence = None
            continue
        if fence is None:
            yield number, line


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors = list(validate(root))
    skill = root / "SKILL.md"
    if not skill.is_file():
        return errors

    text = skill.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    try:
        frontmatter = yaml.safe_load(parts[1]) if len(parts) == 3 else None
    except yaml.YAMLError as exc:
        return errors + [f"Invalid frontmatter YAML: {exc}"]
    if not isinstance(frontmatter, dict):
        return errors + ["Frontmatter must be a mapping"]
    metadata = frontmatter.get("metadata", {})
    if not isinstance(metadata, dict) or not all(
        isinstance(key, str) and isinstance(value, str)
        for key, value in metadata.items()
    ):
        errors.append("metadata must map string keys to string values")
    if frontmatter.get("license") == "MIT" and not (root / "LICENSE").is_file():
        errors.append("MIT license declared without bundled LICENSE")
    if len(text.splitlines()) >= 500:
        errors.append("Keep the entry point below the recommended 500 lines")

    # Scan only maintained package trees, not .git, installed dependencies, or builds.
    files = [path for path in root.iterdir() if path.is_file()]
    for directory in ("agents", "assets", "references", "docs", ".github"):
        parent = root / directory
        if parent.is_dir():
            files.extend(path for path in parent.rglob("*") if path.is_file())

    for path in sorted(files):
        if path.suffix not in {".md", ".yaml", ".yml"}:
            continue
        relative = path.relative_to(root)
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeError as exc:
            errors.append(f"{relative}: invalid UTF-8: {exc}")
            continue
        if path.suffix in {".yaml", ".yml"}:
            try:
                parsed = yaml.safe_load(content)
                if not isinstance(parsed, dict):
                    errors.append(f"{relative}: YAML must be a mapping")
            except yaml.YAMLError as exc:
                errors.append(f"{relative}: invalid YAML: {exc}")
            continue

        # Template links resolve in the generated project, not this package.
        if "assets" in relative.parts:
            continue
        for number, line in prose_lines(content):
            for target in re.findall(r"\]\(([^\s)]+)\)", line):
                target = target.strip("<>")
                url = urlsplit(target)
                if url.scheme or url.netloc or not url.path:
                    continue
                resolved = (path.parent / unquote(url.path)).resolve()
                if not resolved.is_relative_to(root):
                    errors.append(f"{relative}:{number}: link escapes package: {target}")
                elif not resolved.exists():
                    errors.append(f"{relative}:{number}: missing target: {target}")

    ui_path = root / "agents" / "openai.yaml"
    if ui_path.is_file():
        try:
            ui = yaml.safe_load(ui_path.read_text(encoding="utf-8"))
            prompt = ui.get("interface", {}).get("default_prompt", "")
            if f"${frontmatter.get('name')}" not in prompt:
                errors.append("Codex default_prompt must mention the skill's native name")
        except (yaml.YAMLError, AttributeError, TypeError):
            errors.append("Codex UI metadata has an invalid interface structure")
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = check(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: Agent Skills specification, metadata, YAML, and local file links.")
    print("Not checked: external URLs, Markdown anchor fragments, or agent behavior.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
