import { createRequire } from 'module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const w of [1400, 768, 390]) {
  const ctx = await b.newContext({viewport:{width:w,height:900}});
  const p = await ctx.newPage();
  await p.route(/fonts\.(googleapis|gstatic)\.com/, r=>r.abort());
  const errs=[]; p.on('pageerror', e=>errs.push(e.message));
  await p.goto('http://localhost:8765/artefatos/parceiros/');
  await p.waitForTimeout(400);
  const before = await p.textContent('#g-url');
  const dis = await p.$eval('#g-open', e=>e.disabled);
  await p.fill('#g-key', 'abcd1234efgh5678');
  await p.fill('#g-id', '32069845');
  const after = await p.textContent('#g-url');
  const ls = await p.evaluate(()=>localStorage.getItem('soluintel.apiKey'));
  const dis2 = await p.$eval('#g-open', e=>e.disabled);
  const ov = await p.evaluate(()=>document.documentElement.scrollWidth - window.innerWidth);
  console.log(w, {before, dis, after, ls, dis2, overflow: ov, errs});
  await p.locator('#comecar').screenshot({path:`hub-start-${w}.png`});
  await ctx.close();
}
await b.close();
