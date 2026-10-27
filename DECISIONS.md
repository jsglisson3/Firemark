# Decisions (v2)

Why the site looks, reads and works the way it does. Newest first within each section.

## Made with Jeremy (Oct 26, 2026)

| Decision | Why |
|---|---|
| Rebuild from scratch as v2, keep v1 | Start clean with the new design skills, and keep v1 to compare. |
| Direction C, "On the Map" | The promise ("get found") is literally in the hero: someone searches, and the business shows up on the map. Friendly, bold and local, and unlike the cream-and-serif look most new sites have. |
| Logo: a real fire inside a map pin | Merges the 1752 fire mark (a sign that someone has your back) with today's map pin. Jeremy asked for a real orange fire. |
| Pricing: "Let's talk," no numbers | The quote comes after the free check, in writing, before anything starts. |
| About: first name only, brand first | No day job, no life story, never "we." One short "Who you'll work with" section. |
| Career facts stay general | Kept on the About page, but without team sizes, dollar figures or project counts. |
| Timelines | The free check report arrives within 7 days. Most starter websites go live about 30 days after the go-ahead. |
| Area: The Colony first | Every page leads with The Colony. The footer, FAQ and contact page say Dallas–Fort Worth. |

## Design

- **One memorable thing per page.** On the homepage it's the map. Everything around it stays quiet. (Frontend Design skill: spend boldness in one place.)
- **One orchestrated animation**, on the homepage map only: the search types itself, pins drop, the Firemark pin lights up and the result card slides in, about 3 seconds, then it stops. Only transform and opacity move, so nothing shifts on the page (layout shift measured at 0). With reduced motion on, the finished map shows immediately.
- **Colors from the place.** The Colony sits on Lewisville Lake, so the base is lake teal, deep blue-green and a pale mist, with flame orange as the only hot color, used for buttons and the logo's fire. Every text color passes WCAG AA; most pass AAA (numbers on the brand sheet).
- **One typeface, Bricolage Grotesque.** Heavy, friendly headlines and a readable body from one 76 KB file. Self-hosted, so no outside requests.
- **Radius hierarchy:** 28px panels, 18px cards, 14px buttons, round chips. Things get rounder as they get bigger, instead of one radius on everything.
- **Template tells avoided on purpose:** no all-caps labels above headings, no arrows tacked onto buttons, no middle-dot strings, no fake stats, and numbers only where the content really is a sequence (the customer's path, the four steps, the contact page's "what happens next").
- **Phone header:** logo, "Free check" and a labeled Menu button fit on one line down to 384px. Below that, the Menu button shows only its icon (screen readers still hear "Menu"). Below 335px the header button hides, and the free check is still in the menu, the hero and the footer.

## Skills and sources

- **UI UX Pro Max:** used for the page pattern (problem, then solution, then action, with one main call to action), its local-service rule (show a map), the accessibility, touch-target and form rules, and the "Master + Overrides" design-system file (`design-system/firemark/MASTER.md`). Its default palette suggestion (green and orange with Inter) was rejected as generic.
- **Frontend Design:** the design plan, then a self-critique against generic defaults before building, plus screenshot reviews at phone and desktop sizes after every change.
- **Awwwards and Dribbble:** browsed Awwwards Sites of the Day and Dribbble searches (local business sites, map-pin and flame marks) for ideas, not copies. What carried over: one big idea instead of many effects, very large confident headlines, lots of space, and real work shown as real screenshots instead of stock photos.
- **Baymard Institute (forms):** visible labels; required fields marked with * (plus hidden "required" text) and optional fields marked "(optional)"; checks run when a field is left, not while typing; errors clear as soon as they're fixed; valid fields get a check mark; a failed submit shows a summary that links to each problem. Only three fields are required.
- **Lighthouse (phone):** performance 99–100, accessibility 100, best practices 100. SEO is 100 once the draft "noindex" tag is removed (tested on a copy).

## Content rules

