"""Content for the inner pages. tools/build.py runs this file and provides:
   page(file, title, desc, h1, lead, body, banner=..., current=None, head_extra='', body_class='inner')  writes docs/<file>
   form, SITES, site_list(sites, h)        the free check form and the Work list (src/sites.py)
   person(), reach_line(), reach_list()    Jeremy's card and the contact lines, from the settings in tools/build.py
   CONTACT                                 {'email', 'phone', 'booking'} links, or '' while not set
Voice: brand first ("Firemark does..."), never "we", Jeremy by first name only.
Nothing unconfirmed goes on a page: open questions live in REVIEW-v10.md and PICKUP.md, not in [CONFIRM] tags."""

STEPS = [
    'Jeremy looks up how your business shows up on Google today.',
    'Within 7 days you get a short written report. It\'s yours to keep, whatever you decide.',
    'If a website makes sense, you get a written price before anything starts. If it doesn\'t, Jeremy will say so.',
]

ARROW = '<svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg>'
CHECK = '<svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>'
CROSS = '<svg class="icon" aria-hidden="true"><use href="#i-close"/></svg>'


def steps(n=3):
    return '<ol class="next-steps">\n' + '\n'.join(f'              <li>{s}</li>' for s in STEPS[:n]) + '\n            </ol>'


def cta_band(hid, heading):
    """The closing section on Work and About: the homepage close, with a button in place of the form."""
    return f'''    <section class="section closing-section" aria-labelledby="{hid}">
      <div class="wrap">
        <h2 id="{hid}" class="closing-title" data-reveal><span>{heading}</span></h2>
        <div class="closing closing-short">
          <div class="closing-intro" data-reveal>
            <p class="statement">Here's what happens next.</p>
            {steps(3)}
          </div>
          <div class="closing-act" data-reveal>
            <a class="btn btn-wide" href="contact.html">Get my free check</a>
            <p class="form-fine">No payment, no account. You'll hear back within 5 days.</p>
            {person()}
            {reach_line()}
          </div>
        </div>
      </div>
    </section>'''




# ---------------------------------------------------------------- Work

work_body = f'''    <section class="section section-tight work work-page" aria-label="Websites">
      <div class="wrap">
        {site_list(SITES, h='h2')}
      </div>
    </section>
{cta_band("work-cta-h", "Want yours on this list?")}'''

page('work.html', 'Work | Firemark',
     'Websites Firemark has designed and built by hand for independent businesses and local groups.',
     'Recent work',
     'Websites designed and built by hand, one at a time. Tap one to see it live.',
     work_body, current='work.html', head_class='page-head-split')


# ---------------------------------------------------------------- About

about_body = f'''    <section class="section section-tight about-who" aria-labelledby="who-h">
      <div class="wrap about-grid">
        <aside class="about-card" data-reveal aria-label="Jeremy at a glance">
          {person('large')}
          <dl class="facts">
            <div><dt>Based in</dt><dd>The Colony, Texas</dd></div>
            <div><dt>Experience</dt><dd>More than 10 years in IT and online sales</dd></div>
            <div><dt>Education</dt><dd>BBA in Information Systems, Abilene Christian University</dd></div>
            <div><dt>Clients</dt><dd>A handful a year</dd></div>
            <div><dt>Replies</dt><dd>Within 5 days</dd></div>
          </dl>
        </aside>
        <div class="about-text" data-reveal>
          <h2 id="who-h" class="small-h">Who you'll work with</h2>
          <p class="statement">Firemark is Jeremy. He lives here in The Colony, and he's the only person you'll deal with, from the free check to the small edit you send two years from now.</p>
          <p>He has spent more than 10 years in IT and online sales: leading a team of developers, testers and analysts, running large online ordering channels, and connecting the systems behind big businesses. Today he's a lead analyst for supply chain systems.</p>
          <p>Before any of that, he sold advertising to local businesses in college, walking into dozens of shops a day. That's where he learned how busy an owner's day is, and how little patience there is for jargon. Firemark brings big-business know-how to the business down the street, one at a time.</p>
        </div>
      </div>
    </section>

    <section class="section offer about-fit" aria-labelledby="fit-h">
      <div class="wrap">
        <h2 id="fit-h" class="visually-hidden">Is Firemark a fit?</h2>
        <div class="offer-cols">
          <div class="offer-col" data-reveal>
            <h3>Who it's for</h3>
            <p>Independent, owner-run businesses: the barber, the bakery, the plumber, the shop on the corner. Owners who make the decisions, are busy, and aren't sure yet that a website is worth it.</p>
            <p>If you're a franchise with a head office, a large online store, or you need a full agency team, Firemark probably isn't the right fit, and you'll hear that up front.</p>
          </div>
          <div class="offer-col" data-reveal>
            <h3>Working with Jeremy</h3>
            <ul class="ticks" role="list">
              <li>Everything in plain English, no jargon.</li>
              <li>Nothing goes live until you've seen it and said yes.</li>
              <li>Your domain, your content and your site are yours to keep.</li>
              <li>One person to call, before and after launch.</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section name-story" aria-labelledby="story-h">
      <div class="wrap story" data-reveal>
        <span class="story-mark" aria-hidden="true"><svg viewBox="11.5 -0.5 77 119" focusable="false"><use href="#fm-mark"/></svg></span>
        <div class="story-text">
          <h2 id="story-h">Why “Firemark”</h2>
          <p class="statement">In the 1750s, homes insured by the fire insurance company Benjamin Franklin helped start in Philadelphia wore a plaque out front, a fire mark, so anyone on the street could see the place was looked after.</p>
          <p>Firemark makes the same promise for your business, in the place people look now: the map on their phone. The logo is that idea, a map pin with a fire inside.</p>
        </div>
      </div>
    </section>

{cta_band("about-cta-h", "See how your business shows up today.")}'''

