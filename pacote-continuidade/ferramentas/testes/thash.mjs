import { createRequire } from 'module';
const require = createRequire('/opt/node22/lib/node_modules/');
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const URL = 'http://localhost:8765/artefatos/parceiros/grupo-execon/';
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const h of ['s-eua','c-editorias','dest','agt']) {
  const p = await b.newPage({viewport:{width:1400,height:900}});
  await p.route(/fonts\.(googleapis|gstatic)\.com/, r=>r.abort());
  await p.goto(URL+'#'+h); await p.waitForTimeout(1200);
  console.log(h, await p.evaluate((h)=>{const on=[...document.querySelectorAll('.panel')].filter(x=>getComputedStyle(x).display!=='none').map(x=>x.id); const el=document.getElementById(h); return {on, top: el? Math.round(el.getBoundingClientRect().top):null}}, h));
  await p.close();
}
await b.close();
