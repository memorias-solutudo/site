import { createRequire } from 'module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const URL = 'http://localhost:8765/artefatos/parceiros/grupo-execon/';
const shots = process.argv.slice(2);
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const s of shots) {
  const [target, w, file, extra] = s.split('|');
  const p = await b.newPage({viewport:{width:+w,height:1000}});
  await p.route(/fonts\.(googleapis|gstatic)\.com/, r=>r.abort());
  await p.goto(URL + (target.startsWith('#') ? target : ''));
  await p.waitForTimeout(900);
  if (!target.startsWith('#')) {
    // target = selector within a tab: tab>selector
    const [tab, sel] = target.split('>');
    await p.click('#t-'+tab); await p.waitForTimeout(200);
    if (extra === 'drawer') { await p.$$eval('.catcard', els=>els[0].click()); await p.waitForTimeout(300); await p.screenshot({path:file}); await p.close(); continue; }
    const el = p.locator(sel).first();
    await el.scrollIntoViewIfNeeded();
    await el.screenshot({path:file});
  } else {
    await p.screenshot({path:file});
  }
  await p.close();
}
await b.close();
console.log('ok');
