---
name: "<skill-name>"
category: "<debugging|validation|governance|repo-understanding|delivery|hardening|documentation>"
description: "<one sentence: what this skill does and why>"
status: "provisional"
recommended-modes:
  - pr-audit
allowed-tools:
  - git
  - rg
  - python
tags:
  - "<tag-1>"
---

# <Skill Title>

**Tagline:** <single sentence with operator value>

## Purpose

State the operating problem this skill solves and the boundary of responsibility.

## Use when

Invoke this skill when:

1. <trigger condition 1>
2. <trigger condition 2>
3. <trigger condition 3>

## Do not use when

State when this skill is overkill or outside scope.

## Inputs

List required and optional inputs. Be explicit about missing-input behavior.

- diff, PR, or commit range
- stated claim or task objective
- runtime constraints and available environments
- logs, traces, or test artifacts

## Outputs

Define deterministic output contract. Avoid vague summaries.

- claim interpretation
- changed surfaces
- evidence inventory and class
- open assumptions
- verdict and remediation

## Procedure

### Phase 1: Frame

- restate claim
- identify risk surfaces
- define proof standard

### Phase 2: Gather

- collect evidence
- classify each artifact
- mark synthetic versus runtime-relevant evidence

### Phase 3: Challenge

- probe masking and blind spots
- test or verify critical assumptions
- attempt runtime-relevant proof where feasible

### Phase 4: Decide

- classify outcome
- list remediation
- declare merge or release readiness

## Proof requirements

Define minimum proof requirements by claim type.

- internal-only claim: targeted integration evidence may be sufficient
- runtime-visible claim: include at least one runtime-relevant path
- boundary-sensitive claim: include at least one failure-mode proof

## Common failure patterns

- synthetic harness success mistaken for runtime readiness
- unverified environment assumptions
- missing failure-mode coverage
- assertions that validate shape but not behavior

## Adaptation notes

Explain how to adapt for frontend, backend, monorepo, or restricted environments.

## Example invocation

```text
Use <skill-name> on PR #321.

Functional claim:
"..."

Focus on:
- ...

Return:
- ...
```

## Handoff format

```text
<Skill Title> Report

Functional claim:
Changed surfaces:
Evidence inventory:
Synthetic masking detected:
Strongest real-path proof:
Failure-mode proof:
Unverified assumptions:
Classification:
Remediation now:
Still open:
Tracked follow-up:
Readiness verdict:
```
