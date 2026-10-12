#!/usr/bin/env python3
"""Validate ClankerKit skills against the Agent Skills spec and local rules."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"

ALLOWED_TOP_LEVEL = {
    "name",
    "description",
    "license",
    "compatibility",
    "metadata",
    "allowed-tools",
}
REQUIRED_TOP_LEVEL = ALLOWED_TOP_LEVEL
REQUIRED_METADATA = ("category", "status", "tags", "modes", "version", "author")
ALLOWED_STATUS = {"experimental", "provisional", "stable", "deprecated"}
ALLOWED_CATEGORIES = {
    "debugging",
    "validation",
    "governance",
    "repo-understanding",
    "delivery",
    "hardening",
    "documentation",
}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")

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
    (re.compile(r"\bdisable\s+security\b", re.IGNORECASE), "instruction to weaken controls"),
    (re.compile(r"\bbypass\s+auth", re.IGNORECASE), "authentication-control guidance"),
    (re.compile(r"\bexfiltrat(e|ion)\b", re.IGNORECASE), "outbound secret-transfer guidance"),
    (re.compile(r"\brm\s+-rf\s+/\b", re.IGNORECASE), "unsafe destructive command"),
]

LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        inner = value[1:-1]
        if value[0] == '"':
            inner = inner.replace('\\"', '"').replace("\\n", "\n")
        return inner
    return value


def parse_frontmatter(text: str) -> Tuple[Dict[str, object], str]:
    if not text.startswith("---\n"):
        raise ValueError("Missing frontmatter block at file start")
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        raise ValueError("Unclosed frontmatter block")
    raw, body = parts[1], parts[2]
    data: Dict[str, object] = {}
    lines = raw.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        if line.startswith(" ") or line.startswith("\t") or line.lstrip().startswith("- "):
            raise ValueError(
                f"Top-level lists and indented keys are not allowed ({line.strip()}). "
                "Put custom fields under metadata as strings."
            )
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if key == "metadata":
            if value:
                raise ValueError("metadata must be a nested map of strings")
            meta: Dict[str, str] = {}
            index += 1
            while index < len(lines):
                meta_line = lines[index]
                if not meta_line.strip():
                    index += 1
                    continue
                if not meta_line.startswith("  "):
                    break
                stripped = meta_line.strip()
                if stripped.startswith("- "):
                    raise ValueError("metadata values must be strings, not lists")
                if ":" not in stripped:
                    raise ValueError(f"Invalid metadata line: {stripped}")
                meta_key, meta_value = stripped.split(":", 1)
                meta_key = meta_key.strip()
                meta_value = meta_value.strip()
                if meta_value == "" or meta_value[0] in {">", "|"}:
                    raise ValueError(f"metadata.{meta_key} must be a single-line string")
                meta[meta_key] = unquote(meta_value)
                index += 1
            data["metadata"] = meta
            continue
        if value in {">-", ">", "|", "|-"}:
            index += 1
            block: List[str] = []
            while index < len(lines) and (lines[index].startswith("  ") or lines[index].strip() == ""):
                current = lines[index]
                block.append(current[2:] if current.startswith("  ") else "")
                index += 1
            joined = "\n".join(block).strip()
            if value.startswith(">"):
                joined = re.sub(r"\s+", " ", joined)
            data[key] = joined
            continue
        if value == "":
            raise ValueError(
                f"'{key}' has no scalar value. allowed-tools must be a space-separated string, "
                "and custom fields belong under metadata."
            )
        data[key] = unquote(value)
        index += 1
    return data, body


def discover_skills() -> List[Path]:
    return sorted(SKILLS_ROOT.glob("*/SKILL.md"))


def use_when_clause(description: str) -> str:
    match = re.search(r"\bUse when\b", description)
    if not match:
        return description.strip()
    return description[match.end() :].strip(" .")


def check_banned(path: Path, text: str, errors: List[str]) -> None:
    for pattern, label in BANNED_PATTERNS:
        if pattern.search(text):
            errors.append(f"{path}: banned pattern detected ({label})")


def validate_skill(path: Path) -> Tuple[List[str], List[str]]:
    errors: List[str] = []
    warnings: List[str] = []
    rel = path.relative_to(ROOT)
    if rel.parts[:1] != ("skills",) or len(rel.parts) != 3:
        errors.append(f"{path}: skills must live at skills/<name>/SKILL.md")
        return errors, warnings

    text = path.read_text(encoding="utf-8")
    try:
        frontmatter, body = parse_frontmatter(text)
    except ValueError as exc:
        return [f"{path}: {exc}"], []

    extra = set(frontmatter) - ALLOWED_TOP_LEVEL
    if extra:
        errors.append(
            f"{path}: unsupported frontmatter keys {sorted(extra)}. "
            "Move custom fields under metadata."
        )
    missing = REQUIRED_TOP_LEVEL - set(frontmatter)
    if missing:
        errors.append(f"{path}: missing frontmatter keys: {sorted(missing)}")

    name = str(frontmatter.get("name", ""))
    if not name or len(name) > 64 or not NAME_RE.match(name):
        errors.append(f"{path}: name must match ^[a-z0-9]+(-[a-z0-9]+)*$ and be 1-64 chars")
    if name and path.parent.name != name:
        errors.append(f"{path}: name '{name}' does not match directory '{path.parent.name}'")

    description = str(frontmatter.get("description", ""))
    if not description or len(description) > 1024:
        errors.append(f"{path}: description must be 1-1024 characters")
    elif not re.search(r"\bUse when\b", description):
        errors.append(f"{path}: description must include a 'Use when' trigger")

    compatibility = str(frontmatter.get("compatibility", ""))
    if compatibility and len(compatibility) > 500:
        errors.append(f"{path}: compatibility must be 1-500 characters")

    allowed_tools = frontmatter.get("allowed-tools")
    if not isinstance(allowed_tools, str) or not allowed_tools.strip():
        errors.append(f"{path}: allowed-tools must be a non-empty space-separated string")
    elif allowed_tools != " ".join(allowed_tools.split()):
        errors.append(f"{path}: allowed-tools must be a single space-separated list")

    metadata = frontmatter.get("metadata")
    if not isinstance(metadata, dict):
        errors.append(f"{path}: metadata must be a string map")
    else:
        for key in REQUIRED_METADATA:
            value = metadata.get(key, "")
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{path}: metadata.{key} must be a non-empty string")
        category = str(metadata.get("category", ""))
        if category and category not in ALLOWED_CATEGORIES:
            errors.append(f"{path}: invalid category '{category}'")
        status = str(metadata.get("status", ""))
        if status and status not in ALLOWED_STATUS:
            errors.append(f"{path}: invalid status '{status}'")
        version = str(metadata.get("version", ""))
        if version and not VERSION_RE.match(version):
            errors.append(f"{path}: metadata.version must look like 1.2.3")
        for listish in ("tags", "modes"):
            raw_value = str(metadata.get(listish, ""))
            parts = [part.strip() for part in raw_value.split(",") if part.strip()]
            if raw_value and not parts:
                errors.append(f"{path}: metadata.{listish} must contain at least one value")

    body_lines = body.splitlines()
    if len(body_lines) > 500:
        errors.append(f"{path}: body is {len(body_lines)} lines; keep SKILL.md at or under 500")

    for section in REQUIRED_SECTIONS:
        if section not in body:
            errors.append(f"{path}: missing section '{section}'")

    for label, options in RECOMMENDED_SECTION_GROUPS:
        if not any(option in body for option in options):
            warnings.append(f"{path}: missing recommended {label}")

    if "## Procedure" in body and "### Phase" not in body:
        errors.append(f"{path}: procedure must include at least one phase heading")

    if not re.search(r"## Handoff format[\s\S]+```text", body):
        errors.append(f"{path}: handoff format must include a text code block")

    for match in LINK_RE.finditer(body):
        target = match.group(1).strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path_part = target.split("#", 1)[0].split("?", 1)[0]
        if not path_part:
            continue
        resolved = (path.parent / path_part).resolve()
        if not resolved.exists():
            errors.append(f"{path}: relative link does not resolve: {target}")

    check_banned(path, text, errors)
    for extra in path.parent.rglob("*"):
        if not extra.is_file() or extra == path:
            continue
        if extra.suffix.lower() not in {".md", ".py", ".sh", ".txt", ".json", ".yml", ".yaml"}:
            continue
        check_banned(extra, extra.read_text(encoding="utf-8", errors="replace"), errors)

    return errors, warnings


def validate_repo_scripts() -> List[str]:
    errors: List[str] = []
    scripts = ROOT / "scripts"
    for path in sorted(scripts.rglob("*")):
        if not path.is_file():
            continue
        if path.suffix.lower() not in {".py", ".sh"}:
            continue
        check_banned(path, path.read_text(encoding="utf-8", errors="replace"), errors)
    return errors


def main() -> int:
    skills = discover_skills()
    if not skills:
        print("No skills found.")
        return 1

    names: Dict[str, Path] = {}
    all_errors: List[str] = []
    all_warnings: List[str] = []
    for skill in skills:
        errors, warnings = validate_skill(skill)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
        try:
            frontmatter, _body = parse_frontmatter(skill.read_text(encoding="utf-8"))
        except ValueError:
            continue
        name = str(frontmatter.get("name", ""))
        if name in names:
            all_errors.append(f"{skill}: duplicate skill name '{name}' also at {names[name]}")
        elif name:
            names[name] = skill

    all_errors.extend(validate_repo_scripts())

    nested = [path for path in SKILLS_ROOT.glob("*/*/*") if path.name == "SKILL.md"]
    for path in nested:
        all_errors.append(f"{path}: nested skill path is not allowed; use skills/<name>/SKILL.md")

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
