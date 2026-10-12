# ClankerKit Skills Index

Generated from `skills/*/SKILL.md`. Do not edit by hand.
Run `python scripts/build_skill_catalog.py` after skill changes.

## debugging

- [`ci-failure-triage`](../skills/ci-failure-triage/SKILL.md) (experimental)
  Use when a pull request or main branch check is red and the log is the evidence you have.

- [`fix-flaky-test`](../skills/fix-flaky-test/SKILL.md) (experimental)
  Use when a test fails intermittently and quarantine or a rerun is being treated as the fix.

- [`trace-the-failure`](../skills/trace-the-failure/SKILL.md) (provisional)
  Use when a bug, red test, or incident needs a deterministic repro before any fix.

## delivery

- [`dependency-upgrade`](../skills/dependency-upgrade/SKILL.md) (experimental)
  Use when upgrading a direct dependency, especially across a major version, and you need a rollback path.

- [`deterministic-execution-lane`](../skills/deterministic-execution-lane/SKILL.md) (provisional)
  Use when a multi-step change must continue until done or blocked, without silent skips.

- [`dockerize-and-deploy`](../skills/dockerize-and-deploy/SKILL.md) (experimental)
  Use when adding a Dockerfile or shipping an image and you need build, run, and rollback evidence.

- [`mcp-server-builder`](../skills/mcp-server-builder/SKILL.md) (experimental)
  Use when adding an MCP tool, resource, or prompt and you need a schema plus a real invocation receipt.

- [`merge-train-governor`](../skills/merge-train-governor/SKILL.md) (provisional)
  Use when several changes are competing to merge and promotion order must be explicit.

- [`refactor-safely`](../skills/refactor-safely/SKILL.md) (experimental)
  Use when renaming, splitting, or moving code and the behavior must stay the same.

- [`safe-pr-prep`](../skills/safe-pr-prep/SKILL.md) (provisional)
  Use when opening or updating a PR and the diff needs a claim-to-evidence handoff.

- [`tdd-loop`](../skills/tdd-loop/SKILL.md) (experimental)
  Use when implementing a behavior and you want the test to fail for the right reason before production code changes.

## documentation

- [`docs-from-code`](../skills/docs-from-code/SKILL.md) (experimental)
  Use when docs drift from flags, routes, or setup steps, or when a change needs docs that were verified by running them.

- [`incident-postmortem`](../skills/incident-postmortem/SKILL.md) (experimental)
  Use when an incident is over or stable and the team needs a record that separates evidence from guesswork.

- [`operator-handoff`](../skills/operator-handoff/SKILL.md) (provisional)
  Use when work is pausing, swapping owners, or leaving a session that held the only copy of the plan.

- [`release-notes-and-changelog`](../skills/release-notes-and-changelog/SKILL.md) (experimental)
  Use when cutting a release or updating a changelog and the notes must match the history.

- [`skill-creator`](../skills/skill-creator/SKILL.md) (experimental)
  Use when creating or reshaping a SKILL.md, including its frontmatter trigger, metadata, and handoff.

## governance

- [`code-review`](../skills/code-review/SKILL.md) (experimental)
  Use when a human or agent asks for a code review before merge and wants defects, risks, and missing tests rather than a style rewrite.

- [`escalation-and-blockers`](../skills/escalation-and-blockers/SKILL.md) (provisional)
  Use when an agent must decide whether to continue, stop, or hand the work to a human.

- [`gate-and-done`](../skills/gate-and-done/SKILL.md) (provisional)
  Use when a change is called ready and reviewers need one pass or fail contract instead of separate evidence, gate, and done checks.

- [`orchestrator-hardening`](../skills/orchestrator-hardening/SKILL.md) (provisional)
  Use when an agent session needs capability routing, continuation rules, or a missing control loop in AGENTS.md.

- [`skill-intake-gate`](../skills/skill-intake-gate/SKILL.md) (provisional)
  Use when reviewing a new or changed SKILL.md, helper script, or skill proposed for this catalog.

- [`skill-security-scan`](../skills/skill-security-scan/SKILL.md) (experimental)
  Use when adding a skill from outside this catalog, or when skill-intake-gate needs a file-level safety pass.

