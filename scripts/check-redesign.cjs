/* Run against the Jekyll output served at http://127.0.0.1:4000. */
const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROME_PATH || '/usr/bin/google-chrome', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', error => errors.push(error.message));
  for (const width of [1440, 390]) {
    await page.setViewportSize({ width, height: 1000 });
    for (const [name, path] of [['home', '/'], ['publications', '/publications/']]) {
      const response = await page.goto('http://127.0.0.1:4000' + path);
      if (await page.locator('.masthead').evaluate(el => getComputedStyle(el).position) !== 'sticky') throw Error('Preview stylesheet did not load');
      if (!response.ok()) throw Error('Page failed: ' + path);
      if (await page.evaluate(() => document.documentElement.scrollWidth > innerWidth)) throw Error('Horizontal overflow: ' + name + ' at ' + width);
      await page.screenshot({ path: '_site/review-' + name + '-' + width + '.png', fullPage: true });
      if (width === 1440) {
        const image = await page.screenshot({ type: 'jpeg', quality: 65 });
        console.log('REVIEW_START_' + name);
        const encoded = image.toString('base64');
        for (let i=0; i<encoded.length; i+=4096) console.log(encoded.slice(i,i+4096));
        console.log('REVIEW_END_' + name);
      }
    }
    const visible = () => page.locator('[data-publication]:visible').count();
    if (await visible() !== 15) throw Error('Incomplete catalogue');
    for (const [name, expected] of [['Journal articles', 10], ['Working papers', 2], ['Reports', 3], ['All', 15]]) {
      const button = page.getByRole('button', { name, exact: true });
      await button.click();
      if (await visible() !== expected || await button.getAttribute('aria-pressed') !== 'true') throw Error('Filter failed: ' + name + ' visible=' + await visible() + ' pressed=' + await button.getAttribute('aria-pressed') + ' errors=' + errors.join(';') + ' cards=' + await page.locator('[data-publication]').evaluateAll(cards => JSON.stringify(cards.map(c => [c.dataset.type, c.hidden, getComputedStyle(c).display]))));
    }
    await page.locator('input[type=search]').fill('pretis 2024');
    if (await visible() !== 2) throw Error('Multi-term search failed');
    await page.locator('input[type=search]').fill('no such publication');
    if (!await page.locator('[data-publication-empty]').isVisible()) throw Error('Empty state failed');
    await page.locator('input[type=search]').fill('');
    await page.locator('input[type=search]').focus();
    await page.keyboard.press('Tab');
    if (await page.locator(':focus').getAttribute('data-filter') !== 'all') throw Error('Keyboard order failed');
  }
  const noJS = await browser.newContext({ javaScriptEnabled: false });
  const fallback = await noJS.newPage();
  await fallback.goto('http://127.0.0.1:4000/publications/');
  if (await fallback.locator('[data-publication]:visible').count() !== 15) throw Error('No-JS fallback failed');
  if (errors.length) throw Error(errors.join('\n'));
  await browser.close();
  console.log('PASS: desktop/mobile layout, 15 records, filters, search, empty state, keyboard order and no-JS fallback.');
})().catch(error => { console.error(error); process.exit(1); });
