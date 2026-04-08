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

TruthForge determines whether code changes proved their functional claims in runtime terms or only passed synthetic harnesses.

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
3. A change touches risky boundaries such as UI, routes, auth, subprocesses, filesystem, environment assumptions, runtime wrappers, or control surfaces.
4. Tests rely heavily on mocks, stubs, monkeypatches, fake payloads, or full builder or service replacement.
5. A repo-wide truth-recovery effort is underway after incidents or suspicious merges.

## Do not use when

Do not invoke TruthForge for tiny isolated pure-function changes unless there is reason to suspect the evidence is misleading.

TruthForge should not become a tax on trivial refactors.

## Core rule

A change does not get credit for proving reality when it only proved mocks.

Synthetic evidence may support a claim, but it cannot substitute for runtime-relevant proof when the claim is runtime-visible.

## Repo-truth-recovery program mode

When mode is `repo-truth-recovery`, TruthForge must run as one parent program artifact, not scattered ad hoc reviews.

### Parent program requirements

1. Create one parent truth-recovery artifact.
2. Force all findings under that parent.
3. Use one shared evidence schema and one shared classification model.
4. Keep per-domain scope bounded.

### Tracker-neutral terminology

TruthForge is repo agnostic. Queue artifact naming can be:

- issue
- ticket
- workpacket
- task

The skill must map local tracker nouns into one normalized queue model in the report.

### Required audits

TruthForge must run these three audits:

1. `Merged Code Truth Audit`
What already merged is real, risky, partial, or synthetic by proxy.

2. `Intent Drift Audit`
What the project originally intended versus what current code and workflows are optimized for.

3. `Open Queue Rebaseline`
Which open queue artifacts are aligned, stale, superseded, or need re-scope.

### Finding disposition states

Every finding must end in exactly one disposition:

- `fixed_now`
- `child_wp`
- `superseded_closed`
- `rescoped_new_wp`
- `audited_safe_no_action`

## Audit domains

TruthForge must use a bounded domain profile.

If the repo already defines audit domains, use those.
If not, use this default generic profile:

1. User-facing surfaces (UI, API, CLI, operator interfaces)
2. Services and business logic paths
3. IO and host dependencies (subprocess, filesystem, shell, git, environment assumptions)
4. Runtime and deployment flows (containers, startup, wrappers, orchestration)
5. Security and access control (authn, authz, privileged controls)
6. Quality gates and delivery workflows (CI, PR checks, release wrappers)
7. Queue and planning artifacts (issues, tickets, workpackets, tasks)

If a domain is intentionally omitted, TruthForge must state why and mark confidence impact.

## Inputs

TruthForge expects as many of the following as available:

- current diff, PR, or commit range
- stated functional claim
- incident notes or failing behavior
- test and CI artifacts
- logs, traces, metrics, console output
- local, staging, or smoke environment details
- environment assumptions and tooling constraints
- queue tracker state
- architecture intent references, docs, or runbooks

If key inputs are missing, TruthForge must state what is missing and how confidence is degraded.

## Outputs

TruthForge must produce a structured report containing:

- functional claim
- changed surfaces
- evidence inventory and evidence classes
- synthetic masking detected
- real-path proof identified
- failure-mode proof identified
- unverified assumptions
- merged-code classification
- queue classification where applicable
- disposition per finding
- remediated now
- deferred tracked work
- merge or governance readiness verdict

## Classifications

### Merged-code classification

Every reviewed code finding must be one of:

- `SAFE`
- `PARTIAL`
- `FALSE_CONFIDENCE_RISK`
- `BROKEN_IN_RUNTIME_RISK`

### Open-queue classification

Every open queue artifact must be one of:

- `KEEP`
- `RESCOPE`
- `SUPERSEDED`
- `RETIRE`
- `SPLIT`

## Evidence classes

TruthForge sorts evidence into:

- `unit_synthetic`
- `resilience_failure_mode`
- `integration_real_path`
- `runtime_smoke`
- `deploy_or_runtime_observation`

All green checks are not equal.
TruthForge must identify which evidence class actually carries each claim.

## Required proof standard

For runtime-visible or boundary-sensitive claims, merge readiness normally requires:

- at least one runtime-relevant proof path
- at least one failure-mode or assumption-oriented proof
- explicit declaration of unverified assumptions

