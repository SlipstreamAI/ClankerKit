---
name: api-contract-check
description: "Compares an API or schema change with its consumers and flags breaking changes. Use when a pull request changes request or response shapes, status codes, OpenAPI, protobuf, or shared types."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: validation
  status: experimental
  tags: "api, schema, compatibility"
  modes: "pr-audit, release"
  version: "0.1.0"
  author: SlipstreamAI
---

# API Contract Check

**Tagline:** Catch breaking request and response changes before callers do.

## Purpose

API Contract Check decides whether a schema or handler change is compatible for existing callers. It looks at the contract artifact and at least one real consumer, not only the handler diff.

## Use when

1. Fields, enums, status codes, or required parameters change.
2. An OpenAPI, JSON Schema, GraphQL, or protobuf file is in the diff.
3. A shared type is imported by more than one package.

## Do not use when

- Internal refactors with no serialized shape change.
- Designing a brand-new API with no callers. Document the contract, and skip the breaking-change verdict.

## Inputs

- The contract diff.
- Known consumers: clients, tests, fixtures, or downstream packages.
- The compatibility promise, if the repo has one. Otherwise assume existing clients keep working.

## Outputs

- Breaking, compatible, or additive classification per change.
- Callers that must move in the same change.
- A contract test, fixture, or example payload you ran or could not run.

## Procedure

### Phase List the shape changes

1. Enumerate added, removed, renamed, and retyped fields, plus status code changes.
2. Mark each as additive, compatible, or breaking. Removing or renaming a response field is breaking unless every caller ships together.
3. Required new request fields are breaking for old clients.

### Phase Find consumers

1. Search for the field names and the operation id or route.
2. Include generated clients and fixture payloads.
3. If this is a monorepo, list packages that import the type.

### Phase Check a payload

1. Run a contract test if one exists.
2. Otherwise validate one example request and response against the new schema, or show that no schema file exists.
3. Do not invent an example and call it a passing contract test.

### Phase Decide the release impact

1. Breaking changes need a version bump, a migration note, or a same-commit consumer update.
2. Additive changes still need the contract file updated if the repo keeps one.

## Proof requirements

- Each breaking change names the field and a consumer or states that no consumer was found in-repo.
- The contract file path is cited, or its absence is explicit.

## Common failure patterns

- Updating the handler and leaving OpenAPI stale.
- Calling a change compatible because the server still starts.
- Ignoring generated clients.

## Adaptation notes

- Events and queues: treat payload schemas like response bodies.
- GraphQL: a removed field is breaking. A new nullable field is additive.

## Example invocation

```text
Use api-contract-check.

Change: invoice.status gains value void.
Consumers: web app and public OpenAPI.

Return breaking versus additive, and the fixture you checked.
```

## Handoff format

```text
API Contract Check Report

Status: success | partial | blocked | failed
Contract files:
Shape changes:
Classification:
Consumers:
Payload or test evidence:
Version or migration note:
Unverified callers:
```
