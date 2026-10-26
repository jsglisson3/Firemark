// Makes the PNG icons and the share image from the SVG logo files.
// Usage (from the project folder): node tools/make-assets.js
// Needs Playwright (npm i -D playwright, then npx playwright install chromium).
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '..');
const symbol = fs.readFileSync(path.join(root, 'docs/images/brand/firemark-symbol.svg'), 'utf8')
  .replace(/<title>.*?<\/title>/, '')
  .replace(/<metadata>[\s\S]*?<\/metadata>/, '');

const icons = [
  // file, canvas size, symbol height, background (null = transparent)
  ['favicon-32.png', 32, 30, null],
  ['apple-touch-icon.png', 180, 116, '#F6F5F3'],
  ['favicon-192.png', 192, 124, '#F6F5F3'],
  ['favicon-512.png', 512, 330, '#F6F5F3'],
  ['favicon-512-maskable.png', 512, 270, '#F6F5F3'],
];

(async () => {
  const browser = await chromium.launch();
  for (const [file, size, h, bg] of icons) {
    const page = await browser.newPage({ viewport: { width: size, height: size } });
    const svg = symbol.replace('<svg ', `<svg style="height:${h}px;width:auto;display:block" `);
    await page.setContent(`<!doctype html><html><body style="margin:0;width:${size}px;height:${size}px;display:grid;place-items:center;background:${bg || 'transparent'}">${svg}</body></html>`);
    await page.screenshot({ path: path.join(root, 'docs/images', file), omitBackground: !bg });
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
