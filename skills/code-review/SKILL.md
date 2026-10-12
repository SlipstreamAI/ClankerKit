---
name: code-review
description: "Reviews a diff and returns severity-ranked findings tied to files and behavior. Use when a human or agent asks for a code review before merge and wants defects, risks, and missing tests rather than a style rewrite."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: governance
  status: experimental
  tags: "review, pull-request, quality"
  modes: "pr-audit, pre-merge"
  version: "0.1.0"
  author: SlipstreamAI
---

# Code Review

**Tagline:** Findings a reviewer can act on, ranked by severity.

## Purpose

Code Review produces findings, not a vague approval. Each finding has a severity, a location, why it matters, and what would resolve it. Nits are separated so they do not bury blockers.

## Use when

1. A pull request needs review comments before merge.
2. You want a second pass focused on correctness, risk, and missing proof.
3. An agent authored the diff and a human needs the sharp edges called out.

## Do not use when

- Security-only review. Use security-review, then bring blockers back here if you also need a general pass.
- Rewriting the change to match personal taste when behavior is correct.

## Inputs

- Diff and the author's claim of what it does.
- Test evidence the author already attached, if any.
- Review focus, if the requester named one.

## Outputs

- Findings grouped as blocker, should-fix, and nit.
- What looks correct, so the author knows what you actually checked.
- Missing proof, if the claim is ahead of the evidence.

## Procedure

### Phase Read the claim, then the diff

1. Restate what the author says changed.
2. Skim the file list for unexpected surfaces before reading line by line.
3. Note tests added or not added.

### Phase Hunt defects

1. Look for wrong conditions, error paths, races, null handling, and API mismatches.
2. Check that new branches have a caller and that removed branches have no caller left.
3. Prefer one specific finding over a general concern.

### Phase Rank and separate

1. Blocker: incorrect behavior, data loss, or a broken contract.
2. Should-fix: likely bug or missing test on the claimed behavior.
3. Nit: naming, comments, or local style. Do not let nits outnumber real findings without saying the behavior looked sound.

### Phase Match the verdict to the findings

1. Request changes if any blocker exists.
2. Approve with comments only when blockers are absent and residual risk is named.
3. Do not approve solely because the suite is green.

## Proof requirements

- Every blocker and should-fix cites a file.
- The claim you reviewed is quoted or paraphrased so the author can correct you.
- Missing tests are a finding when the claim is behavioral and untested.

## Common failure patterns

- Commenting only on formatting.
- A finding with no consequence.
- Approving a behavioral claim you did not find a test or repro for, without saying the proof is missing.

## Adaptation notes

- Large diffs: review by claim, and list files you did not read.
- Generated code: review the generator inputs and the diff of generated outputs separately.

## Example invocation

```text
Use code-review on PR #44.

Author claim: refunds are rejected after settlement.
Focus: the settlement check and its tests.

Return blockers, should-fixes, and nits.
```

## Handoff format

```text
Code Review Report

Status: success | partial | blocked | failed
Claim reviewed:
Files read:
Files not read:
Blockers:
Should-fix:
Nits:
Proof gap:
Recommendation: request-changes | comment | approve-with-risk
```