page('about.html', 'About | Firemark',
     'Firemark helps independent businesses in The Colony, Texas get found online. One person, start to finish, with a handful of clients a year.',
     'Small on purpose.',
     'A handful of clients a year, so each one gets full attention, start to finish.',
     about_body, current='about.html', head_class='page-head-split')


# ---------------------------------------------------------------- Contact (the free check)

ways = [x for x in (CONTACT['email'], CONTACT['phone'], CONTACT['booking']) if x]
if ways:
    other = '<h2 class="small-h">Other ways to reach Jeremy</h2>\n        ' + reach_list('reach-list reach-big')
else:
    other = '<h2 class="small-h">Just have a question?</h2>\n        <p>Put it in the note on the form. You don\'t need a website or a listing yet, and you\'ll hear back within 5 days.</p>'

FAQ = [
    ('What does the free check cost?', 'Nothing. No payment, no account, and nothing to buy afterwards. The report is yours to keep.'),
    ('I already have a Facebook page. Isn\'t that enough?', 'Facebook is great for staying in touch with people who already know you. When someone searches Google or Maps for what you do, a website and a Google listing are what show up.'),
    ('I already have a website. Can Firemark help?', 'Start with the free check. You\'ll get an honest read on whether it\'s working or whether a fresh start makes more sense.'),
    ('How long does a website take?', 'Most starter websites go live about 45 days after you give the go-ahead.'),
    ('What does it cost?', 'It depends on what your business needs, so the price comes after the free check, in writing, before anything starts.'),
    ('Who owns the website?', 'You do. Your domain is registered in your name, and your content is yours to keep. Once your site is live, Firemark may show it as an example of recent work.'),
    ('What area do you cover?', 'Firemark is based in The Colony and works with independent businesses across Dallas–Fort Worth.'),
]
faq_html = '\n'.join(f'''          <details>
            <summary>{q}<svg class="icon" aria-hidden="true"><use href="#i-plus"/></svg></summary>
            <p>{a}</p>
          </details>''' for q, a in FAQ)

contact_body = f'''    <section class="section section-tight" aria-label="Free check form">
      <div class="wrap contact-grid">
{form}
        <div class="contact-aside">
          <h2 class="small-h">What happens next</h2>
          {steps(3)}
          <figure class="report report-mini" data-reveal>
            <div class="report-page" data-ui>
              <div class="report-head"><svg class="report-mark" viewBox="11.5 -0.5 77 119" aria-hidden="true" focusable="false"><use href="#fm-mark"/></svg><span class="report-brand">Firemark</span><span class="report-kind">Free check</span></div>
              <p class="report-title">Can customers find you?</p>
              <div class="report-block">
                <p class="report-h">What a customer sees when they search</p>
                <table class="report-table">
                  <thead><tr><th scope="col">Search</th><th scope="col">Where you showed up</th></tr></thead>
                  <tbody>
                    <tr><td>bakery near me</td><td><span class="flag flag-bad">Not on the first page</span></td></tr>
                    <tr><td>bakery The Colony</td><td><span class="flag flag-mid">Below the map</span></td></tr>
                    <tr><td>Main Street Bakery</td><td><span class="flag flag-ok">Top of the map</span></td></tr>
                  </tbody>
                </table>
              </div>
              <p class="report-more">Then the three fixes that matter most, in plain English.</p>
            </div>
            <figcaption>Part of a sample report, for a made-up bakery.</figcaption>
          </figure>
          {other}
        </div>
      </div>
    </section>
    <section class="section faq-section" aria-labelledby="faq-h">
      <div class="wrap faq-grid">
        <h2 id="faq-h" data-reveal>Questions owners ask</h2>
        <div class="faq" data-reveal>
{faq_html}
        </div>
      </div>
    </section>'''

