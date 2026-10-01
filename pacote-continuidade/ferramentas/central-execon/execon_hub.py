# -*- coding: utf-8 -*-
"""Registra a Execon no hub de parceiros (cartão + seletor), com os números calculados pela build."""
import sys, re
SP = '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad'
sys.path.insert(0, SP)
import execon_rubric as R, execon_src as S, execon_parc as PA
HUB = '/home/user/soluintel/artefatos/parceiros/index.html'
JS = '/home/user/soluintel/artefatos/parceiros/parceiros.js'
ns = R.now_sents()
NT = R.score(ns[0][0], ns, R.NOW_HEADS, True, ns[-1][0], 'desc', R.NOW_WA, R.UNIQ)[0]
DT = S.score_desc()[0]
CARD = f'''    <div class="pcard done" data-nome="Grupo Execon" data-busca="grupo execon engenharia e construcao construtora construtoras casas de alto padrao sao paulo sp 23008544 gestao de obras reforma area de lazer pergolado ninho verde riviera de santa cristina estados unidos eua" data-estado="completa">
      <div class="ptop">
        <img class="plogo" src="https://solutudo-cdn.s3-sa-east-1.amazonaws.com/prod/adv_ads/6324d19e-3374-46c0-bc9c-1ce9ac1e0fec/634835d9-d6a0-4acb-af7d-182eac1e09ff.jpg" alt="Logotipo do Grupo Execon" loading="lazy" referrerpolicy="no-referrer">
        <div>
          <div class="pname">Grupo Execon</div>
          <div class="pmeta">Construtoras · São Paulo/SP · ID 23008544</div>
        </div>
      </div>
      <span class="st ok">● Central completa · 30/09/2026</span>
      <div class="chips">
        <span class="chip lav">Destaque</span><span class="chip lav">Solusite em montagem</span>
        <span class="chip" style="background:var(--tint-cyan);color:#0B5E70">Primeira pelo processo da API</span>
        <span class="chip" style="background:var(--tint-peach);color:#A33A12">Setor regulado</span>
      </div>
      <p class="pdesc">Primeira central feita pelo processo da API, com <b>dez execuções de agentes</b> na curadoria. O cadastro guarda duas histórias: o texto de 2022 fala em "sonho da casa própria" e "9 anos", e o banner de 28/09 já fala em alto padrão e expansão para os EUA. O verificador barrou <b>29 afirmações</b>, entre anos, números de obras e "projetos arquitetônicos" sem CAU, e travou os EUA numa frase só. <b>6 dos 9 produtos</b> passaram pelo tradutor automático.</p>
      <div class="kpi">
        <div><b>{NT}→{DT}</b>descrição</div>
        <div><b>{S.N_PUB}</b>páginas publicáveis</div>
        <div><b>{len(PA.CORRECOES)}</b>correções de cadastro</div>
        <div><b>63</b>imagens</div>
      </div>
      <a class="open" href="grupo-execon/">Abrir central</a>
    </div>

'''
s = open(HUB, encoding='utf-8').read()
if 'data-nome="Grupo Execon"' in s:
    a = s.index('    <div class="pcard done" data-nome="Grupo Execon"'); b = s.index('<a class="open" href="grupo-execon/">Abrir central</a>\n    </div>\n\n', a) + len('<a class="open" href="grupo-execon/">Abrir central</a>\n    </div>\n\n')
    s = s[:a] + CARD + s[b:]
else:
    anchor = '  </div>\n  <p class="nores" id="nores">'
    assert s.count(anchor) == 1
    s = s.replace(anchor, CARD.rstrip('\n') + '\n\n' + anchor, 1)
open(HUB, 'w', encoding='utf-8').write(s)
j = open(JS, encoding='utf-8').read()
if 'grupo-execon' not in j:
    old = '''    {
      pasta: "blocok-o-original",
      nome: "Blocok O Original",
      meta: "Pardinho e Avaré/SP",
      estado: "completa"
    }
  ];'''
    assert j.count(old) == 1
    j = j.replace(old, old[:-5] + ''',
    {
      pasta: "grupo-execon",
      nome: "Grupo Execon",
      meta: "São Paulo/SP",
      estado: "completa"
    }
  ];''', 1)
    open(JS, 'w', encoding='utf-8').write(j)
print('hub ok', NT, DT, S.N_PUB, len(PA.CORRECOES))
