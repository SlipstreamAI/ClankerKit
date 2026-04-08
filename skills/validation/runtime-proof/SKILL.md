---
name: "runtime-proof"
category: "validation"
description: "Validation skill for testing whether a runtime-visible claim is proven by runtime-relevant evidence instead of synthetic harness success."
status: "provisional"
recommended-modes:
  - pr-audit
  - incident
  - pre-merge
allowed-tools:
  - bash
  - git
  - rg
  - python
  - pytest
  - playwright
  - browser
tags:
  - validation
  - runtime-proof
  - claim-verification
  - evidence-quality
---

# RuntimeProof

**Tagline:** A validation skill that separates behavior proof from harness comfort.

## Purpose

RuntimeProof evaluates whether a functional claim is proven in a way that survives outside synthetic test harnesses.

It focuses on evidence quality, path realism, and assumption integrity.

## Use when

Invoke RuntimeProof when:

1. A PR claims a runtime-visible outcome.
2. Tests are green but confidence feels shallow.
3. A fix touches boundaries like routes, auth, subprocesses, filesystem, or config.
4. You need a deterministic claim-versus-proof verdict before merge.

## Do not use when

Do not invoke RuntimeProof for trivial pure-logic edits with no external collaborators unless there is suspicion of misleading evidence.

## Inputs

- stated functional claim
- diff, PR, or commit range
- test results and CI output
- runtime logs, traces, or console output if available
- known environment assumptions
- available environments and tool constraints

If key inputs are missing, RuntimeProof must list what is missing and lower confidence.

## Outputs

RuntimeProof must return:

- claim statement in testable language
- changed surfaces and risk boundaries
- evidence inventory with classes
- proof strength summary
- unverified assumptions
- validation verdict
- required remediation

## Evidence classes

- `unit_synthetic`
- `integration_real_path`
- `runtime_smoke`
- `resilience_failure_mode`
- `deploy_or_runtime_observation`

## Procedure

### Phase 1: Define claim and boundaries

1. Rewrite the claim as a falsifiable runtime statement.
2. List changed surfaces and classify risk.
3. Define minimum evidence required for this claim type.

### Phase 2: Inventory evidence

1. Gather tests, smokes, logs, and observations.
2. Classify each item by evidence class.
3. Mark each item as direct, indirect, or synthetic support.

### Phase 3: Challenge proof quality

1. Identify where critical dependencies were mocked or bypassed.
2. Check whether strongest evidence exercised real collaborators.
3. Validate at least one failure mode for risky claims when feasible.

### Phase 4: Validate assumptions

Check assumptions that commonly break runtime:

- environment variables
- binary availability
- filesystem paths
- auth context
- service connectivity
- startup parity between local and deployment paths

Record unverified assumptions explicitly.

### Phase 5: Return verdict

Classify result:

- `PROVEN`
- `PARTIAL`
- `WEAK_PROOF_RISK`
- `RUNTIME_FAILURE_RISK`

If below `PROVEN`, provide exact remediation required to raise confidence.

## Common failure patterns

1. Route tests replace full service path and claim end-to-end confidence.
2. Assertions verify response shape, not underlying behavior.
3. High-risk dependencies are mocked in every test path.
4. Failure-mode tests are absent for env, IO, auth, or connectivity misses.
5. Confidence language overstates what evidence actually proves.

## Adaptation notes

- frontend-only repos: runtime proof may be browser-level evidence with real network responses
- backend repos: runtime proof should include real route or CLI execution through core collaborators
- monorepos: validate cross-package boundaries touched by the change
- restricted environments: downgrade confidence and list missing proof artifacts

## Handoff format

```text
RuntimeProof Report

Functional claim:
Changed surfaces:
Evidence inventory:
- unit_synthetic:
- integration_real_path:
- runtime_smoke:
- resilience_failure_mode:
- deploy_or_runtime_observation:

Proof strength summary:
Synthetic masking detected:
Failure-mode coverage:
Unverified assumptions:

Classification:
- PROVEN | PARTIAL | WEAK_PROOF_RISK | RUNTIME_FAILURE_RISK

Required remediation:
Readiness verdict:
- READY
- READY WITH EXPLICIT RISK
- NOT READY
```
