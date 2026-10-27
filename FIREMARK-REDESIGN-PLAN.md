# Firemark redesign plan (v10)

Written Oct 27, 2026, overnight. This file records what was wrong with v9, what v10 changes, the design rules it follows, and what research it leans on. The site itself is in `docs/` (built from `src/` with `tools/build.py`). It is still a hidden draft (`LAUNCHED = False`).

## 1. The business, in one paragraph

Firemark is Jeremy, one person in The Colony, Texas, who builds websites and Google listings for independent, owner-run businesses nearby, then keeps them running for a monthly fee. The buyer is a busy owner (barber, bakery, plumber) who isn't sure a website is worth it. The site has one job: get that owner to ask for the **free check**, a written report on how they show up on Google today, within 7 days. Everything else (the work, the offer, Jeremy) exists to make that ask feel safe.

## 2. Audit of v9, most serious first

| # | Problem | Why it mattered | v10 fix |
|---|---|---|---|
| 1 | Placeholder contact details and [CONFIRM]/[PLACEHOLDER] tags visible on the page | A visitor sees an unfinished business, and a fake email or phone breaks trust | Contact details live in one settings block in `tools/build.py`. Anything empty is simply not shown. The build **refuses to finish** if a `[PLACEHOLDER` or `[CONFIRM` would reach a page. |
| 2 | Photo placeholder for Jeremy | An empty "photo goes here" box looks broken | A deliberate stone tile with the flame pin, plus his name and town. Set `HEADSHOT = True` when the photo exists and it swaps in everywhere. |
| 3 | Children visible in the Friends of the Library screenshots | No permission for identifiable kids | The photo circles in all five library screenshots are filled with flat tints. Nothing identifiable is left. |
| 4 | "5 days" reply vs "7 days" report read like two answers to one question | Confusing promise | Each number has one meaning, said the same way everywhere: "You'll hear back within 5 days, and your report arrives within 7." |
| 5 | Error summary said "Fix these to send your request" | Sounds like blame | The title counts the problems: "One quick fix and it's ready to send:" / "Two quick fixes…". |
| 6 | Unlabelled form controls; required/optional unclear | Accessibility and drop-off | Every field has a visible label with "(required)" or "(optional)". New "What would help most?" pick list is a real fieldset with a legend. |
| 7 | "[CONFIRM what the plan includes]" and the [CONFIRM] pricing note | Unfinished offer | The offer section says plainly what the starter project and monthly plan include, with no prices: "What it costs: let's talk." The wording is in the review list for Jeremy. |
| 8 | Homepage "Why the name" section was weak (Jeremy's note) | It explained the brand instead of helping the owner | Removed from the homepage. Replaced with "One person, start to finish." and five short questions all answered **Jeremy**. The name story now lives briefly on About, with corrected history. |
| 9 | Ownership question left open | Owners worry about being locked in | One line, repeated where price is discussed: "Your domain, your content and your site are yours to keep." |
| 10 | The hero map was decoration | It didn't show what the service does | The map now performs the result: a search is typed, the pin drops, a listing card appears. Visitors can pick their own trade and watch it retype. |
| 11 | Work list sizing and wrap issues, About degree wording | Small polish | Work rows rebuilt with desktop and phone shots; degree corrected to "BBA in Information Systems". |

## 3. The direction

**Idea:** The real corner of Main St and S Colony Blvd, with the flame pin on it, sits *inside the headline*, as a tile the size of a word after "Put your business". Below the headline the map opens to full width. The headline literally puts the business on the map.

**The one live thing:** "Try it with your trade." Tap Barber, Plumber, Nail salon or Tacos and the search retypes ("barber near me"), the listing name changes and the pin drops again. Without JavaScript the buttons stay hidden and the map still reads.

**What it stays away from:** glass, gradients, glows, icon cards, fake stats or ratings, tracked-out all-caps labels, numbered markers on things that aren't steps, dark mode for its own sake.

**Sections, each with one claim:**
1. Hero: you'll be found on the map (the map proves it).
2. See what your customers see: the free check is real and useful (a full sample report page for a made-up bakery proves it, clearly labelled as a sample).
3. Recent work: Jeremy builds real sites (two real sites, desktop and phone shots).
4. Get found. Stay found.: what you get, and that price is a conversation (starter project, monthly plan, "let's talk").
5. One person, start to finish.: who you'll deal with (five questions, one name).
6. Let's get your business on the map.: what happens next, and the form.

## 4. Tokens

Kept from v8/v9 (settled): light paper and charcoal with a subtle orange, Bricolage Grotesque, the FLAME PIN logo.

| Role | Value |
|---|---|
| Paper (page) | `#F6F5F3` |
| Stone (fields, footer) | `#ECEAE6`, deeper `#E3E0DA` |
| White (cards, form) | `#FFFFFF` |
| Ink | `#1D1C1A` |
| Muted text | `#57534E` |
| Accent (buttons, links) | `#B23F0E`, pressed `#93330A` |
| Flame (logo, pin, focus) | `#EC4E1C` |
| Field line | `#8A857D` |

Type: Bricolage Grotesque only. Display `clamp(2.4rem, 0.9rem + 6.6vw, 7rem)`, h2 `clamp(2rem, 1.25rem + 3.1vw, 3.75rem)`, lead `clamp(1.25rem, 1.05rem + 0.75vw, 1.75rem)`, body 18px, small 15px. Sentence case everywhere.

Layout: one pair of page margins `clamp(1.25rem, 0.4rem + 3.6vw, 3.5rem)`, max width 88rem, section gap `clamp(5rem, 2.5rem + 8vw, 10rem)`. Two-column splits on desktop, single column under 64rem.

Shape: 8px radius on panels and cards; pill buttons; no drop shadows except the two interface pieces (the map card and the phone menu sheet).

Buttons: one primary style (orange pill, white text). Secondary actions are underlined text links with an arrow.

Focus: 3px flame outline with 2px offset on every control.

Motion: one orchestrated hero sequence (map opens, search types, pin drops, card appears), a gentle staggered reveal of section parts, and feedback on the trade picker. All of it is off when the visitor asks for reduced motion, and the page is complete without it.

Breakpoints: phone under 40rem (headline tile hidden, map pin raised), tablet 40–64rem, desktop above 64rem.

## 5. Decisions made overnight

- **Name story off the homepage.** Jeremy wasn't sure it earned its place, and the owner doesn't need it to decide. The "One person" Q&A says the same thing ("you're looked after") in a way that answers a real worry. A three-sentence version stays on About. The history was corrected: the fire mark came from the 1750s Philadelphia fire insurance company Benjamin Franklin helped start.
- **A sample report instead of a list of features.** Showing the actual thing the owner receives is stronger than describing it. It is plainly captioned as a sample for a made-up bakery.
- **Contact settings block.** `EMAIL`, `PHONE`, `BOOKING_URL`, `HEADSHOT`, `WEB3FORMS_KEY` in `tools/build.py`. Empty means hidden. The form falls back to opening a pre-filled email to `FALLBACK_EMAIL` until the Web3Forms key is in.
- **Pick list on the form.** "What would help most?" with four optional choices, so Jeremy knows where to start before he replies.

## 6. Research behind it

Dribbble (captured on Jeremy's PC on Oct 27, 50 shots across 10 searches; files in the project folder under `redesign-v10/dribbble/`):

- **NexUX Lab, "Roofing Company Website"** (dribbble.com/shots/27718334): puts the local place in the headline and sells "a real person who knows your project". Supports the place-first hero and the "One person, start to finish." section.
- **Peno Lab, "Tree Service Website"** (27746529) and **Trexa Lab, "Trofo Roofing"** (27612799): phone number in the header and hero. The `PHONE` setting puts it in the header menu, closing section and footer once there is a number.
- **Arman Hossain Somoy, "Contact Form UI Design"** (26956078): promises beside the form and "What do you need?" chips. Led to the next-steps list beside the form and the "What would help most?" pick list.
- **Odama, "SaaS Pricing Page"** (22276265): a custom "let's talk" card next to priced plans. Confirms a single, calm "What it costs: let's talk." panel is a recognised pattern.
- **Wavespace, "Frank Codina Personal Brand"** (27531757) and **Karpi Studio, "West Stringfellow"** (27236640): about pages carried by a large portrait. The headshot is the single biggest missing piece; the About card is built to take it.
- **tubik, mobile websites** (24205620, 24031129, 20486946): phone screens shown as the product. Matches the phone shots beside each site in Work.
- **Andrés Soria, "Graphy footer"** (25878447): the call to action closes the page above a light, quiet footer. Matches the closing section over the Stone footer.
- What the shots also showed, and v10 avoids: invented star ratings and "500+ clients" counters, dark gradient heroes, glass cards.

Earlier research still applies: `design-research.md`, `header-hero-research/design-research.md` (Awwwards, 217 shots) and `design-system/firemark/RESEARCH-v3.md`.

## 7. Skills used

- **design-taste-frontend** (tasteskill v2): dealt the "sentence as layout" direction, ran the browser inspector and lint on every page, and set the look-and-fix loop.
- **frontend-design**: plan-then-critique pass, typography and the "spend your boldness in one place" rule (the map in the headline).
- **ui-ux-pro-max**: form, accessibility and mobile checklists (labels, touch targets, focus, contrast, reduced motion).

## 8. Checks on the v10 build (run Oct 27, 2026, final build)

- Accessibility scan (axe-core): **0 issues** on all 8 pages at 390 and 1440 pixels, with the phone menu open, and with reduced motion on.
- Lighthouse (performance / accessibility / best practices / SEO). SEO reads 66–69 only because every page carries the draft `noindex` tag on purpose; it goes to 100 at launch.

| Page | Phone | Desktop | Phone LCP |
|---|---|---|---|
| Home | 97 / 100 / 100 | 100 / 100 / 100 | 2.5 s |
| Work | 98 / 100 / 100 | 100 / 100 / 100 | 2.4 s |
| About | 99 / 100 / 100 | 100 / 100 / 100 | 2.0 s |
| Free check | 99 / 100 / 100 | 100 / 100 / 100 | 2.0 s |
| Privacy | 100 / 100 / 100 | 100 / 100 / 100 | 1.7 s |
| 404 | 99 / 100 / 100 | 100 / 100 / 100 | 2.1 s |

  Layout shift is 0 and blocking time is 0 ms on every page.
- HTML valid (html-validate). No sideways scroll at 320, 390, 600, 768, 1024, 1280, 1440 or 1920 pixels.
- Tested by hand in a browser: the trade picker retypes the search and renames the result; the phone menu opens, dims the page and closes on Escape; the form's error list counts the fixes and shrinks as each one is fixed.
- Inspector (design-taste-frontend): homepage 0 fails. Inner pages flag "few pictures" because there is no headshot and no photography yet. This clears once the photo is in.

## 8b. Critique rounds

- **Round 1** (homepage): checkbox pills looked like radio buttons (now square boxes with a tick); the closing column left a gap beside the long form (now sticks while you scroll); the last Q&A question wrapped; the Franklin history was loose (corrected).
- **Round 2** (in-between widths and inner pages): Work and Privacy had a dead half-screen beside a short headline (headline and lead now share the row); About's name squeezed beside the tile (the card stacks); the "not the official site" tag became a tall pill when it wrapped; Privacy was one narrow column (now a two-column sheet); the 404 and thanks pages were bare lists (now the homepage map, with "No results on this street" and the links as chips); the contact page now shows part of the sample report beside the form, so people see what they're asking for.
- **Round 3** (details and behaviour): the pin in the headline tile was clipped at the top (re-centred); on phones the tile was hidden, so the idea didn't reach phone visitors (it now ends the second line, "on the map." plus the tile); the phone menu didn't separate itself from the page (the page behind now dims); fixed errors stayed listed in the form's error summary (it now updates live); the price panel now links to the FAQ on price and ownership.
- **Round 4** (rhythm): three neighbouring sections were all "text left, panel right". On wide screens "One person, start to finish." now puts the story beside the heading and the five questions in one row, each answered **Jeremy** in large type, sized to its panel so the names never touch. Work screenshots got a smaller 480px size so phones download less.
- **Against the Dribbble set:** every strong local-business shot puts the owner's face in the first screen or two (NexUX roofing, Quality Leads Australia's founder card, the Codina and Stringfellow about pages). Firemark can't do that honestly until there's a headshot, so the design leaves a slot for it in the About card and beside the form, and `HEADSHOT = True` fills both. What the set does that v10 deliberately doesn't: invented ratings and "200k+ customers" counters, dark gradient heroes, glass panels, stock team photos.

## 9. What Jeremy needs to confirm

See `REVIEW-v10.md`.
