# Check: Claim vs Proof

## Intent

Verify that the strongest evidence actually proves the stated claim.

## Questions

1. What exact claim is being made in runtime terms?
2. Which changed surface could falsify the claim?
3. What is the strongest direct evidence item?
4. Is that evidence synthetic, indirect, or runtime-relevant?
5. What assumptions are still open?

## Pass criteria

- claim is explicit and falsifiable
- at least one direct proof item maps to claim behavior
- evidence class is appropriate for claim risk
- open assumptions are declared and bounded

## Fail signals

- claim is broad but evidence only checks wiring
- all evidence depends on mocks for risk-heavy dependencies
- proof validates structure, not behavior
- confidence language exceeds evidence quality

## Output

```text
Claim vs Proof Result
Claim:
Strongest evidence:
Evidence class:
Gap summary:
Open assumptions:
Verdict: PASS | PASS_WITH_RISK | FAIL
```