page('contact.html', 'Get your free check | Firemark',
     'Request a free, plain-English check of how your business shows up on Google. Firemark, The Colony, Texas.',
     'Get your free check.',
     'Tell Jeremy about your business. Within 7 days you\'ll know how it shows up on Google: where you appear, what\'s working and what to fix first.',
     contact_body, current='contact.html')


# ---------------------------------------------------------------- Privacy

delete_how = (f'Email {CONTACT["email"]} and ask' if CONTACT['email'] else 'Ask through the <a href="contact.html">free check form</a>, or reply to any email from Jeremy')
privacy_sections = [
    ('What Firemark collects', '<p>Only what you send. When you fill out the free check form, that\'s your name, your business name, your email and anything else you choose to add, like a phone number, a link or a note.</p>'),
    ('How it\'s used', '<p>To reply to you and do your free check. That\'s it. Your details aren\'t sold or shared for marketing, and you won\'t be added to a mailing list.</p>'),
    ('Where it\'s kept', '<p>The form is delivered by Web3Forms, a form service, which passes your message on to Firemark\'s email. What Web3Forms itself keeps is covered by the privacy policy on <a href="https://web3forms.com/">web3forms.com</a>. If the form opens your email app instead, your message goes straight from your email to Firemark.</p>'),
    ('Hosting', '<p>The site is hosted on GitHub Pages. Like most web hosts, GitHub keeps basic technical logs, such as IP addresses, to keep the service secure. This site uses no cookies, ads or tracking.</p>'),
    ('Deleting your details', f'<p>{delete_how}. Anything Firemark has from you will be deleted.</p>'),
    ('Changes', '<p>If this page changes, the date below changes too. Last updated October&nbsp;27, 2026.</p>'),
]
privacy_body = '''    <section class="section section-tight" aria-label="Privacy details">
      <div class="wrap">
        <div class="prose">
''' + '\n'.join(f'          <section><h2>{h}</h2>{t}</section>' for h, t in privacy_sections) + '''
        </div>
      </div>
    </section>'''

page('privacy.html', 'Privacy | Firemark',
     'What Firemark collects through this website and what happens to it.',
     'Privacy',
     'The short version: Firemark only collects what you send, and only uses it to do your free check and reply to you.',
     privacy_body, head_class='page-head-split')


# ---------------------------------------------------------------- 404 and thanks: the homepage map, standing still

def map_band(card, pin=True, label=''):
    pin_html = ('<span class="map-ring" aria-hidden="true"></span>\n          <span class="map-pin" aria-hidden="true"><svg class="mark" viewBox="11.5 -0.5 77 119" focusable="false"><use href="#fm-mark"/></svg></span>'
                if pin else '<span class="map-ring map-ring-empty" aria-hidden="true"></span>')
    return f'''    <figure class="hero-map map-still" aria-label="{label}">
        <div class="map-band">
          {{{{MAP}}}}
          {pin_html}
          {card}
        </div>
        <figcaption class="map-foot wrap"><span class="map-credit">Map data © <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors</span></figcaption>
      </figure>'''


lost_body = map_band('''<nav class="place-card place-card-lost" data-ui aria-label="Where to go next">
            <div class="pc-search"><svg class="icon" aria-hidden="true"><use href="#i-search"/></svg><span>the page you wanted</span></div>
            <div class="pc-result">
              <div class="pc-top"><b>No results on this street</b></div>
              <span class="pc-meta">Try one of these instead:</span>
              <ul class="chips" role="list"><li><a class="chip" href="index.html">Home</a></li><li><a class="chip" href="work.html">Work</a></li><li><a class="chip" href="about.html">About</a></li><li><a class="chip" href="contact.html">Free check</a></li></ul>
            </div>
          </nav>''', pin=False, label='A street map of The Colony with an empty spot where the page should be')

