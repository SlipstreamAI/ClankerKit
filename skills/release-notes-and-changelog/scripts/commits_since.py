#!/usr/bin/env python3
"""Print commit subjects since a ref. Local git only."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="List commit subjects since a ref.")
    parser.add_argument("ref")
    parser.add_argument("--repo", default=".")
    args = parser.parse_args()
    repo = Path(args.repo)
    result = subprocess.run(
        ["git", "log", "--pretty=format:%h%x09%s", f"{args.ref}..HEAD"],
        cwd=repo,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        sys.stderr.write(result.stderr.strip() or "git log failed\n")
        return result.returncode or 1
    print(result.stdout.strip() or "(no commits)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
