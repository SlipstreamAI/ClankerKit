# Quickstart for Consumers

## Goal

Get practical value from ClankerKit in one session without importing the whole library.

## 5-minute setup

1. Pick one skill from [`skills-index.md`](/C:/DEV2/ClankerKit/docs/skills-index.md).
2. Give your agent the skill name and your task context.
3. Ask for the exact handoff format defined in that skill.
4. Add one related check from `checks/`.
5. Save the result in your PR, issue, or incident artifact.

## Recommended first bundle

Start with:

- `map-the-system`
- `runtime-proof`
- `truthforge`

Then add:

- `orchestrator-hardening`
- `deterministic-execution-lane`

## Example prompt to your agent

```text
Use `map-the-system` first, then `runtime-proof` on my implementation claim.
Return both reports in each skill's handoff format.
If runtime-visible claims are under-proven, escalate through `truthforge`.
```

## Local adaptation guidance

- keep core skills unchanged
- add local adapter notes in your repo for tools, environments, and tracker nouns
- preserve deterministic output contracts so reports stay comparable over time

## Common adoption mistakes

- importing too many skills at once
- skipping handoff formats and using freeform summaries
- accepting confidence claims without evidence classes
- treating governance skills as optional on high-risk changes
