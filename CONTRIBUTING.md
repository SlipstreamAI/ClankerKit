# Contributing to ClankerKit

ClankerKit is a public skill catalog. Quality and safety gates are strict on purpose.

## Contribution principles

- Keep skills repo-agnostic unless the skill is about this catalog.
- One skill, one operating problem, one handoff.
- The description states what the skill does and when to use it.
- Proof is an artifact, a command, or an explicit gap. It is not a tone of confidence.
- Status starts at `experimental`. Promote it only after real use.

## What can be contributed

- Skills at `skills/<skill-name>/SKILL.md`
- Checks, patterns, examples, and docs
- Bundle definitions in `bundles/<name>/bundle.json`

Category lives in frontmatter `metadata`, not in the path.

## Required skill shape

Use [`templates/skill-template.md`](templates/skill-template.md) and the `skill-creator` skill.

Frontmatter, top level only:

- `name` matches the directory and `^[a-z0-9]+(-[a-z0-9]+)*$`
- `description` is at most 1024 characters and contains `Use when`
- `license`, `compatibility`
- `allowed-tools` as a space-separated string
- `metadata` string map with `category`, `status`, `tags`, `modes`, `version`, `author`

Body sections:

- Purpose, Use when, Do not use when
- Inputs, Outputs
- Procedure with at least one `### Phase` heading
- Proof requirements
- Common failure patterns
- Adaptation notes
- Example invocation
- Handoff format, including a `text` code block

Keep `SKILL.md` at or under 500 lines. Put long checklists in `references/`. Add a script only when it collects evidence more reliably than prose.

## Status promotion

- `experimental`: new, or not yet used on a real repository.
- `provisional`: used, still expected to change.
- `stable`: the contract held across more than one real use and a maintainer accepts the churn risk.
- `deprecated`: kept so old links resolve. Point at the replacement in the body.

A promotion needs a note in the pull request naming the repositories or incidents that exercised the skill. A green validator run is not that evidence.

## Review

Run `skill-intake-gate` on the contribution, and `skill-security-scan` when the change adds scripts or comes from outside the repo.

Before opening a pull request:

```bash
python scripts/validate_skills.py
python scripts/test_tooling.py
python scripts/build_skill_catalog.py
```

CI checks those commands, Markdown, an offline link pass, a skills CLI install smoke, and the site build.

## Unsafe content

Contributions are rejected when they include:

- instructions to skip authentication or other safety controls
- guidance for moving secrets off the host
- destructive defaults without an explicit guarded context
- a claim of proof that does not name the evidence

## Pull request process

1. Fork and branch from `main`.
2. Keep the change to one theme.
3. Regenerate the catalog so `catalog.json`, the README table, and `.claude-plugin/marketplace.json` match.
4. Fill in the pull request template.
5. Governance and validation skills need CODEOWNERS review.

## Licensing

By contributing, you agree your contributions are licensed under Apache-2.0.
