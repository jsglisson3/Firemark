# Pick up here (Firemark v2)

Last updated Oct 27, 2026, after the header, hero, closing CTA and footer build (v9).

## Where things stand

The v2 site is built and checked. Everything is in `docs/`:
- the homepage, with the map animation
- Work (a simple list of sites, one card each), About and the free check page
- Privacy, the 404 page, a thanks page the form lands on when JavaScript is off (`thanks.html`) and a brand sheet (`brand.html`, not linked from the site). Those last three are hidden from search.
- the icons, the link-preview image, the sitemap and robots.txt

Checks on the latest build:
- The HTML is valid.
- The accessibility scan finds 0 issues on every page, at phone and desktop widths, with the phone menu open too (v9, Oct 27).
- Keyboard: every control has a visible focus ring, the phone menu closes on Escape and hands focus back, and links to parts of a page land below the sticky header.
- No sideways scrolling at any width from 320 to 1440 pixels (v9), 1920 on v8.
- Lighthouse on a phone (v8): performance 99–100, accessibility 100, best practices 100. SEO is 100 once the draft noindex tag comes off. Run it again on v9 once it is live.

It is still a **draft**. Every page carries a yellow draft banner and a noindex tag, so search engines skip it. Contact details are placeholders.

**To continue in a new chat:** attach or paste this file plus `BRIEF.md` and `DECISIONS.md`, and say what you want to do next. If you make a Claude project for Firemark, keep it lean: those three files are enough.

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
- Closing section: a photo of Jeremy next to the form (a marked placeholder until there is a headshot).
- Form service: Web3Forms (see Set up).
- The reasons behind the header, hero, closing CTA and footer are in `design-research.md` at the root of this folder.

## Before launch

### Approve or edit these promises (yellow [CONFIRM] tags)
- [ ] Home, How it works: "You get a clear price before anything starts."
- [ ] Home, What it costs: "the price comes after the free check, in writing, before anything starts."
- [ ] Home, Stay found: what the monthly plan includes ("New hours, a new photo, a menu change. Send a note and it's handled.").
- [ ] Home, What it costs: "Domain and email accounts are billed by those providers at their regular prices."
- [ ] Contact FAQ, Who owns the website: "You do. Your domain is registered in your name, and your content is yours to keep. Once your site is live, Firemark may show it as an example of recent work." (About repeats the ownership part.) Put the same portfolio line in your written quote or agreement.
- [ ] Privacy: "Your details aren't sold, and you won't be added to a mailing list."
- [x] Work: permission from GLP and from the Friends of The Colony Public Library to show their sites (given Oct 26).
- [ ] Work: ask the Friends specifically about the library program photos in the screenshots, some of which show children.

### Fill in these blanks (yellow [PLACEHOLDER] tags)
- [ ] Email address: placeholder hello@firemarktech.com. Set it up at your domain, then put it in `data-fallback-email` in `src/partials/form.html`, and replace the [PLACEHOLDER: email] tags in the phone menu, the closing section and the footer (`src/index.html`), on the contact page (`src/pages.py`) and in the homepage's structured data. Search both files for PLACEHOLDER.
- [ ] Phone number: phone menu, closing section, footer, contact page and structured data (same search).
- [ ] Booking link for "Book a 15-minute call" (Calendly, Cal.com or Google Calendar booking pages all work). Put the address in the `href` of the two links marked `data-booking-link`.
- [ ] Photo: `docs/images/jeremy.webp` is a marked placeholder (a gray circle that says so). Replace that one file with a square headshot, at least 448 pixels on each side, saved as WebP under the same name (send Claude the photo and it converts it). It shows small next to the form on the homepage and larger on About. Then delete the two "[PLACEHOLDER: photo]" tags (`src/index.html` and `src/pages.py`) and rebuild.
- [ ] Privacy page: it already names Web3Forms. Once your account exists, check how long Web3Forms keeps a copy of each message and fix the [CONFIRM] there, plus the "last updated" date. If you add analytics, add a short section saying what it collects.
- [ ] Work links: the two live-site links go to jsglisson3.github.io, which shows your last name in the address. Fine for now; switch them to the clients' own domains once those exist.

