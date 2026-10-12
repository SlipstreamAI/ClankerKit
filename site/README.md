# ClankerKit site

Static marketplace generated from `skills/*/SKILL.md` and `catalog.json`.

```bash
python scripts/build_skill_catalog.py
cd site
npm ci
npm run build
npm run preview
```

The build is Astro, Tailwind, and Pagefind. `npm run build` writes `site/dist`, including the Pagefind index.

## Netlify

`netlify.toml` at the repository root is the deploy config. Publish directory is `site/dist`. Netlify sets `URL` during the build, and Astro uses it for canonical links.

This site is not configured for GitHub Pages.
