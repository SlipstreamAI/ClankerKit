# ClankerKit

Skills for agents that ship real software, with receipts.

[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Skill Gates](https://github.com/SlipstreamAI/ClankerKit/actions/workflows/skill-gates.yml/badge.svg)](https://github.com/SlipstreamAI/ClankerKit/actions/workflows/skill-gates.yml)
[![skills](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FSlipstreamAI%2FClankerKit%2Fmain%2Fcatalog.json&query=%24.skill_count&label=skills)](catalog.json)
[![Agent Skills](https://img.shields.io/badge/spec-Agent%20Skills-1b2836)](https://agentskills.io/specification)
[![Site](https://img.shields.io/badge/site-Netlify-00AD9F)](site/README.md)

ClankerKit is an open catalog of agent skills for building, testing, securing, and proving software. A skill is a folder with a `SKILL.md` file: one job, an explicit trigger, and a handoff another person can audit. Claims need receipts.

## Install

```bash
npx skills add SlipstreamAI/ClankerKit --skill runtime-proof
```

```text
/plugin marketplace add SlipstreamAI/ClankerKit
/plugin install pr-safety@clankerkit
```

```bash
./scripts/install.sh runtime-proof --agent cursor
```

Per-agent paths, including Codex and Grok Build, are in [docs/install.md](docs/install.md). Bundles live in `bundles/`.

## Compatibility

Verified against public docs on 2026-10-12. Corrections are in [docs/research-corrections.md](docs/research-corrections.md).

| Agent | Install that we document | Where it loads project skills |
| --- | --- | --- |
| Claude Code | `/plugin marketplace add SlipstreamAI/ClankerKit` then `/plugin install <bundle>@clankerkit`, or `npx skills add` | `.claude/skills/` |
| Cursor | `npx skills add --agent cursor`, or `scripts/install.sh --agent cursor` | `.agents/skills/` and `.cursor/skills/` |
| Codex | `npx skills add --agent codex`, or copy into `.agents/skills/` | `.agents/skills/` (CLI global install uses `~/.codex/skills/`) |
| Grok Build | `npx skills add --agent grok` | `.grok/skills/` |
| GitHub Copilot | `npx skills add --agent github-copilot`, or copy into `.agents/skills/` | `.agents/skills/`, `.github/skills/`, or `.claude/skills/` |

This repo also symlinks [`.agents/skills`](.agents/skills) at the catalog so Codex, Cursor, and Copilot can discover the skills in a checkout. Installing a bundle into the repo you are actually changing is the better default. Forty-plus skills in one session crowd the prompt.

## Catalog

Generated from `skills/*/SKILL.md`. Do not edit the table by hand.

<!-- CATALOG:START -->
| Skill | Category | Status | Use when |
| --- | --- | --- | --- |
| [ci-failure-triage](skills/ci-failure-triage/SKILL.md) | debugging | experimental | a pull request or main branch check is red and the log is the evidence you have |
| [fix-flaky-test](skills/fix-flaky-test/SKILL.md) | debugging | experimental | a test fails intermittently and quarantine or a rerun is being treated as the fix |
| [trace-the-failure](skills/trace-the-failure/SKILL.md) | debugging | provisional | a bug, red test, or incident needs a deterministic repro before any fix |
| [dependency-upgrade](skills/dependency-upgrade/SKILL.md) | delivery | experimental | upgrading a direct dependency, especially across a major version, and you need a rollback path |
| [deterministic-execution-lane](skills/deterministic-execution-lane/SKILL.md) | delivery | provisional | a multi-step change must continue until done or blocked, without silent skips |
| [dockerize-and-deploy](skills/dockerize-and-deploy/SKILL.md) | delivery | experimental | adding a Dockerfile or shipping an image and you need build, run, and rollback evidence |
| [mcp-server-builder](skills/mcp-server-builder/SKILL.md) | delivery | experimental | adding an MCP tool, resource, or prompt and you need a schema plus a real invocation receipt |
| [merge-train-governor](skills/merge-train-governor/SKILL.md) | delivery | provisional | several changes are competing to merge and promotion order must be explicit |
| [refactor-safely](skills/refactor-safely/SKILL.md) | delivery | experimental | renaming, splitting, or moving code and the behavior must stay the same |
| [safe-pr-prep](skills/safe-pr-prep/SKILL.md) | delivery | provisional | opening or updating a PR and the diff needs a claim-to-evidence handoff |
| [tdd-loop](skills/tdd-loop/SKILL.md) | delivery | experimental | implementing a behavior and you want the test to fail for the right reason before production code changes |
| [docs-from-code](skills/docs-from-code/SKILL.md) | documentation | experimental | docs drift from flags, routes, or setup steps, or when a change needs docs that were verified by running them |
| [incident-postmortem](skills/incident-postmortem/SKILL.md) | documentation | experimental | an incident is over or stable and the team needs a record that separates evidence from guesswork |
| [operator-handoff](skills/operator-handoff/SKILL.md) | documentation | provisional | work is pausing, swapping owners, or leaving a session that held the only copy of the plan |
| [release-notes-and-changelog](skills/release-notes-and-changelog/SKILL.md) | documentation | experimental | cutting a release or updating a changelog and the notes must match the history |
| [skill-creator](skills/skill-creator/SKILL.md) | documentation | experimental | creating or reshaping a SKILL.md, including its frontmatter trigger, metadata, and handoff |
| [code-review](skills/code-review/SKILL.md) | governance | experimental | a human or agent asks for a code review before merge and wants defects, risks, and missing tests rather than a style rewrite |
| [escalation-and-blockers](skills/escalation-and-blockers/SKILL.md) | governance | provisional | an agent must decide whether to continue, stop, or hand the work to a human |
| [gate-and-done](skills/gate-and-done/SKILL.md) | governance | provisional | a change is called ready and reviewers need one pass or fail contract instead of separate evidence, gate, and done checks |
| [orchestrator-hardening](skills/orchestrator-hardening/SKILL.md) | governance | provisional | an agent session needs capability routing, continuation rules, or a missing control loop in AGENTS.md |
| [skill-intake-gate](skills/skill-intake-gate/SKILL.md) | governance | provisional | reviewing a new or changed SKILL.md, helper script, or skill proposed for this catalog |
| [skill-security-scan](skills/skill-security-scan/SKILL.md) | governance | experimental | adding a skill from outside this catalog, or when skill-intake-gate needs a file-level safety pass |
| [truth-recovery-program](skills/truth-recovery-program/SKILL.md) | governance | provisional | history, open work, or prior merges can no longer be trusted at face value |
| [truthforge](skills/truthforge/SKILL.md) | governance | provisional | a PR, incident, or agent says a runtime-visible change works or is done and the evidence may be mocked, shallow, or incomplete |
| [db-migration-safety](skills/db-migration-safety/SKILL.md) | hardening | experimental | a pull request adds SQL or a migration framework change that alters tables, indexes, or backfills |
| [observability-add](skills/observability-add/SKILL.md) | hardening | experimental | a feature is shipping and operators could not tell whether it worked or failed |
| [production-readiness-pass](skills/production-readiness-pass/SKILL.md) | hardening | provisional | a change is headed to production and operational failure modes are still unproven |
| [prompt-injection-hardening](skills/prompt-injection-hardening/SKILL.md) | hardening | experimental | building or reviewing retrieval, email, ticket, or web content that a model will read |
| [secrets-and-config-audit](skills/secrets-and-config-audit/SKILL.md) | hardening | experimental | reviewing how an app is configured, before deploy, or after a secret may have landed in a file |
| [security-review](skills/security-review/SKILL.md) | hardening | experimental | a change touches auth, user input, queries, shell, files, deserialization, or dependencies and needs severity-ranked findings |
| [blast-radius-scan](skills/blast-radius-scan/SKILL.md) | repo-understanding | provisional | a diff looks small but shared types, config, or data paths may spread the effect |
| [find-the-real-entrypoints](skills/find-the-real-entrypoints/SKILL.md) | repo-understanding | provisional | you need the path a real user, job, or caller hits before changing behavior |
| [legacy-code-archaeology](skills/legacy-code-archaeology/SKILL.md) | repo-understanding | experimental | you must change old code and the reason it exists is not in the current comments |
| [map-the-system](skills/map-the-system/SKILL.md) | repo-understanding | provisional | the repo is unfamiliar or a change could cross service, package, or runtime boundaries |
| [onboard-to-repo](skills/onboard-to-repo/SKILL.md) | repo-understanding | experimental | an agent or human is new to a repo and needs a map before editing |
| [accessibility-audit](skills/accessibility-audit/SKILL.md) | validation | experimental | a screen changes and someone needs a WCAG-oriented pass that says what was actually exercised |
| [agent-eval-harness](skills/agent-eval-harness/SKILL.md) | validation | experimental | an agent prompt, tool, or model change needs a repeatable pass rate instead of a single impressive example |
| [api-contract-check](skills/api-contract-check/SKILL.md) | validation | experimental | a pull request changes request or response shapes, status codes, OpenAPI, protobuf, or shared types |
| [evidence-research-flywheel](skills/evidence-research-flywheel/SKILL.md) | validation | provisional | gathering repo or external evidence and handing off a bounded plan without dropping provenance |
| [frontend-ui-verify](skills/frontend-ui-verify/SKILL.md) | validation | experimental | a pull request claims a screen, component, or interaction changed and unit tests are the only proof |
| [performance-profile](skills/performance-profile/SKILL.md) | validation | experimental | someone wants a speed or cost improvement and the only evidence so far is a feeling or a single anecdote |
| [runtime-proof](skills/runtime-proof/SKILL.md) | validation | provisional | a fix, feature, or deploy claim depends on real execution and a green suite is the only receipt offered |
| [test-surface-skeptic](skills/test-surface-skeptic/SKILL.md) | validation | provisional | coverage looks broad but the assertions may be mocks, snapshots, or tautologies |
| [write-real-tests](skills/write-real-tests/SKILL.md) | validation | experimental | a change needs coverage that proves behavior, especially when existing tests only assert mocks, snapshots, or implementation details |
<!-- CATALOG:END -->

## Bundles

| Bundle | Install | What it is for |
| --- | --- | --- |
| `pr-safety` | `/plugin install pr-safety@clankerkit` | Review a PR with gates, proof, and findings |
| `incident` | `/plugin install incident@clankerkit` | Trace a failure and write the handoff |
| `new-repo-onboarding` | `/plugin install new-repo-onboarding@clankerkit` | First hour in an unfamiliar repo |
| `testing` | `/plugin install testing@clankerkit` | Behavior tests, flakes, and UI proof |
| `security` | `/plugin install security@clankerkit` | Diff, config, prompt, and skill review |
| `ship` | `/plugin install ship@clankerkit` | Upgrades, migrations, containers, notes |
| `full-catalog` | `/plugin install full-catalog@clankerkit` | Every skill |

## Design principles

- Claims need receipts.
- Real proof beats a green harness that replaced the boundary.
- Deterministic beats vibes.
- Repo understanding comes before broad edits.
- Skills stay inspectable, composable, and safe to run in more than one repository.

The longer note on why this exists is in [docs/philosophy.md](docs/philosophy.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). New skills start as `experimental`. Validation is `python scripts/validate_skills.py`.

## License

Apache-2.0. See [LICENSE](LICENSE).
