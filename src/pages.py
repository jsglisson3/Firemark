"""Content for the inner pages. tools/build.py runs this file and provides two names:
   page(file, title, desc, h1, lead, body, banner=..., current=None)  writes docs/<file>
   form                                                               the free check form (src/partials/form.html)
Voice: brand first ("Firemark does..."), never "we", Jeremy by first name only.
Anything not yet true or not yet decided is marked [PLACEHOLDER] or [CONFIRM] and listed in PICKUP.md."""

CHECK = '<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>'
CROSS = '<svg class="icon" aria-hidden="true"><use href="#i-close"/></svg>'


def ticks(items):
    return '<ul class="build-list">' + ''.join(
        f'<li>{CHECK}<span><strong>{a}</strong> {b}</span></li>' for a, b in items) + '</ul>'


def media(slug, alt_desktop, alt_phone, first=False):
    load = 'fetchpriority="high"' if first else 'loading="lazy"'
    return f'''<div class="project-media">
          <div class="shot-desktop"><img src="images/work/{slug}-desktop-960.webp" srcset="images/work/{slug}-desktop-640.webp 640w, images/work/{slug}-desktop-960.webp 960w, images/work/{slug}-desktop-1440.webp 1440w" sizes="(min-width: 66rem) 57rem, 88vw" width="1440" height="900" {load} decoding="async" alt="{alt_desktop}"></div>
          <div class="shot-phone"><img src="images/work/{slug}-phone-300.webp" srcset="images/work/{slug}-phone-300.webp 300w, images/work/{slug}-phone-600.webp 600w" sizes="(min-width: 40rem) 11rem, 7.5rem" width="600" height="1298" loading="lazy" decoding="async" alt="{alt_phone}"></div>
        </div>'''


def cta_band(hid, heading, text, tone='tone-stone'):
    return f'''    <section class="cta-band {tone}" aria-labelledby="{hid}">
      <div class="wrap">
        <h2 id="{hid}">{heading}</h2>
        <p class="lead measure">{text}</p>
        <a class="btn btn-flame" href="contact.html">Get my free check</a>
      </div>
    </section>'''


# ---------------------------------------------------------------- Work

glp = f'''      <article class="case" aria-labelledby="glp-h">
        <div class="case-top">
          <h2 id="glp-h">GLP Home Options</h2>
          <p class="lead">A home-buying business in Chattanooga, Tennessee.</p>
        </div>
        {media("glp", "Screenshot of the GLP Home Options homepage. The headline reads: Real home options. Clear next steps. Beside it is a photo of the two co-founders.", "The same homepage on a phone.", first=True)}
        <div class="case-grid">
          <div class="case-col">
            <h3>The job</h3>
            <p>People who call a home-buying company are often in a hard spot: an inherited house, a move, repairs they can't afford. GLP wanted a site that lays out every option, including the ones where they don't buy the house, so people can trust them.</p>
            <h3>What was built</h3>
            {ticks([
              ("A seller net sheet.", "Homeowners type what they owe and what the house might sell for, then see what they'd keep from listing versus a cash offer. It updates as they type and prints for the kitchen table."),
              ("Every option, side by side.", "Selling direct, listing with an agent and keeping the home, each with who it's best for and how long it takes."),
              ("Plain-English writing.", "No jargon and no pressure. Terms like seller financing get a short explanation right where they come up."),
              ("A short contact form.", "Only a name and phone number are required. Everything else is optional."),
            ])}
            <h3>The details</h3>
            <p>A privacy policy and terms page, a clean preview when the link is texted or posted, and a layout that works well on phones.</p>
            <p class="case-link"><a href="https://jsglisson3.github.io/GLP-Home-Options/" target="_blank" rel="noopener">Visit the GLP Home Options site<span class="visually-hidden"> (opens in a new tab)</span></a></p>
          </div>
          <figure class="feature-shot">
            <a href="images/work/glp-netsheet-1200.webp"><img src="images/work/glp-netsheet-800.webp" srcset="images/work/glp-netsheet-800.webp 800w, images/work/glp-netsheet-1200.webp 1200w" sizes="(min-width: 60rem) 36rem, 88vw" width="1200" height="948" loading="lazy" decoding="async" alt="The seller net sheet: inputs for mortgage owed, sale price and a cash offer on the left, and two columns comparing what the owner keeps from listing and from selling direct on the right. Opens the full-size image."></a>
            <figcaption>The seller net sheet. Change a number and both columns update. Tap the image to see it full size.</figcaption>
          </figure>
        </div>
      </article>'''

