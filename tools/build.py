"""Builds the Firemark website into docs/.

Sources live in src/ (not published):
  src/index.html            homepage template ({{...}} slots are filled in below)
  src/partials/sprite.html  icons and the Firemark pin
  src/partials/form.html    the free check form (homepage and contact page)
  docs/images/map/the-colony.svg  the street map (homepage, 404, thanks), drawn from OpenStreetMap by
                            design-system/firemark/map-source/render_full.py
  src/pages.py              content for the inner pages
  src/sites.py              the list of websites on the Work page and the homepage

Run from the project folder:  python tools/build.py
"""
import pathlib, re, subprocess, sys, importlib.util, html as htmlesc

# ---- Launch settings ------------------------------------------------------------
DOMAIN = 'firemarktech.com'   # the domain, no https://
LAUNCHED = False              # True on launch day: removes the draft banner and the noindex tag from public pages
HIDDEN = {'brand.html', '404.html', 'thanks.html'}   # these stay hidden from search engines even after launch
PUBLIC = ['index.html', 'work.html', 'about.html', 'contact.html', 'privacy.html']   # listed in sitemap.xml
VERSION = '15'                # bump when docs/css/site.css or docs/js/site.js change, so visitors get the new files

# ---- Contact details: fill these in when they exist, then rebuild ------------------
# Anything left empty is simply left off the site (no placeholder text is ever shown).
# The free check form is always there, so people can always reach you.
EMAIL = ''                    # e.g. 'hello@firemarktech.com'  (shows in the menu, closing section, footer, contact page)
PHONE = ''                    # e.g. '(469) 555-0123'          (same places; tap to call on phones)
BOOKING_URL = ''              # e.g. a Cal.com or Calendly link for "Book a 15-minute call"
HEADSHOT = False              # True once docs/images/jeremy.webp is a real square photo (448px or larger)
WEB3FORMS_KEY = ''            # the access key from web3forms.com; until then the form opens a pre-filled email
FALLBACK_EMAIL = 'hello@firemarktech.com'   # where that pre-filled email goes (make sure this inbox exists)
# -----------------------------------------------------------------------------------

ROBOTS_META = '  <meta name="robots" content="noindex, nofollow">\n'
BANNER = re.compile(r'  <aside class="draft-banner".*?</aside>\n\n?', re.S)
ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
DOCS = ROOT / 'docs'


def finish(file, html):
    """Applies the launch settings to a finished page."""
    if LAUNCHED and file not in HIDDEN:
        html = html.replace(ROBOTS_META, '')
    if LAUNCHED and file != 'brand.html':
        html = BANNER.sub('', html)
    if DOMAIN != 'firemarktech.com':
        html = html.replace('firemarktech.com', DOMAIN)
    if re.search(r'\[(PLACEHOLDER|CONFIRM)', html):
        sys.exit(f'{file}: a [PLACEHOLDER] or [CONFIRM] tag would be shown to visitors. Fix it in src/ first.')
    return html


def esc(s):
    return htmlesc.escape(s, quote=True)


# ---- Contact pieces, built from the settings above --------------------------------
tel = re.sub(r'[^\d+]', '', PHONE)
if tel and not tel.startswith('+'):
    tel = '+1' + tel[-10:]
EMAIL_LINK = f'<a href="mailto:{esc(EMAIL)}">{esc(EMAIL)}</a>' if EMAIL else ''
PHONE_LINK = f'<a href="tel:{tel}">{esc(PHONE)}</a>' if PHONE else ''
BOOKING_LINK = f'<a href="{esc(BOOKING_URL)}" target="_blank" rel="noopener">Book a 15-minute call<span class="visually-hidden"> (opens in a new tab)</span></a>' if BOOKING_URL else ''
DIRECT = [x for x in (EMAIL_LINK, PHONE_LINK) if x]


def reach_line():
    """'Rather email or call?' line for the closing sections. Empty until there is an email or phone."""
    if not DIRECT:
        return ''
    return '<p class="alt-route">Rather email or call? ' + ' or '.join(DIRECT) + '.</p>'


def reach_list(cls='reach-list'):
    """Email, phone and booking as a list, for the footer and the contact page."""
    items = [f'<li>{x}</li>' for x in (EMAIL_LINK, PHONE_LINK, BOOKING_LINK) if x]
    if not items:
        items = ['<li><a href="contact.html">Send a note with the free check form</a></li>']
    return f'<ul class="{cls}" role="list">' + ''.join(items) + '</ul>'


