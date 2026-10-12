---
name: secrets-and-config-audit
description: "Audits environment variables, config files, and committed secrets against 12-factor hygiene. Use when reviewing how an app is configured, before deploy, or after a secret may have landed in a file."
license: Apache-2.0
compatibility: "Claude Code, Cursor, Codex, Grok Build, and GitHub Copilot. Needs git and a search tool such as rg."
allowed-tools: Bash Read Grep
metadata:
  category: hardening
  status: experimental
  tags: "secrets, config, env, 12-factor"
  modes: "pre-merge, release-readiness"
  version: "0.1.0"
  author: SlipstreamAI
---

# Secrets and Config Audit

**Tagline:** Config comes from the environment. Secrets stay out of git.

## Purpose

Secrets and Config Audit checks that configuration is explicit, required values fail closed, and secrets are not sitting in tracked files. Example files show names, not live values.

## Use when

1. A service is being prepared to deploy.
2. A diff adds env vars, config files, or credential handling.
3. You suspect a secret was committed.

## Do not use when

- Rotating a credential in a live secret store. That is an operator action outside this skill.
- A general security review of request handling. Use security-review.

## Inputs

- Repo root.
- The list of environments, if known.
- A local scanner such as gitleaks, if installed. Otherwise the bundled scanner.

## Outputs

- Env vars the code reads.
- Tracked files that look like secrets.
- Fail-closed gaps: missing required config that silently defaults.
- Remediation that does not include the secret value.

Run [scan_config.py](scripts/scan_config.py) locally. It prints file paths and rule names, not a place to paste live tokens.

## Procedure

### Phase Inventory reads

1. Find where the process reads environment variables or config files.
2. Compare that list to example env files and deployment docs.
3. Note required keys that default to a development value.

### Phase Scan tracked files

1. Run `python scripts/scan_config.py --repo <root>` from this skill directory.
2. If gitleaks or a similar tool is already installed, run it too and include its result.
3. Do not copy secret values into the handoff. Cite the path and the rule.

### Phase Check fail-closed behavior

1. Required production config should fail startup when absent.
2. Example files should be clearly examples and should not contain live keys.
3. Ignore files that are gitignored only if they are not force-added. Check `git ls-files` for the path.

### Phase Remediate in the report

1. For a committed secret: remove it from the tree, say rotation is required, and do not print the value.
2. For a missing example key: add the name with a placeholder.
3. For a silent default: name the safer failure mode.

## Proof requirements

- The scanner command and a summary of hits or a clean result.
- Env keys are names only.
- Any committed secret is described by path and rule, never by value.

## Common failure patterns

- Pastes of tokens into the handoff, the PR, or a new doc.
- An example file that is a copy of production config.
- A default admin password presented as convenience.

## Adaptation notes

- Frontend builds: public config must be intended to be public. Everything else stays server-side.
- Monorepos: scan the package that deploys, and say which packages you skipped.

## Example invocation

```text
Use secrets-and-config-audit.

Repo: this checkout.
Focus: the new worker env vars.

Return key names, scanner hits, and fail-closed gaps.
```

## Handoff format

```text
Secrets and Config Audit Report

Status: success | partial | blocked | failed
Config keys read:
Example file gaps:
Scanner:
Hits (path and rule only):
Fail-closed gaps:
Remediation:
Not scanned:
```
