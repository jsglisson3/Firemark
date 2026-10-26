// Makes the PNG icons and the share image from the SVG logo files.
// Usage (from the project folder): node tools/make-assets.js
// Needs Playwright (npm i -D playwright, then npx playwright install chromium).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const clean = f => fs.readFileSync(path.join(root, f), 'utf8')
  .replace(/<title>.*?<\/title>/, '')
  .replace(/<metadata>[\s\S]*?<\/metadata>/, '');
// The pin is tall and narrow, so the small icons use the charcoal tile (the same drawing as favicon.svg).
const tile = clean('docs/images/brand/firemark-app-icon.svg');
const fav = clean('docs/favicon.svg');

const icons = [
  // file, canvas size, svg, drawn size (the maskable icon keeps the pin inside the safe zone)
  ['favicon-32.png', 32, fav, 32],
  ['apple-touch-icon.png', 180, tile, 180],
  ['favicon-192.png', 192, tile, 192],
  ['favicon-512.png', 512, tile, 512],
  ['favicon-512-maskable.png', 512, tile, 512],
];

(async () => {
  const browser = await chromium.launch();
  for (const [file, size, src, d] of icons) {
    const page = await browser.newPage({ viewport: { width: size, height: size } });
    let svg = src.replace('<svg ', `<svg style="width:${d}px;height:${d}px;display:block" `);
    if (file.includes('maskable')) svg = svg.replace(/rx="[^"]*"/, 'rx="0"');
    await page.setContent(`<!doctype html><html><body style="margin:0;width:${size}px;height:${size}px;display:grid;place-items:center;background:transparent">${svg}</body></html>`);
    await page.screenshot({ path: path.join(root, 'docs/images', file), omitBackground: true });
    await page.close();
    console.log('made docs/images/' + file);
  }
  const og = await browser.newPage({ viewport: { width: 1200, height: 630 } });
  await og.goto('file://' + path.join(root, 'tools/og-card.html'));
  await og.evaluate(() => document.fonts.ready);
  await og.waitForTimeout(300);
  await og.screenshot({ path: path.join(root, 'docs/images/og-card.jpg'), type: 'jpeg', quality: 88 });
  console.log('made docs/images/og-card.jpg');
  await browser.close();
})();
