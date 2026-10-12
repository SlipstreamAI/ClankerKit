# Research corrections

Checked 2026-10-12 against the public pages named in the upgrade plan. The upgrade follows the plan except where these notes disagree.

## What held up

- Agent Skills frontmatter is `name`, `description`, `license`, `compatibility`, `metadata` (string map), and `allowed-tools` as a space-separated string. `name` must match the directory. Descriptions should say what the skill does and when to use it. Source: [agentskills.io/specification](https://agentskills.io/specification).
- `npx skills add <repo> --skill <name>` is the skills CLI (vercel-labs/skills). It discovers `skills/<name>/SKILL.md`.
- Claude Code marketplaces use `.claude-plugin/marketplace.json` with `name`, `owner`, and `plugins[]`. Several plugins can share `source: "./"` when each entry lists its own skill directories. Install shape `/plugin marketplace add owner/repo` and `/plugin install <plugin>@<marketplace>` matches the docs.
- Cursor loads `.agents/skills/`, `.cursor/skills/`, and the Claude and Codex compatibility dirs. Source: [cursor.com/docs/skills](https://cursor.com/docs/skills).
- SkillsMP's Claude skills page featured `frontend-design`, `skill-creator`, `brainstorming`, and `vercel-react-best-practices` on the day of the check, along with other skills. Source: [skillsmp.com/claude-skills](https://skillsmp.com/claude-skills).
- Smithery and mcp.so are MCP directories. The plan used them as a comparison for browsable directories, not as skill catalogs. That comparison is fair.

## What the plan got wrong or stale

- Nested `skills/<category>/<name>/SKILL.md` is discoverable by the current skills CLI, which walks skill containers three levels deep, and by Cursor, which walks recursively. Flat `skills/<name>/` is still the layout this repo uses, because it is the common denominator and it matches the spec's "directory name equals `name`" rule without a category prefix. The plan was right to flatten, and too strong if read as "nesting cannot be installed".
- Codex does not only read `~/.codex/skills/`. The Codex docs scan `.agents/skills` in the repo and `$HOME/.agents/skills`. `~/.codex/skills/` is the skills CLI global install path for `--agent codex`. `agents/openai.yaml` remains optional UI metadata.
- Cursor's skills CLI project path is `.agents/skills/`, not `.cursor/skills/`. Both directories work when Cursor loads the project. `scripts/install.sh --agent cursor` copies to `.cursor/skills/` on purpose.
- There is no skills CLI target named "Grok Bot". The target is `grok`, labeled Grok Build, with `.grok/skills/` and `~/.grok/skills/`. Docs in this repo use that name.
- GitHub Copilot does load Agent Skills. Project dirs include `.github/skills/`, `.claude/skills/`, and `.agents/skills/`. The compatibility matrix includes Copilot for that reason.
- `brainstorming` on SkillsMP is from `obra/superpowers`, not from `anthropics/skills`. The React skill featured there is `vercel-react-best-practices`.
- cursor.directory is a live plugin and rules directory, not a skills-only gallery.
- The marketplace site is configured for Netlify (`netlify.toml`), not GitHub Pages. That follows the owner request over the plan's hosting default.

## Not claimed

This pass did not submit the catalog to SkillsMP, cursor.directory, or an awesome-list. Those are launch tasks, not part of the repo upgrade.
