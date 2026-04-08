---
name: "merge-train-governor"
category: "delivery"
description: "Delivery skill for single-lane merge governance with queue triage, validator gates, review hygiene, and controlled promotion."
status: "provisional"
recommended-modes:
  - pre-merge
  - merge-train
  - release-readiness
allowed-tools:
  - git
  - rg
  - python
  - pytest
  - repo-tools
tags:
  - merge-train
  - governance
  - delivery
  - readiness
---

# Merge Train Governor

**Tagline:** Move fast on one lane, never blind.

## Purpose

Govern merge lanes with explicit queue selection, deterministic gates, and safe promotion rules.

## Use when

1. multiple candidate changes compete for merge priority
2. you need strict pre-merge gate behavior
3. review hygiene and release workflow drift need correction
4. promotion must be explicit and audited

## Do not use when

Do not use for local exploratory branches that are not intended for merge.

## Inputs

- active queue snapshot
- lane policy and merge constraints
- required validator and smoke commands
- review requirements and risk policy
- promotion target and rollback criteria

## Outputs

- selected lane and rationale
- gate pass or fail report
- review hygiene findings
- promotion decision
- blocked reasons with required actions

## Procedure

### Phase 1: queue triage

1. classify candidate items by impact and risk
2. pick one active lane
3. freeze unrelated scope

### Phase 2: gate execution

1. run required validators
2. run runtime-relevant smoke checks
3. fail closed on critical check failure

### Phase 3: review hygiene

1. verify required metadata and ownership
2. verify unresolved review threads and risk acknowledgements
3. reject merge on missing required review evidence

### Phase 4: promotion contract

1. if gates pass, promote with explicit target
2. verify post-promotion health checks
3. define rollback trigger and owner

## Proof requirements

- gate results are attached with command outputs or artifact paths
- readiness claims map to concrete check evidence
- risky surfaces require explicit acceptance or block

## Common failure patterns

1. merging multiple unrelated queue items in one lane
2. auto-merge behavior without full gate evidence
3. release promotion without post-promotion checks
4. review status inferred instead of verified

## Adaptation notes

- github or gitlab: map review and status APIs into same gate contract
- monorepos: require package-level impact map before lane selection
- no preview env: tighten local smoke and staged validation requirements

## Handoff format

```text
Merge Train Governor Report

Queue snapshot:
Selected lane:
Selection rationale:

Gate results:
Review hygiene:
Promotion checks:

Verdict:
- READY
- READY WITH EXPLICIT RISK
- NOT READY

Blockers:
Next required action:
```
