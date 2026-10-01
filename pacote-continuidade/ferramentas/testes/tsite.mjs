import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
import fs from 'fs';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ viewport: { width: 1500, height: 1000 }, deviceScaleFactor: 1.5 });
const errs = [];
p.on('pageerror', e => errs.push('JS: ' + e.message));
p.on('console', m => { if (m.type() === 'error' && !/ERR_|net::|Failed to load resource/.test(m.text())) errs.push('console: ' + m.text()); });
await p.route('**://solutudo-cdn.s3-sa-east-1.amazonaws.com/**', r => r.abort());
await p.route('**://fonts.googleapis.com/**', r => r.abort());
await p.route('**://fonts.gstatic.com/**', r => r.abort());
const base = 'http://localhost:8765/artefatos/parceiros/laae-laboratorio/';
await p.goto(base + '#site', { waitUntil: 'load' });
await p.addStyleTag({ content: 'html{scroll-behavior:auto!important}' });
await p.waitForTimeout(300);
const doc = fs.readFileSync('/home/user/soluintel/docs/solusite-padrao.md','utf8');
const spec = doc.match(/## 7\.[\s\S]*?```text\n([\s\S]*?)```/)[1].replace(/\n$/,'');
const info = await p.evaluate(() => ({
  siteOn: document.getElementById('p-site').classList.contains('on'),
  menu: [...document.querySelectorAll('#p-site .cm-i')].map(a => a.textContent.trim()),
  secs: [...document.querySelectorAll('#p-site .csec')].map(s => s.id),
  pages: document.querySelectorAll('#p-site .pgtbl tr').length - 1,
  faq: document.querySelectorAll('#p-site .faqi').length,
  cit: document.querySelectorAll('#p-site .citl li').length,
  marks: document.querySelectorAll('#p-site mark.pv').length,
  contMenu: document.querySelectorAll('#p-cont .cm-i').length,
  specLen: document.getElementById('spec-text').textContent.length,
  ldOk: (() => { try { JSON.parse(document.getElementById('ld-sobre').textContent); return true; } catch(e) { return String(e); } })(),
}));
console.log('SITE', JSON.stringify(info));
console.log('spec idêntica à fonte:', await p.evaluate(() => document.getElementById('spec-text').textContent) === spec);
// texto único idêntico entre Solusite e Destaque
const same = await p.evaluate(() => {
  const norm = t => t.replace(/\s+/g,' ').trim();
  const site = document.querySelector('#p-site .pgf-body').cloneNode(true);
  site.querySelectorAll('.pgf-crumb,h1,.pg-btn,.pgf-upd').forEach(n => n.remove());
  const dest = document.querySelector('#p-dest .col.next .colb').cloneNode(true);
  return { site: norm(site.textContent), dest: norm(dest.textContent) };
});
console.log('texto único idêntico nas duas abas:', same.site === same.dest, same.site.length, same.dest.length);
if (same.site !== same.dest) { for (let i=0;i<Math.min(same.site.length,same.dest.length);i++){ if(same.site[i]!==same.dest[i]){ console.log('diverge em', i, JSON.stringify(same.site.slice(i-40,i+60)), '||', JSON.stringify(same.dest.slice(i-40,i+60))); break; } } }
// menu → seção (Solusite)
await p.click('#p-site a.cm-i[href="#s-gate"]'); await p.waitForTimeout(500);
console.log('menu s-gate', JSON.stringify(await p.evaluate(() => ({ hash: location.hash, top: Math.round(document.getElementById('s-gate').getBoundingClientRect().top), on: document.querySelector('#p-site .cm-i.on')?.textContent.trim() }))));
// link cruzado: Destaque → Solusite
await p.click('#t-dest'); await p.waitForTimeout(300);
await p.click('#p-dest a[href="#s-conteudo"]'); await p.waitForTimeout(700);
console.log('Destaque→Solusite', JSON.stringify(await p.evaluate(() => ({ siteOn: document.getElementById('p-site').classList.contains('on'), top: Math.round(document.getElementById('s-conteudo').getBoundingClientRect().top) }))));
// link cruzado: Solusite → Conteúdo
await p.click('#p-site a[href="#c-editorias"]'); await p.waitForTimeout(700);
console.log('Solusite→Conteúdo', JSON.stringify(await p.evaluate(() => ({ contOn: document.getElementById('p-cont').classList.contains('on'), top: Math.round(document.getElementById('c-editorias').getBoundingClientRect().top) }))));
// hash direto
for (const h of ['s-paginas','c-fixados']) {
  await p.goto('about:blank'); await p.goto(base + '#' + h, { waitUntil: 'load' }); await p.waitForTimeout(600);
  console.log('load #' + h, JSON.stringify(await p.evaluate(id => ({ panel: document.querySelector('.panel.on').id, top: Math.round(document.getElementById(id).getBoundingClientRect().top) }), h)));
}
// copiar
await p.context().grantPermissions(['clipboard-read','clipboard-write']);
await p.goto('about:blank'); await p.goto(base + '#s-spec', { waitUntil: 'load' }); await p.waitForTimeout(500);
await p.click('#s-spec .copybtn'); await p.waitForTimeout(200);
console.log('copiar:', await p.evaluate(() => document.querySelector('#s-spec .copybtn').textContent));
// screenshots desktop
await p.goto('about:blank'); await p.goto(base + '#site', { waitUntil: 'load' });
await p.addStyleTag({ content: 'html{scroll-behavior:auto!important}' });
for (const id of ['s-padrao','s-conteudo','s-paginas','s-faq','s-tecnica','s-gate']) {
  await p.evaluate(i => document.getElementById(i).scrollIntoView(), id); await p.waitForTimeout(350);
  await p.screenshot({ path: 'sd-' + id + '.png' });
}
// mobile
for (const [w,h] of [[390,844],[768,900]]) {
  await p.setViewportSize({width:w,height:h});
  for (const hh of ['#site','#s-conteudo','#s-paginas','#s-tecnica','#dest']) {
    await p.goto('about:blank'); await p.goto(base + hh, { waitUntil:'load' }); await p.waitForTimeout(400);
    const r = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
    console.log(w + 'px ' + hh.padEnd(12), 'rolagem horizontal:', r.sw > r.cw, r.sw);
  }
  if (w === 390) for (const id of ['s-padrao','s-conteudo','s-paginas']) {
    await p.goto('about:blank'); await p.goto(base + '#' + id, { waitUntil:'load' }); await p.waitForTimeout(500);
    await p.screenshot({ path: 'sm-' + id + '.png' });
  }
}
console.log('ERROS:', errs.length ? errs : 'nenhum');
await b.close();
