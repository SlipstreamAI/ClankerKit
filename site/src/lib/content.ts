import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { marked } from "marked";

const repoRoot = join(dirname(fileURLToPath(import.meta.url)), "../../..");

export type SkillRecord = {
  name: string;
  description: string;
  use_when: string;
  license: string;
  compatibility: string;
  allowed_tools: string[];
  category: string;
  status: string;
  tags: string[];
  modes: string[];
  path: string;
  files: string[];
  metadata: Record<string, string>;
};

export type BundleRecord = {
  name: string;
  title: string;
  description: string;
  version: string;
  category: string;
  skills: string[];
  path: string;
};

export type Catalog = {
  schema_version: number;
  skill_count: number;
  repository: string;
  skills: SkillRecord[];
  bundles: BundleRecord[];
};

export type SkillPage = SkillRecord & {
  raw: string;
  html: string;
};

export function loadCatalog(): Catalog {
  return JSON.parse(readFileSync(join(repoRoot, "catalog.json"), "utf8")) as Catalog;
}

export function loadSkill(name: string): SkillPage {
  const catalog = loadCatalog();
  const record = catalog.skills.find((skill) => skill.name === name);
  if (!record) {
    throw new Error(`Missing catalog record for ${name}`);
  }
  const raw = readFileSync(join(repoRoot, "skills", name, "SKILL.md"), "utf8");
  const body = raw.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, "");
  const html = marked.parse(body, { async: false }) as string;
  return { ...record, raw, html };
}

export function relatedSkills(skill: SkillRecord, limit = 4): SkillRecord[] {
  const catalog = loadCatalog();
  return catalog.skills
    .filter((item) => item.category === skill.category && item.name !== skill.name)
    .slice(0, limit);
}

export const repo = "SlipstreamAI/ClankerKit";

export function installCommands(name: string): Record<string, string> {
  return {
    npx: `npx skills add ${repo} --skill ${name}`,
    claude: `/plugin marketplace add ${repo}\n/plugin install full-catalog@clankerkit`,
    cursor: `npx skills add ${repo} --skill ${name} --agent cursor`,
    codex: `npx skills add ${repo} --skill ${name} --agent codex`,
    grok: `npx skills add ${repo} --skill ${name} --agent grok`,
    copilot: `npx skills add ${repo} --skill ${name} --agent github-copilot`,
  };
}
