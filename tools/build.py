"""Builds the Firemark website into docs/.

Sources live in src/ (not published):
  src/index.html            homepage template ({{SPRITE}} and {{FORM}} are filled in)
  src/partials/sprite.html  icons and the Firemark pin
  src/partials/form.html    the free check form (homepage and contact page)
  src/pages.py              content for the inner pages

Run from the project folder:  python tools/build.py
"""
import pathlib, re, subprocess, sys, importlib.util

# ---- Launch settings: the only lines you should need to change ----
DOMAIN = 'firemarktech.com'   # the domain you bought, no https:// (for example 'firemarktech.co')
LAUNCHED = False              # True on launch day: removes the draft banner and the noindex tag from public pages
HIDDEN = {'brand.html', '404.html'}   # these stay hidden from search engines even after launch
PUBLIC = ['index.html', 'work.html', 'about.html', 'contact.html', 'privacy.html']   # listed in sitemap.xml
# ---------------------------------------------------------------------
ROBOTS_META = '  <meta name="robots" content="noindex, nofollow">\n'
BANNER = re.compile(r'  <aside class="draft-banner".*?</aside>\n\n?', re.S)


def finish(file, html):
    """Applies the launch settings to a finished page."""
    if LAUNCHED and file not in HIDDEN:
        html = html.replace(ROBOTS_META, '')
    if LAUNCHED and file != 'brand.html':
        html = BANNER.sub('', html)
    if DOMAIN != 'firemarktech.com':
        html = html.replace('firemarktech.com', DOMAIN)
    return html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
DOCS = ROOT / 'docs'

sprite = (SRC / 'partials' / 'sprite.html').read_text(encoding='utf-8')
form = (SRC / 'partials' / 'form.html').read_text(encoding='utf-8')

# 1) Homepage
home = (SRC / 'index.html').read_text(encoding='utf-8').replace('{{SPRITE}}', sprite).replace('{{FORM}}', form)
(DOCS / 'index.html').write_text(finish('index.html', home), encoding='utf-8')
print('built index.html')

# 2) Shared header and footer for inner pages, with links pointed at real pages
header = re.search(r'  <header class="site-header".*?</header>\n', home, re.S).group(0)
footer = re.search(r'  <footer class="site-footer">.*?</footer>\n', home, re.S).group(0)
for a, b in [('href="#work"', 'href="work.html"'), ('href="#offer"', 'href="index.html#offer"'), ('href="#check"', 'href="contact.html"')]:
    header = header.replace(a, b)
footer = footer.replace('href="#main"', 'href="#main"')

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
  <link rel="stylesheet" href="css/site.css?v=7">
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  {sprite}

  <aside class="draft-banner" aria-label="Draft notice">{banner}</aside>

'''

def page(file, title, desc, h1, lead, body, banner='Draft preview. Contact details are placeholders until launch.', current=None):
    h = header
    if current:
        h = h.replace(f'href="{current}"', f'href="{current}" aria-current="page"', 1)
    canonical = '' if file == '404.html' else f'<link rel="canonical" href="https://firemarktech.com/{file}">'
    html = HEAD.format(title=title, desc=desc, canonical=canonical, sprite=sprite, banner=banner)
    html += h + f'''
  <main id="main">
    <div class="wrap page-head">
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
    </div>
{body}
  </main>

''' + footer + '''
  <script src="js/site.js?v=7" defer></script>
</body>
</html>
'''
    (DOCS / file).write_text(finish(file, html), encoding='utf-8')
    print('built', file)

# 3) Inner pages (content in src/pages.py)
pages_py = SRC / 'pages.py'
if pages_py.exists():
    spec = importlib.util.spec_from_file_location('pages', pages_py)
    mod = importlib.util.module_from_spec(spec)
    mod.page = page
    mod.form = form
    spec.loader.exec_module(mod)

# 4) 404 must work at any address, so its links start from the site's root folder.
#    The site is served from firemarktech.com, so the root is "/".
#    (It was "/Firemark/" while the preview lived at jsglisson3.github.io/Firemark/.)
SITE_ROOT = '/'
p404 = DOCS / '404.html'
if p404.exists():
    s = p404.read_text(encoding='utf-8')
    s = re.sub(r'(href|src)="(?!https?:|#|mailto:|/)([^"]+)"', lambda m: f'{m.group(1)}="{SITE_ROOT}{m.group(2)}"', s)
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
