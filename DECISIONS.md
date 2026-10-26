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
- Left out on purpose: testimonials, reviews, client logos, ratings and stats (there aren't any yet), prices, stock photos, analytics and a cookie banner (the site sets no cookies).

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
- The map is drawn, not traced from real map data, so there are no license questions. It is not geographically exact. **[CONFIRM]** whether Jeremy wants it traced from the real streets later.
- Motion: one load sequence (pin, ring, card at 350/600/900 ms), shown once. With reduced motion or no JavaScript, the final state shows at once.
- Concepts 2 and 3 were reference only and are not kept in the repository.

## Buttons
- **Decision:** primary buttons are charcoal with white text and a small orange ember dot, not solid orange. Secondary is a charcoal outline.
- **Why:** keeps orange subtle, per Jeremy's note. **[CONFIRM]** if he wants more orange.
- **Alternative built and ready:** burnt-orange buttons (Ember #B23F0E with white text, which passes AA, and a gold dot). Switch on by changing `<html lang="en">` to `<html lang="en" data-buttons="orange">` in src/index.html and tools/build.py, then rebuild. Plain Flame orange is not used for buttons, because white text on it fails contrast.

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
- Lighthouse mobile (local, after the polish pass): Performance 99, Accessibility 100, Best Practices 100, SEO 69 (low only because the draft is noindex). LCP 2.0s, CLS 0.