If this standard cannot be met due to environment limits, TruthForge must say why, downgrade confidence, and state exactly what evidence is missing.

## Common failure patterns

TruthForge should aggressively inspect for:

1. Endpoint tests that stub or replace the full builder, service, or core execution path.
2. Mocking the exact dependency most likely to fail in runtime.
3. Assertions that verify only shape or status instead of real behavior.
4. UI tests that prove shell rendering without proving successful data load.
5. Missing failure-mode tests for env vars, filesystem, binaries, auth, service errors, or container differences.
6. New runtime assumptions added without documentation or validation.
7. Real route or service code paths never exercised in realistic conditions.
8. CI setups treating synthetic success as equivalent to runtime-relevant proof.

## Procedure

### Phase 1: Extract claims and scope

1. State functional claims in one sentence each.
2. List changed surfaces.
3. Mark claim type: runtime-visible, boundary-sensitive, internal-only, or pure logic.
4. Assign scope to audit domains.

### Phase 2: Inventory and classify evidence

1. Gather tests, smokes, logs, observations, and manual repro artifacts.
2. Classify each item by evidence class.
3. Mark support type as direct, indirect, or synthetic.

### Phase 3: Inspect synthetic masking

Identify where evidence was weakened by mocks, stubs, monkeypatches, fake services, hard-coded payloads, bypassed auth, bypassed subprocesses, or bypassed filesystem or config dependencies.

### Phase 4: Test runtime assumptions

Validate assumptions where feasible:

- required binaries
- required env vars
- filesystem paths
- auth context parity
- service connectivity
- container dependency parity
- startup and deploy path parity

If assumptions cannot be validated, record them as unverified.

### Phase 5: Verdict and disposition

For each finding:

1. assign classification
2. assign disposition state
3. assign remediation lane
4. assign owner and tracking link if deferred

## Remediation in two speeds

### Speed 1: Fix now

Use for bounded low or medium remediations:

- missing failure-mode tests
- missing real-path tests
- bad route or build stubs
- local runtime-proof fixes
- narrow assumption validation gaps

### Speed 2: Track for merge train

Use for larger or cross-subsystem work:

- multi-domain remediations
- runtime or live-proof infrastructure work
- changes requiring staged rollout or coordinated ownership

## Open-queue ruthless pass

For each open queue artifact, TruthForge must ask:

1. Does this align with the current north star?
2. Is the problem statement still true?
3. Was it already partially solved another way?
4. Is it targeting a superseded architecture?
5. Should it become a different queue artifact?

If not aligned, classify and dispose as `RETIRE`, `SUPERSEDED`, or immediate `RESCOPE`.

## Merge-governance rules

1. Synthetic tests do not count as runtime proof for runtime-visible claims.
2. Endpoint tests that stub the full builder or service path count only as limited wiring coverage.
3. Mocking the exact runtime-risk dependency reduces production evidence value.
4. Runtime-visible changes are not merge-ready when meaningful evidence is only synthetic.
5. Unverified assumptions must be explicit.
6. Missing real-path proof usually classifies below `SAFE`.

## Handoff format

```text
TruthForge Report

Program mode:
Parent program:
Domain profile used:
Audit domains covered:
Audit domains skipped:

Functional claim(s):
Changed surfaces:

Evidence inventory:
- unit_synthetic:
- resilience_failure_mode:
- integration_real_path:
- runtime_smoke:
- deploy_or_runtime_observation:

Synthetic masking detected:
Strongest real-path proof:
Failure-mode proof:
Unverified assumptions:

Merged-code classification:
- SAFE | PARTIAL | FALSE_CONFIDENCE_RISK | BROKEN_IN_RUNTIME_RISK

Open-queue classification:
- KEEP | RESCOPE | SUPERSEDED | RETIRE | SPLIT

Finding dispositions:
- fixed_now | child_wp | superseded_closed | rescoped_new_wp | audited_safe_no_action

Remediated now:
Tracked follow-up:
Still open:

Merge readiness verdict:
- READY
- READY WITH EXPLICIT RISK
- NOT READY
```

## Philosophy

TruthForge exists to prevent agents and humans from mistaking synthetic confidence for reality.

Its job is not to generate comfort.
Its job is to recover truth.
