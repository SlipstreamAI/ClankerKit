---
name: skill-creator
description: "Authors a new ClankerKit skill that follows the Agent Skills spec and the local evidence contract. Use when creating or reshaping a SKILL.md, including its frontmatter trigger, metadata, and handoff."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: documentation
  status: experimental
  tags: "skills, authoring, spec"
  modes: "contribution, meta"
  version: "0.1.0"
  author: SlipstreamAI
---

# Skill Creator

**Tagline:** Author one spec-compliant skill with a real handoff.

## Purpose

Skill Creator produces one skill directory that an agent can trigger and a reviewer can check. The description says what the skill does and when to use it. The body ends in a handoff a later session can audit.

## Use when

1. You are adding a skill to ClankerKit or to a consuming repo.
2. An existing skill's description does not say when to trigger it.
3. A contribution needs to pass scripts/validate_skills.py.

## Do not use when

- Writing a general agent persona or a huge multi-purpose prompt.
- Installing unreviewed third-party skills. Use skill-security-scan first.

## Inputs

- The single job the skill performs.
- The situations that should trigger it, and the situations that should not.
- The evidence the skill must demand.

## Outputs

- skills/<name>/SKILL.md with spec frontmatter.
- Optional references, assets, or scripts.
- Validator result.

Copy [the template](assets/SKILL.template.md) and follow [frontmatter rules](references/frontmatter.md).

## Procedure

### Phase Bound the job

1. One skill, one operating problem. If you need two handoffs, you need two skills.
2. Name it with lowercase letters, numbers, and single hyphens. The folder name matches `name`.
3. Write the trigger as concrete situations, not topics.

### Phase Write frontmatter

1. description is one block under 1024 characters and contains the words Use when.
2. Put category, status, tags, modes, version, and author under metadata as strings.
3. allowed-tools is a space-separated string, not a YAML list.
4. Set status to experimental until the skill has been used on a real repo.

### Phase Write the body

1. Include purpose, use when, do not use when, inputs, outputs, procedure phases, proof, failure patterns, adaptation, an example, and a text handoff.
2. Keep SKILL.md under 500 lines. Move long checklists to references/.
3. Add a script only when it gathers evidence more reliably than prose.

### Phase Validate

1. Run `python scripts/validate_skills.py` from the ClankerKit repo.
2. Run `python scripts/build_skill_catalog.py` so the catalog and README table stay current.
3. Read the description as if you had not seen the body, and confirm it would trigger on the example.

## Proof requirements

- Validator output is in the handoff.
- The description contains a Use when clause a stranger can match.
- The handoff block is a text fence with deterministic fields.

## Common failure patterns

- A description that only says what the skill is about.
- Top-level custom keys that the Agent Skills spec does not define.
- A skill that claims proof without telling the agent what artifact to collect.

## Adaptation notes

- Consuming repos may omit ClankerKit metadata, but name, description, and the handoff still apply.
- If the skill needs a script, keep the script local and free of network side effects unless the skill's job is explicitly a networked check.

## Example invocation

```text
Use skill-creator.

Job: check that a changelog entry exists for user-visible PRs.
Trigger: preparing a release.
Do not trigger: internal refactors with no release.

Return the new skill path and the validator result.
```

## Handoff format

```text
Skill Creator Report

Status: success | partial | blocked | failed
Skill path:
Trigger sentence:
Out of scope:
Validator:
Catalog regenerated:
Open questions:
```
