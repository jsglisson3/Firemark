# Pick up here (Firemark v2)

Last updated Oct 26, 2026, during the afternoon build session.

## Where things stand

The v2 site is built and checked. Everything is in `docs/`:
- the homepage, with the map animation
- Work (two case studies), About and the free check page
- Privacy, the 404 page and a brand sheet (`brand.html`, not linked from the site)
- the icons, the link-preview image, the sitemap and robots.txt

Checks on the latest build:
- The HTML is valid.
- The accessibility scan finds 0 issues on every page, at phone and desktop widths.
- No sideways scrolling at any width from 320 to 1920 pixels.
- Lighthouse on a phone: performance 99–100, accessibility 100, best practices 100. SEO is 100 once the draft noindex tag comes off.

It is still a **draft**. Every page carries a yellow draft banner and a noindex tag, so search engines skip it. Contact details are placeholders.

**To continue in a new chat:** attach or paste this file plus `BRIEF.md` and `DECISIONS.md`, and say what you want to do next. If you make a Claude project for Firemark, keep it lean: those three files are enough.

## Settled Oct 26

- Domain: **firemarktech.com**.
- The free check report arrives **within 7 days**. Most starter websites go live **about 30 days after the go-ahead**.
- About page: keep the career facts, but general (no team size, dollar figures or project counts).

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
- [ ] Email address: placeholder hello@firemarktech.com. Set it up at your domain, then also put it in `data-fallback-email` in `src/partials/form.html` and in the homepage's structured data (`src/index.html`, search for PLACEHOLDER).
- [ ] Phone number: footer, contact page, homepage and structured data.
- [ ] Booking link for "Book a 15-minute call" (Calendly, Cal.com or Google Calendar booking pages all work). Put the address in the `href` of the two links marked `data-booking-link`.
- [ ] Photo: the current one is a placeholder. Use a local headshot, or delete the photo blocks on Home and About.
- [ ] Privacy page: the form service's name and where it stores messages, plus the "last updated" date. If you add analytics, add a short section saying what it collects.
- [ ] Work links: the two live-site links go to jsglisson3.github.io, which shows your last name in the address. Fine for now; switch them to the clients' own domains once those exist.

### Set up
- [ ] **Buy the domain.**
- [ ] **Email at the domain** (for example Google Workspace or Microsoft 365).
- [ ] **Form service.** Without one, the form opens a pre-filled email. That works, but a service is smoother. Formspree, Basin and Web3Forms all work with a static site. Put the service's form address in `data-endpoint=""` in `src/partials/form.html`, rebuild, send a test, and name the service on the privacy page.
- [ ] **Trademark check.** Search "Firemark" at the USPTO (tmsearch.uspto.gov) before you print cards or signs.
- [ ] **Firemark's own Google Business Profile** as a service-area business (it can hide your home address). You'll be doing this for clients, so it's good practice.

### Launch day
1. In `tools/build.py`, set `LAUNCHED = True` (and `DOMAIN` if it changed), then run `python tools/build.py`. That removes the draft banners and the noindex tags. The brand sheet and the 404 page stay hidden from search.
2. Commit and sync in VS Code.
3. GitHub: **Settings > Pages > Deploy from a branch > main > /docs**. Add your domain under **Custom domain**. GitHub creates a `docs/CNAME` file, so pull it afterwards. Turn on **Enforce HTTPS** once it's offered.
4. At the domain registrar, point the domain at GitHub Pages. Use the A records GitHub lists for apex domains (currently 185.199.108.153, 185.199.109.153, 185.199.110.153 and 185.199.111.153), plus a `www` CNAME to `jsglisson3.github.io`. Check GitHub's "Managing a custom domain" page for current values.
5. **Don't add the CNAME file before the domain is live.** If you do, the github.io preview starts redirecting to a domain that doesn't exist yet.
6. After launch: add the site to Google Search Console, submit `sitemap.xml`, send yourself a test free check, and run Lighthouse on your phone.

## Notes

- **Edit `src/`, not `docs/*.html`.** The build overwrites the pages in `docs/`. CSS (`docs/css/site.css`) and the script (`docs/js/site.js`) are edited directly.
- **v1** is still in `Documents\Firemark`. Nothing in v2 depends on it.
- **Logo files on Windows:** SVGs copied to your computer through the Claude app may get a small `<metadata>` block (content credentials) added at the top. It's harmless, and browsers ignore it.
- **Design skills:** copies of Frontend Design and UI UX Pro Max belong in `.claude/skills/` inside this folder, so any session with it open gets them without a reinstall. The Claude app can't write into `.claude` folders from a cloud session, so they came as a zip (`firemark-v2-claude-skills.zip`): extract it into `Documents\Firemark-v2` and check that `.claude\skills\ui-ux-pro-max\SKILL.md` exists. See `.claude/skills/README.md` afterwards. The design rules they produced are in `design-system/firemark/MASTER.md`.
- **Free checks:** `free-check/TEMPLATE.md` has the 20-minute routine and the report template.
- **Client footers:** `snippets/site-by-firemark.html` has the small "Site by Firemark" badge. Always ask the client first.
