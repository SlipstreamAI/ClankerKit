#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
CATALOG_PATH = SKILLS_ROOT / "catalog.json"


def discover_skills() -> List[Path]:
    return sorted(
        p for p in SKILLS_ROOT.glob("**/SKILL.md") if p.name == "SKILL.md"
    )


def parse_frontmatter(text: str) -> Tuple[Dict[str, object], str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing frontmatter block")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("Unclosed frontmatter block")
    raw = parts[1]
    body = parts[2]
    data: Dict[str, object] = {}
    current_list_key: str | None = None
    for raw_line in raw.splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith("- "):
            if current_list_key is None:
                continue
            item = line.split("- ", 1)[1].strip().strip('"')
            data.setdefault(current_list_key, [])
            assert isinstance(data[current_list_key], list)
            data[current_list_key].append(item)
            continue
        current_list_key = None
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            current_list_key = key
            data[key] = []
        else:
            data[key] = value.strip('"')
    return data, body


def build_catalog() -> Dict[str, object]:
    entries = []
    for path in discover_skills():
        rel = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(text)
        entries.append(
            {
                "name": frontmatter.get("name", ""),
                "category": frontmatter.get("category", ""),
                "description": frontmatter.get("description", ""),
                "status": frontmatter.get("status", ""),
                "recommended_modes": frontmatter.get("recommended-modes", []),
                "allowed_tools": frontmatter.get("allowed-tools", []),
                "tags": frontmatter.get("tags", []),
                "path": rel,
            }
        )
    entries = sorted(entries, key=lambda x: (x["category"], x["name"]))
    return {
        "schema_version": 1,
        "skill_count": len(entries),
        "skills": entries,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or verify skills catalog.")
    parser.add_argument("--check", action="store_true", help="Fail if catalog is out of date.")
    args = parser.parse_args()

    catalog = build_catalog()
    rendered = json.dumps(catalog, indent=2, sort_keys=False) + "\n"

    if args.check:
        if not CATALOG_PATH.exists():
            print(f"Catalog missing: {CATALOG_PATH}")
            return 1
        existing_text = CATALOG_PATH.read_text(encoding="utf-8")
        try:
            existing_obj = json.loads(existing_text)
        except json.JSONDecodeError:
            print("Catalog file is not valid JSON.")
            return 1
        if existing_obj != catalog:
            print("Catalog is out of date. Run: python scripts/build_skill_catalog.py")
            return 1
        print("Catalog is up to date.")
        return 0

    CATALOG_PATH.write_text(rendered, encoding="utf-8")
    print(f"Wrote catalog: {CATALOG_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
