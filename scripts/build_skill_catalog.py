#!/usr/bin/env python3
"""Build catalog.json, the README catalog table, the skills index, llms.txt, and the marketplace manifest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_skills import discover_skills, parse_frontmatter, use_when_clause  # noqa: E402

CATALOG_PATH = ROOT / "catalog.json"
README_PATH = ROOT / "README.md"
INDEX_PATH = ROOT / "docs" / "skills-index.md"
LLMS_PATH = ROOT / "llms.txt"
SITE_PUBLIC = ROOT / "site" / "public"
MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"
BUNDLES_ROOT = ROOT / "bundles"
CATALOG_START = "<!-- CATALOG:START -->"
CATALOG_END = "<!-- CATALOG:END -->"

REPO = "SlipstreamAI/ClankerKit"
RAW_BASE = f"https://github.com/{REPO}/blob/main"


def load_bundles() -> List[Dict[str, object]]:
    bundles = []
    if not BUNDLES_ROOT.exists():
        return bundles
    for path in sorted(BUNDLES_ROOT.glob("*/bundle.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        data["path"] = path.relative_to(ROOT).as_posix()
        bundles.append(data)
    return bundles


def skill_record(path: Path) -> Dict[str, object]:
    text = path.read_text(encoding="utf-8")
    frontmatter, _body = parse_frontmatter(text)
    metadata = dict(frontmatter["metadata"])  # type: ignore[arg-type]
    description = str(frontmatter["description"])
    files = sorted(
        item.relative_to(path.parent).as_posix()
        for item in path.parent.rglob("*")
        if item.is_file() and item.name != "SKILL.md"
    )
    return {
        "name": frontmatter["name"],
        "description": description,
        "use_when": use_when_clause(description),
        "license": frontmatter.get("license", ""),
        "compatibility": frontmatter.get("compatibility", ""),
        "allowed_tools": str(frontmatter.get("allowed-tools", "")).split(),
        "metadata": metadata,
        "category": metadata.get("category", ""),
        "status": metadata.get("status", ""),
        "tags": [part.strip() for part in str(metadata.get("tags", "")).split(",") if part.strip()],
        "modes": [part.strip() for part in str(metadata.get("modes", "")).split(",") if part.strip()],
        "path": path.relative_to(ROOT).as_posix(),
        "files": files,
    }


def build_catalog() -> Dict[str, object]:
    skills = [skill_record(path) for path in discover_skills()]
    skills.sort(key=lambda item: (str(item["category"]), str(item["name"])))
    bundles = load_bundles()
    known = {str(item["name"]) for item in skills}
    for bundle in bundles:
        listed = bundle.get("skills", [])
        if listed == "*" or listed == ["*"]:
            bundle["skills"] = sorted(known)
            continue
        missing = [name for name in listed if name not in known]
        if missing:
            raise SystemExit(f"Bundle {bundle.get('name')} references missing skills: {missing}")
    return {
        "schema_version": 2,
        "skill_count": len(skills),
        "repository": REPO,
        "skills": skills,
        "bundles": bundles,
    }


def render_catalog_table(catalog: Dict[str, object]) -> str:
    lines = [
        "| Skill | Category | Status | Use when |",
        "| --- | --- | --- | --- |",
    ]
    for skill in catalog["skills"]:  # type: ignore[index]
        use_when = str(skill["use_when"]).replace("|", "\\|")
        name = skill["name"]
        lines.append(
            f"| [{name}](skills/{name}/SKILL.md) | {skill['category']} | {skill['status']} | {use_when} |"
        )
    return "\n".join(lines)


def render_readme(catalog: Dict[str, object], existing: str) -> str:
    if CATALOG_START not in existing or CATALOG_END not in existing:
        raise SystemExit("README.md is missing CATALOG:START/END markers")
    table = render_catalog_table(catalog)
    before, rest = existing.split(CATALOG_START, 1)
    _old, after = rest.split(CATALOG_END, 1)
    return f"{before}{CATALOG_START}\n{table}\n{CATALOG_END}{after}"


def render_index(catalog: Dict[str, object]) -> str:
    lines = [
        "# ClankerKit Skills Index",
        "",
        "Generated from `skills/*/SKILL.md`. Do not edit by hand.",
        "Run `python scripts/build_skill_catalog.py` after skill changes.",
        "",
    ]
    current = None
    for skill in catalog["skills"]:  # type: ignore[index]
        category = str(skill["category"])
        if category != current:
            current = category
            lines.extend([f"## {category}", ""])
        lines.append(f"- [`{skill['name']}`](../skills/{skill['name']}/SKILL.md) ({skill['status']})")
        lines.append(f"  Use when {skill['use_when']}.")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_llms(catalog: Dict[str, object]) -> str:
    lines = [
        "# ClankerKit",
        "",
        "> Skills for agents that ship real software, with evidence receipts.",
        "",
        "Install one skill with `npx skills add SlipstreamAI/ClankerKit --skill <name>`.",
        "The machine-readable catalog is `catalog.json`.",
        "",
        "## Skills",
        "",
    ]
    for skill in catalog["skills"]:  # type: ignore[index]
        lines.append(
            f"- [{skill['name']}]({RAW_BASE}/skills/{skill['name']}/SKILL.md): {skill['description']}"
        )
    lines.extend(["", "## Bundles", ""])
    for bundle in catalog["bundles"]:  # type: ignore[index]
        joined = ", ".join(bundle["skills"])
        lines.append(f"- {bundle['name']}: {bundle['description']} Skills: {joined}.")
    lines.append("")
    return "\n".join(lines)


def render_marketplace(catalog: Dict[str, object]) -> Dict[str, object]:
    plugins = []
    for bundle in catalog["bundles"]:  # type: ignore[index]
        if bundle.get("name") == "full-catalog":
            skill_paths = ["./skills"]
        else:
            skill_paths = [f"./skills/{name}" for name in bundle["skills"]]
        plugins.append(
            {
                "name": bundle["name"],
                "source": "./",
                "description": bundle["description"],
                "version": bundle.get("version", "1.0.0"),
                "author": {"name": "SlipstreamAI"},
                "skills": skill_paths,
                "category": bundle.get("category", "workflow"),
            }
        )
    return {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": "clankerkit",
        "description": "ClankerKit skills for agents that build, test, secure, and prove real software.",
        "owner": {"name": "SlipstreamAI"},
        "plugins": plugins,
    }


def generated_files(catalog: Dict[str, object], readme_text: str) -> Dict[Path, str]:
    marketplace = json.dumps(render_marketplace(catalog), indent=2) + "\n"
    catalog_text = json.dumps(catalog, indent=2) + "\n"
    llms = render_llms(catalog)
    files = {
        CATALOG_PATH: catalog_text,
        README_PATH: render_readme(catalog, readme_text),
        INDEX_PATH: render_index(catalog),
        LLMS_PATH: llms,
        SITE_PUBLIC / "llms.txt": llms,
        SITE_PUBLIC / "catalog.json": catalog_text,
        MARKETPLACE_PATH: marketplace,
    }
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Build or verify the ClankerKit catalog.")
    parser.add_argument("--check", action="store_true", help="Fail if generated files are stale.")
    args = parser.parse_args()

    catalog = build_catalog()
    readme_text = README_PATH.read_text(encoding="utf-8")
    files = generated_files(catalog, readme_text)

    if args.check:
        stale = []
        for path, content in files.items():
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(path.relative_to(ROOT).as_posix())
        if stale:
            print("Generated files are out of date:")
            for path in stale:
                print(f"- {path}")
            print("Run: python scripts/build_skill_catalog.py")
            return 1
        print(f"Catalog is up to date ({catalog['skill_count']} skills).")
        return 0

    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
