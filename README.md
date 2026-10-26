# Firemark website (v2)

The website for Firemark: websites and Google listings for independent businesses in The Colony, Texas.
Version 2 is a rebuild from scratch. Version 1 stays in `Documents\Firemark` for comparison.

Start with **PICKUP.md**. It has where things stand, the before-launch list and how to publish.

## What's where

| Folder or file | What it is |
|---|---|
| `docs/` | **The website itself.** Everything GitHub Pages publishes. Open `docs/index.html` to see it. |
| `docs/css/site.css` | All the styles. Edit this file directly. |
| `docs/js/site.js` | The phone menu, the homepage map animation and the free check form. Edit directly. |
| `docs/images/brand/` | Logo files (SVG): full logo, symbol, one-color versions, and the "Site by Firemark" badge. |
| `src/` | The page sources. **Edit these, not the `.html` files in `docs/`,** then run the build. |
| `src/index.html` | The homepage. |
| `src/pages.py` | Work, About, Contact, Privacy, the 404 page and the brand sheet. |
| `src/partials/` | Pieces shared by several pages: the icon set and the free check form. |
| `tools/build.py` | Rebuilds every page in `docs/` from `src/`. |
| `tools/` (other) | Optional helpers: icon and share-image maker, accessibility checker, screenshot tool. |
| `design-system/firemark/MASTER.md` | The design rules: colors, type, spacing, components, checklist. |
| `directions/` | The three design directions from the Oct 26 direction check (C was chosen). |
| `free-check/TEMPLATE.md` | How to run a free check, and the report template to send. |
| `snippets/` | The "Site by Firemark" footer badge for client sites. |
| `BRIEF.md` | The original brief plus the v2 decisions (the decisions win where they differ). |
| `COPY.md`, `DECISIONS.md` | What the site says, and why it looks and works the way it does. |

## Preview it

Open `docs/index.html` in a browser, or in VS Code right-click it and choose **Open with Live Server**.
The 404 page only looks right on the real domain, because its links start with `/`.

## Change a page

1. Edit the text in `src/index.html` (homepage) or `src/pages.py` (other pages).
2. In a terminal in this folder, run `python tools/build.py` (on Windows, `py tools/build.py` also works).
3. Refresh the page in your browser. The build also turns straight quotes into curly ones and keeps short phrases like "Dallas–Fort Worth" from splitting across lines.

## Publish (when ready)

GitHub Pages serves the `docs` folder: repository **Settings > Pages > Deploy from a branch > main > /docs**.
Before you switch it on, go through the before-launch list in PICKUP.md.

## Optional tools

They need Node.js and Playwright (`npm i -D playwright axe-core`, then `npx playwright install chromium`):

- `node tools/make-assets.js` remakes the PNG icons and the link-preview image from the logo.
- `node tools/a11y-check.js http://localhost:8500` checks every page for accessibility problems (serve `docs/` first).
- `node tools/shot.js <url> out.png 390 844 full` takes a full-page screenshot.