- [`truth-recovery-program`](../skills/truth-recovery-program/SKILL.md) (provisional)
  Use when history, open work, or prior merges can no longer be trusted at face value.

- [`truthforge`](../skills/truthforge/SKILL.md) (provisional)
  Use when a PR, incident, or agent says a runtime-visible change works or is done and the evidence may be mocked, shallow, or incomplete.

## hardening

- [`db-migration-safety`](../skills/db-migration-safety/SKILL.md) (experimental)
  Use when a pull request adds SQL or a migration framework change that alters tables, indexes, or backfills.

- [`observability-add`](../skills/observability-add/SKILL.md) (experimental)
  Use when a feature is shipping and operators could not tell whether it worked or failed.

- [`production-readiness-pass`](../skills/production-readiness-pass/SKILL.md) (provisional)
  Use when a change is headed to production and operational failure modes are still unproven.

- [`prompt-injection-hardening`](../skills/prompt-injection-hardening/SKILL.md) (experimental)
  Use when building or reviewing retrieval, email, ticket, or web content that a model will read.

- [`secrets-and-config-audit`](../skills/secrets-and-config-audit/SKILL.md) (experimental)
  Use when reviewing how an app is configured, before deploy, or after a secret may have landed in a file.

- [`security-review`](../skills/security-review/SKILL.md) (experimental)
  Use when a change touches auth, user input, queries, shell, files, deserialization, or dependencies and needs severity-ranked findings.

## repo-understanding

- [`blast-radius-scan`](../skills/blast-radius-scan/SKILL.md) (provisional)
  Use when a diff looks small but shared types, config, or data paths may spread the effect.

- [`find-the-real-entrypoints`](../skills/find-the-real-entrypoints/SKILL.md) (provisional)
  Use when you need the path a real user, job, or caller hits before changing behavior.

- [`legacy-code-archaeology`](../skills/legacy-code-archaeology/SKILL.md) (experimental)
  Use when you must change old code and the reason it exists is not in the current comments.

- [`map-the-system`](../skills/map-the-system/SKILL.md) (provisional)
  Use when the repo is unfamiliar or a change could cross service, package, or runtime boundaries.

- [`onboard-to-repo`](../skills/onboard-to-repo/SKILL.md) (experimental)
  Use when an agent or human is new to a repo and needs a map before editing.

## validation

- [`accessibility-audit`](../skills/accessibility-audit/SKILL.md) (experimental)
  Use when a screen changes and someone needs a WCAG-oriented pass that says what was actually exercised.

- [`agent-eval-harness`](../skills/agent-eval-harness/SKILL.md) (experimental)
  Use when an agent prompt, tool, or model change needs a repeatable pass rate instead of a single impressive example.

- [`api-contract-check`](../skills/api-contract-check/SKILL.md) (experimental)
  Use when a pull request changes request or response shapes, status codes, OpenAPI, protobuf, or shared types.

- [`evidence-research-flywheel`](../skills/evidence-research-flywheel/SKILL.md) (provisional)
  Use when gathering repo or external evidence and handing off a bounded plan without dropping provenance.

- [`frontend-ui-verify`](../skills/frontend-ui-verify/SKILL.md) (experimental)
  Use when a pull request claims a screen, component, or interaction changed and unit tests are the only proof.

- [`performance-profile`](../skills/performance-profile/SKILL.md) (experimental)
  Use when someone wants a speed or cost improvement and the only evidence so far is a feeling or a single anecdote.

- [`runtime-proof`](../skills/runtime-proof/SKILL.md) (provisional)
  Use when a fix, feature, or deploy claim depends on real execution and a green suite is the only receipt offered.

- [`test-surface-skeptic`](../skills/test-surface-skeptic/SKILL.md) (provisional)
  Use when coverage looks broad but the assertions may be mocks, snapshots, or tautologies.

- [`write-real-tests`](../skills/write-real-tests/SKILL.md) (experimental)
  Use when a change needs coverage that proves behavior, especially when existing tests only assert mocks, snapshots, or implementation details.