- Every claim is true. Anything unknown is a yellow **[PLACEHOLDER]**. Any promise Jeremy must approve is a yellow **[CONFIRM]**. All of them are listed in PICKUP.md.
- Facts about Jeremy come only from the brief's list. No employer names anywhere.
- Left out on purpose: testimonials, reviews, client logos, ratings and stats (there aren't any yet), prices, stock photos, analytics and a cookie banner (the site sets no cookies today). Oct 26: the privacy page no longer promises "no cookies or tracking", so analytics can be added later; add a privacy section if they are.

## Technical

- Hand-built HTML, CSS and a small script. No framework, no build step needed to view it. `tools/build.py` only stitches shared pieces (header, footer, form, icons) into each page.
- The site lives in `docs/` so GitHub Pages can publish just that folder.
- The free check form has no service behind it yet. Until one is added, submitting opens a pre-filled email to Firemark, and shows the address as a link in case no mail app opens. A hidden "leave this empty" field stops simple spam bots.
- Every page is "noindex" until launch, so search engines skip the draft.
- The 404 page uses links that start with `/`, so it works at any address on the final domain.


# DECISIONS addendum: v3 look (Oct 26, 2026)


## Palette: light paper, charcoal, subtle orange
- **Decision:** drop lake teal and deep blue-green. Paper #F6F5F3 and Stone #ECEAE6 backgrounds, Charcoal #1D1C1A text and buttons, Graphite #57534E for secondary text. Orange is the accent only: Flame #EC4E1C, Ember #B23F0E for small text and icons on light (it passes AA), Gold #FFB22E for the logo core and on dark.
- **Why:** Jeremy said he doesn't like the blue, wants "subtle orange and black gray" that works with the logo's flame, and prefers lighter designs over heavy dark ones. The orange is kept rare so it reads as "the spot" on the map.
- Old CSS variable names (--mist, --teal, --deep, --shore) still exist as aliases of the new colors, so nothing else broke.
- Only the footer stays dark (charcoal). The problem, check and "Why the name" sections moved from dark bands to Stone.

## Logo: the flame pin (variant A)
- **Decision:** a charcoal map pin whose hole is a flame, with a gold core, plus a lowercase "firemark" wordmark in Bricolage Grotesque 700, outlined to paths. Three variants (A, B, C) are in design-system/firemark/logo-variants/ for comparison. A is recommended because it reads at 16px and works in one color.
- Files: horizontal lockup, reverse, one-color dark and white, symbol (same four), favicon.svg (switches for dark browser tabs), favicon PNGs, and a "Site by Firemark" badge.
- **[CONFIRM]** Jeremy approves A and the lowercase wordmark.

## Hero: the street map
- **Decision:** Concept 1 of 3. A quiet drawn street map of a Colony-style grid with Main St, S Colony Blvd and Hwy 121. A flame pin drops onto Main St, then a listing card appears ("Your bakery, Open now, Call / Directions / Website"). The headline is still "Put your business on the map."
- **Why:** it shows the literal promise (being found on a map) instead of talking about it, and it is the one memorable element. The rest of the page stays calm.
- Round 3 replaced the drawn map with real streets (see below).
- Motion: one load sequence (pin, ring, card at 350/600/900 ms), shown once. With reduced motion or no JavaScript, the final state shows at once.
- Concepts 2 and 3 were reference only and are not kept in the repository.

## Round 3: Jeremy's notes (Oct 26, evening)
- **Hero: concepts 1 and 2 blended.** Jeremy liked both and not 3. The listing card now starts as a search: "bakery near me" types in, the pin drops onto Main St, and "Your bakery" appears as the result with Call / Directions / Website. One sequence of about 2 seconds, played once.
- **Real streets.** Jeremy chose real streets over the drawn map. The hero map is traced from an OpenStreetMap export he downloaded on Oct 26, 2026, covering Main St and S Colony Blvd (bounds 33.0721 to 33.0875 N, 96.9023 to 96.8686 W). It shows real roads, buildings and the Lewisville Lake shoreline, in the same quiet style. The pin is on the real Main St × S Colony Blvd intersection.
  - **License:** OpenStreetMap data is under the ODbL. That requires the visible credit "Map data © OpenStreetMap contributors", linked to openstreetmap.org/copyright. It sits under the map on the homepage and on the share image. Don't remove it.
  - The source file and the two scripts that turn it into the SVG are in design-system/firemark/map-source/.
- **Orange buttons by default.** Burnt orange (Ember #B23F0E, white text 5.6:1) with a gold dot. The charcoal version is kept as the switch `data-buttons="charcoal"` on `<html>`.
- **Less cartoony type.** Jeremy found the text cartoony. Headings were Bricolage at weight 800 with the optical size at 96 (the poster cut, with ink traps and squeezed letters). They are now weight 620 with optical size pinned at 32, a calmer cut of the same font, so the one-typeface rule still holds. The "firemark" wordmark was re-outlined at weight 660, optical size 32, and the badges were redone to match. Other faces were tried (Inter Tight, Geist, Instrument Sans, Schibsted Grotesk). The calmer Bricolage cut was kept because it fixes the problem without adding a second font.

## Buttons (superseded in round 3: orange is now the default)
- **Decision:** primary buttons are charcoal with white text and a small orange ember dot, not solid orange. Secondary is a charcoal outline.
- **Why:** keeps orange subtle, per Jeremy's note. **[CONFIRM]** if he wants more orange.
- Plain Flame orange is never used for buttons, because white text on it fails contrast.

## Polish pass (same day)
- Redrew the side streets as a believable suburban network: gently bowed streets that meet the main roads, short cross streets and cul-de-sacs. The first version used loose wavy lines that read as texture, not streets.
- Removed the map's tinted background, which left a visible seam beside the headline. The map is now lines on the page color.
- Small laptops (about 990 to 1150px wide): the card moves under the pin so it isn't clipped, the map slides right, and the lead gets narrower so no streets run behind it.
- Road names are hidden on phones (the card already says "On Main St"). S Colony Blvd's name only shows when it fits on screen.
- Fixed the logo mark being cut off on its left side wherever it was used inline (story art, "The Colony, Texas" line).
- Fixed a flash on load where the pin and card showed, vanished, then dropped in. A two-line script in the page head now hides them before first paint, with a 3-second safety net.

## Research takeaways (full notes in design-system/firemark/RESEARCH-v3.md)
- Strong local-business award winners lead with one specific, real-world image of the place, not stock photos or gradients.
- Best-in-class heroes use one confident idea and one motion moment, with plenty of space around it.
- Awwwards and Dribbble pages could not be loaded visually from this environment. Research was done from Awwwards' text pages and other sources, and the notes say which.

## Checks run
- axe-core: 0 violations on every page at 390px and 1440px.
- No sideways scrolling at 320, 360, 390, 1440 and 1920px. Hero screenshots checked at 320, 390, 768, 1024, 1100, 1240, 1280, 1440 and 1920.
- Motion: with reduced motion, the pin, glow and card are fully visible at once. Without JavaScript they're visible too. With motion, they start hidden and are all in place by 2 seconds.
- Lighthouse mobile (local, after round 3): Performance 99, LCP 2.2s, total page weight 207 KiB, Accessibility 100, Best Practices 100, SEO 69 (low only because the draft is noindex). CLS 0.


# DECISIONS addendum: v4, simpler site

Append this to DECISIONS.md, after the v3 addendum.

## Round 4: simpler (Oct 26, 2026, late evening)
Jeremy said the site felt cookie-cutter and asked for it to be simpler. The homepage went from ten sections to five: the map hero, Recent work, What you get, "Firemark is Jeremy" (with the fire-mark story), and the free check form. It's about 40% shorter on desktop.
- **Cut from the homepage:** the 3-step "customer's path" section (the hero already says it), the two-column offer with icons, the 4-step "How it works" route, the separate pricing panel, the "Who you'll work with" chips, and the 6-question FAQ.
- **Merged:** the offer and price are now one plain list that ends in "What it costs: Let's talk." Who Jeremy is and why the name now share one section.
- **Moved:** the four most useful questions now live on the contact page, next to the form. The "What happens next" steps stay there too, since they really are a sequence.
- **About:** the 6-item "What you can count on" grid and the good-fit/not-a-fit tick lists became three short paragraphs.
- **Nav:** Work, What you get, About, and the free check button.
- **Kept on purpose:** the real-streets map, the search-to-result moment, the fire-mark story and the case studies. That's where the personality is.

- **Cache:** site.css and site.js are now linked as `?v=4`. Bump that number in src/index.html and tools/build.py whenever either file changes, so returning visitors get the new version.


# Logo update (v6, Oct 26, 2026)

The logo is now the flame pin with a capital-F "Firemark" wordmark. Full notes, runner-ups and small-size rules: design-system/firemark/DECISIONS-v6-logo.md. This replaces the logo entry in the v3 addendum above.


# Work as a simple list (v8, Oct 26, 2026)

Jeremy plans to keep adding sites and can't write a case study for each, so Work and the homepage's "Recent work" are now a plain list: one card per site with a screenshot, the name, one short line (what kind of business, where) and a link. The case-study write-ups (the job, what was built, the feature screenshots) are gone. The list comes from `src/sites.py`, so adding a site is one copied block plus a screenshot (steps in PICKUP.md). The homepage shows the first 4; Work shows all. Concepts keep the "not the official site" tag. CSS and JS are now `?v=8`.


# Header, hero, closing CTA and footer (v9, Oct 27, 2026)

Built from `design-research.md` (Awwwards and Dribbble research, 20 or more candidates per section, scored and linked). Jeremy's calls from Oct 26 and 27 are in the build:
- **Header:** logo, three links (Work, What you get, About), "The Colony, Texas" in small text from 64rem, and the orange button. The header blurs what scrolls under it, with a solid Paper fallback. On phones the Menu button opens a Paper sheet under the header: the three links large, then a full-width "Get my free check", the email and phone, and the place. Escape closes it and hands focus back to the Menu button; so does a tap outside, or tabbing past it.
- **Hero:** headline stays "Put your business on the map." The chip above it is gone. Under the two buttons sit the two promises: the written report within 7 days, and a starter site live in about 45 days (changed from 30 on Oct 26). "See the work" carries a small down arrow, the one arrow on the site, because it points where the page goes.
- **Closing CTA:** one Stone card at the end of the homepage: "Let's get your business on the map.", "Here's what happens next." with the three numbered steps (a real sequence), a round photo of Jeremy with "Rather email or call?", and the form in a white card. Work and About end with a shorter card: heading, two steps and the button. The submit button says "Get my free check" on every page, with "No payment, no account. You'll hear back within 5 days." under it.
- **Photo:** Jeremy chose a photo over name-only (Oct 27). Until there is a headshot, `docs/images/jeremy.webp` is a gray circle that says it is a placeholder, and the name line carries a [PLACEHOLDER: photo] tag. The earlier stand-in was a stock photo of a stranger; it is gone. One file serves the homepage (small) and About (large).
- **Footer:** Stone, not charcoal (Jeremy picked A Stone from three options). Three columns: the logo with the Dallas–Fort Worth line and "Firemark is Jeremy. Small on purpose."; Reach Jeremy (email, phone, "You'll hear back within 5 days."); Explore (Work, What you get, About, Free check, Privacy). The baseline keeps the year and "Back to top". No oversized wordmark.
- **Form service: Web3Forms.** The form posts to Web3Forms with a hidden access key (a [PLACEHOLDER] until Jeremy pastes his), a subject line that names the business, two honeypots, and a redirect to `thanks.html` for browsers without JavaScript. With JavaScript the thanks line shows in place. Until the key is in, the script falls back to the pre-filled email. The privacy page names Web3Forms, with a [CONFIRM] on how long it keeps messages.
- **Nothing dark anymore.** The homepage is Paper with Stone bands (What you get, the closing card, the footer). The dark story band from v3 is gone, and so is the CSS for sections that no longer exist (`tone-deep`, `btn-ghost`, the old cta-band, pricing, route and FAQ grid rules).
- Cache: `?v=9`.

## Checks run (v9)
- axe-core: 0 violations on all eight pages at 390px and 1440px, and on the homepage with the phone menu open.
- Keyboard: desktop Tab order is skip link, logo, Work, What you get, About, the button, then the hero. On phones, Enter opens the menu, Escape closes it and returns focus, tabbing past the sheet closes it. The focus ring is the 3px Flame outline everywhere.
- Links to parts of a page land under the sticky header (scroll padding 72px on phones, 80px on desktop), including after the smooth scroll from the header button.
- No sideways scroll at 320, 390, 1100 or 1440. Reduced motion shows the finished map at once. No console errors or failed requests on any page.


# Overnight redesign (v10, Oct 27, 2026)

Full write-up: `FIREMARK-REDESIGN-PLAN.md`. Open items: `REVIEW-v10.md`. Kept as settled: light paper and charcoal with subtle orange, the flame pin logo, "Put your business on the map.", "Let's talk" pricing, first name only, the 7-day report, 5-day reply and about-45-day site, "Get my free check", the Stone footer with the Dallas–Fort Worth line.
- **Map in the headline.** A word-sized tile of the real corner sits after "Put your business", and the map band below performs a search. Visitors can try their own trade.
- **Name story off the homepage** (Jeremy, Oct 27: "not even sure if I want the whole why the name"). Replaced with "One person, start to finish." and five questions all answered "Jeremy". A short version stays on About, with the history corrected (the 1750s Philadelphia fire insurance company Franklin helped start).
- **Sample free check report** on the homepage, captioned as a made-up bakery.
- **No placeholder text on the page.** Contact settings in `tools/build.py`; empty means hidden; the build refuses placeholder tags. The headshot spot is a stone tile with the pin until `HEADSHOT = True`.
- **Children removed** from the Friends of the Library screenshots (photo circles blanked) until the Friends say otherwise.
- **Form:** "(required)/(optional)" in words, a "What would help most?" pick list, and an error title that counts the fixes.
- Cache: `?v=10`.

# Homepage top rebuilt (v11 and v12, Oct 27, 2026)

Jeremy: the header, hero and map "does not look that great ... redo the entire thing". Three directions were previewed (Maps panel, Split, Phone); he picked the Maps panel and v11 shipped it. v12 pushes it further:

- **The map is now the real thing.** `docs/images/map/the-colony.svg` is drawn from the full OpenStreetMap export (`design-system/firemark/map-source/render_full.py`): every building, the parks and Lewisville Lake shoreline, roads by size, the Sam Rayburn Tollway, and gray dots where real shops and restaurants are. Street names are HTML, so they use Bricolage. The old hand-traced `src/partials/map.svg` is gone; the 404 and thanks pages use the new map too.
- **Composition:** headline, lead, button and the two promises sit on the page at left; the map fills the right side with the search box and trade buttons floating on it, as in Google Maps. Phones: map on top, words underneath.
- **Listing card:** name, category, "Open · Closes 6 PM", and Directions / Call / Website, like a real Maps result. The trade buttons change the search, name, category and hours.
- **Motion:** the map flies in to Main St, the search types, the pin drops and the glow pulses. Reduced motion shows the finished picture.
- **Removed:** the five "Who...? Jeremy" cards. "Jeremy" now appears once in the About blurb, in the sample report's signature and next to the form. Footer heading "Get in touch". Header: Contact link added, the small "The Colony, Texas" line removed (the hero says it).

## V13 map feedback (Oct 27, 2026)
- **Pin stands clear of the streets.** The flame pin has a thin white outline, and every business sits on a lot beside its street instead of on the road line.
- **Each trade is on its own street.** Bakery on Main St, barber on S Colony Blvd, plumber on Paige Rd, nail salon on Clover Valley Dr, taco shop on Worley Dr (real OpenStreetMap streets). Picking a trade glides the map to that spot, so it doesn't look like one plaza. Spots and street names are `data-x`/`data-y`/`data-street` on the trade buttons in `src/index.html`; any street name the pin would cover hides itself.
- **Google Maps and Apple Maps, said plainly.** A note at the top of the map reads "What customers see on Google Maps and Apple Maps", and the intro sentence names both, so the map isn't mistaken for a Firemark product. No Google or Apple logos.

## V14 map blends in (Oct 27, 2026)
- **No box around the map.** The map's colors are softer (lighter buildings, no outlines, gentler roads) and it fades into the page on the left, top and bottom, so it reads as part of the page.
- **Google Maps / Apple Maps switch** replaces the "What customers see on..." note. It shows the same listing laid out each app's way (Apple: a sheet with a grab handle and tile buttons). No Google or Apple logos.

## V15 top half rebuilt (Oct 27, 2026)
- **The map runs behind the whole top of the page** and fades out under the words, so the hero is one picture instead of text beside a box.
- **One panel, like a maps app's results:** the search, the five trades and your listing sit together in a single white panel; the pin is on the map beside it. The Google/Apple switch is gone.
- **"Where customers find you: Google Maps, Apple Maps"** sits at the bottom right of the map as plain names. The official logos aren't used: Google and Apple both require permission for their logos, and the names say the same thing.
- **Phones and tablets:** the words come first, then the map with the panel resting on it.