def nav_reach():
    if not DIRECT:
        return ''
    return '<p class="nav-reach">' + ''.join(f'<span>{x}</span>' for x in DIRECT) + '</p>'


def person(size='small'):
    """Jeremy next to the form. A real photo once HEADSHOT is True; until then a signed card, never a gray placeholder."""
    if HEADSHOT:
        art = '<img class="person-photo" src="images/jeremy.webp" width="448" height="448" loading="lazy" alt="Jeremy, who runs Firemark.">'
    else:
        art = '<span class="person-mark" aria-hidden="true"><svg viewBox="0 0 77 119" focusable="false"><use href="#fm-mark"/></svg></span>'
    return f'''<div class="person person-{size}">
            {art}
            <p class="person-text"><span class="person-name">Jeremy</span><span class="person-role">Firemark, The Colony, Texas</span></p>
          </div>'''


def ld_contact():
    out = ''
    if EMAIL:
        out += f',\n    "email": "{EMAIL}"'
    if PHONE:
        out += f',\n    "telephone": "{tel}"'
    return out


sprite = (SRC / 'partials' / 'sprite.html').read_text(encoding='utf-8')
form = (SRC / 'partials' / 'form.html').read_text(encoding='utf-8')
form = form.replace('{{WEB3FORMS_KEY}}', esc(WEB3FORMS_KEY)).replace('{{FALLBACK_EMAIL}}', esc(FALLBACK_EMAIL))


