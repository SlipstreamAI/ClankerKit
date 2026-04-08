# Check: Orchestrator Routing Check

## Intent

Verify that a repository's orchestration contract is deterministic, risk-aware, and evidence-aware.

## Run when

- bootstrapping orchestration language into `AGENTS.md`
- upgrading weak routing or escalation rules
- auditing session-governance drift

## Required sections

- orchestration intent and scope boundary
- routing signals and scoring model
- lane definitions and selection policy
- escalation thresholds
- continuation authority
- stop conditions
- proof expectations by claim type
- operator confirmation boundaries

## Determinism checks

1. Are routing signals explicit and bounded?
2. Is lane selection rule-based instead of discretionary prose?
3. Are mandatory escalations defined for ambiguity, contradiction, and high risk?
4. Are proof requirements tied to claim type?
5. Are continuation and pause boundaries explicit?

## Fail signals

- orchestration language implies token-level routing claims
- no mandatory escalation path for risky work
- no judge or governance lane for contradictory evidence
- continuation authority unclear
- runtime-visible claims allowed without runtime-relevant proof

## Output

```text
Orchestrator Routing Check Result

Contract status:
Missing sections:
Weak sections:
Determinism score:

Pass conditions met:
Fail signals detected:
Required patch actions:

Verdict:
- PASS
- PASS_WITH_RISK
- FAIL
```
