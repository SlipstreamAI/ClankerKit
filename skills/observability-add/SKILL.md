---
name: observability-add
description: "Adds logs, metrics, or traces that answer a specific production question, without leaking secrets. Use when a feature is shipping and operators could not tell whether it worked or failed."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: hardening
  status: experimental
  tags: "observability, logs, metrics, traces"
  modes: "feature, release-readiness"
  version: "0.1.0"
  author: SlipstreamAI
---

# Observability Add

**Tagline:** Add the signal that answers a production question.

## Purpose

Observability Add starts from the question an operator will ask at 2am, then adds the smallest signal that answers it. A sample line, metric name, or trace attribute is the receipt.

## Use when

1. A new job, route, or integration has no success or failure signal.
2. An incident showed that a path was invisible.
3. You need correlation across a request and a worker.

## Do not use when

- Dumping objects into logs.
- Building a metrics platform.

## Inputs

- The production question.
- Existing logging, metrics, and trace tools in the repo.
- The request or job id that should correlate events.

## Outputs

- Signal added: log, metric, or span.
- A sample event with secret fields removed.
- How you confirmed it emitted.

## Procedure

### Phase Write the question

1. Phrase the question as something an operator can answer yes, no, or with a count.
2. Choose log, metric, or trace based on that question. Counts and rates want a metric. A single failed payload wants a log. A hop wants a span.
3. Reuse the repo's existing libraries.

### Phase Add the signal

1. Include a correlation id that already exists, or add one at the boundary.
2. Log identifiers and outcomes, not secrets, tokens, or full personal data.
3. Name the metric or event so it matches neighboring names.

### Phase Prove it emitted

1. Trigger the success path and the failure path if you can do so safely.
2. Capture one redacted sample.
3. If you cannot run the app, show the call site and mark emission unmeasured.

### Phase Leave the operator a sentence

1. Write where to look and what a healthy event looks like.
2. Note what this signal still cannot tell you.

## Proof requirements

- The question and the signal match.
- The sample contains no secret. Say what you removed.
- Emission is measured or explicitly unmeasured.

## Common failure patterns

- A log of the entire request body.
- A metric with no way to distinguish failure from success.
- A new tracing stack beside the one the repo already uses.

## Adaptation notes

- Batch jobs: a start, a count, and a terminal success or failure is enough.
- Frontend: a user-facing error needs a client event that does not include the auth token.

## Example invocation

```text
Use observability-add.

Question: did the invoice email send fail, and which invoice was it?
Existing tool: structured logs with request_id.

Return the event name and a redacted sample.
```

## Handoff format

```text
Observability Add Report

Status: success | partial | blocked | failed
Question:
Signal:
Correlation id:
Sample:
How emission was checked:
Fields omitted:
Still invisible:
```
