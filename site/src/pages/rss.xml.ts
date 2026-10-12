import type { APIRoute } from "astro";
import { loadCatalog } from "../lib/content";

export const GET: APIRoute = () => {
  const catalog = loadCatalog();
  const site = "https://clankerkit.netlify.app";
  const items = catalog.skills
    .map(
      (skill) => `<item>
        <title>${escapeXml(skill.name)}</title>
        <link>${site}/skills/${skill.name}</link>
        <guid>${site}/skills/${skill.name}</guid>
        <description>${escapeXml(skill.description)}</description>
        <category>${escapeXml(skill.category)}</category>
      </item>`,
    )
    .join("");
  const xml = `<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>ClankerKit skills</title>
    <link>${site}</link>
    <description>Agent skills that ship with receipts.</description>
    ${items}
  </channel>
</rss>`;
  return new Response(xml, {
    headers: { "Content-Type": "application/rss+xml; charset=utf-8" },
  });
};

function escapeXml(value: string): string {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}
