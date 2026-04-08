# Pattern: Deterministic Evidence Gates

## Intent

Replace subjective merge arguments with deterministic evidence requirements.

## Gate model

Define gates by claim type and risk surface:

- low-risk internal change
- runtime-visible feature
- boundary-sensitive integration
- irreversible state mutation

Each gate defines:

- required evidence classes
- required failure-mode checks
- maximum unresolved assumptions allowed

## Example baseline gate policy

### Internal-only claim

- required: `integration_real_path` or equivalent direct proof
- optional: failure-mode proof if dependency risk is low

### Runtime-visible claim

- required: one runtime-relevant path (`integration_real_path` or `runtime_smoke`)
- required: one failure-mode or assumption-oriented proof
- required: explicit open assumptions list

### Boundary-sensitive claim

- required: runtime-relevant path through real collaborator boundaries
- required: missing dependency or degraded path test
- required: observability evidence if available

## Enforcement options

- advisory: report generated, does not block merge
- soft gate: block unless risk accepted by named owner
- hard gate: block until gate criteria are met

## Failure handling

If evidence is missing:

1. downgrade verdict
2. state exact missing proof
3. create tracked follow-up
4. do not present synthetic evidence as equivalent substitute