fotcpl = f'''      <article class="case" aria-labelledby="fotcpl-h">
        <div class="case-top">
          <span class="concept-tag">Volunteer concept, not the official site</span>
          <h2 id="fotcpl-h">Friends of The Colony Public Library</h2>
          <p class="lead">A redesign concept for the library's nonprofit friends group, built as a volunteer.</p>
        </div>
        {media("fotcpl", "Screenshot of the redesign concept for Friends of The Colony Public Library. The headline reads: Supporting The Colony Public Library, beside photos of library programs.", "The same concept on a phone.")}
        <div class="case-grid">
          <div class="case-col">
            <h3>The job</h3>
            <p>The Friends do a lot for the library: technology grants, book donations, genealogy projects and Little Free Libraries. The concept shows how a site could make that work visible, and make it easy to join, give and follow along.</p>
            <h3>What was built</h3>
            {ticks([
              ("Membership up front.", "What it costs, what members get and one clear button to join or renew."),
              ("Easy ways to help.", "Kroger Community Rewards with a one-tap copy of the organization number, North Texas Giving Day and book donations."),
              ("Library moments, in one place.", "A photo gallery, every newsletter and a link to the library's events calendar."),
              ("Built for everyone.", "An accessibility statement and a privacy page, written in plain English."),
            ])}
            <p class="case-link"><a href="https://jsglisson3.github.io/FOTCL/" target="_blank" rel="noopener">See the redesign concept<span class="visually-hidden"> (opens in a new tab)</span></a></p>
          </div>
          <figure class="feature-shot">
            <a href="images/work/fotcpl-join-1200.webp"><img src="images/work/fotcpl-join-800.webp" srcset="images/work/fotcpl-join-800.webp 800w, images/work/fotcpl-join-1200.webp 1200w" sizes="(min-width: 60rem) 36rem, 88vw" width="1200" height="554" loading="lazy" decoding="async" alt="The Become a Friend section: membership is 15 dollars a year, with buttons to see membership levels or join online, and four member benefits. Opens the full-size image."></a>
            <figcaption>Membership, front and center: the price, the benefits and one button to join. Tap the image to see it full size.</figcaption>
          </figure>
        </div>
      </article>'''

work_body = f'''    <div class="wrap">
{glp}
{fotcpl}
      <p class="case-note"><span class="ph">[CONFIRM with GLP and with the Friends that their sites can be shown here.]</span></p>
    </div>
{cta_band("work-cta-h", "Want a site like these for your business?", "Start with a free check. Firemark looks at how your business shows up on Google today and sends a short, plain-English report.")}'''

page('work.html', 'Work | Firemark',
     'Two websites designed and built by hand: GLP Home Options in Chattanooga, and a redesign concept for Friends of The Colony Public Library.',
     'Two sites, built by hand.',
     'What each one needed to do, and how it was built to do that.',
     work_body, current='work.html')


# ---------------------------------------------------------------- About

PRINCIPLES = [
    ('Built for your business.', 'Every site is made by hand around what you do, not squeezed into a template.'),
    ('Plain English.', 'No jargon. Anything technical gets explained in everyday words.'),
    ('You approve everything.', 'Nothing goes live until you\'ve seen it and said yes.'),
    ('One person to call.', 'No help desk and no tickets. You deal directly with the person who built your site.'),
    ('Honest advice.', 'If a few fixes are all you need, that\'s what you\'ll hear.'),
    ('You own it.', 'Your domain and your content are yours to keep. <span class="ph">[CONFIRM]</span>'),
]

