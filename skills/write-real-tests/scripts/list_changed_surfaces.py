#!/usr/bin/env python3
"""List changed files and whether a nearby test file exists."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

TEST_MARKERS = ("test_", "_test.", ".spec.", ".test.", "/test/", "/tests/", "/__tests__/")


def git_output(args: list[str]) -> list[str]:
    result = subprocess.run(["git", *args], text=True, capture_output=True, check=False)
    if result.returncode != 0:
        sys.stderr.write(result.stderr.strip() or "git failed\n")
        sys.exit(result.returncode or 1)
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def looks_like_test(path: str) -> bool:
    lowered = path.lower()
    return any(marker in lowered for marker in TEST_MARKERS)


def nearby_tests(path: str, tracked: list[str]) -> list[str]:
    stem = Path(path).stem.removeprefix("test_").removesuffix(".test").removesuffix(".spec")
    parent = str(Path(path).parent)
    found = []
    for candidate in tracked:
        if not looks_like_test(candidate):
            continue
        if stem and stem in Path(candidate).stem:
            found.append(candidate)
        elif parent and candidate.startswith(parent):
            found.append(candidate)
    return found[:8]


def main() -> int:
    parser = argparse.ArgumentParser(description="List changed source files and nearby tests.")
    parser.add_argument("diff_args", nargs="*", help="Extra git diff args, such as main...HEAD")
    args = parser.parse_args()
    diff_args = args.diff_args or ["HEAD"]
    changed = git_output(["diff", "--name-only", *diff_args])
    tracked = git_output(["ls-files"])
    if not changed:
        print("No changed files.")
        return 0
    for path in changed:
        kind = "test" if looks_like_test(path) else "source"
        print(f"{kind}\t{path}")
        if kind == "source":
            tests = nearby_tests(path, tracked)
            if tests:
                for test in tests:
                    print(f"  nearby\t{test}")
            else:
                print("  nearby\t(none found)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
