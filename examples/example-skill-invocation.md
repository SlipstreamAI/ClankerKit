# Example Skill Invocation

## Scenario

A PR claims:
"The operator status page now shows branch and sync status in local runtime."

## Invocation

```text
Use truthforge on PR #184.

Functional claim:
"The operator status page now shows branch and sync status in local runtime."

Focus on:
- real git and filesystem assumptions
- whether evidence is synthetic or runtime-relevant
- failure handling when git binary or repo path is missing

Return:
- TruthForge Report
- merge-readiness verdict
```

## Expected output shape

```text
TruthForge Report
Functional claim:
Changed surfaces:
Evidence inventory:
Synthetic masking detected:
Strongest real-path proof:
Failure-mode proof:
Unverified assumptions:
Classification:
Remediated now:
Still open:
Tracked follow-up:
Merge readiness verdict:
```
