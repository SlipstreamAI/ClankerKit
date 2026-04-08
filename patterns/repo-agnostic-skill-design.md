# Pattern: Repo-Agnostic Skill Design

## Intent

Design skills that transfer across repositories without hiding critical environmental differences.

## What to keep generic

- procedure phases
- evidence classes
- classification system
- output contract

## What to make adaptable

- available tools
- runtime environments
- deployment model
- auth and dependency constraints
- risk thresholds

## Adaptation strategy

1. Declare baseline assumptions.
2. Detect missing capabilities in the target repo.
3. Downgrade confidence when strong proof is unavailable.
4. List exact evidence needed to upgrade confidence.

## Required adaptation section in every skill

- frontend-only adaptation
- backend or service adaptation
- monorepo adaptation
- no-staging or no-smoke adaptation
- restricted-tooling adaptation

## Anti-patterns

- pretending environment limits do not matter
- claiming cross-repo validity without stating assumptions
- baking one stack's internals into a supposedly generic skill

## Quality check

A repo-agnostic skill is successful when:

- two different repos can run it with only adapter-level edits
- output format stays identical
- confidence handling remains honest under constraints
