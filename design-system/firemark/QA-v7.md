# Quality pass on the live draft (v6 → v7), Oct 26, 2026

Checked the v6 build (commit 7ff2724) served under /Firemark/, all six public pages, at phone (390px) and desktop (1440px) width.

## Scores (after fixes)
- Lighthouse, phone: performance 97–100, accessibility 100, best practices 100. Desktop: 100 / 100 / 100.
- SEO shows 63–66 only because of the draft noindex tag. Expected; goes to 100 at launch.
- Accessibility scan (axe, WCAG 2.2 AA): 0 issues on every page at both widths.
- Keyboard: skip link first, every control reachable in order, visible focus ring on all of them, no hidden focus stops.
- Reduced motion: with "reduce motion" on, no animations run and scrolling isn't smooth-scrolled.
- No sideways scrolling at 320, 360, 375, 390, 414, 768, 1024, 1280, 1440 or 1920px.
- HTML validator: 0 errors after the fix below.
- Links: all internal links work. The GLP and library repos exist; the outside links (github.io sites, OpenStreetMap) couldn't be opened from the test machine's network, so give them one click on your phone.

## Found and fixed in v7
| What | How bad | Fix |
|---|---|---|
| Invalid HTML on every page: a hidden 6 KB block of image-editor metadata (C2PA) was pasted into the icon sprite | Low (invisible, but extra weight on every page and fails validation) | Removed |
| Form error box used a level-3 heading right after the page title on Contact (skips a level for screen readers) | Low | Now a level-2 heading |
| Work screenshots told the browser they were wider than they are on phones, so phones downloaded a bigger image than needed | Low (about 40–140 KB extra on phones) | Corrected the `sizes` hints |
| "Email at your own name" reads oddly | Copy | "Email with your business name" |
| About: "How it works with Jeremy" heading | Copy | "Working with Jeremy" |
| About: "make sure yours are there, and stay right" | Copy | "...and stay up to date" |
| Contact said "Based in The Colony, working across DFW" right above an FAQ answer saying the same thing | Copy (repeat) | Dropped the extra line; the FAQ answer stays |
| Privacy promised "no cookies, ads or tracking" | Your request | Section removed, so you can add analytics later |
| No answer about who owns the site, or that you can show it | Your request | New Contact FAQ "Who owns the website?": you own it, and Firemark may show it as recent work [CONFIRM] |
| Work page still asked to confirm permission from GLP and the Friends | Out of date | Permission is in; the tag now only asks about the program photos with children |

PICKUP.md, COPY.md and DECISIONS.md are updated to match.

## Flagged for the header / hero / CTA / footer rebuild (not changed)
- "A short, plain-English report" appears in the hero, the homepage form section, and the closing CTAs on Work and About. Worth varying the wording.
- The homepage form section says the report is free twice ("Free, no strings" under the hero, then "It's free, and it's yours to keep").
- "Book a 15-minute call" links to the top of the page until a real booking link exists. Fine as a placeholder, but hide it if launch comes first.
- Footer has an empty-looking band above its text on phones until the lazy-loaded logo appears. Load the footer logo normally in the rebuild.
- Homepage phone LCP is about 2–2.5 s, driven by the hero heading font. Fine now; keep the new hero this light or lighter.
- About 26–35 KB of the stylesheet is unused rules left from v2 (old grids, route and price blocks). Harmless; worth trimming when the CSS is next reworked.

## Known and expected (not counted)
noindex until launch; og:image points at firemarktech.com; contact details are [PLACEHOLDER].