about_body = f'''    <section class="wrap about-for" aria-labelledby="for-h">
      <h2 class="small-h" id="for-h">Who Firemark is for</h2>
      <div class="fit">
        <div>
          <h3>A good fit</h3>
          <ul class="fit-list">
            <li>{CHECK}<span>Independent, owner-run businesses: the barber, the bakery, the plumber, the shop on the corner</span></li>
            <li>{CHECK}<span>Owners who make the decisions and sign the checks</span></li>
            <li>{CHECK}<span>Businesses that want more people nearby to find them</span></li>
          </ul>
        </div>
        <div>
          <h3>Probably not the right fit</h3>
          <ul class="fit-list not">
            <li>{CROSS}<span>Franchises, which usually have a head office that handles this</span></li>
            <li>{CROSS}<span>Large online stores with hundreds of products</span></li>
            <li>{CROSS}<span>Companies that need a full agency team</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section tone-white" aria-labelledby="how-h">
      <div class="wrap">
        <div class="section-head">
          <h2 id="how-h">What you can count on</h2>
        </div>
        <ul class="principles">
          {''.join(f'<li>{CHECK}<strong>{a}</strong><span>{b}</span></li>' for a, b in PRINCIPLES)}
        </ul>
      </div>
    </section>

    <section class="section" aria-labelledby="who-h">
      <div class="wrap who who-top">
        <div class="who-photo">
          <img src="images/jeremy-placeholder.webp" width="200" height="200" loading="lazy" alt="Jeremy, who runs Firemark.">
          <span class="ph">[PLACEHOLDER: photo, optional]</span>
        </div>
        <div class="measure">
          <h2 id="who-h">Who you'll work with</h2>
          <p class="lead">Firemark is Jeremy, based here in The Colony. He has spent more than 10 years in IT and online sales, leading online ordering channels and working on the systems behind large businesses. Firemark brings that know-how to independents, one business at a time.</p>
          <ul class="tick-list who-list">
            <li>{CHECK}<span>10+ years in IT and online sales</span></li>
            <li>{CHECK}<span>Led a team of developers, testers and analysts</span></li>
            <li>{CHECK}<span>Ran large-scale online ordering channels</span></li>
            <li>{CHECK}<span>Dozens of projects connecting business systems</span></li>
            <li>{CHECK}<span>Degree in Management Information Systems</span></li>
          </ul>
        </div>
      </div>
    </section>

    <section class="section tone-stone" aria-labelledby="story-h">
      <div class="wrap story">
        <div class="then-now" aria-hidden="true">
          <figure>
            <svg class="art" viewBox="0 0 120 140">
              <path d="M14 10H106V78C106 106 84 122 60 132C36 122 14 106 14 78Z" fill="none" stroke="#8A857D" stroke-width="3"/>
              <path d="M22 18H98V78C98 101 80 114 60 123C40 114 22 101 22 78Z" fill="none" stroke="#8A857D" stroke-width="1.5" opacity=".6"/>
              <text x="60" y="80" text-anchor="middle" font-family="Bricolage Grotesque, sans-serif" font-weight="800" font-size="26" fill="#8A857D">1752</text>
            </svg>
            <figcaption>Then: on the wall</figcaption>
          </figure>
          <svg class="arrow icon"><use href="#i-arrow"/></svg>
          <figure>
            <svg class="art" viewBox="0 0 74 116"><use href="#fm-mark"/></svg>
            <figcaption>Now: on the map</figcaption>
          </figure>
        </div>
        <div class="story-text measure">
          <h2 id="story-h">Why the name</h2>
          <p style="margin-top: var(--space-s)">In 1752, Benjamin Franklin helped start what's now America's oldest fire insurance company. Every building it covered got a fire mark: a plaque of four clasped hands, mounted out front where anyone could see it. It told the whole street that someone had that building's back.</p>
          <p>Today, people meet your business on a phone first, through a website and a Google listing. Firemark makes sure yours are there, and stay right.</p>
          <p class="strong">The logo is a map pin with a fire inside: the old mark, made for the map.</p>
        </div>
      </div>
    </section>

{cta_band("about-cta-h", "See how your business shows up.", "Start with a free check. You'll get a short, plain-English report, and you decide what to do with it.", tone='tone-white')}'''

page('about.html', 'About | Firemark',
     'Firemark helps independent businesses in The Colony, Texas get found online. One person, start to finish, with a handful of clients a year.',
     'Small on purpose.',
     'Firemark is based in The Colony and takes on a handful of clients a year, so each one gets full attention, start to finish.',
     about_body, current='about.html')


# ---------------------------------------------------------------- Contact (the free check)

