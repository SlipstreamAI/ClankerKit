---
name: refactor-safely
description: "Refactors code while pinning current behavior with characterization tests. Use when renaming, splitting, or moving code and the behavior must stay the same."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: delivery
  status: experimental
  tags: "refactor, characterization, safety"
  modes: "refactor, pre-merge"
  version: "0.1.0"
  author: SlipstreamAI
---

# Refactor Safely

**Tagline:** Move structure without changing behavior.

## Purpose

Refactor Safely separates structure changes from behavior changes. If behavior must change, that is a different task. This skill starts by recording what the code does now.

## Use when

1. You plan to rename, extract, split a module, or untangle a function without a product change.
2. The code is untested and a move would hide a behavior change.
3. A review needs confidence the diff is a move, not a rewrite.

## Do not use when

- Feature work disguised as cleanup.
- Formatting-only edits that the formatter already owns.

## Inputs

- The structure change you intend.
- The behavior that must stay put, as observables.
- Test command.

## Outputs

- Characterization tests or an explicit gap if they cannot be added.
- The mechanical steps taken.
- Any behavior delta you noticed, which stops the refactor claim.

## Procedure

### Phase Pin behavior

1. List observables: return values, persisted rows, emitted events, status codes.
2. Add or identify tests that pass on the current code and would fail if those observables changed.
3. Run them and record the pass before moving code.

### Phase Change structure in small steps

1. Prefer rename, then extract, then rewire. Commit-sized steps if the repo allows.
2. Do not change conditionals, defaults, or error messages in the same step.
3. Re-run the characterization tests after each step.

### Phase Inspect the diff

1. The diff should read as moves and signature plumbing.
2. If a conditional changed, stop calling the change a refactor and split it out.
3. Search for old names that should have moved.

### Phase Report the boundary

1. State the behavior you pinned and the structure you changed.
2. Name anything you did not characterize.

## Proof requirements

- A test command passed before and after the move, or the gap is explicit.
- The handoff lists any intentional behavior change as out of scope rather than hiding it.

## Common failure patterns

- Cleanup that also fixes a bug with no test.
- A green suite that never covered the moved behavior.
- Deleting tests to finish the move.

## Adaptation notes

- Untested legacy code: a characterization test at the outermost boundary is enough to start.
- Generated files: regenerate and diff, do not hand-edit the output and call it a refactor.

## Example invocation

```text
Use refactor-safely.

Goal: split BillingCalculator into tax and total modules.
Observable: invoice totals for the fixture carts stay identical.

Return the characterization command and any behavior delta.
```

## Handoff format

```text
Refactor Safely Report

Status: success | partial | blocked | failed
Structure change:
Observables pinned:
Characterization command:
Before:
After:
Behavior delta:
Not characterized:
```
