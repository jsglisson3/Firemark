# Firemark design system: MASTER

The single source of truth for how Firemark looks and behaves. Built with the UI UX Pro Max "Master + Overrides" pattern, then hand-tuned for direction C ("On the Map"). Before building a page, read this file, then check `pages/<page>.md`. If a page file exists, its rules win.

UI UX Pro Max's default suggestion for this query was green and orange with Inter. It was rejected as a generic default. Its structural rules (funnel pattern, local-service map, accessibility, forms) were kept.

## Pattern
- **Funnel: problem, then solution, then action**, with a small call to action at each stop and one main CTA: **Get my free check**.
- **Trust path:** credibility (who, where), then proof (real work), then a clear way to reach out. No fake reviews, logos or stats.
- **Local service rule (UI UX Pro Max):** show a map. The map is the hero: a light street map of The Colony (Main St, S Colony Blvd, Hwy 121) with the Firemark pin at Main and S Colony.

## Color (v3, Oct 26, 2026: light stone, charcoal, subtle orange)
Jeremy dropped the lake teal. He wants light pages, charcoal and gray, and orange used sparingly. The old token names (`--mist`, `--teal`, `--deep`, `--shore`) still exist in `site.css` and point at the new colors, so older rules keep working.

| Role | Name | Hex | Notes |
|---|---|---|---|
| Page ground | Paper | `#F6F5F3` | Main background. Deliberately cooler than the cream most new sites use |
| Light bands | Stone | `#ECEAE6` | "Your next customer" and the free check sections, soft panels |
| Surface | White | `#FFFFFF` | Cards, form, white sections |
| Text, headings, main buttons, the mark | Charcoal | `#1D1C1A` | 15.6:1 on paper |
| Secondary text | Graphite | `#57534E` | 7.0:1 on paper, 6.3:1 on stone |
| Small orange text and icons | Ember | `#B23F0E` | 5.3:1 on paper |
| Accent | Flame | `#EC4E1C` | Logo fire, map pin, the dot on main buttons, focus ring, big step numbers. Never small text |
| Logo core, links on charcoal | Gold | `#FFB22E` | |
| Text on charcoal | Ash | `#C9C4BC` | 9.6:1 on charcoal |
| Map | Land / Water | `#F2F1EE` / `#E4E2DD` | Illustrations only |
| Lines | Line / Strong line | `#DEDBD5` / `#8A857D` | Dividers / input borders (3.6:1 on white) |

**Where it's dark:** only the "Why Firemark" story band and the footer. Everything else is light.

**Where the orange goes:** the logo's fire, the hero pin and its glow, the main buttons (Ember), link underlines, the focus ring, the big step numbers, and ticks and icons in Ember. That's all.

## Type
- **Bricolage Grotesque** (variable: weight 200 to 800, optical size 12 to 96) for everything, self-hosted.
- Display and headings: weight 620 with optical size pinned to 32 (`font-variation-settings: "opsz" 32`), tracking -0.03 to -0.035em, line-height about 0.97. Jeremy found the display cut at 800 (opsz 96) cartoony on Oct 26, 2026, so don't go back to it.
- Small headings: weight 650, opsz 24.
- Body: weight 400, 17 to 19px, line-height 1.55, optical sizing on.
- Labels and buttons: weight 600 to 700, sentence case. Never all caps.

## Shape and space
- Radius hierarchy: 28px for big panels (hero map, pricing panel), 18px for cards, 14px for buttons and inputs, full pill for chips. Never one radius for everything.
- 4/8 spacing rhythm. Section padding scales with the screen (4 to 8rem).
- Content max width 84rem. Text measure under 70 characters.

## Motion
- One orchestrated moment: the hero map. The pin drops onto Main St, its glow opens and the listing card appears. About 1.5 seconds, then it stops.
- Animate transform and opacity only. When reduced motion is on, show the final state immediately.
- Everything else is still, except state changes people trigger (menu, FAQ, form).

## Components
- **Primary button:** Ember (#B23F0E) background, white text (5.6:1), with a small gold "ember" dot before the label. 14px radius, at least 48px tall. Never Flame as a button background, because white text on it fails contrast. Alternative, switched off: `data-buttons="charcoal"` on `<html>` gives a charcoal button with a Flame dot.
- **Secondary action:** underlined text link (Flame underline). `.btn-outline` (charcoal border) for a second button on light bands; `.btn-ghost` on charcoal.
- **Chips:** pill, Paper background, Charcoal text, used for project scope and map actions.
- **Form:** visible labels. Required fields are marked with * plus hidden "required" text, and optional fields say "(optional)", following Baymard. Fields validate on blur, errors clear as soon as they're fixed, valid fields get a check, and a focusable error summary appears on a failed submit.
- **Icons:** Phosphor (regular weight), one family, decorative icons marked `aria-hidden`.
- **Navigation:** the same on every page. On phones: logo, a "Free check" button and a labeled Menu button; below 384px the Menu button shows only its icon (its name stays "Menu" for screen readers) and below 335px the header button hides. The phone menu always ends with "Get my free check." The current page is underlined in Flame.
- **Logo:** the flame-pin mark (one shape that reads as a flame and a map pin) with the fire lit inside, plus the lowercase `firemark` wordmark in Bricolage Grotesque 700, converted to outlines. Inline use: the `#fm-mark` symbol in `src/partials/sprite.html`; recolor with `--mark-body`, `--mark-flame`, `--mark-core`.

## Avoid
- Fake testimonials, reviews, logos, ratings or stats.
- Emoji as icons, stock photos, gradients other than the logo fire.
- All-caps eyebrow labels, middle-dot meta strings, arrows tacked onto buttons, numbered markers on things that aren't steps.
- "We" in the copy. Firemark is one person.

## Pre-delivery checklist (UI UX Pro Max + this project)
Last run Oct 26, 2026 on every page.
- [x] Text contrast 4.5:1 or better everywhere (axe: 0 issues at 390px and 1440px)
- [x] Visible keyboard focus on every control; focus never hidden under the sticky header
- [x] Targets at least 44px (inline text links excepted); no horizontal scroll from 320 to 1920px
- [x] Reduced motion respected; hero shows its final state
- [x] Images have width and height, WebP, and lazy loading below the fold
- [x] Lighthouse on a phone: performance 99–100, accessibility 100, best practices 100; SEO 100 without the draft noindex
- [x] Every claim true; every unknown marked [PLACEHOLDER] or [CONFIRM] (listed in PICKUP.md)
