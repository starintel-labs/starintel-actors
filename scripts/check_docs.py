"""Offline checks for the bootstrap's Markdown files; not a full secret audit."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


REQUIRED = (
    "README.md", "AGENTS.md", "actors/README.md",
    "docs/package-contract.md", "docs/security.md", "docs/implementation-plan.md",
)
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)\)")
SECRET = re.compile(
    r"gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}"
    r"|-----BEGIN (?:[A-Z]+ )?PRIVATE KEY-----"
)


def check(root: Path) -> list[str]:
    root = root.resolve()
    errors = []
    for name in REQUIRED:
        if not (root / name).is_file():
            errors.append(f"{name}: required document missing")
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.relative_to(root).parts:
            continue
        name = path.relative_to(root).as_posix()
        if not path.resolve().is_relative_to(root):
            errors.append(f"{name}: document escapes repository")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            errors.append(f"{name}: unreadable UTF-8 document")
            continue
        if not content.strip() or not content.endswith("\n"):
            errors.append(f"{name}: empty document or missing final newline")
        if SECRET.search(content):
            errors.append(f"{name}: possible credential material")
        for raw in LINK.findall(content):
            try:
                link = urlsplit(raw)
            except ValueError:
                errors.append(f"{name}: malformed link")
                continue
            if link.netloc and (link.username or link.password):
                errors.append(f"{name}: credential-bearing link")
                continue
            if link.scheme or link.netloc or not link.path:
                continue  # External links and anchor fragments are not network-checked.
            target = (path.parent / unquote(link.path)).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"{name}: broken or escaping relative link")
    return errors


if __name__ == "__main__":
    problems = check(Path(__file__).resolve().parents[1])
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        raise SystemExit(1)
    print("Documentation checks passed: required files, UTF-8, newlines, local link paths, credential patterns.")