### Set up
- [x] **Buy the domain.** Bought 2026-10-26 at Cloudflare Registrar and connected to GitHub Pages the same day: https://firemarktech.com (and www) serve the site over HTTPS, still as a hidden draft. See **Domain** under Notes.
- [ ] **Email at the domain** (for example Google Workspace or Microsoft 365).
- [ ] **Form service: Web3Forms** (chosen Oct 27). Sign up at web3forms.com with the address the form should deliver to (the free plan is enough). Paste the access key it gives you into `src/partials/form.html`, as the `value` of the `access_key` field, in place of the [PLACEHOLDER] text. Rebuild (ask Claude), then send yourself a test from the live site and check it arrives. Until the key is in, the form falls back to opening a pre-filled email, so nothing is broken meanwhile. Browsers with JavaScript off are sent to `thanks.html` after submitting; everyone else sees the thanks line in place.
- [ ] **Trademark check.** Search "Firemark" at the USPTO (tmsearch.uspto.gov) before you print cards or signs.
- [ ] **Firemark's own Google Business Profile** as a service-area business (it can hide your home address). You'll be doing this for clients, so it's good practice.

### Launch day
The domain is already connected, so launch is just switching the draft off.
1. In `tools/build.py`, set `LAUNCHED = True`, then run `python tools/build.py`. That removes the draft banners and the noindex tags. The brand sheet and the 404 page stay hidden from search. (Your PC has no Python, so ask Claude to run the build.)
2. Commit and sync in VS Code. Don't delete `docs/CNAME`; it holds the domain.
3. After launch: add the site to Google Search Console, submit `sitemap.xml`, send yourself a test free check, and run Lighthouse on your phone.

## Notes

- **Domain:** firemarktech.com is registered at Cloudflare. Its DNS has four A records for @ (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153) and a CNAME for www to jsglisson3.github.io, all set to DNS only (grey cloud). Leave them grey: the orange proxy gets in the way of GitHub's certificate. GitHub Pages has the custom domain set (that's what `docs/CNAME` is) and Enforce HTTPS on. The old jsglisson3.github.io/Firemark/ address redirects to the domain. `SITE_ROOT` in `tools/build.py` is "/" to match.
- **Edit `src/`, not `docs/*.html`.** The build overwrites the pages in `docs/`. CSS (`docs/css/site.css`) and the script (`docs/js/site.js`) are edited directly. They are linked as `?v=9`; bump that number in `src/index.html` and `tools/build.py` whenever either file changes, so returning visitors get the new version.
- **v9 (Oct 27):** the header (phone sheet menu that ends with the button, email, phone and place), the hero promises under the buttons, the Stone closing card (three steps, photo, form) that Work and About reuse in a short form, and the Stone footer. Reasons and the research behind them: `design-research.md`.
- **v1** is still in `Documents\Firemark`. Nothing in v2 depends on it.
- **Logo files on Windows:** SVGs copied to your computer through the Claude app may get a small `<metadata>` block (content credentials) added at the top. It's harmless, and browsers ignore it.
- **Design skills:** copies of Frontend Design and UI UX Pro Max belong in `.claude/skills/` inside this folder, so any session with it open gets them without a reinstall. The Claude app can't write into `.claude` folders from a cloud session, so they came as a zip (`firemark-v2-claude-skills.zip`): extract it into `Documents\Firemark-v2` and check that `.claude\skills\ui-ux-pro-max\SKILL.md` exists. See `.claude/skills/README.md` afterwards. The design rules they produced are in `design-system/firemark/MASTER.md`.
- **Free checks:** `free-check/TEMPLATE.md` has the 20-minute routine and the report template.
- **Client footers:** `snippets/site-by-firemark.html` has the small "Site by Firemark" badge. Always ask the client first.
