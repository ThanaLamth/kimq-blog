// Chụp ảnh màn hình theo data/screenshots.json, lưu vào images/<slug>/<name>.webp
// Cần: npm i puppeteer-core
// Trình duyệt: đặt BROWSER_WS_ENDPOINT (CDP của trình duyệt từ xa) hoặc CHROME_PATH (Chrome trên máy).
// Tuỳ chọn mỗi ảnh: waitMs, waitUntil, scrollY, scrollToText (cuộn tới đoạn chữ và tô nổi bật), highlight:false,
// clickText (bấm nút có đúng chữ này trước khi chụp, ví dụ để chụp hộp thoại đăng nhập),
// fill ({"placeholder": "chữ cần gõ"}: gõ vào ô có placeholder tương ứng, dùng để ghi lại thử nghiệm).
// Dùng: node scripts/capture_screenshots.mjs [slug ...]  (bỏ trống = tất cả; ảnh đã có thì bỏ qua, thêm --force để chụp lại)
import fs from 'node:fs';
import path from 'node:path';
import { createRequire } from 'node:module';

const require = createRequire(process.env.PUPPETEER_PATH ? process.env.PUPPETEER_PATH + '/' : import.meta.url);
const puppeteer = require('puppeteer-core');
const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const spec = JSON.parse(fs.readFileSync(path.join(root, 'data/screenshots.json'), 'utf8'));
const args = process.argv.slice(2);
const force = args.includes('--force');
const slugs = args.filter(a => !a.startsWith('--'));
const targets = slugs.length ? slugs : Object.keys(spec);

const browser = process.env.BROWSER_WS_ENDPOINT
  ? await puppeteer.connect({ browserWSEndpoint: process.env.BROWSER_WS_ENDPOINT })
  : await puppeteer.launch({ executablePath: process.env.CHROME_PATH, args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: 1366, height: 860 });
await page.setExtraHTTPHeaders({ 'Accept-Language': 'vi-VN,vi;q=0.9,en;q=0.8' });

const log = [];
for (const slug of targets) {
  for (const shot of spec[slug] || []) {
    const out = path.join(root, 'images', slug, `${shot.name}.webp`);
    if (fs.existsSync(out) && !force) { log.push(`skip ${slug}/${shot.name}`); continue; }
    fs.mkdirSync(path.dirname(out), { recursive: true });
    try {
      const res = await page.goto(shot.url, { waitUntil: shot.waitUntil || 'networkidle2', timeout: 60000 });
      await new Promise(r => setTimeout(r, shot.waitMs || 2500));
      await page.evaluate(() => {
        const re = /^(accept all|accept|allow all|agree|i agree|got it|đồng ý|chấp nhận( tất cả)?|ok)$/i;
        for (const b of document.querySelectorAll('button, a[role=button]')) {
          if (re.test((b.innerText || '').trim())) { b.click(); break; }
        }
      });
      await new Promise(r => setTimeout(r, 1000));
      await page.evaluate(() => {
        for (const b of document.querySelectorAll('[role=dialog] button[aria-label], button[aria-label*="lose" i], button[aria-label*="đóng" i]')) {
          if (/close|đóng|dismiss/i.test(b.getAttribute('aria-label') || '')) b.click();
        }
      });
      for (const [ph, text] of Object.entries(shot.fill || {})) {
        const input = await page.$(`input[placeholder="${ph}"], textarea[placeholder="${ph}"]`);
        if (input) { await input.click({ clickCount: 3 }); await input.type(text, { delay: 20 }); }
      }
      if (shot.fill) await new Promise(r => setTimeout(r, 1500));
      if (shot.clickText) {
        await page.evaluate(text => {
          const b = [...document.querySelectorAll('button, a, [role=button]')].find(e => (e.innerText || '').trim().toLowerCase() === text.toLowerCase());
          if (b) b.click();
        }, shot.clickText);
        await new Promise(r => setTimeout(r, shot.clickWaitMs || 4000));
      }
      if (shot.scrollY) await page.evaluate(y => window.scrollTo(0, y), shot.scrollY);
      if (shot.scrollToText) {
        await page.evaluate((text, highlight) => {
          const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
          let node;
          while ((node = walker.nextNode())) {
            if (node.textContent.trim() === text) {
              const el = node.parentElement;
              el.scrollIntoView({ block: 'center' });
              if (highlight) { el.style.outline = '3px solid #e11d48'; el.style.outlineOffset = '4px'; el.style.background = '#fde68a'; }
              return;
            }
          }
        }, shot.scrollToText, shot.highlight !== false);
        await new Promise(r => setTimeout(r, 800));
      }
      await page.screenshot({ path: out, type: 'webp', quality: 80 });
      log.push(`ok   ${slug}/${shot.name} (${res ? res.status() : '?'}) ${await page.title()}`);
    } catch (e) {
      log.push(`FAIL ${slug}/${shot.name} ${e.message}`);
    }
  }
}
await page.close();
process.env.BROWSER_WS_ENDPOINT ? await browser.disconnect() : await browser.close();
console.log(log.join('\n'));
