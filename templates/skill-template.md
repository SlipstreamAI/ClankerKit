---
name: example-skill
description: "Does one job and records the receipt. Use when the operator is in this specific situation."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
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

**Tagline:** One sentence an operator can repeat.

## Purpose

State the operating problem and the boundary. Name the neighboring skill you will not absorb.

## Use when

1. Trigger that a stranger can match from the description alone.
2. A second concrete trigger.

## Do not use when

- The neighboring job that has its own skill.

## Inputs

- Diff, claim, or artifact the procedure requires.
- What to do when an input is missing: partial, blocked, or a named default.

## Outputs

- The fields the handoff must contain.
- Status: success, partial, blocked, or failed.

## Procedure

### Phase 1: Frame

1. Restate the claim.
2. Name the proof that would change your mind.

### Phase 2: Gather

1. Collect artifacts.
2. Mark each one synthetic or runtime-relevant.

### Phase 3: Decide

1. Match the verdict to the artifacts.
2. List the next action for every gap.

## Proof requirements

- The command, file, or observation that must exist.
- What is explicitly unmeasured.

## Common failure patterns

- A green harness treated as runtime proof.
- A verdict that disagrees with the matrix.

## Adaptation notes

- How to shrink the procedure when a tool or environment is missing.

## Example invocation

```text
Use example-skill on the current diff.

Claim:
"..."

Return the handoff with commands and results.
```

## Handoff format

```text
Example Skill Report

Status: success | partial | blocked | failed
Claim:
Evidence:
Unverified assumptions:
Verdict:
Next action:
```
