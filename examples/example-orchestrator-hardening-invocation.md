# Example Orchestrator Hardening Invocation

## Scenario

A repository has inconsistent orchestration behavior:

- sessions route easy and risky work through the same lane
- AGENTS lacks explicit escalation thresholds
- continuation authority is implicit and inconsistent

## Invocation

```text
Use orchestrator-hardening on this repository.

Objective:
Bootstrap or harden an AGENTS orchestration contract.

Requirements:
1. inspect AGENTS and any orchestration docs
2. classify contract status as missing, weak, or strong
3. if missing, emit a bounded Orchestration & Capability Routing insertion block
4. if weak, emit a minimal patch plan
5. define deterministic lane routing and escalation thresholds
6. define continuation authority and stop boundaries
7. define proof expectations by claim type

Return:
- OrchestratorHardening Report
- bootstrap insertion block or patch plan
- routing check result
```

## Expected output shape

```text
OrchestratorHardening Report

Contract status:
Detected policy files:
Queue noun normalization:

Routing signal table:
Lane policy:
Escalation matrix:

Continuation authority:
Stop conditions:
Proof policy by claim type:

Bootstrap insertion block:
Patch plan:

Classification:
- READY
- READY WITH EXPLICIT RISK
- NOT READY
```
