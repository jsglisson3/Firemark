# Pick up here (Firemark v2)

Last updated Oct 27, 2026, after the overnight redesign (v10).

## Where things stand

v10 is a full redesign of the v9 site, built and checked, still a hidden **draft**. What changed and why: `FIREMARK-REDESIGN-PLAN.md`. What Jeremy needs to approve: `REVIEW-v10.md`.

Everything is in `docs/`:
- the homepage: the map tile inside the headline, the map that types a search and drops the pin (with "Try it with your trade"), a sample free check report, Recent work, Get found. Stay found. (what you get, "let's talk"), One person, start to finish., and the closing form
- Work, About (with a short "Why Firemark"), the free check page with the FAQ, Privacy, 404, thanks and the brand sheet

Checks on the v10 build:
- Accessibility scan (axe): 0 issues on all eight pages at phone and desktop widths, with the phone menu open, and with reduced motion on.
- Lighthouse on a phone: homepage performance 97, accessibility 100, best practices 100. SEO is held down on purpose by the draft noindex tag.
- HTML valid. No sideways scrolling at any width.

**No more [PLACEHOLDER] or [CONFIRM] tags on the page.** Contact details live in one settings block at the top of `tools/build.py` (`EMAIL`, `PHONE`, `BOOKING_URL`, `HEADSHOT`, `WEB3FORMS_KEY`, `FALLBACK_EMAIL`). Anything empty is left off the site. The build stops with an error if a `[PLACEHOLDER` or `[CONFIRM` tag would reach a page.

**To continue in a new chat:** attach or paste this file plus `BRIEF.md`, `DECISIONS.md` and `REVIEW-v10.md`, and say what you want to do next.

## Add a site to Work

Work and the homepage's "Recent work" are a plain list: one card per site with a screenshot, the name, one short line and a link. No write-up per site. The list lives in one file, `src/sites.py`.

1. Open `src/sites.py`. Copy one block, from `{` down to `},`, and paste it at the top of the list so the newest site comes first.
2. Change the words: `name`, `about` (one line: what kind of business, and where), `link` (the full address), `image` (a short lowercase name, like `bakery`) and `tag` (leave it `""`, or use "Volunteer concept, not the official site" for a concept).
3. Send Claude the site's link. Claude takes the screenshot, saves it as `docs/images/work/<image>-desktop-640.webp` and `-960.webp`, runs the build and hands back a drop-in (or pushes it).

The homepage shows the first 4 sites and links to Work for the rest. Ask the business before you list their site.

## Settled Oct 26 and 27

- Domain: **firemarktech.com**.
- The free check report arrives **within 7 days**. A reply to any message comes **within 5 days**. Most starter websites go live **about 45 days after the go-ahead** (changed from 30 on Oct 26). Those three numbers are the only promises the site makes; they appear in the hero, the closing card, the form, the footer, the contact page and the thanks page.
- About page: keep the career facts, but general (no team size, dollar figures or project counts).
- Headline stays "Put your business on the map." The submit button says "Get my free check" everywhere.
- Footer: Stone (light), keeps the Dallas–Fort Worth line, no oversized wordmark.
- Closing section: a photo of Jeremy next to the form. Until there is a headshot, a stone tile with the flame pin stands in (set `HEADSHOT = True` in `tools/build.py` when the photo is in).
- Form service: Web3Forms (see Set up).
- The reasons behind the header, hero, closing CTA and footer are in `design-research.md` at the root of this folder.

## Before launch

Work through `REVIEW-v10.md`. In short: approve the handful of promises it lists, fill in the settings block in `tools/build.py` as each thing exists (email, Web3Forms key, phone and booking link if wanted, headshot), and ask the Friends of the Library about showing their program photos (blanked out for now).

- [ ] Work links: the two live-site links go to jsglisson3.github.io, which shows your last name in the address. Fine for now; switch them to the clients' own domains once those exist.

