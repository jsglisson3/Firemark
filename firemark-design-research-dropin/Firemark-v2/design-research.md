# Design research: header, hero, closing CTA and footer for Firemark

Written Oct 26, 2026, for the v2 site (firemarktech.com, repo jsglisson3/Firemark, built on the v7 drop-in). This is the research and the recommendation only. Nothing has been built. Read "The decisions I need" at the end, then say go.

## What this is based on, and what it is not

**Visited and read.** Every Awwwards listing the brief named (Sites of the Day, Sites of the Month, Header Design, Business & Corporate, Design Agencies, Portfolio, Nominees, Collections), then the Awwwards page and the live site for 41 candidates, plus maxibestof.one's Hero, Footer and Call to Action sections. For 29 of those live sites I read the real page content: the header, the first screen, the last section before the footer, and the footer. Every link below was opened in this session. Nothing is from memory.

**Screenshots.** Your PC captured 217 screenshots of 53 of the 54 pages at 1440px and 390px (top of page, bottom of page, and the open phone menu on 33 sites). They are in `Documents\FiremarkTech\research-shots` with a `results.csv`. My connection to your PC dropped after the capture finished, so I could not look at them. The scores below come from reading each site's content and structure, not from seeing it rendered. Where a score depends on how a page looks on a phone, it is marked as a read, not a view. Flip through the `-m-top.jpg` and `-m-menu.jpg` files for the eight finalists before you say go; it will take five minutes and it is the one check I could not do.

**Blocked or failed, skipped as the brief asks.**
- Dribbble: every page (search pages, tag pages and the 13 individual shots) returned empty to my fetcher. No Dribbble shot was judged. Your PC did capture the 13 shot pages as images (`dr-*-d-shot.jpg`); they are listed at the end for you to look at, but they did not shape the picks. Given the brief ranks Dribbble below live sites anyway, this costs less than it sounds.
- Awwwards Elements (`/elements/`): blocked by the site's robots rules.
- maxibestof Header section: returned an error. Hero, Footer and CTA sections loaded.
- Live sites that refused: Nova Dental (webflow.io, robots), Pamidor Design (robots for me, SSL error for your PC), Garvin Promotion Group (server error).
- maxibestof entries are the site's own descriptions and tags, not live visits. The live URLs sit behind redirects I did not follow. They are marked "(description)" in the tables and count as supporting evidence only.

**Also used.** The two skills in the repo: the frontend-design skill (for the design plan and the anti-template checks) and UI UX Pro Max (its landing-pattern and UX-guideline data: "Minimal Single Column", "Hero + Features + CTA", sticky-nav and motion rules).

## The short version

The current v7 site is already closer to the best live examples than it is to the award showpieces. The research says keep its bones and sharpen four things:

1. **Header:** wordmark, three links, one button, and a quiet "The Colony, Texas" next to the button. Sticky, thin, no tricks.
2. **Hero:** keep the search-result map. Put the two real promises (report in 7 days, site live in about 30) in the first screen, and move the place chip up into the header.
3. **Closing CTA:** keep the form as the last section, but frame it as three plain lines about what happens next, with Jeremy in it, and a reply-time promise.
4. **Footer:** light, not charcoal. Three short columns (Firemark, Reach Jeremy, Explore), a one-line "Firemark is Jeremy, in The Colony, Texas", and a baseline. The mark loads normally.

Every pick is light, static, and buildable in a day or two each.

---

## 1. Header

