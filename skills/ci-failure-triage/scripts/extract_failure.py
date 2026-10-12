#!/usr/bin/env python3
"""Print the most useful failure tail from a CI log. Local file only."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MARKERS = re.compile(
    r"(error|failed|failure|traceback|assertion|npm err!|pytest|##\[error\])",
    re.IGNORECASE,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract a failure tail from a log file.")
    parser.add_argument("log", type=Path)
    parser.add_argument("--lines", type=int, default=40)
    args = parser.parse_args()
    if not args.log.is_file():
        sys.stderr.write(f"Log not found: {args.log}\n")
        return 2
    rows = args.log.read_text(encoding="utf-8", errors="replace").splitlines()
    indexes = [i for i, row in enumerate(rows) if MARKERS.search(row)]
    if not indexes:
        print("\n".join(rows[-args.lines :]))
        return 0
    start = max(0, indexes[0] - 2)
    end = min(len(rows), max(indexes[-1] + 3, start + args.lines))
    if end - start > args.lines * 3:
        start = max(0, indexes[-1] - args.lines)
        end = min(len(rows), indexes[-1] + 3)
    print(f"lines {start + 1}-{end} of {len(rows)}")
    print("\n".join(rows[start:end]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
