---
name: accessibility-audit
description: "Audits a UI change against keyboard, name, contrast, and error-state checks with evidence. Use when a screen changes and someone needs a WCAG-oriented pass that says what was actually exercised."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: validation
  status: experimental
  tags: "accessibility, wcag, ui"
  modes: "pr-audit, ui"
  version: "0.1.0"
  author: SlipstreamAI
---

# Accessibility Audit

**Tagline:** Check the interaction, and write down what you did not check.

## Purpose

Accessibility Audit records checks you performed. It does not issue a conformance certificate from a glance. Keyboard use, accessible names, contrast on the changed UI, and error announcement are the default set.

## Use when

1. A form, dialog, menu, or navigation change is in a PR.
2. A design relies on color or a click-only control.
3. You need a partial WCAG pass with explicit gaps.

## Do not use when

- A full-site legal conformance audit.
- Visual polish with no interaction claim. Use frontend-ui-verify for screenshots, and this skill when the claim is about access.

## Inputs

- The screen and the changed components.
- A way to run the UI.
- The checks in scope. Default to the reference list.

## Outputs

- Checks passed, failed, or not run.
- Evidence: steps, computed name, or contrast values you actually observed.
- Fixes ranked by who is blocked.

Work from [the WCAG checks](references/wcag-checks.md). Do not mark a row you did not perform.

## Procedure

### Phase Set the scope

1. Name the components a person reaches in the changed flow.
2. Include the error state if the flow can fail validation.
3. Say which assistive technology you have. If you have none, you can still do keyboard, name, and contrast checks, and you must say so.

### Phase Keyboard and focus

1. Reach every new control without a pointer.
2. Confirm focus is visible and does not get trapped, except a modal that traps focus on purpose and releases it on close.
3. Record the key sequence.

### Phase Names, contrast, and errors

1. Each control has a name you can point to in the markup or accessibility tree.
2. Text and essential icons on the changed UI meet the contrast level you measured, or you mark contrast not measured.
3. Errors are not conveyed by color alone and are attached to the field.

### Phase Report the gap

1. Failed checks include the element and the fix.
2. Not-run checks stay not-run. Do not average them into a score.
3. Do not write 'WCAG compliant' for a partial pass.

## Proof requirements

- Each passed check has a step or a cited attribute.
- The handoff lists not-run checks.

## Common failure patterns

- An automated scanner score with no keyboard pass.
- A conformance claim from the happy path only.
- Removing a focus outline to make a screenshot look cleaner.

## Adaptation notes

- Native apps: swap keyboard for the platform's switch or keyboard equivalent and name it.
- No running UI: review the markup and mark every runtime check not-run.

## Example invocation

```text
Use accessibility-audit on the invoice create dialog.

Checks: keyboard, names, contrast, errors.
AT available: none.

Return the matrix and the fixes.
```

## Handoff format

```text
Accessibility Audit Report

Status: success | partial | blocked | failed
Scope:
Assistive tech:
Passed:
Failed:
Not run:
Fixes:
Conformance claim: none | partial-notes-only
```
