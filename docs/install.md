# Install ClankerKit skills

Skills are folders. Copy the folder, or let the skills CLI copy it. Do not pipe a remote script into a shell.

Replace `<name>` with a skill directory name, such as `runtime-proof`. Replace `<bundle>` with a name from `bundles/`.

## Claude Code

Marketplace (one plugin per bundle). The marketplace name is `clankerkit`.

```text
/plugin marketplace add SlipstreamAI/ClankerKit
/plugin install pr-safety@clankerkit
```

Each plugin's `source` is the repo root, and its `skills` list names only that bundle's directories. That is the current Claude Code pattern for several plugins sharing one `skills/` tree.

A single skill, without a bundle:

```bash
npx skills add SlipstreamAI/ClankerKit --skill runtime-proof --agent claude-code
```

Project path: `.claude/skills/<name>/`. User path: `~/.claude/skills/<name>/`.

## Cursor

The skills CLI installs Cursor project skills into `.agents/skills/` and global skills into `~/.cursor/skills/`.

```bash
npx skills add SlipstreamAI/ClankerKit --skill runtime-proof --agent cursor
```

Cursor itself also loads `.cursor/skills/` and, for compatibility, `.claude/skills/` and `.codex/skills/`. Manual copy:

```bash
./scripts/install.sh runtime-proof --agent cursor
```

That script uses `.cursor/skills/` so the skill is obvious in the Cursor project tree. Either path works.

## Codex

Official Codex discovery for a repository is `.agents/skills/` from the current directory up to the repo root. User skills are read from `~/.agents/skills/` as well. The skills CLI's global Codex path is `~/.codex/skills/`.

```bash
npx skills add SlipstreamAI/ClankerKit --skill runtime-proof --agent codex
./scripts/install.sh runtime-proof --agent codex
```

Optional UI metadata can live at `agents/openai.yaml` inside a skill. ClankerKit skills do not require it.

## Grok Build

The skills CLI agent id is `grok` (labeled Grok Build), not a separate product path named "Grok Bot".

```bash
npx skills add SlipstreamAI/ClankerKit --skill runtime-proof --agent grok
./scripts/install.sh runtime-proof --agent grok
```

Project path: `.grok/skills/<name>/`. User path: `~/.grok/skills/<name>/`.

Any agent that can read a URL can also start from `catalog.json` and the raw `SKILL.md`. `AGENTS.md` explains how to pick one skill and return its handoff.

## GitHub Copilot

Copilot project skills load from `.github/skills/`, `.claude/skills/`, or `.agents/skills/`. The skills CLI agent id is `github-copilot`.

```bash
npx skills add SlipstreamAI/ClankerKit --skill runtime-proof --agent github-copilot
./scripts/install.sh runtime-proof --agent copilot
```

`scripts/install.sh --agent copilot` copies into `.github/skills/`.

## Check the CLI without installing

```bash
npx skills add SlipstreamAI/ClankerKit --list
```

A local smoke test from a throwaway directory:

```bash
tmpdir=$(mktemp -d)
cd "$tmpdir"
npx skills add /path/to/ClankerKit --skill runtime-proof --agent claude-code --yes
test -f .claude/skills/runtime-proof/SKILL.md
```