### What the best ones have in common
- One row: wordmark on the left, three to five links, one button on the right. Wishbone (3 links + "Book a call"), CE Growth Partners (5 + "Start a conversation."), Revelatio (4 + "Get in touch"), Relevo & Vinco (5 + "Order a kit"), P+Z (6 + "Let's talk").
- The button names the first step, not "Contact": Book a call, Start a conversation, Order a kit, Request a quote, Let's talk. "Contact Us" only appears on the enterprise sites (Comrade, Idealworks "Contact Sales").
- A small signal of place or availability in the header on the local and small firms: BCG shows "Gold Coast, AU" with a clock, Two26 shows business hours, Signal-A shows local time, Banham opens with "Prefer to call?" and a phone number.
- Mega menus and promo bars belong to big companies (Comrade, Banham, LAPL, Idealworks, Kohen's 16 practice areas). Every small firm in the set keeps it to a single row.
- On phones, a labeled toggle that reads "Menu" and flips to "Close" (LPAS, Right Hemisphere, Kohen's "Ouvrir le menu"), and the phone menu ends in the contact action (Revelatio's mobile list ends with Contact; the current Firemark menu already ends with "Get my free check").
- Light backgrounds. The dark headers are on the dark showpieces (Emotion, Dobre).
- Scroll behavior could not be read from page content, and the capture only has top and bottom states, so the recommendation below leans on UI UX Pro Max's sticky-nav rule (never cover content or the focused control) rather than on examples.

### Shortlist (8 of 26 headers reviewed)
Scores are 1 to 5: Clarity, Trust, Conversion, Mobile (read, not viewed), Weight, Accessibility, Buildable, Distinctive.

| # | Site | Links | What to steal | What to skip | C | T | Cv | M | W | A | B | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Wishbone Advisory (Austin, TX; Nominee Oct 26, 2026) | [Awwwards](https://www.awwwards.com/sites/wishbone-advisory) / [live](https://wishboneadvisory.com) | Logo, Services / Results / About, "Book a call". Three links is enough. | Nothing. | 5 | 4 | 5 | 4 | 5 | 4 | 5 | 3 |
| 2 | CE Growth Partners (Nominee Oct 25, 2026) | [Awwwards](https://www.awwwards.com/sites/ce-growth-partners) / [live](https://cegrowthpartners.com/) | "Start a conversation." as the button label: low pressure, full stop included. | A sub-menu under Technology. | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 3 |
| 3 | BCG Building Design (Gold Coast; Nominee Oct 26, 2026) | [Awwwards](https://www.awwwards.com/sites/bcg-building-design) / [live](https://bcgbuildingdesign.com.au/) | "Gold Coast, AU" in the header. A local firm says where it is before you scroll. | The live clock; "Project Enquiry" as a nav item rather than a button. | 4 | 4 | 3 | 4 | 5 | 4 | 5 | 4 |
| 4 | Two26 Studio (Nominee Oct 23, 2026) | [Awwwards](https://www.awwwards.com/sites/two26-studio) / [live](https://two26.studio/) | Business hours in the header. Two links and "Let's Talk". | Placeholder links (#). | 4 | 3 | 4 | 4 | 4 | 3 | 5 | 4 |
| 5 | Revelatio Studio (SOTD Aug 12, 2026, 7.37) | [Awwwards](https://www.awwwards.com/sites/revelatio-studio) / [live](https://revelatio.studio/) | Four links + "Get in touch"; the phone menu repeats the links and ends with Contact. | Language toggle (not needed). | 4 | 4 | 4 | 4 | 3 | 4 | 4 | 3 |
| 6 | Relevo & Vinco (Porto; Nominee Oct 22, 2026, Header Design tag) | [Awwwards](https://www.awwwards.com/sites/relevo-vinco) / [live](https://relevovinco.com/) | A text wordmark with a full stop, and a button that names the thing you get: "Order a kit". | The scroll-driven scenes everywhere else on the page. | 4 | 4 | 5 | 4 | 2 | 3 | 4 | 5 |
| 7 | LPAS (SOTD Oct 10, 2026, 7.24, Header Design tag) | [Awwwards](https://www.awwwards.com/sites/lpas) / [live](https://lpas.com/) | "Menu" flips to "Close"; the open menu groups links under three headings with socials below. | No button at all; the whole nav hides behind Menu even on desktop. | 3 | 4 | 2 | 4 | 3 | 4 | 4 | 4 |
| 8 | Banham (London; Nominee Oct 22, 2026) | [Awwwards](https://www.awwwards.com/sites/banham-1) / [live](https://www.banham.co.uk/) | "Prefer to call?" and the number, one line above the header. | The mega menu, the utility links, two competing buttons. | 3 | 5 | 3 | 3 | 3 | 4 | 3 | 3 |

Reviewed and cut: Comrade (promo bar + mega menu + two actions + phone), Potadot (seven items, three languages, phone and email), Kohen Avocats (16 practice-area links), LAPL (search + six mega menus), Idealworks, Reckoner (three dropdowns, no button), Right Hemisphere (CONTACT as a nav item plus MENU/CLOSE), Signal-A (time widget), Squared Media (five links, language, "Mail ons" and "Plan een call"), Biite (six links, no button), No Jiggery (a dropdown), Brikken (no nav found in the content), Bennett & Clive ("Contact" not even linked), The Line (eight links), P+Z, Impasto (seven links, no button), Son Daven (nine links). The pattern in the cuts: more than five links, or no single obvious button.

### Finalists
1. **Wishbone.** The whole structure in one line. Three links and one named action is what a busy owner can parse in a second.
2. **CE Growth Partners.** Same structure; the label "Start a conversation." is the best-written button in the set. For Firemark the button is already "Get my free check", which is better still because it names a concrete, free thing.
3. **BCG Building Design.** The only header in the set that says where the business is. For a company whose whole pitch is local, that one detail does more than a tagline.

### Final pick: "One row, one button, one place"
Draws from Wishbone (structure), BCG (place), Revelatio and the current site (phone menu order), LPAS (Menu/Close).

Desktop (1440):
```
| [flame-pin] Firemark      Work   What you get   About        The Colony, Texas  [ Get my free check ] |
|---------------------------------------------------------------------------------------- hairline ---|
```
- Height 64px. Wordmark lockup at 28px tall (mark + capital-F "Firemark", the v6 brand files). Links at 16px, weight 600, Charcoal; the current page is underlined in Flame (already so).
- "The Colony, Texas" in Graphite, 15px, weight 500, between the links and the button. Hidden below 1024px. This replaces the pin chip in the hero (see Hero), so the place appears once above the fold, not twice.
- Button: the Ember primary (`.btn.btn-flame.btn-small`), 40px tall in the header, 48px in the menu.
- Sticky. After the page scrolls past 24px, the header gets a 1px Line hairline and a Paper background at 92% opacity with `backdrop-filter: blur(8px)` (fallback: solid Paper). No shrink, no fade, no hide-on-scroll. The UX rule is that a sticky bar must never cover content or a focused control: keep `scroll-padding-top: 72px` on `html` so anchor jumps and keyboard focus land below the bar (the v7 QA pass confirmed focus is never hidden; keep it that way).

Phone (390):
```
| [flame-pin] Firemark                 [ Free check ]  [ ≡ Menu ] |
```
- Height 56px. The button stays (it already does); below 384px the Menu button shows only its icon with the name kept for screen readers; below 335px the button hides (both already in v7).
- The menu is a sheet that drops from under the header, not a full-screen takeover. Three links at 28px, weight 620, 56px tall each; a hairline; "Get my free check" as a full-width button; then one line in Graphite: "[PLACEHOLDER: email] · [PLACEHOLDER: phone]" written as two short links on one line, no middle dot (two `<a>`s with a space and a thin rule between them); then "The Colony, Texas".
- "Menu" flips to "Close" with `aria-expanded`. Esc closes, tapping outside closes, choosing a link closes, and focus returns to the Menu button. The sheet is short, so the page is not scroll-locked.

Motion: the sheet fades in and slides down 8px over 160ms, ease-out. Hover on links: the underline grows from 0 to 100% over 120ms. Under `prefers-reduced-motion: reduce`, everything appears instantly.

Draft copy:
- Links: Work, What you get, About.
- Button: Get my free check (short form on phones: Free check).
- Place: The Colony, Texas.

---

## 2. Hero

### What the best ones have in common
- One sentence that says what the business does and for whom, then one line of support. Wishbone ("The growth partner for B2B and eCom brands, from strategy to scale."), CE Growth ("Turn marketing complexity into measurable growth."), BCG, Biite, RIO.
- The local firms put the place in the first screen: BCG's H1 is literally "Building Designer Gold Coast"; RIO's headline is "Rio Property knows Cape Town"; Potadot shows "Serving KL, JB, Melaka & all of Malaysia"; Revelatio writes "Recife, Brazil / Working Globally".
- Two actions: a small, concrete first step, and a second link that points at proof. Wishbone: "Book a 15-minute call" + "Or get a free Amazon listing teardown". P+Z: "Request a quote" + "See how we plan protection ↓" (scrolls to the proof). Potadot, CE Growth and Squared all pair "Let's talk / Start a conversation / Plan een kennismaking" with "See our work / See the work / Bekijk het werk".
- A risk-reducer line under the buttons: Plumeform's "100 free monthly responses, no credit card". The current Firemark hero already does this ("Free, no strings.").
- Concrete numbers that are promises, not statistics. Squared Media puts "vanaf €2.000" and "binnen 3 werkdagen" (from €2,000, within 3 working days) in the hero. Kohen promises a written analysis "sous 24 heures ouvrées". Relevo & Vinco promises a reply within two working days. This is the most useful finding for Firemark: you cannot show stats or logos, but you can state what you promise, and the best sites do exactly that.
- The visual is the product doing its job, not a stock photo: Biite's metric panel, Plumeform's live survey, Wishbone's result cards, LAPL's "What can we help you find?" with a search field. Firemark's search card dropping a pin on real streets is the same idea, done for a local business.
- The heavy heroes (A24's 3D discs, Emotion's WebGL, Belgrade Arbor's video, Agrumea's Three.js, Squared's 3D island) win awards and lose a phone on a parking lot. Each would cost the v7 Lighthouse 97 to 100.

### Shortlist (8 of 29 heroes reviewed)

| # | Site | Links | What to steal | What to skip | C | T | Cv | M | W | A | B | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Wishbone Advisory | [Awwwards](https://www.awwwards.com/sites/wishbone-advisory) / [live](https://wishboneadvisory.com) | "Book a 15-minute call" + a free second offer. The time makes the ask small. | Three stat cards under the hero. Firemark has no stats and should not invent any. | 5 | 4 | 5 | 4 | 5 | 4 | 5 | 3 |
| 2 | RIO Property (Cape Town; HM Aug 11, 2026) | [Awwwards](https://www.awwwards.com/sites/rio-property) / [live](https://www.rioproperty.co.za/) | The city in the headline, stacked on four lines, and the frank subline "You're probably here to see what we actually do." | All-caps buttons, the client logo strip. | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 4 |
| 3 | Plumeform (Nominee Oct 18, 2026, Header Design tag) | [Awwwards](https://www.awwwards.com/sites/plumeform) / [live](https://plumeform.com) | The line under the button that removes the risk ("no credit card"). | SaaS demo, arrows glued to every button. | 5 | 4 | 5 | 4 | 3 | 4 | 4 | 3 |
| 4 | Biite (Nominee Oct 17, 2026, Header Design tag) | [Awwwards](https://www.awwwards.com/sites/biite) / [live](https://biite.nl/) | Headline, two buttons, and a product panel instead of a photo. | The numbers in the panel (Leads 341, etc.). | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 4 |
| 5 | Squared Media (Amsterdam; Nominee Oct 18, 2026) | [Awwwards](https://www.awwwards.com/sites/squared-media-1) / [live](https://squared-media.nl) | "From €2,000" and "live within 3 working days" in the hero. Promises as numbers. | The real-time 3D island and talking mascot. | 5 | 3 | 5 | 3 | 1 | 3 | 2 | 5 |
| 6 | P+Z Fine Art Logistics (Nominee Oct 26, 2026) | [Awwwards](https://www.awwwards.com/sites/p-z-fine-art-logistics) / [live](https://www.pnzfas.com/) | Secondary action that scrolls to the proof: "See how we plan protection ↓". | 3D packing studies, video. | 4 | 4 | 4 | 3 | 2 | 3 | 3 | 4 |
| 7 | BCG Building Design | [Awwwards](https://www.awwwards.com/sites/bcg-building-design) / [live](https://bcgbuildingdesign.com.au/) | A plain local H1 and one sentence under it. | No button in the hero at all; depends on one big photo. | 5 | 4 | 2 | 4 | 3 | 4 | 5 | 3 |
| 8 | Los Angeles Public Library (Nominee Oct 7, 2026, Header Design tag) | [Awwwards](https://www.awwwards.com/sites/los-angeles-public-library) / [live](https://www.lapl.org/) | "What can we help you find?" with a search field. A question and a box is a hero. | Everything else; it is an institution-scale site. | 4 | 5 | 3 | 4 | 4 | 5 | 4 | 2 |

Supporting (descriptions on maxibestof, not live visits): [Brand Appart hero](https://maxibestof.one/sections/brand-appart-section-hero-e8taow) (cream page, centered oversized black headline, a book-a-call control in the header, an orange circle as the only accent: the closest palette to Firemark's in the whole set; its fonts PP Neue Montreal and Youth are paid, IBM Plex Mono is free on Google Fonts; Bricolage covers the role), [House of Honey](https://maxibestof.one/sections/house-of-honey-section-hero-buz5n2) (oversized wordmark, split tagline, full-width photo), [Duft und Kultur](https://maxibestof.one/sections/duft-und-kultur-section-hero-rg4au0) (full-bleed image, underlined text link as the only action).

Reviewed and cut: Potadot (eyebrow with middle dots and two badges), CE Growth (text-only; fine but the most template-like), Comrade ("More Jobs. More Revenue. Less Stress." plus award logos), Kohen (hero with a paid-analysis form card), Right Hemisphere (three stacked words and "Things we did"), Relevo & Vinco ("Stand out. Press in."), Brikken (a 30-word sentence and a 3D blob), Signal-A, Revelatio (featured-work videos), No Jiggery (eyebrow + headline, no button until the next block), Bennett & Clive, Son Daven (investment stats), LPAS and Impasto (video), Reckoner, Idealworks (photo + stats), Two26 ("LOOKING SUSPICIOUSLY GOOD"), The Line, and the showpieces (A24, Emotion, Belgrade Arbor, Agrumea, Kigo, Gray, Why Zero, Henrietta, Walton Family Foundation) which were reviewed on Awwwards and excluded on weight.

### Finalists
1. **Wishbone.** Plain sentence, small first step with a time on it, a second free offer, nothing fake.
2. **RIO Property.** The only hero that makes the city the headline and still sounds like a person.
3. **Squared Media** (translated). Not the 3D; the two numbers. A price floor and a delivery time in the first screen is the most convincing thing a small shop can say.

### Final pick: keep the search-result hero, make the promises visible
Draws from Wishbone (two-step ask), RIO and BCG (place first), Squared and Relevo & Vinco (promises as numbers), Plumeform (risk line), Biite and LAPL (the search card as the visual). The current v7 hero already has the right shape; this is a tightening, not a replacement.

Desktop (1440), two columns, text left (44%), map right (56%):
```
| Put your business on the map.                       |  [ real-streets map of The Colony       ] |
|                                                     |  [ "bakery near me" search card          ] |
| Firemark builds websites and Google listings for    |  [ pin drops on Main St, result card:    ] |
| independent businesses in The Colony, then keeps    |  [ Your bakery · Open now · Call/Directions] |
| them running. So when someone nearby searches,      |  [ Map data © OpenStreetMap contributors ] |
| they find you.                                      |                                             |
|                                                     |                                             |
| [ Get my free check ]   See the work ↓              |                                             |
| Free, no strings. In 7 days you'll have a short     |                                             |
| written report on how you show up on Google.        |                                             |
| A starter site goes live in about 30 days.          |                                             |
```
- The pin chip "The Colony, Texas" above the headline goes away (it moved to the header). The headline is the first thing in the column.
- Headline stays "Put your business on the map." at 620 weight, opsz 32, `clamp(2.5rem, 1.6rem + 3.6vw, 4.5rem)`, line-height 0.98, max two lines on desktop, three on a phone. Alternate if you want the city in the H1 (the RIO/BCG pattern): "Put your business on the map in The Colony." It is longer and reads as a mouthful; my call is to keep the short one and let the map and the header carry the place.
- Support line: as above, 19px, Graphite, max 60 characters per line.
- Primary: "Get my free check" (Ember). Secondary: "See the work" as an underlined text link with a small down arrow icon from the sprite (not a glyph pasted on text), scrolling to Recent work. That is the P+Z move: the second action points at proof on the same page. Recent work stays the simple list you asked for (name, one line, thumbnail, link), so the hero never promises a case study it then has to deliver.
- Promise lines, 15px, Graphite, two sentences, each on its own line on desktop: "Free, no strings. In 7 days you'll have a short written report on how you show up on Google." and "A starter site goes live in about 30 days. [CONFIRM the 30 days]". This answers the v7 QA note: "A short, plain-English report" is now said once, here, and the words change in the closing CTA and on Work and About.
- Map: unchanged in content (real OSM streets, the search-to-result moment, the required "Map data © OpenStreetMap contributors" credit). Panel radius 28px. One orchestrated moment of about 1.5 seconds, transform and opacity only, then still. Reduced motion shows the final state.
- Weight: no new assets. The heading font is the LCP element on phones (2 to 2.5 s in the v7 QA); keep the woff2 preload and do not add a photo or a second face.

Phone (390), one column:
```
| Put your business                 |
| on the map.                       |
| Firemark builds websites and ...  |
| [    Get my free check         ]  |
| See the work ↓                    |
| Free, no strings. In 7 days ...   |
| [ map panel, 62vw tall, search    |
|   card at 15px minimum          ] |
```
- Buttons full width, 48px. The map sits below the copy so the promise is read before the illustration loads. The search card text never drops below 15px.

Draft copy, in full:
- H1: Put your business on the map.
- Support: Firemark builds websites and Google listings for independent businesses in The Colony, then keeps them running. So when someone nearby searches, they find you.
- Primary button: Get my free check
- Secondary link: See the work
- Promise lines: Free, no strings. In 7 days you'll have a short written report on how you show up on Google. A starter site goes live in about 30 days. [CONFIRM]
- Map card (unchanged): bakery near me / Your bakery, Open now / On Main St, 2 min away / Call, Directions, Website.

---

## 3. Closing CTA

### What the best ones have in common
- The headline is an invitation in the owner's words, never "Contact us": Wishbone "Let's see if we're a fit.", Biite "Laten we samen kijken waar groei vastloopt" (let's look together at where growth gets stuck), BCG "Tell us about your project", No Jiggery "Tell me about your project", Potadot "Have a workflow that needs a system?", Relevo & Vinco "Let's press something." then "Tell us what goes in the box.", CE Growth "Start with a six-week diagnostic.", Two26 "Okay, that's enough website."
- The first step is named and small, and often has a time on it: a 15-minute call (Wishbone), half an hour and "no sales pitch" (Squared), a six-week diagnostic (CE Growth), a reply within two working days (Relevo & Vinco), a written analysis within 24 working hours (Kohen).
- A person shows up. Biite ends with the founder's portrait, a line about who it is for, and his LinkedIn. Revelatio shows Arthur's photo, name and role next to "Let's talk". Squared's last block is "Plan a call with Wouter". Wishbone and Two26 put a named email address (taylor@, bogdan@) in the section. This is "Firemark is Jeremy" done at the point of decision.
- Short inline forms on the local and service businesses (RIO: five fields; Relevo & Vinco: three; Son Daven: two), buttons to a booking page on the studios. Both work; a form with a promise next to it is the strongest combination in the set.
- One primary action and a quiet alternative ("or email", "Rather email or call?", "WhatsApp"). The weak ones offer three equal buttons (Revelatio's "Get a quote / Join our team / Just say hello").
- Bookends: the closing echoes the hero. Reckoner repeats its hero headline word for word; P+Z's "Your next move. Let's plan it." answers its hero's "We plan the way there."
- Biite's third bullet says it will point you to someone else if another specialist fits better. That one honest line does more for trust than any badge.

### Shortlist (8 of 27 closing sections reviewed)

| # | Site | Links | What to steal | What to skip | C | T | Cv | M | W | A | B | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Biite | [Awwwards](https://www.awwwards.com/sites/biite) / [live](https://biite.nl/) | Headline, three "what happens" lines (including "if someone else fits better, I'll say so"), primary + quiet secondary, founder portrait and LinkedIn. | Nothing. | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 4 |
| 2 | Relevo & Vinco | [Awwwards](https://www.awwwards.com/sites/relevo-vinco) / [live](https://relevovinco.com/) | A three-field form with a reply-time promise beside it, and a button that names the thing ("Send the brief"). | Heavy scroll animation elsewhere. | 5 | 4 | 5 | 4 | 3 | 4 | 5 | 5 |
| 3 | Wishbone Advisory | [Awwwards](https://www.awwwards.com/sites/wishbone-advisory) / [live](https://wishboneadvisory.com) | "Let's see if we're a fit." Low pressure, and the email address right there. | Embedded calendar (no booking tool yet). | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 3 |
| 4 | CE Growth Partners | [Awwwards](https://www.awwwards.com/sites/ce-growth-partners) / [live](https://cegrowthpartners.com/) | Naming the first step in the headline ("Start with a six-week diagnostic."). | The decorative word band under it. | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 3 |
| 5 | Squared Media | [Awwwards](https://www.awwwards.com/sites/squared-media-1) / [live](https://squared-media.nl) | "Half an hour, no sales pitch", and "Plan a call with Wouter": a named person. | WhatsApp, arrows. | 4 | 4 | 5 | 3 | 3 | 3 | 4 | 4 |
| 6 | RIO Property | [Awwwards](https://www.awwwards.com/sites/rio-property) / [live](https://www.rioproperty.co.za/) | The form as the closing section, with written success and error states. | Checkbox rows. | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 3 |
| 7 | Revelatio Studio | [Awwwards](https://www.awwwards.com/sites/revelatio-studio) / [live](https://revelatio.studio/) | A photo, name and role next to "Let's talk". | Three equal buttons after it. | 4 | 4 | 3 | 4 | 3 | 4 | 4 | 4 |
| 8 | No Jiggery (a company of one; Nominee Oct 21, 2026) | [Awwwards](https://www.awwwards.com/sites/no-jiggery) / [live](https://nojiggery.co/) | "Tell me about your project" + "Book a meeting with me". First person, one button. | Nothing to skip; it has no form, which is fine for them. | 5 | 4 | 4 | 4 | 5 | 4 | 5 | 3 |

Reviewed and cut: Brikken ("Have something worth shaping? Let's build it properly." with a list of welcome projects; worth a line in the copy below), BCG ("Tell us about your project" to a separate page), Potadot ("Have a workflow that needs a system?"), Two26 ("Okay, that's enough website."), P+Z ("Your next move. Let's plan it."), Reckoner (hero headline repeated, then a newsletter box), Son Daven, Comrade ("Ready to Grow?"), Signal-A ("Schedule a Discovery call" to an outside booking page), Right Hemisphere, Bennett & Clive (offices + email), Kohen (a paid form), The Line (a "Let's Talk" link), and the ones that end in a newsletter instead of a conversation (Banham, Impasto, Idealworks, Plumeform's footer band). LPAS has no closing action at all.

### Finalists
1. **Biite.** The best-structured closing section in the set and the one closest to Firemark's situation: a founder-led shop that wants to be chosen by the right people.
2. **Relevo & Vinco.** Proves a tiny form can be the end of the page if a promise sits next to it.
3. **Wishbone.** The tone. "Let's see if we're a fit" is how Jeremy already talks ("Let's talk" for the price).

### Final pick: "What happens next", with Jeremy in it
Draws from Biite (structure and the honesty line), Relevo & Vinco (short form + time promise), Wishbone (tone), P+Z and Reckoner (bookend with the hero), Squared (a named person).

This replaces the homepage's last section ("Get your free check.") and the `cta_band` on Work and About. The form itself (name, business, email, optional phone, optional site, optional note, honeypot) stays as it is in v7.

Desktop (1440): one Stone panel, radius 28px, two columns 5:7.
```
| Let's get your business on the map.         |  Your name*            [            ]   |
|                                             |  Business name*        [            ]   |
| Here's what happens next.                   |  Email*                [            ]   |
| 1. Jeremy looks up how your business shows  |  Phone (optional)      [            ]   |
|    up on Google today.                      |  Website or Google listing (optional)   |
| 2. Within 7 days you get a short written    |  Anything Firemark should know? (opt.)  |
|    report, yours to keep, whatever you do   |  [     Get my free check     ]          |
|    with it.                                 |  No payment, no account. [CONFIRM reply |
| 3. If a website makes sense, you get a      |  time]: Jeremy replies within one       |
|    written price before anything starts.   |  business day.                          |
|    If it doesn't, Jeremy will say so.       |                                         |
|                                             |                                         |
| [photo] Jeremy, The Colony                  |                                         |
| Rather email or call? hello@… · (phone)     |                                         |
```
- Headline: 620 weight, `clamp(1.9rem, 1.3rem + 2vw, 2.8rem)`. It answers the hero ("Put your business on the map." becomes "Let's get your business on the map.").
- The three lines are a real sequence, so numbers are right here (the frontend-design skill's rule: number things only when they are steps). Numbers in Ember, 620 weight; text in Charcoal, 17px.
- The person block: a 56px round photo [PLACEHOLDER: photo of Jeremy] with "Jeremy, The Colony" and the "Rather email or call?" line. If you would rather not use a photo, drop the image and keep the name line; the mark does not belong here (it is in the header and footer already).
- Form column: unchanged fields, white surface inside the stone panel, labels visible, validation on blur, error summary on failed submit (all already in v7). The submit button becomes "Get my free check" so the action keeps one name from header to hero to menu to form (v7 has "Request my free check" on the form and "Get my free check" everywhere else; pick one, and the shorter one is already in five places). Under the button, one 15px line: "No payment, no account. Jeremy replies within one business day. [CONFIRM]".
- Success state, in place of the form: "Thanks, {name}. Your free check is on its way. Jeremy will email it to {email} within 7 days." Error state stays as v7 has it.

Phone (390): headline, the three lines, then the form, then the person block and the email/call line. Panel radius 20px, side padding 20px, fields full width, button 48px.

On Work and About (no form): the same headline and lines 1 and 2 only, the "Get my free check" button, and the "Rather email or call?" line. Work's headline can stay specific: "Want a site like these? Start with the free check." About: "See how your business shows up today." Both then use the two lines, which fixes the repeated "short, plain-English report" the QA flagged (that phrase now appears only in the hero).

Draft copy, in full:
- H2: Let's get your business on the map.
- Lead: Here's what happens next.
- 1: Jeremy looks up how your business shows up on Google today.
- 2: Within 7 days you get a short written report. It's yours to keep, whatever you decide.
- 3: If a website makes sense, you get a written price before anything starts. If it doesn't, Jeremy will say so.
- Person line: Jeremy, The Colony
- Alt route: Rather email or call? [PLACEHOLDER: email] or [PLACEHOLDER: phone].
- Submit: Get my free check
- Under the button: No payment, no account. Jeremy replies within one business day. [CONFIRM]
- Success: Thanks, {name}. Your free check is on its way. Jeremy will email it to {email} within 7 days.

Motion: none, except the form's existing valid-field check and the error summary receiving focus. Under reduced motion, no change.

---

## 4. Footer

### What the best ones have in common
- Light sites keep a light footer. Ofform, Wisq, Balmoral Running, Bennett & Clive and Susanne Kaufmann end on white or a pale field; the dark footers belong to the dark or "agency" sites (Dobre, Wenatal, Emotion). Jeremy's rule is light over dark, and the current charcoal footer is the one dark band left on the site.
- Three short groups, not five columns of links. Relevo & Vinco (Workshop / Pages / Contact / Visit, each two to four lines), The Line (Reach out / Find us / Social / nav), Biite (nav / expertise / contact). The 24-link footers (Wishbone, Comrade, Banham, Idealworks) are for sites with 24 pages.
- The local businesses put place and reach in the footer: Relevo & Vinco's "Visit" column has the street address and opening hours; Impasto lists hours for every day; Potadot's address links to Google Maps and it lists the states it serves; Son Daven has the address with a map link; BCG writes "Gold Coast, QLD"; No Jiggery writes "Based in Fremantle Australia".
- A one-line story in the footer: Relevo & Vinco "pressed by hand and by press in Porto since 2014"; No Jiggery "an established company of one, founded by Sarah Jee"; Banham "Trusted, Since 1926"; Two26 "Handmade by humans. Well, digitally."; Wishbone "Built with intention." Bennett & Clive and No Jiggery put the founder's name in the footer.
- Columns named as actions read better than "Links" or "Company": The Line's "Reach out" and "Find us".
- A baseline row with the copyright on the left and small items on the right, and a "Back to top" link (LPAS, The Line, Relevo & Vinco, LAPL).
- The oversized wordmark at the bottom (Ofform, Dobre, Squared, Signal-A's marquee) is the 2025 to 2026 agency signature. It is a look, not a job, and three of the four live on dark pages.

### Shortlist (8 of 31 footers reviewed)

| # | Site | Links | What to steal | What to skip | C | T | Cv | M | W | A | B | D |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Relevo & Vinco | [Awwwards](https://www.awwwards.com/sites/relevo-vinco) / [live](https://relevovinco.com/) | Wordmark, one-line story, Pages, Contact (email + phone), Visit (address + hours), ©, Back to the top. The complete local-business footer in a few lines. | Nothing. | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 4 |
| 2 | The Line Studio (SOTM Nov 2024, 7.76, Footer highlighted) | [Awwwards](https://www.awwwards.com/sites/thelinestudio-com) / [live](https://thelinestudio.com/) | Columns named "Reach out" and "Find us"; Site Credits, Privacy and "Up" on the baseline. | Eight nav links. | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 3 |
| 3 | No Jiggery | [Awwwards](https://www.awwwards.com/sites/no-jiggery) / [live](https://nojiggery.co/) | "An established company of one, founded by Sarah Jee" and "Based in Fremantle Australia". Honest, specific, one line each. | The membership badge (nothing to show yet). | 5 | 5 | 3 | 4 | 5 | 4 | 5 | 3 |
| 4 | Bennett & Clive (SOTD Mar 12, 2024, 7.71, Footer & Contact highlighted) | [Awwwards](https://www.awwwards.com/sites/bennett-clive) / [live](https://bennettandclive.com) | The footer is the contact card: offices, "Work with us", the email, the founder's name. Light, typographic. | Three offices. | 4 | 5 | 4 | 4 | 5 | 4 | 5 | 3 |
| 5 | Potadot | [Awwwards](https://www.awwwards.com/sites/potadot-web-system-solutions) / [live](https://potadot.com.my/) | Address that links to Google Maps; a service-area list; "Est. 2022, Butterworth, Penang". | Five columns and the middle dots. | 4 | 4 | 3 | 3 | 4 | 4 | 4 | 3 |
| 6 | Wishbone Advisory | [Awwwards](https://www.awwwards.com/sites/wishbone-advisory) / [live](https://wishboneadvisory.com) | Email, phone and street address all present; "Built with intention." as the last line. | 24 links in three columns. | 4 | 4 | 3 | 3 | 5 | 4 | 5 | 2 |
| 7 | Ofform (description) | [maxibestof](https://maxibestof.one/sections/ofform-section-footer-wwlja1) | A light footer with three tiny columns and an oversized wordmark, proving the big-type footer works on white. | Suisse Int'l is a paid face; Bricolage would do the same job. Decide whether a huge wordmark is "cookie cutter" for you (see decisions). | 4 | 3 | 2 | 3 | 5 | 3 | 5 | 5 |
| 8 | Son Daven (SOTM Jun 2026; Footer, Location, Contact Block highlighted) | [Awwwards](https://www.awwwards.com/sites/son-daven) / [live](https://sondaven.com/en) | Address with a map link, and a two-field form that lives in the footer. | The FAQ accordion and sales offices in the footer. | 3 | 4 | 4 | 3 | 3 | 3 | 3 | 4 |

Supporting (descriptions): [Dobre Agency](https://maxibestof.one/sections/dobre-agency-section-footer-la6wfl) (near-black, thin contact row with "Melbourne", full-width cream wordmark: the dark agency look to avoid), [Wisq](https://maxibestof.one/sections/wisq-section-footer-oc4qac) (navy on white, three columns, compliance badges, dotted rule), [Balmoral Running](https://maxibestof.one/sections/balmoral-running-section-footer-hz9mwc) (white, three sentence-case link columns, one newsletter field, thin baseline), [Susanne Kaufmann](https://maxibestof.one/sections/susanne-kaufmann-section-footer-iny00p) (pale field, five groups, all caps: too much), [Wenatal](https://maxibestof.one/sections/wenatal-section-footer-i6vv91) (burgundy rounded panel: a color idea, not for this brand).

Reviewed and cut: Squared (three columns plus a giant "SQUARED"), Biite (numbered expertise column, company registration numbers), BCG, LPAS (two office blocks, "Website by Naam"), Impasto (hours for all seven days), Two26, Brikken (one line: logo, company number, socials), Comrade (six columns and "4.8 Rated from 218+ Reviews"), Banham (five columns and eight policies), Idealworks, Reckoner, Revelatio, Signal-A, Plumeform, LAPL, Right Hemisphere (five columns), CE Growth (logo, six links, email, legal), P+Z (no legal line at all).

### Finalists
1. **Relevo & Vinco.** Everything a local customer looks for in a footer, in four short groups.
2. **The Line Studio.** The naming. "Reach out" and "Find us" turn a link dump into directions.
3. **No Jiggery.** The one-line truth about who runs the place.

### Final pick: "Light footer, three short columns, one true line"
Draws from Relevo & Vinco (groups and Back to top), The Line (action names), No Jiggery and Bennett & Clive (the founder line), Potadot (place line). Also fixes the v7 QA note: the footer logo loads normally (no `loading="lazy"`), so there is no empty band on phones.

Desktop (1440), Stone background, 1px Line hairline on top, no charcoal:
```
|---------------------------------------------------------------------------------------------|
| [flame-pin] Firemark            Reach Jeremy                 Explore                        |
| Websites and Google listings    [PLACEHOLDER: email]         Work                           |
| for independent businesses      [PLACEHOLDER: phone]         What you get                   |
| in The Colony, Texas.           Replies within one           About                          |
|                                 business day. [CONFIRM]      Free check                     |
| Firemark is Jeremy, in                                       Privacy                        |
| The Colony, Texas.                                                                           |
|                                                                                              |
| © 2026 Firemark. Made in The Colony, Texas.                                   Back to top ↑ |
```
- Column 1: the full-color lockup (mark + capital-F wordmark) at 32px tall, then one sentence, then the true line "Firemark is Jeremy, in The Colony, Texas." in Charcoal, 600 weight. Drop "working across Dallas–Fort Worth" from the footer sentence; it is in the About copy and the footer reads better short. [CONFIRM you still want DFW here.]
- Column 2, "Reach Jeremy": email and phone as links (each at least 44px tall on phones), then the reply-time line. Column heading at 16px, 620 weight (keep the `<h2 class="footer-h">` pattern already in v7).
- Column 3, "Explore": the five links, 16px, 48px line height on phones.
- Baseline: 14px Graphite. If the OSM map is ever shown in the footer, its credit goes here; today it stays with the hero map.
- Colors: Stone #ECEAE6 ground, Charcoal text (15.6:1), Graphite small text (6.3:1 on Stone), Flame only in the mark and the link underline on hover. The `data-footer="charcoal"` switch is listed under decisions if you want the reverse mark on dark instead.

Phone (390), one column, short:
```
| [flame-pin] Firemark                     |
| Websites and Google listings for ...     |
| Firemark is Jeremy, in The Colony, Texas.|
| Reach Jeremy                             |
| email · phone (two links, stacked)       |
| Replies within one business day.         |
| Explore                                  |
| Work  What you get  About  Free check    |
| Privacy                                  |
| © 2026 Firemark. Made in The Colony.     |
| Back to top ↑                            |
```
- "Explore" links flow as a wrapped row rather than a stack, so the footer stays under one screen.

Draft copy, in full:
- Sentence: Websites and Google listings for independent businesses in The Colony, Texas.
- True line: Firemark is Jeremy, in The Colony, Texas.
- Heading 2: Reach Jeremy. Items: [PLACEHOLDER: email], [PLACEHOLDER: phone], "Replies within one business day." [CONFIRM]
- Heading 3: Explore. Items: Work, What you get, About, Free check, Privacy.
- Baseline: © 2026 Firemark. Made in The Colony, Texas. / Back to top

Motion: none. Link hover: underline in 120ms. Reduced motion: no transition.

---

## How the four sections work as one site

**Type.** Bricolage Grotesque only, self-hosted, already in place. Header links and footer headings 16px / 600 to 620. Hero H1 `clamp(2.5rem, 1.6rem + 3.6vw, 4.5rem)` at 620 / opsz 32 / tracking -0.03em. Closing H2 `clamp(1.9rem, 1.3rem + 2vw, 2.8rem)`, same cut. Body 17 to 19px / 1.55. Footer baseline 14px. The hero headline is the one place type is loud; the closing H2 is a clear step down, and the footer is quiet. Sentence case everywhere, no eyebrow labels (the hero's pin chip was the last one; it moves into the header as plain text).

**Color.** Paper (#F6F5F3) is the page. Stone (#ECEAE6) is the closing panel and the footer, so the page ends in a slightly deeper, calmer tone instead of flipping to charcoal. Charcoal for text and the mark's body. Ember (#B23F0E) for the one button that appears in all four sections and for the step numbers in the closing section. Flame (#EC4E1C) only where it already is: the fire in the mark, the hero pin and its glow, the current-page underline, the focus ring. Gold stays inside the mark. Count the orange on any screen: a button, a pin, a fire. Never more than three.

**Spacing.** Header 64px (56px on phones). Hero padding 5rem top on desktop, 2.5rem on phones, then the normal 6 to 8rem section rhythm. The closing panel sits inside the content width (84rem) with 2rem of Paper around it, so it reads as a card, not a band. Footer padding 4rem / 2.5rem. Measure under 70 characters everywhere; the hero support line under 60.

**The mark.** It appears four times, each time doing a job: in the header as the sign on the door (mark + wordmark); in the hero as the pin that drops onto Main Street (the same shape, in motion once); in the closing section as the Ember dot on the "Get my free check" button, which is the mark's fire reduced to a point; and in the footer as the full lockup again, so the page ends where it began. It is not pasted anywhere else, and it is not a watermark, a divider or a bullet.

**Vocabulary.** The action is "Get my free check" in the header, the phone menu, the hero, the closing section and the form's submit button. "See the work" is the only secondary. "Let's talk" stays the price answer. Jeremy is named in the closing section and the footer, never "we". "Short written report" is the hero's phrase; the closing section says "report, yours to keep"; Work and About say "free check" and no more.

**Motion.** One moment: the hero map. Everything else is a state change someone asked for (menu, form, hover). Transform and opacity only, 120 to 160ms, and nothing at all under reduced motion. No scroll-triggered reveals, no parallax, no marquee.

**Weight.** No new images, no new fonts, no new script. The header's scroll state is a class toggle. The closing panel and footer are CSS. The v7 phone performance (97 to 100) should hold or improve, since the footer logo stops lazy-loading and the hero adds no bytes. While the CSS is open, this is the moment to delete the 26 to 35 KB of unused v2 rules the QA pass found.

**Accessibility.** Every control at least 44px on phones; the header never covers a focused control (`scroll-padding-top`); the menu button has a name, `aria-expanded`, and returns focus; the form keeps its labels, blur validation and focus-managed error summary; contrast stays at 4.5:1 or better on Stone (Graphite is 6.3:1).

## The decisions I need

1. **Footer: light (recommended) or charcoal?** The research and your "light over dark" rule say Stone. Charcoal gives the reverse mark a stage. I can build the switch so it is one attribute either way.
2. **Hero headline:** keep "Put your business on the map." (recommended) or "Put your business on the map in The Colony."?
3. **The 30-day promise** in the hero: confirm the wording "A starter site goes live in about 30 days," or tell me the real range.
4. **Reply time** in the closing section and footer: "within one business day," or something else, or leave it out.
5. **A photo of Jeremy** in the closing section: yes (send one), or name only.
6. **Submit button:** "Get my free check" everywhere (recommended) or "Request my free check" everywhere.
7. **"Working across Dallas–Fort Worth"** in the footer sentence: keep or drop.
8. **Big wordmark footer:** the research found it on three of the four agency footers; I left it out as "cookie cutter". Say so if you want it anyway.

Once you answer, the build goes into Firemark-v2 (not the original Firemark folder) on top of v7: `src/index.html`, `src/pages.py` (the `cta_band` and the shared header/footer), `src/partials/form.html`, `docs/css/site.css`, rebuilt `docs/`, and the `?v=` bumped to 8. The original Firemark folder is not touched.

---

## Appendix A: every candidate reviewed

Awwwards page and live site, with what was read.

Read in full (header, hero, closing section, footer):
Wishbone Advisory · Biite · No Jiggery · BCG Building Design · Right Hemisphere · Kohen Avocats (family law page) · RIO Property · Potadot · Comrade Digital Marketing · Squared Media · Revelatio Studio · Brikken+Co · Signal-A · LPAS · Idealworks · Reckoner · Banham · Los Angeles Public Library · Son Daven · CE Growth Partners · Two26 · Relevo & Vinco · P+Z Fine Art Logistics · Plumeform · Impasto Forno Antico · Bennett & Clive · The Line Studio (27), plus Emotion Agency and Belgrade Arbor via their Awwwards pages and highlighted elements (29).

Live URLs: https://wishboneadvisory.com · https://biite.nl/ · https://nojiggery.co/ · https://bcgbuildingdesign.com.au/ · https://www.righthemisphere.studio/ · https://kohenavocats.com/avocats-droit-famille-paris/ · https://www.rioproperty.co.za/ · https://potadot.com.my/ · https://comradeweb.com/ · https://squared-media.nl · https://revelatio.studio/ · https://www.brikken.co/ · https://signal-a.studio · https://lpas.com/ · https://www.idealworks.com/ · https://reckoner.com/ · https://www.banham.co.uk/ · https://www.lapl.org/ · https://sondaven.com/en · https://cegrowthpartners.com/ · https://two26.studio/ · https://relevovinco.com/ · https://www.pnzfas.com/ · https://plumeform.com · https://www.impastofornoantico.com/ · https://bennettandclive.com · https://thelinestudio.com/ · https://emotion-agency.com/ · https://belgradearbor.rs/en

Awwwards pages: /sites/wishbone-advisory · /sites/biite · /sites/no-jiggery · /sites/bcg-building-design · /sites/right-hemisphere-1 · /sites/avocats-en-droit-de-la-famille · /sites/rio-property · /sites/potadot-web-system-solutions · /sites/comrade-digital-marketing · /sites/squared-media-1 · /sites/revelatio-studio · /sites/brikken-co · /sites/signal-a-studio · /sites/lpas · /sites/idealworks · /sites/reckoner-capital-management · /sites/banham-1 · /sites/los-angeles-public-library · /sites/son-daven · /sites/ce-growth-partners · /sites/two26-studio · /sites/relevo-vinco · /sites/p-z-fine-art-logistics · /sites/plumeform · /sites/impasto-forno-antico · /sites/bennett-clive · /sites/thelinestudio-com · /sites/emotion-agency-1 · /sites/belgrade-arbor (all under https://www.awwwards.com)

Reviewed on Awwwards only and excluded as showpieces (3D, WebGL, scroll-jacking or video-led): A24 (/sites/a24), Why Zero (/sites/why-zero), Agrumea Farm (/sites/agrumea-farm), Kigo Studio (/sites/kigo-studio), Gray. (/sites/gray), Henrietta Said (/sites/henrietta-said), Where Opportunity Takes Root (/sites/where-opportunity-takes-root), Dropbox Brand (/sites/dropbox-brand), Pamidor Design (/sites/pamidor-design, live site refused), Garvin Promotion Group (/sites/garvin-promotion-group, live site errored), Nova Dental (/sites/nova-dental, live site refused).

maxibestof section pages read: Hero (38 entries), Footer (37), Call to Action (29); the Header section errored. Entries described above: Brand Appart, House of Honey, Duft und Kultur (hero); Dobre, Ofform, Wisq, Wenatal, Susanne Kaufmann, Balmoral Running (footer).

## Appendix B: the Dribbble shots your PC captured (not judged)

These loaded as images on your PC but returned nothing to me, so they did not influence the picks. Files are `research-shots\dr-<id>-d-shot.jpg`.
- https://dribbble.com/shots/23321827-Digital-Agency-s-Hero-Section-Concept
- https://dribbble.com/shots/22994751-Website-hero-section
- https://dribbble.com/shots/24300732-Website-Hero-Section-District47-Agency
- https://dribbble.com/shots/21694589-Minimal-footer-Untitled-UI
- https://dribbble.com/shots/24161794-Simple-Footer-Design-for-Agency-Website
- https://dribbble.com/shots/17531323-Neringa-Website-Footer-Design
- https://dribbble.com/shots/22843763-Digitant-Call-to-Action-CTA-Section
- https://dribbble.com/shots/11475978-30-Days-of-Art-4-Call-to-Action-CTA-and-Simple-Footer
- https://dribbble.com/shots/21935626-Header-navigation-menu
- https://dribbble.com/shots/19520859-Header-Navigation
- https://dribbble.com/shots/23555844-Minimal-Design-Agency-Responsive-Page-Website
- https://dribbble.com/shots/20235514-Landing-Page-Website-Photography-Service
- https://dribbble.com/shots/3123681-Small-business-website

## Appendix C: fonts seen on the examples and free stand-ins

Paid faces named on the maxibestof entries: GT America, GT Alpina (Dobre); Suisse Int'l (Ofform); Söhne (Wisq); PP Neue Montreal (Balmoral, Brand Appart); Waldenburg, ABC Marist (Thirdway); Focal (Caffè Uno). Google Fonts stand-ins if you ever need a second face: Instrument Sans or Inter for the grotesques, Fraunces for the serif roles. Firemark does not need any of them; Bricolage Grotesque's weight and optical-size axes already cover every role on the page.
