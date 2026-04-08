# Check: Repo Risk Checklist

## Intent

Quickly map which boundaries can fail before implementation or merge.

## Checklist

- entrypoints touched are known and reviewed
- auth assumptions are explicit
- environment variable dependencies are listed
- filesystem and path assumptions are listed
- subprocess and binary dependencies are listed
- external services or network calls are identified
- startup or deployment scripts changed are reviewed
- observability impact is understood
- rollback path exists for risky changes

## Risk labels

- `low`: isolated logic, low blast radius
- `medium`: internal integration, moderate blast radius
- `high`: runtime-visible or boundary-sensitive
- `critical`: irreversible mutation, money movement, or major control surface

## Output

```text
Repo Risk Checklist Result
Changed surfaces:
Detected boundary risks:
Highest risk label:
Missing validations:
Next required checks:
```
