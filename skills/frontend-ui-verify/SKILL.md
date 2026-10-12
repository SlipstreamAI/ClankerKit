---
name: frontend-ui-verify
description: "Verifies a user-visible UI change by exercising the flow and recording screenshot or trace evidence. Use when a pull request claims a screen, component, or interaction changed and unit tests are the only proof."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: validation
  status: experimental
  tags: "frontend, ui, screenshot, playwright"
  modes: "pr-audit, ui"
  version: "0.1.0"
  author: SlipstreamAI
---

# Frontend UI Verify

**Tagline:** Prove the UI change with a flow, not a unit color.

## Purpose

Frontend UI Verify ties a visual or interaction claim to a path a user can walk. A screenshot, Playwright trace, or equivalent runtime capture is the receipt. Unit tests can support it. They do not replace it.

## Use when

1. A PR changes layout, copy, navigation, forms, or client-side state a person can see.
2. The author says it works in the browser and the diff only shows component tests.
3. You need before and after evidence, including an empty or error state.

## Do not use when

- API-only changes with no UI. Use api-contract-check.
- Accessibility conformance as the main question. Use accessibility-audit, and attach its evidence here if the claim is also visual.

## Inputs

- The user-visible claim.
- How to start the app.
- Viewport or browser you can actually run.

## Outputs

- Steps you performed.
- Artifact paths for screenshots, traces, or a written observation if capture tools are missing.
- Empty, error, and narrow-width results, or an explicit skip.

File the note with [the proof template](assets/proof-note.md).

## Procedure

### Phase Name the flow

1. Write the claim as what a person sees or does.
2. Identify the route or screen and the starting state.
3. Decide the command that boots the app. If you cannot boot it, status stays partial.

### Phase Exercise it

1. Perform the flow in a browser or a Playwright run.
2. Capture a screenshot or trace of the claimed state.
3. Also hit one of: empty state, error state, or a narrow viewport, unless the claim cannot occur there.

### Phase Compare

1. If a before state exists, capture it with the same steps.
2. Describe what changed in the artifact, not only in the diff.
3. Note console errors you observed. Do not claim a clean console you did not look at.

### Phase Bound the proof

1. Say which browsers and widths you did not run.
2. Do not call the UI done from a green component test alone.

## Proof requirements

- An artifact path or a pasted observation tied to a command.
- The steps are specific enough that someone else can repeat them.

## Common failure patterns

- A screenshot of the wrong route.
- Storybook standing in for the integrated page when the claim is about the page.
- Declaring pixel perfection from one width.

## Adaptation notes

- No Playwright: a manual browser note with URL, steps, and what you saw still counts as partial runtime evidence. Say the tool gap.
- Native clients: substitute the platform's screenshot tooling and name the device class.

## Example invocation

```text
Use frontend-ui-verify.

Claim: the empty invoice list shows the create action.
Start: npm run dev
Width: 1280 and 390.

Return steps and artifact paths.
```

## Handoff format

```text
Frontend UI Verify Report

Status: success | partial | blocked | failed
Claim:
Start command:
Steps:
Artifacts:
Empty or error state:
Narrow viewport:
Not run:
Console notes:
```