### Set up
- [x] **Buy the domain.** Bought 2026-10-26 at Cloudflare Registrar and connected to GitHub Pages the same day: https://firemarktech.com (and www) serve the site over HTTPS, still as a hidden draft. See **Domain** under Notes.
- [ ] **Email at the domain** (for example Google Workspace or Microsoft 365).
- [ ] **Form service: Web3Forms** (chosen Oct 27). Sign up at web3forms.com with the address the form should deliver to (the free plan is enough). Paste the access key it gives you into `WEB3FORMS_KEY` at the top of `tools/build.py`. Rebuild (ask Claude), then send yourself a test from the live site and check it arrives. Until the key is in, the form falls back to opening a pre-filled email, so nothing is broken meanwhile. Browsers with JavaScript off are sent to `thanks.html` after submitting; everyone else sees the thanks line in place.
- [ ] **Trademark check.** Search "Firemark" at the USPTO (tmsearch.uspto.gov) before you print cards or signs.
- [ ] **Firemark's own Google Business Profile** as a service-area business (it can hide your home address). You'll be doing this for clients, so it's good practice.

### Launch day
The domain is already connected, so launch is just switching the draft off.
1. In `tools/build.py`, set `LAUNCHED = True`, then run `python tools/build.py`. That removes the draft banners and the noindex tags. The brand sheet and the 404 page stay hidden from search. (Your PC has no Python, so ask Claude to run the build.)
2. Commit and sync in VS Code. Don't delete `docs/CNAME`; it holds the domain.
3. After launch: add the site to Google Search Console, submit `sitemap.xml`, send yourself a test free check, and run Lighthouse on your phone.

## Notes

- **Domain:** firemarktech.com is registered at Cloudflare. Its DNS has four A records for @ (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153) and a CNAME for www to jsglisson3.github.io, all set to DNS only (grey cloud). Leave them grey: the orange proxy gets in the way of GitHub's certificate. GitHub Pages has the custom domain set (that's what `docs/CNAME` is) and Enforce HTTPS on. The old jsglisson3.github.io/Firemark/ address redirects to the domain. `SITE_ROOT` in `tools/build.py` is "/" to match.
- **Edit `src/`, not `docs/*.html`.** The build overwrites the pages in `docs/`. CSS (`docs/css/site.css`) and the script (`docs/js/site.js`) are edited directly. They are linked as `?v=12`; bump `VERSION` in `tools/build.py` whenever either file changes, so returning visitors get the new version.
- **v10 (Oct 27, overnight):** full redesign. See `FIREMARK-REDESIGN-PLAN.md`.
- **v11 and v12 (Oct 27):** homepage top rebuilt around the real map of The Colony. See the end of `DECISIONS.md`.
- **v9 (Oct 27):** the header (phone sheet menu that ends with the button, email, phone and place), the hero promises under the buttons, the Stone closing card (three steps, photo, form) that Work and About reuse in a short form, and the Stone footer. Reasons and the research behind them: `design-research.md`.
- **v1** is still in `Documents\Firemark`. Nothing in v2 depends on it.
- **Logo files on Windows:** SVGs copied to your computer through the Claude app may get a small `<metadata>` block (content credentials) added at the top. It's harmless, and browsers ignore it.
- **Design skills:** copies of Frontend Design and UI UX Pro Max belong in `.claude/skills/` inside this folder, so any session with it open gets them without a reinstall. The Claude app can't write into `.claude` folders from a cloud session, so they came as a zip (`firemark-v2-claude-skills.zip`): extract it into `Documents\Firemark-v2` and check that `.claude\skills\ui-ux-pro-max\SKILL.md` exists. See `.claude/skills/README.md` afterwards. The design rules they produced are in `design-system/firemark/MASTER.md`.
- **Free checks:** `free-check/TEMPLATE.md` has the 20-minute routine and the report template.
- **Client footers:** `snippets/site-by-firemark.html` has the small "Site by Firemark" badge. Always ask the client first.
