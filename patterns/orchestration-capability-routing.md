# Pattern: Orchestration Capability Routing

## Intent

Turn orchestration from ad hoc decisions into a deterministic contract that routes work by risk, complexity, ambiguity, and evidence quality.

## Scope boundary

This pattern is orchestration-layer routing.
It is not token-level decode routing inside model inference.

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
- disagreement or contradiction level

Derived values:

- `risk_score` = blast radius + runtime visibility + auth/security sensitivity + money/irreversible risk + disagreement
- `complexity_score` = scope size + novelty + file overlap risk + (3 - specification clarity)

## Lanes

- `fast_builder`
- `standard_builder`
- `planner`
- `judge`
- `safety_governance_reviewer`
- `orchestrator_integrator`

## Routing rules

1. Use `fast_builder` only for low risk, low complexity, clear specs, and strong evidence.
2. Use `standard_builder` as default for normal work.
3. Escalate to `planner` for high complexity, high risk, or unclear specs.
4. Require `judge` when evidence conflicts, disagreement persists, or evidence is weak.
5. Require `safety_governance_reviewer` for security or irreversible risk.
6. Require `orchestrator_integrator` for final synthesis on non-trivial work.

## Escalation triggers

- ambiguity with non-trivial blast radius
- runtime-visible claim without runtime-relevant proof
- boundary-sensitive claim without failure-mode proof
- unresolved contradiction across agents or evidence
- high overlap with concurrent edits

## Continuation authority

Allow implicit continuation only when:

- required lanes and reviewer roles are satisfied
- no escalation trigger remains unresolved
- proof expectations for claim type are met

Pause for operator input when:

- multiple non-equivalent paths remain viable
- policy-impacting decisions are needed
- risk acceptance is required

## AGENTS bootstrap block

Use this insertion when a repository is missing an orchestration contract:

```markdown
## Orchestration & Capability Routing

This repository uses orchestration-layer capability routing.
It does not claim token-level routing inside model inference.

### Routing signals
- scope_size (0-3)
- novelty (0-3)
- blast_radius (0-3)
- runtime_visibility (0-3)
- auth_security_sensitivity (0-3)
- money_irreversible_risk (0-3)
- evidence_strength (0-3)
- specification_clarity (0-3)
- file_overlap_risk (0-3)
- disagreement_level (0-3)

### Lanes
- fast_builder
- standard_builder
- planner
- judge
- safety_governance_reviewer
- orchestrator_integrator

### Mandatory escalations
- escalate to planner when risk or complexity is high
- escalate to judge on contradiction or weak evidence
- escalate to safety/governance on security or irreversible risk

### Proof expectations
- runtime-visible claims require runtime-relevant proof
- boundary-sensitive claims require runtime-relevant and failure-mode proof
- security-sensitive claims require governance review before merge

### Continuation authority
- implicit continuation is allowed only when required lanes and proof expectations are satisfied
- pause for operator input when ambiguity or policy-impacting risk remains
```

## Companion check

Run [`orchestrator-routing-check.md`](/C:/DEV2/ClankerKit/checks/orchestrator-routing-check.md) after bootstrap or patch application.
