#!/usr/bin/env python3
"""Find tracked files that look like secrets or live env files. Prints paths and rules only."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

NAME_RULES = [
    ("env-file", re.compile(r"(^|/)\.env($|\.)")),
    ("private-key-name", re.compile(r"\.(pem|p12|pfx|key)$", re.I)),
]
CONTENT_RULES = [
    ("private-key-block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("aws-access-key-id", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("assigned-secret", re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{8,}")),
]
SKIP_PARTS = {"node_modules", ".git", "dist", "build", "coverage"}


def tracked(repo: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stderr.strip() or "git ls-files failed\n")
        sys.exit(result.returncode or 1)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan tracked files for secret-shaped content.")
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo)
    hits = 0
    for rel in tracked(repo):
        if any(part in SKIP_PARTS for part in Path(rel).parts):
            continue
        for rule, pattern in NAME_RULES:
            if pattern.search(rel):
                # Example env files are allowed to exist; still report them for review.
                print(f"{rule}\t{rel}")
                hits += 1
        path = repo / rel
        if not path.is_file() or path.stat().st_size > 1_000_000:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for rule, pattern in CONTENT_RULES:
            if pattern.search(text):
                print(f"{rule}\t{rel}")
                hits += 1
                break
    if hits == 0:
        print("no hits")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
