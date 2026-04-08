# Pattern: Governed Agent Loop

## Intent

Run agent work in a loop where evidence quality is evaluated continuously, not only at the end.

## Loop stages

1. Frame the claim
   - restate expected outcome in runtime terms
   - classify risk level and blast radius
2. Plan execution
   - identify changed surfaces and proof targets
   - define minimum evidence class needed
3. Implement and instrument
   - make targeted edits
   - collect execution artifacts while changes are fresh
4. Validate claim
   - run validation skill and classify evidence
   - test at least one failure mode for risky claims
5. Govern merge decision
   - evaluate with governance skill
   - block, accept with explicit risk, or approve
6. Capture handoff
   - publish deterministic report
   - track unresolved assumptions

## Recommended skill sequence

- `map-the-system` before broad edits
- `runtime-proof` after implementation
- `truthforge` for merge-governance verdict
- `operator-handoff` before release handoff

## Decision policy

- runtime-visible claim without runtime-relevant evidence: not ready
- boundary-sensitive change without failure-mode evidence: not ready
- open assumptions without explicit ownership: not ready

## Artifacts to retain

- claim statement
- evidence inventory with classes
- gate verdict
- remediation and follow-up links