page('404.html', 'Page not found | Firemark', 'That page could not be found.',
     'This page isn’t on the map.',
     'The link may be old, or the address may have a typo. One of these should get you back on track.',
     lost_body)


# ---------------------------------------------------------------- Thanks (where the form lands without JavaScript)

thanks_body = map_band('''<div class="place-card" data-ui>
            <div class="pc-search"><svg class="icon" aria-hidden="true"><use href="#i-search"/></svg><span>your business</span></div>
            <div class="pc-result">
              <div class="pc-top"><b>Request received</b><span class="pc-open">On its way</span></div>
              <span class="pc-meta">Your report arrives within 7 days.</span>
              <ul class="chips" role="list"><li><a class="chip" href="index.html">Homepage</a></li><li><a class="chip" href="work.html">See the work</a></li></ul>
            </div>
          </div>''', label='The street map with the Firemark pin and a card that says your request was received')

page('thanks.html', 'Thanks | Firemark', 'Your free check request is in.',
     'Thanks. Your free check is on its way.',
     'Jeremy will look up how your business shows up on Google and email you a short written report within 7 days.',
     thanks_body)


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
      <p class="muted measure">One shape that reads two ways: a flame, and a map pin pointing at your spot. The charcoal body is the old fire mark, and the orange-and-gold fire is lit inside it. Use the charcoal logo on light backgrounds and the paper one on charcoal. The one-color versions have the fire cut out, so they work for single-color print, a sign or a truck decal. Below 32 pixels, use the charcoal app tile instead of the bare pin.</p>
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
        {tile("firemark-app-icon.svg", "App tile", "t-mist", "Favicons and phone home screens")}
      </div>
      <div class="logo-grid small">
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
        <p class="muted measure">Light stone and charcoal, with orange used sparingly: the logo's fire, the map pin, the main buttons (in Ember), link underlines, the focus ring and a few icons. Flame orange is never used for small text. Use Ember for that.</p>
        <ul class="swatches">
          {swatch("Paper", "#F6F5F3", "Page background", "Charcoal text: 15.6:1")}
          {swatch("Stone", "#ECEAE6", "Light bands and soft panels", "Graphite text: 6.3:1")}
          {swatch("White", "#FFFFFF", "Cards, forms, white sections", "Charcoal text: 17.1:1")}
          {swatch("Charcoal", "#1D1C1A", "Text, headings, main buttons, the mark", "White text: 17.1:1", dark=True)}
          {swatch("Graphite", "#57534E", "Secondary text", "On paper: 7.0:1", dark=True)}
          {swatch("Ember", "#B23F0E", "Buttons, small orange text and icons on light", "White text on it: 5.6:1", dark=True)}
        </ul>
        <h3>Fire, map and lines</h3>
        <ul class="swatches mini">
          {swatch("Flame", "#EC4E1C", "Logo fire, map pin, focus ring", "")}
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
          <p class="ts-label">Display, 620 weight, text optical size (opsz 32)</p>
          <p class="ts-h2">Get found. Stay found.</p>
          <p class="ts-label">Section heading, 620 weight</p>
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
            <ul><li>firemarktech.com</li>{''.join(f'<li>{x}</li>' for x in (CONTACT['email'], CONTACT['phone']) if x)}<li>The Colony, Texas</li></ul>
          </div>
        </div>
      </div>
    </section>

    <section class="section tone-white" aria-labelledby="b-more">
      <div class="wrap brand-block">
        <h2 id="b-more">Icons, shapes and motion</h2>
        <ul class="rules">
          <li>{CHECK}<span>Icons come from Phosphor (regular weight, free, open license), drawn in charcoal, with Ember for ticks and a few accents.</span></li>
          <li>{CHECK}<span>Two shapes only: buttons and chips are fully round, like the pins and chips on a map. Pictures, the form and panels get one small 8 pixel corner.</span></li>
          <li>{CHECK}<span>One big moving moment, the homepage map: the search types in, the pin drops and the listing appears. Everything else only rises gently into place once. Anyone who turns on reduced motion sees the finished page right away.</span></li>
        </ul>
      </div>
    </section>'''

page('brand.html', 'Brand sheet | Firemark',
     'The Firemark logo files, colors, type, voice and usage rules.',
     'Firemark brand sheet',
     'Everything needed to keep Firemark looking and sounding the same everywhere: logo files, colors, type, voice and a few rules.',
     brand_body,
     banner='Brand sheet for Jeremy. Not linked from the site and hidden from search engines.')
