# Contributing to ClankerKit

Thanks for contributing. ClankerKit is a public skill library, so quality and safety gates are strict by design.

## Contribution principles

- keep skills repo-agnostic by default
- prefer operational clarity over broad abstraction
- require deterministic outputs and explicit stop boundaries
- encode proof expectations and failure patterns

## What can be contributed

- new skills under `skills/<category>/<skill-name>/SKILL.md`
- checks under `checks/`
- patterns under `patterns/`
- examples under `examples/`
- docs that improve consumption and authoring clarity

## Required shape for skill contributions

Every new skill must include:

- valid frontmatter
- purpose
- use when
- do not use when
- inputs
- outputs
- procedure
- proof requirements
- common failure patterns
- adaptation notes
- handoff format

Use [`templates/skill-template.md`](/C:/DEV2/ClankerKit/templates/skill-template.md).

## Required gates before merge

1. Skill policy gates pass in CI.
2. Catalog generation check passes.
3. PR template sections are complete.
4. CODEOWNERS review is approved for governance or validation changes.

## Unsafe content policy

Contributions will be rejected if they include:

- instructions to bypass auth or security controls
- exfiltration guidance
- destructive defaults without explicit guarded context
- language that claims proof without evidence requirements

## Pull request process

1. Fork and create a branch.
2. Keep scope bounded to one contribution theme.
3. Add or update examples when behavior changes.
4. Open PR and complete the template.
5. Address review feedback and re-run gates.

## Recommended repository protection

For maintainers, enable:

- required status checks (`Skill Gates`)
- required pull request reviews
- CODEOWNERS review enforcement
- no direct pushes to `main`

## Licensing

By contributing, you agree your contributions are licensed under Apache-2.0.
