#!/usr/bin/env python3
"""Statically scan a skill directory. Does not execute the skill."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Split so this file does not contain a pipe-to-shell one-liner.
NET = re.compile(r"https?://", re.I)
B64 = re.compile(r"base64\.(b64decode|decodebytes)")
EVAL = re.compile(r"\beval\s*\(|exec\s*\(")
PIPE = re.compile(r"\|\s*(ba)?sh\b", re.I)
FETCH = re.compile(r"\bcurl\b|\bwget\b|Invoke-WebRequest", re.I)


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a skill directory without running it.")
    parser.add_argument("skill_dir", type=Path)
    args = parser.parse_args()
    root = args.skill_dir
    if not root.is_dir():
        sys.stderr.write(f"Not a directory: {root}\n")
        return 2
    files = [path for path in root.rglob("*") if path.is_file()]
    if not files:
        print("no files")
        return 0
    for path in files:
        rel = path.relative_to(root)
        text = path.read_text(encoding="utf-8", errors="replace")
        rules = []
        if NET.search(text):
            rules.append("network-url")
        if B64.search(text):
            rules.append("encoded-payload")
        if EVAL.search(text):
            rules.append("dynamic-exec")
        if FETCH.search(text):
            rules.append("downloader")
        if PIPE.search(text):
            rules.append("piped-shell")
        if "ignore previous instructions" in text.lower():
            rules.append("instruction-override")
        if rules:
            print(f"{rel}\t{','.join(rules)}")
    print(f"files {len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
