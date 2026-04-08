# Check: Pre-Merge Skeptic

## Intent

Run a final skeptical pass before merge so synthetic confidence does not slip into main.

## Scope

Use on:

- runtime-visible features
- boundary-sensitive refactors
- incidents with fast follow-up fixes

## Skeptic pass

1. Identify the merge claim.
2. List high-risk changed surfaces.
3. Separate real-path proof from synthetic support.
4. Confirm failure-mode coverage for top risks.
5. Confirm unresolved assumptions are explicit.

## Block conditions

- no runtime-relevant evidence for runtime-visible claim
- no failure-mode evidence for boundary-sensitive change
- undocumented assumptions that can break startup, auth, IO, or service access
- evidence report missing or non-deterministic

## Output

```text
Pre-Merge Skeptic Report
Merge claim:
Risk surfaces:
Real-path proof:
Synthetic-only proof:
Failure-mode coverage:
Open assumptions:
Verdict: READY | READY_WITH_RISK | NOT_READY
Required actions:
```
