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
