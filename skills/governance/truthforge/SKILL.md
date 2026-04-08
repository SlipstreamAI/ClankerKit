---
name: "truthforge"
category: "governance"
description: "Governance skill for detecting false-confidence testing, weak runtime proof, and synthetic evidence masquerading as production readiness."
status: "provisional"
recommended-modes:
  - incident
  - pr-audit
  - repo-truth-recovery
  - continuous-governance
allowed-tools:
  - bash
  - git
  - rg
  - python
  - pytest
  - playwright
  - browser
  - repo-tools
tags:
  - governance
  - validation
  - runtime-proof
  - merge-readiness
  - anti-proxy-optimization
---

# TruthForge

**Tagline:** A governance skill that tests whether code proved reality or merely satisfied the harness.

## Purpose

TruthForge is a governance skill for determining whether a change actually proved its functional claim in runtime terms, or merely satisfied a synthetic harness.

It exists to detect and remediate:
- false-confidence testing
- proxy optimization against CI or local harnesses
- synthetic evidence presented as runtime proof
- fragile merges that passed because risky dependencies were mocked, stubbed, monkeypatched, bypassed, or never exercised realistically

TruthForge is not a general coding skill.
It is a truth-enforcement and merge-governance skill.

Its job is to challenge confidence that has not earned the right to exist.

## Use when

Invoke TruthForge when one or more of the following are true:

1. A feature is broken in runtime even though tests or CI are green.
2. A PR claims a runtime-visible outcome but the evidence looks shallow, synthetic, or incomplete.
3. A change touches risky boundaries such as:
   - UI pages or operator surfaces
   - API routes and service boundaries
   - auth or access control
   - subprocesses, binaries, shell calls, or git
   - filesystem assumptions
   - environment or config assumptions
   - containers, startup scripts, or deploy scripts
   - observability, logging, metrics, or control surfaces
   - money movement, state mutation, promotion, execution, or irreversible actions
4. Tests rely heavily on mocks, stubs, monkeypatches, fake payloads, or builder or service replacement.
5. A recent merge needs adversarial review for false-confidence risk.
6. A repo-wide truth-recovery effort is underway after an incident or suspicious merge.

## Do not use when

Do not invoke TruthForge for tiny isolated pure-function changes unless there is reason to suspect the evidence is misleading.

TruthForge should not become a tax on every trivial refactor.

It is for:
- claim validation
- boundary integrity
- merge governance
- production-worthiness review

## Core rule

A change does not get credit for proving reality when it only proved mocks.

Synthetic evidence may support a claim, but it cannot substitute for runtime-relevant proof when the claim is runtime-visible.

## Inputs

TruthForge expects as many of the following inputs as are available:

- current diff, PR, or commit range
- stated functional claim of the change
- failing behavior, incident notes, or bug report
- relevant test results
- CI output
- logs, traces, metrics, or console output
- local runtime access, staging access, or smoke environment details
- environment assumptions
- constraints on available tools or executable commands
- relevant docs, runbooks, or deployment notes

If key inputs are missing, TruthForge must say what is missing and how that weakens the verdict.

## Outputs

TruthForge must produce a structured report containing:

- functional claim
- changed surfaces
- evidence inventory
- evidence classification
- synthetic masking detected
- real-path proof identified
- failure-mode proof identified
- unverified assumptions
- classification
- remediation now
- deferred tracked work
- merge-readiness verdict

## Standard classifications

Every reviewed change, PR, or incident must be classified as one of:

- `SAFE`
  - real-path evidence exists and matches the functional claim
- `PARTIAL`
  - useful evidence exists, but important runtime assumptions remain unproven
- `FALSE_CONFIDENCE_RISK`
  - tests mainly prove mocked, stubbed, monkeypatched, or bypassed behavior
- `BROKEN_IN_RUNTIME_RISK`
  - strong likelihood the feature fails outside the harness or already fails in runtime

## Evidence classes

TruthForge sorts evidence into the following buckets:

- `unit_synthetic`
  - isolated logic proof with synthetic collaborators or controlled internals
- `resilience_failure_mode`
  - evidence that failure cases, missing dependencies, or degraded paths were explicitly tested
- `integration_real_path`
  - evidence that realistic internal paths executed with materially real collaborators
- `runtime_smoke`
  - evidence from a runnable environment that the user-visible or operator-visible path works at a basic level
- `deploy_or_runtime_observation`
  - evidence from deployed or near-runtime observation such as logs, traces, metrics, or confirmed environment behavior

All green checks are not equal.
TruthForge must identify which evidence class is carrying the claim.

## Required proof standard

TruthForge applies this default standard:

For runtime-visible or boundary-sensitive claims, merge readiness normally requires:
- at least one runtime-relevant proof path
- at least one failure-mode or assumption-oriented proof
- explicit declaration of remaining unverified assumptions

If this standard cannot be met because of repo constraints, environment limits, or missing infrastructure, TruthForge must:
- say exactly why
- downgrade confidence appropriately
- state what evidence would be needed for a stronger verdict

## Common failure patterns

TruthForge should aggressively inspect for these patterns:

