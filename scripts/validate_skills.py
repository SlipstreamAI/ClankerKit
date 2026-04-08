#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

REQUIRED_FRONTMATTER_KEYS = {
    "name",
    "category",
    "description",
    "status",
    "recommended-modes",
    "allowed-tools",
    "tags",
}

ALLOWED_STATUS = {"provisional", "stable", "deprecated"}
ALLOWED_CATEGORIES = {
    "debugging",
    "validation",
    "governance",
    "repo-understanding",
    "delivery",
    "hardening",
    "documentation",
}

REQUIRED_SECTIONS = [
    "## Purpose",
    "## Use when",
    "## Do not use when",
    "## Inputs",
    "## Outputs",
    "## Procedure",
    "## Handoff format",
]

RECOMMENDED_SECTION_GROUPS = [
    ("proof section", ["## Proof requirements", "## Required proof standard"]),
    ("failure-pattern section", ["## Common failure patterns"]),
    ("adaptation section", ["## Adaptation notes"]),
]

BANNED_PATTERNS = [
    (re.compile(r"\bcurl\b.*\|\s*(bash|sh)\b", re.IGNORECASE), "pipe-to-shell command"),
    (re.compile(r"\bdisable\s+security\b", re.IGNORECASE), "instruction to disable security"),
    (re.compile(r"\bbypass\s+auth", re.IGNORECASE), "auth bypass guidance"),
    (re.compile(r"\bexfiltrat(e|ion)\b", re.IGNORECASE), "exfiltration guidance"),
    (re.compile(r"\brm\s+-rf\s+/\b", re.IGNORECASE), "unsafe destructive command"),
]


def discover_skills() -> List[Path]:
    return sorted(SKILLS_ROOT.glob("**/SKILL.md"))


def parse_frontmatter(text: str) -> Tuple[Dict[str, object], str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing frontmatter block at file start")
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
                raise ValueError(f"List item without key: {line}")
            item = line.split("- ", 1)[1].strip().strip('"')
            data.setdefault(current_list_key, [])
            assert isinstance(data[current_list_key], list)
            data[current_list_key].append(item)
            continue
        current_list_key = None
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            current_list_key = key
            data[key] = []
        else:
            data[key] = value.strip('"')
    return data, body


def validate_skill(path: Path) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    text = path.read_text(encoding="utf-8")

    try:
        frontmatter, body = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{path}: {exc}"], []

    missing_keys = REQUIRED_FRONTMATTER_KEYS - set(frontmatter.keys())
    if missing_keys:
        errors.append(f"{path}: missing frontmatter keys: {sorted(missing_keys)}")

    category = str(frontmatter.get("category", ""))
    if category and category not in ALLOWED_CATEGORIES:
        errors.append(f"{path}: invalid category '{category}'")

    path_category = path.parts[path.parts.index("skills") + 1]
    if category and path_category != category:
        errors.append(
            f"{path}: category '{category}' does not match directory '{path_category}'"
        )

    status = str(frontmatter.get("status", ""))
    if status and status not in ALLOWED_STATUS:
        errors.append(f"{path}: invalid status '{status}'")

    for list_key in ("recommended-modes", "allowed-tools", "tags"):
        value = frontmatter.get(list_key)
        if not isinstance(value, list) or not value:
            errors.append(f"{path}: '{list_key}' must be a non-empty list")

    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"{path}: missing section '{section}'")

    for label, options in RECOMMENDED_SECTION_GROUPS:
        if not any(opt in body for opt in options):
            warnings.append(f"{path}: missing recommended {label}")

    if "## Procedure" in body and "### Phase" not in body:
        errors.append(f"{path}: procedure must include at least one phase heading")

    handoff_match = re.search(r"## Handoff format[\s\S]+```text", body)
    if not handoff_match:
        errors.append(f"{path}: handoff format must include a text code block")

    for pattern, label in BANNED_PATTERNS:
        if pattern.search(text):
            errors.append(f"{path}: banned pattern detected ({label})")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ClankerKit skill files.")
    parser.parse_args()

    skills = discover_skills()
    if not skills:
        print("No skills found.")
        return 1

    all_errors: List[str] = []
    all_warnings: List[str] = []
    for skill in skills:
        errors, warnings = validate_skill(skill)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

    if all_errors:
        print("Skill validation failed:")
        for err in all_errors:
            print(f"- {err}")
        return 1

    if all_warnings:
        print("Skill validation warnings:")
        for warn in all_warnings:
            print(f"- {warn}")

    print(f"Skill validation passed for {len(skills)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
