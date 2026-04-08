# ClankerKit Super-Skills Port Plan

## Objective

Reduce skill sprawl by collapsing overlapping operational skills into a smaller set of repo-agnostic super skills with deterministic contracts.

## Super-skill set

1. `truth-recovery-program`
2. `deterministic-execution-lane`
3. `merge-train-governor`
4. `evidence-research-flywheel`

## Source-to-super mapping

## `truth-recovery-program`

Absorbs:

- `agentslipstreamai-inception-intent-drift-audit`
- `agentslipstreamai-merged-main-365d-scored-audit`
- `agentslipstreamai-workflow-hardening-audit`
- `truthforge`

## `deterministic-execution-lane`

Absorbs:

- `agentslipstreamai-harness-gold-standard`
- `until-done-execution-loop`
- `agentslipstreamai-shift-skill-mvp`

## `merge-train-governor`

Absorbs:

- `agentslipstreamai-implementation-merge-train-companion`
- `org-manager-sweep`
- `agentslipstreamai-stack-lifecycle-contract`

## `evidence-research-flywheel`

Absorbs:

- `agentslipstreamai-convergence-flywheel-orchestrator`
- `agentslipstreamai-research-squad`
- `agentslipstreamai-principal-research-dossier-mode`
- `agentslipstreamai-radical-innovative-addition`
- `agentslipstreamai-knowledge-compiler`
- `agentslipstreamai-youtube-transcript-intake`

## Parameterization requirements

Every super skill must externalize:

- tracker nouns (`issue`, `ticket`, `task`, `workpacket`)
- environment names (`local`, `staging`, `preview`, `prod-like`)
- runtime entrypoints (UI, API, CLI, job, worker)
- required evidence classes and thresholds
- branch and release policy rules
- validator and smoke command set

## Hardcoded assumptions to remove

- project-specific IDs, lane names, and issue numbers
- repo-specific paths unless defined as inputs
- product-domain language that does not generalize
- environment variables tied to one codebase

## Shared output contracts

All super skills should emit:

- deterministic status (`success`, `partial`, `blocked`, `failed`)
- explicit classification set (declared in each skill)
- evidence artifact paths
- unverified assumptions
- remediation now versus deferred
- owner and tracker link for deferred items

## Rollout sequence

1. Publish super skills in `provisional` state.
2. Run old and new skills in parallel on the same work for 2 to 3 cycles.
3. Compare output quality and remediation outcomes.
4. Mark old skills as deprecated aliases to super skills.
5. Remove duplicate behavior once parity is proven.

## Deprecation strategy

For each absorbed skill:

- keep a compatibility note with redirect target
- keep trigger aliases where practical
- stop extending legacy skill logic
- migrate examples and docs to super skill forms

## Success criteria

- fewer skills with broader reuse
- no loss of deterministic evidence quality
- lower operational confusion in skill selection
- higher cross-repo portability
