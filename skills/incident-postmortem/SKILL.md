---
name: incident-postmortem
description: "Writes a blameless incident postmortem with a timeline, impact, and owned action items. Use when an incident is over or stable and the team needs a record that separates evidence from guesswork."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: documentation
  status: experimental
  tags: "incident, postmortem, timeline"
  modes: "incident, handoff"
  version: "0.1.0"
  author: SlipstreamAI
---

# Incident Postmortem

**Tagline:** A blameless timeline with actions that have owners.

## Purpose

Incident Postmortem turns chat and logs into a timeline someone who was not there can trust. It does not assign personal blame. Unknowns stay unknown.

## Use when

1. An outage, data incident, or severe regression needs a write-up.
2. The timeline in chat contradicts the logs.
3. Action items are being listed without owners.

## Do not use when

- Live incident command. Stabilize first. Use trace-the-failure while the fault is still moving.
- Performance work with no incident.

## Inputs

- Start and end times, or an admission that they are approximate.
- Logs, alerts, deploys, and chat excerpts.
- Who is writing the follow-ups.

## Outputs

- Timeline with evidence pointers.
- User or system impact.
- What went well and what failed in the system, not in a person.
- Action items with owners and a detection note.

## Procedure

### Phase Build the timeline

1. Order events from artifacts. Mark each time as exact or approximate.
2. Include detection, mitigation, and recovery as separate events.
3. Drop color commentary that is not an event.

### Phase State impact

1. Who was affected, for how long, and what they could not do.
2. If impact is unknown, say unknown. Do not convert silence into zero.

### Phase Explain the mechanism

1. Describe the technical path that produced the impact.
2. Separate contributing conditions from the trigger.
3. Name what would have detected it sooner, if anything in the record supports that.

### Phase Write actions

1. Each action has an owner and a concrete outcome.
2. Prefer a detection or guardrail action over a promise to be more careful.
3. Label items the team will not do, so they do not linger as pretend work.

## Proof requirements

- Timeline rows point at a log, deploy, or message.
- Impact is sourced or marked unknown.
- Action items without owners are not called committed.

## Common failure patterns

- A narrative that names a guilty person instead of a missing guardrail.
- Root cause certainty that the logs do not support.
- Action items that are slogans.

## Adaptation notes

- Security incidents: omit exploit detail and secret values. Record the control that failed.
- Small regressions: a short timeline is still a postmortem if impact and one action are real.

## Example invocation

```text
Use incident-postmortem.

Window: 2026-10-11 14:02Z to 14:40Z.
Sources: alert invoice-send-error, deploy 18f3, support notes.

Return timeline, impact, and owned actions.
```

## Handoff format

```text
Incident Postmortem Report

Status: success | partial | blocked | failed
Incident:
Timeline:
Impact:
Mechanism:
Unknowns:
Action items:
Explicitly not doing:
```
