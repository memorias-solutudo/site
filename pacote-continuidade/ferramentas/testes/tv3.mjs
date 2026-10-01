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
await p.route('**://fonts.g*/**', r => r.abort());
const base = 'http://localhost:8765/artefatos/parceiros/laae-laboratorio/';
await p.goto(base + '#site', { waitUntil: 'load' });
await p.addStyleTag({ content: 'html{scroll-behavior:auto!important}' });
await p.waitForTimeout(300);
const doc = fs.readFileSync('/home/user/soluintel/docs/solusite-padrao.md','utf8');
const spec = doc.match(/## 7\.[\s\S]*?```text\n([\s\S]*?)```/)[1].replace(/\n$/,'');
const r = await p.evaluate(() => {
  const norm = t => t.replace(/\s+/g,' ').trim();
  const out = {};
  out.menu = [...document.querySelectorAll('#p-site .cm-i')].map(a => a.textContent.trim());
  out.secs = [...document.querySelectorAll('#p-site .csec')].map(s => s.id);
  // texto do laboratório: Solusite × Destaque
  const site = document.querySelector('#s-conteudo .pgf-body').cloneNode(true);
  site.querySelectorAll('.pgf-crumb,h1,.pg-btn,.pgf-upd').forEach(n => n.remove());
  const dest = document.querySelector('#p-dest .col.next .colb').cloneNode(true);
  out.descSame = norm(site.textContent) === norm(dest.textContent);
  out.descLens = [norm(site.textContent).length, norm(dest.textContent).length];
  // catálogo: cada página × cada ficha
  out.items = [...document.querySelectorAll('#s-analises details.pgd')].map(d => {
    const key = (d.querySelector('button.backlink').getAttribute('onclick').match(/openItem\('([^']+)'/) || [])[1];
    const pg = d.querySelector('.pgf-body');
    const pageTxt = norm([...pg.querySelectorAll(':scope > p, :scope > ul')].slice(0, 3).map(n => n.textContent).join(' '));
    const tpl = document.getElementById('if-' + key);
    const colb = tpl ? tpl.querySelector('.col.next .colb') : null;
    let fichaTxt = '';
    if (colb) { const ps = [...colb.children]; fichaTxt = norm([ps[1], ps[2], ps[3]].filter(Boolean).map(n => n.textContent).join(' ')); }
    return { key, same: pageTxt === fichaTxt, card: !!document.querySelector(`button.catcard[onclick*="'${key}'"]`) };
  });
  // FAQ: página Solutudo × site
  const dq = [...document.querySelectorAll('#p-dest .txt h4')].map(h => norm(h.textContent));
  const sq = [...document.querySelectorAll('#s-faq .faqi h4')].map(h => norm(h.textContent));
  const da = [...document.querySelectorAll('#p-dest .txt h4')].map(h => norm(h.nextElementSibling.textContent));
  const sa = [...document.querySelectorAll('#s-faq .faqi')].map(f => norm(f.querySelector('.faq-a').textContent));
  out.faqSameQ = JSON.stringify(dq.slice(0,8)) === JSON.stringify(sq);
  out.faqSameA = da.slice(0,7).every((a, i) => a === sa[i]);
  out.cards = document.querySelectorAll('#p-dest button.catcard').length;
  out.fichas = document.querySelectorAll('.itemfull').length;
  out.generic = [...document.querySelectorAll('#p-site .pgf-body h1, #p-site .pgf-body h2')].map(h => h.textContent.trim()).filter(t => /^(Serviços|Sobre|Contato|O que analisamos|Como trabalhamos|Onde coletamos|Quem atendemos|Atendimento e pagamento|Perguntas frequentes)$/i.test(t));
  out.ld = (() => { try { JSON.parse(document.getElementById('ld-sobre').textContent); return true; } catch(e) { return String(e); } })();
  out.google = norm(document.querySelector('#p-gmb .txt p')?.textContent || '').length;
  out.bio = norm([...document.querySelectorAll('#p-soc .txt p')][0]?.textContent || '').length;
  return out;
});
console.log(JSON.stringify(r));
console.log('spec idêntica à fonte:', (await p.evaluate(() => document.getElementById('spec-text').textContent)) === spec);
// abrir uma página de análise e a ficha correspondente
await p.evaluate(() => document.getElementById('s-analises').scrollIntoView());
await p.click('#s-analises details.pgd:nth-of-type(1) summary'); await p.waitForTimeout(300);
await p.screenshot({ path: 'v3-analise.png' });
await p.click('#s-analises details.pgd[open] button.backlink'); await p.waitForTimeout(500);
console.log('ficha abre pelo Solusite:', await p.evaluate(() => ({ on: document.getElementById('dw').classList.contains('on'), t: document.getElementById('dw-title')?.textContent })));
await p.screenshot({ path: 'v3-ficha.png' });
await p.keyboard.press('Escape'); await p.waitForTimeout(300);
for (const id of ['s-conteudo','s-blocos','s-alem','s-paginas']) {
  await p.evaluate(i => document.getElementById(i).scrollIntoView(), id); await p.waitForTimeout(350);
  await p.screenshot({ path: 'v3-' + id + '.png' });
}
await p.evaluate(() => { const c = [...document.querySelectorAll('#s-conteudo .card')][1]; c.scrollIntoView(); }); await p.waitForTimeout(300);
await p.screenshot({ path: 'v3-metricas.png' });
// mobile
for (const [w,h] of [[390,844],[768,900]]) {
  await p.setViewportSize({width:w,height:h});
  for (const hh of ['#site','#s-conteudo','#s-analises','#s-alem','#s-paginas','#dest']) {
    await p.goto('about:blank'); await p.goto(base + hh, { waitUntil:'load' }); await p.waitForTimeout(400);
    if (hh === '#s-analises') { await p.evaluate(() => document.querySelectorAll('#s-analises details.pgd').forEach(d => d.open = true)); await p.waitForTimeout(200); }
    const rr = await p.evaluate(() => ({ sw: document.documentElement.scrollWidth, cw: document.documentElement.clientWidth }));
    console.log(w + 'px ' + hh.padEnd(12), 'rolagem horizontal:', rr.sw > rr.cw, rr.sw);
  }
  if (w === 390) { await p.goto('about:blank'); await p.goto(base + '#s-analises', { waitUntil:'load' }); await p.waitForTimeout(400); await p.evaluate(() => { const d = document.querySelector('#s-analises details.pgd'); d.open = true; d.scrollIntoView(); }); await p.waitForTimeout(300); await p.screenshot({ path: 'v3-m-analise.png' }); }
}
console.log('ERROS:', errs.length ? errs : 'nenhum');
await b.close();
