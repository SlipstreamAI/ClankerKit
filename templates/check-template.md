# <Check Name>

## Intent

Define what risk this check is designed to catch.

## Trigger

Run this check when:

- <condition>
- <condition>

## Inputs

- diff or PR link
- claimed outcome
- test and runtime artifacts

## Fast pass questions

1. What exact claim is being made?
2. Which changed surfaces can fail in runtime?
3. Is the strongest evidence synthetic or runtime-relevant?
4. Which assumptions remain unverified?

## Required evidence

- at least one direct proof item tied to the claim
- at least one failure-mode or assumption test for risky changes
- explicit declaration of unverified assumptions

## Red flags

- full path replaced with mocks or stubs
- route wiring tested but collaborator behavior never exercised
- CI green used as sole merge argument
- runtime dependencies not validated

## Output contract

```text
Check: <Check Name>
Claim:
Risk surfaces:
Evidence present:
Evidence missing:
Assumptions open:
Verdict: PASS | PASS_WITH_RISK | FAIL
Required actions:
```
