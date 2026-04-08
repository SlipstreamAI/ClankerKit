# Example Governed Loop

## Objective

Fix an incident where runtime behavior fails while CI is green.

## Loop

1. `map-the-system`
   - identify real entrypoints and dependencies for the failing surface
2. `trace-the-failure`
   - reproduce and isolate the failing path
3. `runtime-proof`
   - verify fix against runtime-relevant evidence
4. `truthforge`
   - evaluate confidence quality and merge readiness
5. `definition-of-done-check`
   - confirm handoff completeness

## Example run command text

```text
Incident:
"Control page returns backend 500 in local runtime, CI green."

Run:
1. map-the-system on affected module
2. trace-the-failure with runtime logs
3. runtime-proof on proposed fix
4. truthforge for merge verdict

Return:
- consolidated evidence report
- remediation completed now
- tracked deferred work
- final readiness verdict
```
