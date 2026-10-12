#!/usr/bin/env python3
"""Flag risky patterns in a local git diff. Prints leads. Does not send data anywhere."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

RULES = [
    ("secret-private-key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("secret-aws-access-key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("secret-assignment", re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[:=]\s*['\"][^'\"]{8,}")),
    ("sql-format", re.compile(r"(?i)(execute|query)\s*\(.*f['\"]|%s.+(SELECT|INSERT|UPDATE|DELETE)")),
    ("html-sink", re.compile(r"(?i)dangerouslySetInnerHTML|innerHTML\s*=")),
    ("shell-true", re.compile(r"shell\s*=\s*True")),
    ("yaml-load", re.compile(r"yaml\.load\s*\(")),
]


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a git diff for risky patterns.")
    parser.add_argument("--repo", default=".", help="Checkout to scan")
    parser.add_argument("diff_args", nargs="*", help="git diff args, default HEAD")
    args = parser.parse_args()
    repo = Path(args.repo)
    diff_args = args.diff_args or ["HEAD"]
    result = subprocess.run(
        ["git", "diff", "--unified=0", *diff_args],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stderr.strip() or "git diff failed\n")
        return result.returncode or 1
    current = ""
    hits = 0
    for line in result.stdout.splitlines():
        if line.startswith("+++ b/"):
            current = line[6:]
            continue
        if not line.startswith("+") or line.startswith("+++"):
            continue
        added = line[1:]
        for rule, pattern in RULES:
            if pattern.search(added):
                hits += 1
                print(f"{rule}\t{current}\t{added.strip()[:180]}")
    if hits == 0:
        print("no leads")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
