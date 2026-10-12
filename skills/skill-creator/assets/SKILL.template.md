---
name: example-skill
description: "Does one job. Use when the operator is in this situation."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot."
allowed-tools: Bash Read Grep
metadata:
  category: validation
  status: experimental
  tags: "example"
  modes: "pr-audit"
  version: "0.1.0"
  author: SlipstreamAI
---

# Example Skill

**Tagline:** One sentence.

## Purpose

What operating problem this solves.

## Use when

1. Trigger.

## Do not use when

- Neighboring job that has its own skill.

## Inputs

- Required input.

## Outputs

- Deterministic output.

## Procedure

### Phase 1: Frame

1. Restate the claim.

### Phase 2: Decide

1. Record the verdict.

## Proof requirements

- The artifact that must exist.

## Common failure patterns

- A pass narrated without the artifact.

## Adaptation notes

- How to shrink the procedure when a tool is missing.

## Example invocation

```text
Use example-skill on the current diff.
```

## Handoff format

```text
Example Skill Report

Status: success | partial | blocked | failed
Claim:
Evidence:
Verdict:
```
