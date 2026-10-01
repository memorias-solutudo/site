# -*- coding: utf-8 -*-
"""Moldura da central da Execon: cabeçalho, abas, CSS e script herdados da LAAE."""
SP = '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad'
STYLE = open(f'{SP}/laae_style.css', encoding='utf-8').read()
SCRIPT = open(f'{SP}/laae_script.js', encoding='utf-8').read()
TABS = [('parc', 'Parceiro'), ('agt', 'Agentes'), ('dest', 'Destaque'), ('site', 'Solusite'), ('cont', 'Conteúdo')]
SCRIPT = SCRIPT.replace("['parc','dest','site','gmb','soc','cont']", "['parc','agt','dest','site','cont']")
SCRIPT = SCRIPT.replace("['dest','site','gmb','soc','cont'].indexOf(h)", "['agt','dest','site','cont'].indexOf(h)")
assert "'agt'" in SCRIPT and SCRIPT.count("'gmb'") == 0

EXTRA_CSS = r'''
  /* Execon · marcas de fonte próprias deste caso */
  mark.pv.cs,.pvl.cs{box-shadow:inset 0 -2px 0 #0B7FAB}
  mark.pv.pub,.pvl.pub{background:#FFF4E5;box-shadow:inset 0 -2px 0 #B45309}
  mark.pv.setor,.pvl.setor{box-shadow:inset 0 -2px 0 var(--g500)}
  mark.pv.conf,.pvl.conf{background:#FFE4E0;box-shadow:inset 0 -2px 0 #C42B22}
  mark.pv.vazio,.pvl.vazio{background:var(--g100);box-shadow:inset 0 -2px 0 var(--g500)}
  mark.pv.trad,.pvl.trad{background:#FFE4E0;box-shadow:inset 0 -2px 0 #7A1D14}
  .nh{font-weight:800;color:var(--ink);margin-top:12px}
  .nh:first-child{margin-top:0}
  /* agentes */
  .ag-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin-top:14px}
  .ag{background:var(--white);border:var(--line);border-radius:16px;padding:14px 15px;display:flex;flex-direction:column;gap:7px}
  .ag-h{display:flex;align-items:center;gap:9px}
  .ag-n{flex:none;width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12.5px;font-weight:800;color:#fff;background:var(--grad-cta)}
  .ag-t{font-weight:800;font-size:13.8px;letter-spacing:-.02em;line-height:1.2}
  .ag-t small{display:block;font-weight:700;font-size:11px;color:var(--g500);letter-spacing:0;margin-top:1px}
  .ag p{font-size:12.8px;color:var(--g700);line-height:1.5;margin:0}
  .ag .ag-k{display:flex;flex-wrap:wrap;gap:5px}
  .ag .ag-k span{font-size:10.5px;font-weight:800;padding:3px 8px;border-radius:var(--pill);background:var(--g100);color:var(--g700)}
  .ag .ag-k span.ok{background:var(--tint-mint);color:#06724F}
  .ag .ag-k span.pa{background:var(--tint-yellow);color:#7A5A00}
  .ag .ag-k span.no{background:#FFE4E0;color:#A3200F}
  .phase{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:10px}
  .phase span{font-size:12px;font-weight:800;padding:6px 12px;border-radius:var(--pill);background:var(--tint-lav);color:#7B00BE}
  .phase i{font-style:normal;color:var(--g500);font-weight:800}
  .verdict{display:flex;align-items:center;gap:12px;flex-wrap:wrap;padding:14px 16px;border-radius:14px;margin-top:12px;font-weight:700;font-size:14px}
  .verdict b{font-size:12px;letter-spacing:.06em;text-transform:uppercase;padding:5px 11px;border-radius:var(--pill)}
  .verdict.ok{background:var(--tint-mint);color:#064E36}.verdict.ok b{background:#06724F;color:#fff}
  .verdict.pa{background:var(--tint-yellow);color:#5A4200}.verdict.pa b{background:#7A5A00;color:#fff}
  .verdict.no{background:#FFE4E0;color:#7A1D14}.verdict.no b{background:#A3200F;color:#fff}
  .ba{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px}
  .ba > div{border-radius:14px;padding:13px 15px;border:var(--line);background:var(--white)}
  .ba h5{font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--g600);margin-bottom:6px}
  .ba .bnow{background:#FFF8F5;border-color:rgba(255,104,73,.25)}
  .ba .bnext{background:#F3FCF8;border-color:rgba(0,181,137,.3)}
  .ba p{font-size:13.4px;line-height:1.5;margin:4px 0 0;color:var(--ink)}
  @media(max-width:760px){.ba{grid-template-columns:1fr}}
'''

def page(title, hero_badge, h1, crumbs, panels, drawers=''):
    ON = ' class="on"'
    tabs = '\n'.join('      <button id="t-%s"%s onclick="show(\'%s\')">%s</button>' % (k, ON if i == 0 else '', k, lab) for i, (k, lab) in enumerate(TABS))
    style = STYLE.replace('</style>', EXTRA_CSS + '</style>')
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700;9..40,800&display=swap" />
{style}
</head>
<body>

<div class="topbar">
  <div class="tb-in">
    <a href="../" class="logo" style="text-decoration:none;color:inherit"><span class="heart"></span> Solutudo <span style="font-weight:700;color:var(--g600);font-size:13px">· parceiros</span></a>
    <nav class="seg" aria-label="Abas">
{tabs}
    </nav>
    <div id="pnav" data-atual="grupo-execon"></div>
  </div>
</div>

<div class="hero">
  <span class="vbadge">{hero_badge}</span>
  <h1>{h1}</h1>
  <p class="crumbs">{crumbs}</p>
</div>

<div class="wrap">

  <a class="backlink" href="../"><span aria-hidden="true">←</span> Todos os parceiros</a>

{panels}

</div>

{drawers}
<div class="dw-back" id="dw-back" onclick="closeItem()"></div>
<aside class="dw" id="dw" role="dialog" aria-modal="true" aria-labelledby="dw-title"></aside>

{SCRIPT}

<script src="../parceiros.js" defer></script>
</body>
</html>
'''
