# Research: hero, header and logo (Oct 26, 2026)

What I looked at before redesigning Firemark's hero, header and logo, and what each one taught.

**What I could and couldn't see.** I read Awwwards' current Sites of the Day list (Sep 26 to Oct 26, 2026) and the award pages for the local-business winners, including their jury scores, tags and listed palettes. Awwwards and Dribbble block screenshots from my cloud workspace, and Dribbble's search pages don't load without a browser. So the Dribbble notes are based on shot titles and the patterns they name, plus what I already know of well-known marks. I haven't described any visual I couldn't check.

## Awwwards: what local businesses that win are doing

Four of the last 31 Sites of the Day are for local businesses: a body shop, a custom-car shop, a clinic and a residential development. That makes them the closest award-level match for Firemark's clients.

| Site | What it is | What it teaches Firemark |
|---|---|---|
| [ESR Bespoke](https://www.awwwards.com/sites/esr-bespoke) (SOTD Oct 23, 2026) | Luxury body shop, Australia | Its palette is only black and white (#000, #fff). A trade business looks premium through restraint, not effects. **Applied:** charcoal and white do the work, and orange appears in only a few places. |
| [Forge Automotive](https://www.awwwards.com/sites/forge-automotive) (SOTD Oct 25) | Custom car shop, UK | Two colors (#0C0C0C and #410306), with the brand's craft as the story. **Applied:** the 1752 fire mark is Firemark's craft story, so it sits in the logo instead of being decoration. |
| [Odyssée](https://www.awwwards.com/sites/odyssee) (SOTD Oct 8) | One clinic | Two colors (#1E305E and #F6F4F2), a calm layout, and its suburb named up front. Local and premium aren't opposites. **Applied:** "The Colony, Texas" sits right at the top of the hero. |
| [Belgrade Arbor](https://www.awwwards.com/sites/belgrade-arbor) (SOTD Oct 17) | Residential development, Belgrade | Light paper (#F4F0DB) with one dark ink. Light can still feel expensive. |
| [twks](https://www.awwwards.com/sites/twks) (SOTD) | Studio | Black, white and a single red-orange (#D14836) used sparingly. This is the closest match to "subtle orange with black and gray." |

**The catch:** the jury gives these sites their lowest marks for accessibility (ESR 6.4/10, Emotion Agency 6.6, Belgrade Arbor 6.8) and usability. Most of them get their wow from heavy WebGL and scroll-jacking. Firemark's customers are on phones and aren't technical, and the brief asks for Lighthouse 95+ and WCAG AA. **Takeaway:** borrow the restraint, scale and confidence, and leave out the heavy 3D. The wow comes from one crafted moment that loads instantly.

## Award-winning patterns worth taking

- **Type as the image.** [Pangram Pangram](https://www.awwwards.com/sites/pangram-pangram-foundry) (Site of the Day, Nov 11, 2021), Obys' [FORMAT](https://format.obys.agency/) (SOTD Oct 19) and [Uncommon Studio](https://uncommonstudio.com.au/) set headlines so large they become the picture. Bricolage Grotesque at weight 800 and optical size 96 can carry that. **Applied:** the headline is the biggest thing on the page, and the logo's flame pin becomes its full stop.
- **One orchestrated moment.** [By-Kin](https://by-kin.com/), praised as a "masterclass in restraint," and [Lando Norris](https://www.awwwards.com/sites/lando-norris) (Site of the Day, Nov 17, 2025, scored 8.18) each have one interaction done very well, not ten. **Applied:** one sequence of about 1.5 seconds, played once: the pin drops onto Main St, a soft glow opens under it, and the listing card appears. With reduced motion turned on, the finished picture shows straight away.
- **Show the result, don't describe it.** Dribbble's 2026 Select picks ([Bearplus' CargoKite](https://dribbble.com/shots/24525873-CargoKite-Homepage-Design-Ocean-Transportation-Website-Design), [Excited's AI simulation landing page](https://dribbble.com/shots/26888374-Landing-Page-for-an-AI-Simulation-Platform)) explain the product with a demo inside the hero. **Applied:** the hero shows the result Firemark sells: your business on the map, with a "Call / Directions / Website" card.
- **Floating header.** Most recent agency Sites of the Day use a slim header that sits over the hero and becomes a solid bar on scroll. **Applied:** a slim, sticky, light header with the logo, four links and one button. It is slightly see-through, and a hairline border appears once you scroll. I didn't overlay it on the hero, because the map would show through behind the links on phones.

## Logo research (Dribbble and classic marks)

- **Pins on Dribbble** ([Mike Bruner's pin tag](https://dribbble.com/mike-bruner/tags/pin), [map pin kits](https://dribbble.com/mario93)): most pin logos are a letter or an icon dropped inside a pin. That's the most common move, and the previous Firemark logo did it too (fire inside a pin).
- **Flames on Dribbble** ([le feu](https://dribbble.com/shots/6936298-le-feu-Flame-Logo), [E Flame mark](https://dribbble.com/shots/2793445-E-Flame-Logo-Mark), [Superhot](https://dribbble.com/shots/22314638-Superhot-Flame-Logo-Design-2)): the best flame marks are one silhouette with one or two tongues and no outline. Gradient flames, Tinder's especially, are the cliché to avoid.
- **The idea that came out of it:** a flame and a map pin are the same shape upside down. A flame is round at the bottom and pointed at the top, and a pin is the reverse. Give one silhouette a flame's top and a pin's point, and it reads as both at once. No letter inside and no badge around it. It's one shape, so it works at 16 pixels, cut as a truck decal, and in one color.
- **The 1752 fire mark:** the original was a cast plaque nailed to the front of a building. The recommended logo's charcoal body is the mark, and the fire is lit inside it. Variant C puts the symbol on a plaque, for stickers, the app icon and the client badge.

## What I deliberately didn't take

- **WebGL, 3D and scroll-jacking.** These are behind most of the jury's "wow," and also behind their low accessibility and usability scores. They would also wreck load time on a phone with one bar of signal in a parking lot.
- **Dark, full-bleed heroes.** ESR and Forge are dark, but Jeremy prefers light, and a bakery or barber site has to feel friendly, not like a sports car.
- **Generic AI-site tells.** I checked the hero against the usual giveaways: a warm cream page with a serif headline and a clay accent, a dark page with one neon accent, uppercase eyebrow labels, rows of identical rounded cards, gradient washes, arrows tacked onto button text, and numbered markers on things that aren't steps. None of these are in the hero. The one label above the headline ("The Colony, Texas") stays because it carries real information.

## Palette research

- Jeremy's direction (Oct 26): light, charcoal and gray, subtle orange, and an orange that suits the logo's flame.
- Award-winning light sites use a neutral paper, never pure white, with one near-black ink (ESR, Odyssée, Belgrade Arbor). I avoided the warm cream background (around #F4F1EA) that most AI-made sites use right now, and picked a cooler stone instead.
- Orange is used in at most four places on the hero: the logo's fire, the pin, the focus ring and one small detail. Buttons are charcoal. That's what keeps the orange subtle.

Sources: [Awwwards Sites of the Day](https://www.awwwards.com/websites/sites_of_the_day/), the award pages linked above, [Awwwards design agencies](https://www.awwwards.com/websites/design-agencies/), [Dribbble Select best shots 2026](https://dribbble.com/resources/agencies/ultimate-dribbble-select-best-shots), [Hon Tran's 2026 award picks](https://www.hontran.dev/blog/best-award-winning-websites-2026), [Wavespace: black and orange websites](https://www.wavespace.agency/blog/black-and-orange-websites).
