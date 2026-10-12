---
name: gate-and-done
description: "Defines the evidence contract, evaluates explicit merge or release gates, and checks definition-of-done across code, proof, docs, and handoff. Use when a change is called ready and reviewers need one pass or fail contract instead of separate evidence, gate, and done checks."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: governance
  status: provisional
  tags: "governance, gates, evidence, done"
  modes: "evidence-contract, pre-merge, release-readiness"
  version: "1.0.0"
  author: SlipstreamAI
---

# Gate and Done

**Tagline:** One contract for evidence, merge gates, and done criteria.

## Purpose

Gate and Done replaces three overlapping skills (`evidence-contract`, `deterministic-gate`, and `definition-of-done-check`) with one readiness decision. It says what evidence counts, which gates apply to this risk, and whether every done criterion has a receipt.

## Use when

1. Reviewers disagree about what counts as proof for a merge or release.
2. A change is proposed as complete and needs a deterministic ready or not-ready verdict.
3. High-risk work needs a stronger gate than a low-risk refactor.

## Do not use when

- Exploratory branches with no merge or release intent.
- A repo that already runs this same contract and only needs a single failing check re-run.

## Inputs

- Diff, PR, or release candidate.
- Claim type: internal-only, runtime-visible, boundary-sensitive, or security-sensitive.
- Local done criteria, or the default set in this skill if the repo has none.
- Available validation commands and environments.

## Outputs

- Evidence class policy used for this decision.
- Gate table with pass, fail, or unmeasured per gate.
- Done-criteria matrix.
- Verdict: READY, READY WITH EXPLICIT RISK, or NOT READY.

Evidence classes and the blank report live in [evidence classes](references/evidence-classes.md) and [gate report](assets/gate-report.md).

## Procedure

### Phase Define the contract

1. Name the claim types in scope for this change.
2. Assign a minimum evidence class to each claim using the reference. Do not use one bar for every claim.
3. Write the downgrade rule: missing evidence lowers confidence, and security-sensitive claims cannot pass on synthetic evidence alone.

### Phase Set the gates

1. List gates that match the risk: tests for the changed behavior, runtime-relevant proof if the claim is user-visible, docs and handoff if an operator must continue, rollback if the change ships.
2. Make each gate measurable. 'Looks good' is not a gate.
3. Record local policy that raises a threshold. Do not delete a gate to make the change pass.

### Phase Verify done criteria

1. Map every done criterion to a command, artifact, or file.
2. Check implementation, validation, documentation, and handoff separately. A green test run does not cover missing operator notes.
3. Mark each criterion pass, fail, or unmeasured.

### Phase Decide

1. Fail the verdict if any blocking gate fails or a security-sensitive claim has only synthetic evidence.
2. Use READY WITH EXPLICIT RISK only when the residual risk is named, owned, and accepted in the handoff.
3. List the next action that would flip each failure to pass.

## Proof requirements

- Every in-scope claim type has an evidence class and a downgrade rule.
- Every gate result points at an artifact or is explicitly unmeasured.
- The verdict matches the matrix. A failed blocking gate cannot be narrated as ready.

## Common failure patterns

- One proof standard for a copy change and a migration.
- Pass inferred from effort, green CI, or a partial checklist.
- Docs and rollback omitted from done criteria on a production change.

## Adaptation notes

- Product repos: add rollout and rollback gates.
- Libraries: add API compatibility and changelog gates.
- Restricted environments: mark unavailable proof as unmeasured and downgrade, do not invent a result.

## Example invocation

```text
Use gate-and-done on PR #128.

Claim: checkout works for a guest user.
Risk: runtime-visible, boundary-sensitive.
Done criteria: behavior test, failure-path note, changelog line.

Return the gate table and a READY or NOT READY verdict.
```

## Handoff format

```text
Gate and Done Report

Status: success | partial | blocked | failed
Claim types:
Evidence classes:
Gate table:
Done matrix:
Blocking criteria:
Residual risk:
Verdict: READY | READY WITH EXPLICIT RISK | NOT READY
Required next action:
```