def load(name):
    spec = importlib.util.spec_from_file_location(name, SRC / f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    return spec, mod

spec, sites_mod = load('sites')
spec.loader.exec_module(sites_mod)
SITES = sites_mod.SITES
HOME_SITES = 4   # how many sites "Recent work" on the homepage shows


def site_list(sites, h='h3'):
    """One entry per site from src/sites.py: screenshots, name, one line, link. Phone shot is used when it exists."""
    rows = []
    for i, s in enumerate(sites):
        name, about = esc(s['name']), esc(s['about'])
        img, tag = s['image'], s.get('tag', '')
        tag_html = f'\n            <p class="site-tag">{esc(tag)}</p>' if tag else ''
        phone = ''
        if (DOCS / 'images' / 'work' / f'{img}-phone-300.webp').exists():
            phone = f'''
            <div class="site-phone"><img src="images/work/{img}-phone-300.webp" srcset="images/work/{img}-phone-300.webp 300w, images/work/{img}-phone-600.webp 600w" sizes="(min-width: 64rem) 13rem, 22vw" width="600" height="1298" loading="lazy" decoding="async" alt=""></div>'''
        rows.append(f'''        <li class="site{' site-flip' if i % 2 else ''}" data-reveal>
          <a class="site-media" href="{esc(s['link'])}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true">
            <div class="site-desk"><img src="images/work/{img}-desktop-960.webp" srcset="images/work/{img}-desktop-480.webp 480w, images/work/{img}-desktop-640.webp 640w, images/work/{img}-desktop-960.webp 960w, images/work/{img}-desktop-1440.webp 1440w" sizes="(min-width: 88rem) 39rem, (min-width: 64rem) 44vw, 74vw" width="1440" height="900" loading="lazy" decoding="async" alt=""></div>{phone}
          </a>
          <div class="site-text">
            <{h} class="site-name">{name}</{h}>
            <p class="site-about">{about}</p>{tag_html}
            <a class="text-link site-link" href="{esc(s['link'])}" target="_blank" rel="noopener">Visit the site<span class="visually-hidden">: {name} (opens in a new tab)</span><svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg></a>
          </div>
        </li>''')
    return '<ul class="site-list" role="list">\n' + '\n'.join(rows) + '\n      </ul>'


def fill(html):
    """Fills the shared {{...}} slots used by the homepage and the inner pages."""
    return (html.replace('{{SPRITE}}', sprite).replace('{{FORM}}', form)
            .replace('{{V}}', VERSION).replace('{{NAV_REACH}}', nav_reach()).replace('{{REACH_LINE}}', reach_line())
            .replace('{{REACH_LIST}}', reach_list()).replace('{{PERSON}}', person()).replace('{{LD_CONTACT}}', ld_contact()))


# 1) Homepage
home = fill((SRC / 'index.html').read_text(encoding='utf-8'))
home = home.replace('{{WORK_LIST}}', site_list(SITES[:HOME_SITES]))
(DOCS / 'index.html').write_text(finish('index.html', home), encoding='utf-8')
print('built index.html')

# 2) Shared header and footer for inner pages, with links pointed at real pages
header = re.search(r'  <header class="site-header".*?</header>\n', home, re.S).group(0)
footer = re.search(r'  <footer class="site-footer">.*?</footer>\n', home, re.S).group(0)
for a, b in [('href="#work"', 'href="work.html"'), ('href="#offer"', 'href="index.html#offer"'), ('href="#check"', 'href="contact.html"')]:
    header = header.replace(a, b)

HEAD = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex, nofollow">
  {canonical}
  <meta name="theme-color" content="#F6F5F3">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Firemark">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:image" content="https://firemarktech.com/images/og-card.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="The Firemark logo and the line Put your business on the map, next to a street map with the Firemark pin on Main Street.">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="icon" href="images/favicon-32.png" sizes="32x32" type="image/png">
  <link rel="apple-touch-icon" href="images/apple-touch-icon.png">
  <link rel="manifest" href="site.webmanifest">
  <link rel="preload" href="fonts/bricolage-grotesque-latin-opsz-normal.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="css/site.css?v={v}">
</head>
<body class="{body}">
  <a class="skip-link" href="#main">Skip to main content</a>
  {sprite}

  <aside class="draft-banner" aria-label="Draft notice">{banner}</aside>

'''


def page(file, title, desc, h1, lead, body, banner='Draft preview. Not yet public.', current=None, head_extra='', body_class='inner', head_class=''):
    h = header
    if current:
        h = h.replace(f'<li><a href="{current}"', f'<li><a href="{current}" aria-current="page"', 1)
    canonical = '' if file == '404.html' else f'<link rel="canonical" href="https://firemarktech.com/{file}">'
    html = HEAD.format(title=title, desc=desc, canonical=canonical, sprite=sprite, banner=banner, v=VERSION, body=body_class)
    html += h + f'''
  <main id="main">
    <div class="wrap page-head{' ' + head_class if head_class else ''}">
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>{head_extra}
    </div>
{body}
  </main>

''' + footer + f'''
  <script src="js/site.js?v={VERSION}" defer></script>
</body>
</html>
'''
    html = fill(html)
    (DOCS / file).write_text(finish(file, html), encoding='utf-8')
    print('built', file)

# 3) Inner pages (content in src/pages.py)
spec, mod = load('pages')
mod.page = page
mod.form = form
mod.SITES = SITES
mod.site_list = site_list
mod.reach_line = reach_line
mod.reach_list = reach_list
mod.person = person
mod.CONTACT = {'email': EMAIL_LINK, 'phone': PHONE_LINK, 'booking': BOOKING_LINK}
spec.loader.exec_module(mod)

# 4) 404 must work at any address, so its links start from the site's root folder ("/" on firemarktech.com).
SITE_ROOT = '/'
p404 = DOCS / '404.html'
s = p404.read_text(encoding='utf-8')
s = re.sub(r'(href|src)="(?!https?:|#|mailto:|tel:|/)([^"]+)"', lambda m: f'{m.group(1)}="{SITE_ROOT}{m.group(2)}"', s)
p404.write_text(s, encoding='utf-8')
print('404.html made root-relative')

# 5) Sitemap and robots.txt, so the domain setting flows through
(DOCS / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
    f'  <url><loc>https://{DOMAIN}/{"" if p == "index.html" else p}</loc></url>\n' for p in PUBLIC) + '</urlset>\n', encoding='utf-8')
(DOCS / 'robots.txt').write_text(
    ('# Draft: every page also carries a noindex tag until launch (LAUNCHED in tools/build.py).\n' if not LAUNCHED else '') +
    f'User-agent: *\nAllow: /\nDisallow: /brand.html\n\nSitemap: https://{DOMAIN}/sitemap.xml\n', encoding='utf-8')
print('built sitemap.xml and robots.txt for', DOMAIN, '(launched)' if LAUNCHED else '(draft)')

# 6) Typographer's quotes and no-break phrases on every page
subprocess.run([sys.executable, str(ROOT / 'tools' / 'typeset.py')], check=True)
