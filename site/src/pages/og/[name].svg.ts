import type { APIRoute } from "astro";
import { loadCatalog } from "../../lib/content";

export function getStaticPaths() {
  return loadCatalog().skills.map((skill) => ({ params: { name: skill.name } }));
}

export const GET: APIRoute = ({ params }) => {
  const name = params.name || "skill";
  const catalog = loadCatalog();
  const skill = catalog.skills.find((item) => item.name === name);
  const category = skill?.category || "skill";
  const status = skill?.status || "";
  const svg = `<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="#172432"/>
  <rect width="22" height="630" fill="#e6b400"/>
  <text x="72" y="150" fill="#e6b400" font-family="Arial, sans-serif" font-size="28" letter-spacing="4">${escapeXml(category.toUpperCase())}</text>
  <text x="72" y="280" fill="#f7fafc" font-family="Arial, sans-serif" font-size="72">${escapeXml(name)}</text>
  <text x="72" y="360" fill="#c5d0db" font-family="Arial, sans-serif" font-size="32">${escapeXml(status)} · ClankerKit</text>
</svg>`;
  return new Response(svg, { headers: { "Content-Type": "image/svg+xml; charset=utf-8" } });
};

function escapeXml(value: string): string {
  return value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");
}
