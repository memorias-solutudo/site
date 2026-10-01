import { createRequire } from 'module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const URL = 'http://localhost:8765/artefatos/parceiros/grupo-execon/';
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const out = {};
for (const w of [1400, 768, 390]) {
  const p = await b.newPage({viewport:{width:w,height:900}});
  await p.route(/fonts\.(googleapis|gstatic)\.com/, r=>r.abort());
  const errs=[]; p.on('pageerror', e=>errs.push(e.message)); p.on('console', m=>{ if(m.type()==='error') errs.push('console: '+m.text()); });
  await p.goto(URL); await p.waitForTimeout(400);
  const res = {};
  for (const t of ['parc','agt','dest','site','cont']) {
    await p.click('#t-'+t); await p.waitForTimeout(150);
    res[t] = await p.evaluate((t)=>({vis: getComputedStyle(document.getElementById('p-'+t)).display!=='none', ov: document.documentElement.scrollWidth - window.innerWidth, h: document.getElementById('p-'+t).scrollHeight}), t);
  }
  // drawer for every catalog card
  await p.click('#t-dest'); await p.waitForTimeout(100);
  const n = await p.$$eval('.catcard', els=>els.length);
  const dr = [];
  for (let i=0;i<n;i++){
    await p.$$eval('.catcard', (els,i)=>els[i].click(), i); await p.waitForTimeout(80);
    dr.push(await p.evaluate(()=>{const d=document.getElementById('dw'); return {on:d.classList.contains('on'), t:(document.getElementById('dw-title')||{}).textContent, ov: d.scrollWidth - d.clientWidth}}));
    await p.keyboard.press('Escape'); await p.waitForTimeout(50);
  }
  res.drawers = dr;
  out[w] = {res, errs};
  if (w===1400) {
    await p.goto(URL+'#s-eua'); await p.waitForTimeout(900);
    out.hash = await p.evaluate(()=>({site: getComputedStyle(document.getElementById('p-site')).display!=='none', top: Math.round(document.getElementById('s-eua').getBoundingClientRect().top)}));
  }
  await p.close();
}
console.log(JSON.stringify(out, null, 1));
await b.close();
