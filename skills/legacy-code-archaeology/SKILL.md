---
name: legacy-code-archaeology
description: "Recovers the intent of legacy code from git history, callers, and tests. Use when you must change old code and the reason it exists is not in the current comments."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: repo-understanding
  status: experimental
  tags: "legacy, git-history, intent"
  modes: "pre-edit, refactor"
  version: "0.1.0"
  author: SlipstreamAI
---

# Legacy Code Archaeology

**Tagline:** Recover why the code exists before you change it.

## Purpose

Legacy Code Archaeology separates original intent from later patches. History is evidence only when the commit or test still explains the behavior. Guessing is labeled guessing.

## Use when

1. You need to change a function nobody on the current team wrote.
2. A weird conditional looks like a bug and might be a fix for an incident.
3. A refactor is unsafe until you know which callers depend on the odd behavior.

## Do not use when

- Greenfield code with a clear spec.
- Blaming an author. The output is intent and risk, not a verdict on a person.

## Inputs

- The symbol, file, or behavior.
- A git history you can read.
- The change you want to make, if you already know it.

## Outputs

- Current behavior, with a caller or test.
- Commits that introduced or altered it, with subjects and dates.
- Intent: supported, or unverified.
- What a change would put at risk.

## Procedure

### Phase Pin the current behavior

1. Find callers and tests for the symbol.
2. State what it does now from the code and a test, not from the oldest commit alone.
3. If there is no test, say the behavior is read from code only.

### Phase Read the history

1. Use `git log -S` or `git log -L` for the symbol, and `git blame` for the specific lines.
2. Open the commits that introduced the odd branch.
3. Extract the message, the linked issue if present, and the behavior change in that diff.

### Phase Separate intent from accretion

1. Original intent: why the first version existed, if the commit supports it.
2. Later patches: incident fixes, compatibility, or dead ends.
3. If two commits disagree, show both. Do not pick a story because it is tidy.

### Phase Advise the change

1. List callers that still need the odd behavior.
2. Recommend a characterization test before a delete.
3. Mark anything the history does not prove as unverified.

## Proof requirements

- Commit ids are in the handoff for historical claims.
- Current behavior cites a file or test.
- Unverified intent is not written as fact.

## Common failure patterns

- A blame line used as a personality critique.
- Deleting a branch because it looks ugly, with no caller check.
- Treating a commit subject as proof when the diff does something else.

## Adaptation notes

- Shallow clones: say the history is incomplete and avoid strong intent claims.
- Generated code: find the generator input. The generated blame is the wrong layer.

## Example invocation

```text
Use legacy-code-archaeology on Billing.prorate.

Question: why does a zero-day period return the full amount?
Planned change: return zero.

Return behavior, commits, and caller risk.
```

## Handoff format

```text
Legacy Code Archaeology Report

Status: success | partial | blocked | failed
Symbol:
Current behavior:
Evidence:
Commits:
Intent:
Later patches:
Caller risk:
Unverified:
```