contact_body = f'''    <div class="wrap contact contact-page">
{form}
      <div class="contact-intro">
        <h2 class="small-h">What happens next</h2>
        <ol class="next-steps">
          <li><span><strong>You send the form.</strong> It takes about a minute.</span></li>
          <li><span><strong>Firemark looks you up the way a customer would:</strong> on Google Search and Maps, on a phone.</span></li>
          <li><span><strong>You get a short report in plain English:</strong> where you show up, what's working and what to fix first. It's free, and it's yours to keep.</span></li>
        </ol>
        <h2 class="small-h">Other ways to reach Firemark</h2>
        <ul class="contact-ways">
          <li><svg class="icon" aria-hidden="true"><use href="#i-mail"/></svg><span>Email <span class="ph">[PLACEHOLDER: hello@firemarktech.com]</span></span></li>
          <li><svg class="icon" aria-hidden="true"><use href="#i-phone"/></svg><span>Call or text <span class="ph">[PLACEHOLDER: phone]</span></span></li>
          <li><svg class="icon" aria-hidden="true"><use href="#i-cal"/></svg><span><a href="#main" data-booking-link>Book a 15-minute call</a> <span class="ph">[PLACEHOLDER: booking link]</span></span></li>
        </ul>
        <p class="muted area-note">Based in The Colony, working with independent businesses across Dallas–Fort Worth.</p>
      </div>
    </div>'''

page('contact.html', 'Get your free check | Firemark',
     'Request a free, plain-English check of how your business shows up on Google. Firemark, The Colony, Texas.',
     'Get your free check.',
     'Tell Firemark about your business. Within 7 days, you\'ll get a short, plain-English report on how it shows up on Google.',
     contact_body, current='contact.html')


# ---------------------------------------------------------------- Privacy

privacy_sections = [
    ('What Firemark collects', '<p>Only what you send. When you fill out the free check form, that\'s your name, your business name, your email and anything else you choose to add, like a phone number, a link or a note.</p>'),
    ('How it\'s used', '<p>To reply to you and do your free check. That\'s it. Your details aren\'t sold, and you won\'t be added to a mailing list. <span class="ph">[CONFIRM]</span></p>'),
    ('Where it\'s kept', '<p><span class="ph">[PLACEHOLDER: the form service, once chosen, and where it stores messages. Until then, the form opens an email to Firemark instead.]</span></p>'),
    ('Cookies and tracking', '<p>This site doesn\'t use cookies, ads or tracking. Everything on it, including the fonts and images, is served from the site itself. <span class="ph">[CONFIRM at launch, and update this if analytics are added.]</span></p>'),
    ('Hosting', '<p>The site is hosted on GitHub Pages. Like most web hosts, GitHub keeps basic technical logs, such as IP addresses, to keep the service secure.</p>'),
    ('Deleting your details', '<p>Email <span class="ph">[PLACEHOLDER: hello@firemarktech.com]</span> and ask. Anything Firemark has from you will be deleted.</p>'),
    ('Changes', '<p>If this page changes, the date below changes too. Last updated <span class="ph">[PLACEHOLDER: date at launch]</span>.</p>'),
]
privacy_body = '''    <div class="wrap">
      <div class="prose">
''' + '\n'.join(f'        <section><h2>{h}</h2>{t}</section>' for h, t in privacy_sections) + '''
      </div>
    </div>'''

page('privacy.html', 'Privacy | Firemark',
     'What Firemark collects through this website and what happens to it.',
     'Privacy',
     'The short version: Firemark only collects what you send, and uses it to do your free check and reply to you. <span class="ph">[CONFIRM]</span>',
     privacy_body,
     banner='Draft preview. This privacy page is a plain-English draft with placeholders.')


# ---------------------------------------------------------------- 404

lost_body = '''    <div class="wrap lost">
      <ul class="lost-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="work.html">Work</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Get your free check</a></li>
      </ul>
    </div>'''

page('404.html', 'Page not found | Firemark', 'That page could not be found.',
     'This page isn’t on the map.',
     'The link may be old, or the address may have a typo. One of these should get you back on track.',
     lost_body)


# ---------------------------------------------------------------- Brand sheet (not linked from the site)

def tile(file, label, tone, note=''):
    return f'''<figure class="logo-tile {tone}">
            <div class="logo-art"><img src="images/brand/{file}" alt="" loading="lazy"></div>
            <figcaption><strong>{label}</strong>{f'<span>{note}</span>' if note else ''}<a href="images/brand/{file}" download>Download SVG<span class="visually-hidden">: {label}</span></a></figcaption>
          </figure>'''


def swatch(name, hexv, use, ratio, dark=False):
    return f'''<li class="swatch">
            <span class="chip-color{' on-dark' if dark else ''}" style="background:{hexv}"></span>
            <strong>{name}</strong><code>{hexv}</code><span>{use}</span><span class="ratio">{ratio}</span>
          </li>'''


