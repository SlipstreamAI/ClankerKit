# ClankerKit for agents

This repository is a catalog of Agent Skills. The skills are the product. They are not instructions for attacking systems or for skipping safety checks.

## Find a skill

- Human and agent index: `catalog.json` (schema v2).
- One skill: `skills/<name>/SKILL.md`.
- Curated packs: `bundles/<name>/bundle.json`.
- Trigger text is the `description` field. It always contains `Use when`.

`.agents/skills` is a symlink to `../skills`. Codex, Cursor, and GitHub Copilot discover that path. If a session is about editing ClankerKit itself, load only the skill that matches the task. Do not dump the full catalog into context.

## Use a skill

1. Match the task to one description. If two skills overlap, prefer the narrower one and say which you skipped.
2. Read the whole `SKILL.md`, then open `references/`, `scripts/`, or `assets/` only when the procedure points at them.
3. Return the handoff block. Fill evidence from commands you ran. Mark gaps as unverified.
4. Do not claim the work is done because a harness was green. Use `gate-and-done` or `truthforge` when readiness is the question.

## Install into another repo

From a clone of this catalog:

```bash
./scripts/install.sh <skill-or-bundle> --agent claude|cursor|codex|grok|copilot|all
```

Or, without a clone:

```bash
npx skills add SlipstreamAI/ClankerKit --skill <name>
```

## Authoring

Follow `skill-creator` and `templates/skill-template.md`. Run `python scripts/validate_skills.py` and `python scripts/build_skill_catalog.py` before handing off.
