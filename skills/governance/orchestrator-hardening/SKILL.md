---
name: "orchestrator-hardening"
category: "governance"
description: "Governance skill for bootstrapping and hardening deterministic orchestration and capability routing contracts in consuming repositories."
status: "provisional"
recommended-modes:
  - bootstrap
  - governance-reset
  - continuous-governance
allowed-tools:
  - git
  - rg
  - python
  - repo-tools
tags:
  - governance
  - orchestration
  - routing
  - escalation
  - proof-policy
---

# OrchestratorHardening

**Tagline:** Make orchestration intentional, risk-aware, and evidence-aware.

## Purpose

OrchestratorHardening establishes or upgrades a repository's orchestration contract so work is routed by difficulty, risk, ambiguity, and evidence quality instead of ad hoc judgment.

It inspects local orchestration language, bootstraps missing contract sections, and emits deterministic routing and escalation rules for future sessions.

## Core distinction

This skill must teach and enforce:

- `NOT`: token-level decode routing inside model inference
- `YES`: orchestration-layer capability routing at task, stage, lane, and governance levels

## Use when

1. a repo has no clear orchestrator contract in `AGENTS.md`
2. orchestration behavior is inconsistent across sessions
3. easy work and high-risk work are using the same lane by default
4. escalations happen too late or not at all
5. merge decisions depend on confidence language instead of proof policy

## Do not use when

Do not invoke for tiny one-off edits that do not affect orchestration behavior or governance boundaries.

## Inputs

- target repository root
- `AGENTS.md` or equivalent agent policy files
- orchestration docs or runbooks, if present
- local queue nouns (`issue`, `ticket`, `task`, `workpacket`, or equivalents)
- current lane model, if present
- current proof expectations by claim type, if present

If key policy files are missing, the skill must degrade confidence and still emit a bounded bootstrap contract.

## Outputs

OrchestratorHardening must produce:

- contract status: `missing`, `weak`, or `strong`
- detected orchestration language inventory
- routing signal table and lane selection policy
- escalation threshold matrix
- continuation authority and stop boundaries
- proof expectation policy by claim type
- bootstrap insertion block for `AGENTS.md`
- minimal patch plan if a contract exists but is weak

## Routing signals

Score each signal on `0-3`:

- scope size
- novelty
- blast radius
- runtime visibility
- auth or security sensitivity
- money or irreversible risk
- evidence strength
- specification clarity
- file overlap risk
- agent disagreement or contradiction level

Derived terms:

- `risk_score` = blast radius + runtime visibility + auth/security sensitivity + money/irreversible risk + disagreement
- `complexity_score` = scope size + novelty + file overlap risk + (3 - specification clarity)
- `evidence_gap` = 3 - evidence strength

## Lanes

- `fast_builder`
- `standard_builder`
- `planner`
- `judge`
- `safety_governance_reviewer`
- `orchestrator_integrator`

## Lane selection policy

1. `fast_builder` allowed only when:
   - `risk_score <= 3`
   - `complexity_score <= 3`
   - `evidence_strength >= 2`
   - `specification_clarity >= 2`
2. `standard_builder` default when:
   - `risk_score <= 6`
   - `complexity_score <= 6`
3. `planner` required when:
   - `risk_score >= 7`, or
   - `complexity_score >= 7`, or
   - `specification_clarity <= 1`
4. `judge` required when:
   - disagreement >= 2, or
   - conflicting evidence exists, or
   - `evidence_strength <= 1`
5. `safety_governance_reviewer` required when:
   - auth/security sensitivity >= 2, or
   - money/irreversible risk >= 1, or
   - runtime-visible claim lacks required proof class
6. `orchestrator_integrator` required for final synthesis on all non-trivial lanes.

## Escalation rules

Escalation is mandatory when any of these hold:

- ambiguous spec with non-trivial risk
- runtime-visible or boundary-sensitive claim without real-path proof
- auth, security, or irreversible risk above low threshold
- unresolved contradiction between agents, tests, or runtime evidence
- high file-overlap risk with concurrent work

## Continuation authority

Implicit continuation is allowed only when:

- selected lane and required reviewers are satisfied
- no stop condition is active
- required proof policy for current claim type is met

Pause for operator input when:

- risk is high and policy allows multiple non-equivalent paths
- acceptance criteria are unclear
- remediation changes product intent or operational policy

## Stop conditions

- missing required policy file with no safe bootstrap target
- unresolved critical contradiction
- required reviewer lane not satisfied
- required proof class unavailable for high-risk claim
- active security or irreversible risk without operator approval

## Proof expectations by claim type

- `internal-only`: integration-real-path proof usually sufficient
- `runtime-visible`: require runtime-relevant proof path
- `boundary-sensitive`: require runtime-relevant plus failure-mode proof
- `security-sensitive`: require runtime-relevant proof, failure-mode proof, and governance review

## Procedure

### Phase 1: discover local orchestration context

1. locate `AGENTS.md` and other orchestration docs
2. extract existing routing, escalation, and proof language
3. normalize local queue nouns

### Phase 2: assess contract quality

1. mark contract status as `missing`, `weak`, or `strong`
2. identify missing sections and weak thresholds
3. preserve valid local conventions

### Phase 3: bootstrap or patch

1. if missing, emit bounded `Orchestration & Capability Routing` insertion block
2. if weak, emit minimal patch plan with line-level upgrade targets
3. never overwrite strong local sections without explicit request

### Phase 4: encode routing and escalation model

1. define signal scoring
2. map scoring to lanes
3. define mandatory escalations and reviewer lanes
4. define continuation authority and stop boundaries

### Phase 5: emit companion artifacts

1. output AGENTS bootstrap snippet
2. output routing pattern reference
3. output invocation example and routing check

## Common failure patterns

1. confusing orchestration-layer routing with token-level routing
2. treating all tasks as one lane regardless of risk
3. missing escalation rules for contradiction and ambiguity
4. no explicit continuation authority, so sessions drift
5. no proof expectations by claim type, so risk and evidence mismatch

## Adaptation notes

- frontend-heavy repos: weight runtime visibility and UI smoke evidence
- backend-heavy repos: weight boundary and failure-mode proof expectations
- monorepos: add package-overlap and ownership checks to file-overlap signal
- restricted environments: preserve routing model and downgrade confidence where proof cannot be collected

## Example invocation

```text
Use orchestrator-hardening on this repository.

Goal:
Bootstrap or harden AGENTS orchestration contract.

Tasks:
1. inspect AGENTS and orchestration docs
2. classify contract status
3. emit bootstrap insertion block or minimal patch plan
4. define deterministic lane routing and escalation thresholds
5. return routing check results
```

## Handoff format

```text
OrchestratorHardening Report

Contract status:
Detected policy files:
Queue noun normalization:

Routing signal table:
Lane policy:
Escalation matrix:

Continuation authority:
Stop conditions:
Proof policy by claim type:

Bootstrap insertion block:
Patch plan:

Classification:
- READY
- READY WITH EXPLICIT RISK
- NOT READY
```