1. Endpoint tests that stub or replace the full builder, service, or core execution path.
2. Tests that monkeypatch or mock the exact dependency most likely to fail in production.
3. Assertions that verify only shape, status code, render shell, or happy-path structure instead of real behavior.
4. UI tests that prove the page chrome exists but not that data loaded successfully.
5. Missing failure-mode tests for environment variables, filesystem dependencies, missing binaries, missing auth, service errors, or container differences.
6. Changes that add runtime assumptions without documenting or validating them.
7. Real route or service code paths never exercised in realistic conditions.
8. CI setups that treat synthetic success as equivalent to runtime-relevant proof.

## Procedure

### Phase 1: Extract the claim
For the current incident, PR, diff, or change set:

1. State the main functional claim in one sentence.
2. List the surfaces changed.
3. Identify whether the claim is:
   - runtime-visible
   - boundary-sensitive
   - internal-only
   - pure logic

### Phase 2: Inventory evidence
Collect and classify all available evidence:

- unit tests
- integration tests
- failure-mode tests
- browser or UI smokes
- logs, traces, metrics, or console output
- deployed or runtime observations
- CI results
- manual reproduction evidence

For each item:
- classify the evidence type
- state what claim it actually supports
- note whether it is direct, indirect, or synthetic support

### Phase 3: Inspect synthetic masking
Identify where evidence was weakened by:

- mocks
- stubs
- monkeypatches
- fake builders or services
- hard-coded payloads
- bypassed auth
- bypassed subprocesses
- bypassed filesystem or config dependencies

Be specific.
Do not merely say “too much mocking.”
Explain what exact failure mode was masked.

### Phase 4: Test runtime assumptions
Find unverified assumptions such as:

- required binaries exist
- environment variables are present
- files or directories exist
- auth context matches between environments
- service connectivity exists
- container images include required dependencies
- deploy or startup paths match local assumptions

Validate these assumptions directly where feasible.
If they cannot be validated, record them explicitly as unverified.

### Phase 5: Reach verdict and define remediation
Return:

- classification
- strongest supporting real-path evidence
- strongest synthetic evidence
- failure-mode coverage present or missing
- runtime assumptions still open
- exact remediation required
- whether the change is merge-ready

If the change is not merge-ready, say so plainly.

## Remediation rules

TruthForge must not stop at description when remediation is feasible.

When the issue is local and tractable:
1. fix the runtime issue
2. add missing failure-mode handling when appropriate
3. add the tests that would have caught the miss
4. run the strongest available smoke or runtime-relevant validation
5. record before and after evidence

For larger remediations:
1. create a parent remediation artifact or workpacket
2. create child tracked work for deferred items
3. ensure no important finding remains only in chat or short-term memory

## Merge-governance rules

TruthForge enforces the following default rules:

1. Synthetic tests do not count as runtime proof for runtime-visible claims.
2. Endpoint tests that stub the full builder or service path count only as limited wiring coverage.
3. Mocking the exact runtime-risk dependency reduces the value of the test as production evidence.
4. Runtime-visible changes should not be treated as merge-ready when all meaningful evidence is synthetic.
5. Remaining unverified assumptions must be stated explicitly.
6. If real-path or runtime-relevant proof is missing, the change should usually be classified below `SAFE`.

## Handoff format

TruthForge should return a report in this shape:

```text
TruthForge Report

Functional claim:
Changed surfaces:

Evidence inventory:
- unit_synthetic:
- resilience_failure_mode:
- integration_real_path:
- runtime_smoke:
- deploy_or_runtime_observation:

Synthetic masking detected:
- ...

Strongest real-path proof:
- ...

Failure-mode proof:
- ...

Unverified assumptions:
- ...

Classification:
- SAFE | PARTIAL | FALSE_CONFIDENCE_RISK | BROKEN_IN_RUNTIME_RISK

Remediated now:
- ...

Still open:
- ...

Tracked follow-up:
- ...

Merge readiness verdict:
- READY
- READY WITH EXPLICIT RISK
- NOT READY
Example invocation
Example A: PR audit
Use TruthForge on PR #184.

Functional claim:
“The operator page now correctly loads repository status and branch information.”

Focus on:
- whether the route or page only proved mocked collaborators
- whether git or filesystem assumptions were actually exercised
- whether there is at least one runtime-relevant proof path
- whether missing dependency failure modes were tested

Return a TruthForge Report and a merge-readiness verdict.
Example B: Incident mode
Use TruthForge on this incident:

Observed runtime behavior:
“The control page returns backend 500s in local runtime even though CI is green.”

Tasks:
- reproduce the issue
- identify the synthetic-confidence gap
- fix the issue if feasible
- add the exact tests or smokes that would have caught it
- return a TruthForge Report with remediation and follow-up work
Adaptation notes

TruthForge is repo-agnostic in intent, but it must be adapted to the repo’s actual constraints.

Adapt for:

frontend-only repos where runtime proof may mean browser-level evidence
backend or service repos where runtime proof may mean real route, job, or CLI execution
monorepos where changed surfaces span multiple packages
repos without staging or smoke environments
repos where auth, binaries, or external services are only partially available in local development

Do not fake compliance.
If the environment cannot provide strong proof, lower confidence and say what is missing.

Philosophy

TruthForge exists to prevent agents and humans from mistaking synthetic confidence for reality.

Its job is not to generate comfort.
Its job is to recover truth.