brand_body = f'''    <section class="wrap brand-block" aria-labelledby="b-logo">
      <h2 id="b-logo">Logo</h2>
      <p class="muted measure">One shape that reads two ways: a flame, and a map pin pointing at your spot. The charcoal body is the 1752 fire mark, and the orange-and-gold fire is lit inside it. Use the charcoal mark on light backgrounds and the white one on charcoal. The one-color versions have the fire cut out, so they work for a single-color print, a sign or a truck decal.</p>
      <div class="logo-grid">
        {tile("firemark-logo.svg", "Logo", "t-mist", "For light backgrounds")}
        {tile("firemark-logo-reverse.svg", "Logo, reverse", "t-deep", "For dark backgrounds")}
        {tile("firemark-logo-mono-dark.svg", "One color, dark", "t-white", "Single-color printing")}
        {tile("firemark-logo-mono-white.svg", "One color, white", "t-teal", "On photos and colored backgrounds")}
      </div>
      <div class="logo-grid small">
        {tile("firemark-symbol.svg", "Symbol", "t-mist", "App icons, favicons")}
        {tile("firemark-symbol-reverse.svg", "Symbol, reverse", "t-deep")}
        {tile("firemark-symbol-mono-dark.svg", "Symbol, one color", "t-white")}
        {tile("firemark-symbol-mono-white.svg", "Symbol, white", "t-teal")}
        {tile("site-by-firemark-badge.svg", "Site by Firemark", "t-white", "For client site footers")}
        {tile("site-by-firemark-badge-reverse.svg", "Site by Firemark, reverse", "t-deep", "For dark client footers")}
      </div>
      <h3>Using it</h3>
      <ul class="rules">
        <li>{CHECK}<span>Leave clear space around the logo at least as wide as the mark.</span></li>
        <li>{CHECK}<span>Keep the full logo at least 120 pixels wide on screens and 1 inch wide in print. Below that, use the symbol.</span></li>
        <li>{CROSS}<span>Don't recolor the fire, stretch the logo, or add shadows and outlines.</span></li>
        <li>{CROSS}<span>Don't put the full-color logo on a photo. Use the white one.</span></li>
      </ul>
    </section>

    <section class="section tone-white" aria-labelledby="b-color">
      <div class="wrap brand-block">
        <h2 id="b-color">Color</h2>
        <p class="muted measure">Light stone and charcoal, with orange used sparingly: the logo's fire, the map pin, the lit dot on main buttons, the focus ring and a few icons. Flame orange is never used for small text. Use Ember for that.</p>
        <ul class="swatches">
          {swatch("Paper", "#F6F5F3", "Page background", "Charcoal text: 15.6:1")}
          {swatch("Stone", "#ECEAE6", "Light bands and soft panels", "Graphite text: 6.3:1")}
          {swatch("White", "#FFFFFF", "Cards, forms, white sections", "Charcoal text: 17.1:1")}
          {swatch("Charcoal", "#1D1C1A", "Text, headings, main buttons, the mark", "White text: 17.1:1", dark=True)}
          {swatch("Graphite", "#57534E", "Secondary text", "On paper: 7.0:1", dark=True)}
          {swatch("Ember", "#B23F0E", "Small orange text and icons on light", "On paper: 5.3:1", dark=True)}
        </ul>
        <h3>Fire, map and lines</h3>
        <ul class="swatches mini">
          {swatch("Flame", "#EC4E1C", "Logo fire, map pin, button dot, focus ring", "")}
          {swatch("Gold", "#FFB22E", "Logo fire core; links and focus on charcoal", "")}
          {swatch("Ash", "#C9C4BC", "Secondary text on charcoal", "On charcoal: 9.6:1", dark=True)}
          {swatch("Land", "#F2F1EE", "Map illustration", "")}
          {swatch("Water", "#E4E2DD", "Map illustration", "")}
          {swatch("Line", "#DEDBD5", "Borders and dividers", "")}
        </ul>
      </div>
    </section>

    <section class="section" aria-labelledby="b-type">
      <div class="wrap brand-block">
        <h2 id="b-type">Type</h2>
        <p class="muted measure">One family, Bricolage Grotesque, from Google Fonts (free, open license). Headings are heavy and tight; body text is regular and roomy. Sentence case everywhere, never all caps.</p>
        <div class="type-specimen">
          <p class="ts-display">Put your business on the map.</p>
          <p class="ts-label">Display, 800 weight, tight spacing</p>
          <p class="ts-h2">Get found. Stay found.</p>
          <p class="ts-label">Section heading, 800 weight</p>
          <p class="ts-lead">One starter project puts you on the map. A small monthly plan keeps you there.</p>
          <p class="ts-label">Lead text, 400 weight</p>
          <p class="ts-body">Firemark looks at how your business shows up on Google today and sends a short, plain-English report. No cost, no pressure.</p>
          <p class="ts-label">Body text, 400 weight, 17 to 19 pixels</p>
        </div>
      </div>
    </section>

    <section class="section tone-white" aria-labelledby="b-voice">
      <div class="wrap brand-block">
        <h2 id="b-voice">Voice</h2>
        <p class="muted measure">A sharp neighbor who's great at this. Plain English, short sentences, talking to "you." The brand speaks first: "Firemark builds…", never "we." Jeremy appears by first name only.</p>
        <div class="voice-grid">
          <div class="voice-col">
            <h3>Say it like this</h3>
            <ul class="rules">
              <li>{CHECK}<span>Firemark builds websites and Google listings for independent businesses in The Colony.</span></li>
              <li>{CHECK}<span>Get my free check</span></li>
              <li>{CHECK}<span>Your site goes live, your listing is right, and the monthly plan keeps it that way.</span></li>
            </ul>
          </div>
          <div class="voice-col">
            <h3>Not like this</h3>
            <ul class="rules not">
              <li>{CROSS}<span>We leverage cutting-edge digital solutions to elevate your brand.</span></li>
              <li>{CROSS}<span>Submit</span></li>
              <li>{CROSS}<span>Seamless end-to-end digital presence management.</span></li>
            </ul>
          </div>
        </div>
        <h3>Lines to reuse</h3>
        <ul class="lines">
          <li><strong>Put your business on the map.</strong><span>The main line. Homepage, share image, business card.</span></li>
          <li><strong>Get found. Stay found.</strong><span>The offer: the starter project and the monthly plan.</span></li>
          <li><strong>Small on purpose.</strong><span>Why there are only a handful of clients a year.</span></li>
          <li><strong>Your next customer is searching right now.</strong><span>The problem, in one sentence.</span></li>
        </ul>
      </div>
    </section>

    <section class="section" aria-labelledby="b-card">
      <div class="wrap brand-block">
        <h2 id="b-card">Business card</h2>
        <p class="muted measure">Standard US size, 3.5 by 2 inches. Front and back.</p>
        <div class="cards">
          <div class="biz-card front"><img src="images/brand/firemark-logo-reverse.svg" alt="Card front: the reverse Firemark logo on charcoal." loading="lazy"><span>Put your business on the map.</span></div>
          <div class="biz-card back">
            <img src="images/brand/firemark-symbol.svg" alt="" loading="lazy">
            <div><strong>Jeremy</strong><span>Firemark</span></div>
            <ul><li>firemarktech.com</li><li><span class="ph">[PLACEHOLDER: email]</span></li><li><span class="ph">[PLACEHOLDER: phone]</span></li><li>The Colony, Texas</li></ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section tone-white" aria-labelledby="b-more">
      <div class="wrap brand-block">
        <h2 id="b-more">Icons, shapes and motion</h2>
        <ul class="rules">
          <li>{CHECK}<span>Icons come from Phosphor (regular weight, free, open license), drawn in charcoal, with Ember for ticks and a few accents.</span></li>
          <li>{CHECK}<span>Corners get rounder as things get bigger: 28 pixels for panels, 18 for cards, 14 for buttons, fully round for chips.</span></li>
          <li>{CHECK}<span>One moving moment per page at most, like the homepage map. Anyone who turns on reduced motion sees the finished picture right away.</span></li>
        </ul>
      </div>
    </section>'''

page('brand.html', 'Brand sheet | Firemark',
     'The Firemark logo files, colors, type, voice and usage rules.',
     'Firemark brand sheet',
     'Everything needed to keep Firemark looking and sounding the same everywhere: logo files, colors, type, voice and a few rules.',
     brand_body,
     banner='Brand sheet for Jeremy. Not linked from the site and hidden from search engines.')
