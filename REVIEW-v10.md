# v10: things for Jeremy to check

Nothing below is shown on the site as a tag. Each line is a sentence the site already uses, or a gap the site works around. Tick it, or tell Claude what to change.

## Promises and wording to approve
- [ ] Price: "After your free check, you get a price for exactly what yours needs, in writing, before anything starts." (homepage, What it costs; also the third next step)
- [ ] Next step 3: "If a website makes sense, you get a written price before anything starts. If it doesn't, Jeremy will say so."
- [ ] Monthly plan: Hosting ("Your site stays online at a secure address. You never have to deal with a web host."), Updates ("Kept up to date behind the scenes, so it keeps working."), Small edits ("Send a note when something changes, and it gets done. One person to call.").
- [ ] Starter project: a website that works on phones, your Google listing set up right, email with your business name.
- [ ] About: "Nothing goes live until you've seen it and said yes."
- [ ] Ownership: "Your domain, your content and your site are yours to keep." (Put the portfolio line in your written quote too.)
- [ ] Privacy: "Your details aren't sold or shared, and you won't be added to a mailing list." Also check how long Web3Forms keeps a copy once your account exists, and the date ("Last updated October 27, 2026").
- [ ] The free check sample on the homepage is for a made-up "Main Street Bakery" and is captioned as a sample. Fine to keep?

## Gaps the site works around (fill in `tools/build.py`, then rebuild)
- [ ] `EMAIL`: once the Google Workspace address works. Until then no email address is shown anywhere except as the form's fallback.
- [ ] `FALLBACK_EMAIL` is `hello@firemarktech.com`. Make sure that inbox (or alias) exists before launch, or change it.
- [ ] `WEB3FORMS_KEY`: paste the key. Until then the form opens a pre-filled email.
- [ ] `PHONE` and `BOOKING_URL`: optional. Nothing shows until they're set.
- [ ] `HEADSHOT = True` after replacing `docs/images/jeremy.webp` with a square photo (448px or larger). Until then a stone tile with the flame pin stands in. This is the biggest missing piece on About.

## Work
- [ ] The Friends of the Library screenshots now have the program photos blanked out (flat circles), so no children show. Ask the Friends if they'd like real photos shown; if yes, Claude can put the originals back.
- [ ] GLP screenshots show Joey and Ethan (the owners). GLP gave permission on Oct 26.

## Repo tidy (delete when convenient)
- [ ] `firemark-design-research-dropin/`
- [ ] `docs/images/jeremy-placeholder.webp`
- [ ] Old case-study images nothing uses any more: `docs/images/work/fotcpl-join-800.webp`, `fotcpl-join-1200.webp`, `glp-netsheet-800.webp`, `glp-netsheet-1200.webp`
