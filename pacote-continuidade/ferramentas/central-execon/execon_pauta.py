# -*- coding: utf-8 -*-
"""Aba Conteúdo: lê 32-pauta.md (escrito pelo planejador de pauta) e devolve as estruturas da aba."""
import os, re, html
P = '/tmp/claude-0/-home-user-site/ca93b4a4-2949-59bb-bf95-0eb026ad284b/scratchpad/dossie-grupo-execon/32-pauta.md'
READY = os.path.exists(P)
E = html.escape

def clean(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    t = t.replace('`', '').strip()
    return t

def sections(txt, level):
    """divide por cabeçalhos de um nível: devolve [(título, corpo)]"""
    rx = re.compile(r'^' + '#' * level + r' +(.+?)\s*$', re.M)
    idx = [(m.start(), m.end(), m.group(1)) for m in rx.finditer(txt)]
    out = []
    for i, (a, b, t) in enumerate(idx):
        end = idx[i + 1][0] if i + 1 < len(idx) else len(txt)
        out.append((clean(t), txt[b:end]))
    return out

def table(txt):
    rows = []
    for ln in txt.splitlines():
        ln = ln.strip()
        if not ln.startswith('|'): continue
        cells = [clean(c) for c in ln.strip('|').split('|')]
        if all(re.fullmatch(r':?-{2,}:?', c.replace(' ', '')) for c in cells if c): continue
        rows.append(cells)
    return rows[1:] if rows else []   # tira o cabeçalho

def kv(txt):
    """bloco '- chave: valor' com sublistas; devolve {chave: texto} e {chave: [itens]}"""
    vals, lists, cur = {}, {}, None
    for raw in txt.splitlines():
        if not raw.strip(): continue
        m = re.match(r'^[-*]\s*\**([A-Za-zçãõéêíóú_ ]{2,20}?)\**\s*:\**\s*(.*)$', raw)
        if m and not raw.startswith((' ', '\t')):
            cur = m.group(1).strip().lower().replace(' ', '_')
            vals[cur] = clean(m.group(2)); lists[cur] = []
            continue
        m2 = re.match(r'^\s+[-*]\s+(.*)$', raw) or (cur != 'legenda' and re.match(r'^\s*\d+[.)]\s+(.*)$', raw))
        if cur and m2:
            lists[cur].append(clean(m2.group(1))); continue
        if cur and not raw.lstrip().startswith(('#', '|')):
            vals[cur] = (vals[cur] + '\n' + clean(raw)).strip()
    return vals, lists

def pick(d, *keys, default=''):
    for k in keys:
        if d.get(k): return d[k]
    return default

SLOT_NAME = {'A': 'A · Processo e origem', 'B': 'B · Oferta', 'C': 'C · Conversão', 'D': 'D · Público e experiência', 'E': 'E · Território', 'F': 'F · Dúvidas'}
ICONS = {'sobre', 'oferta', 'dif', 'prova', 'contato', 'onde'}

CONT_FONTES = []; CONT_NOTA = ''; ED = []; DATAS = []; DATAS_OUT = []; DATAS_HEAD = ''; DATAS_NOTE = ''
HL = []; HL_OUT = []; HL_HEAD = ''; HL_WHY = ''; CIDADES_RULE = []; CIDADES_HEAD = ''; FIX = []
SIG_ROWS = []; SIG_TEXT = ''; SIG_HTML = ''; SIG_WHY = ''; BIO = ''; BIO_N = 0; BIO_WHY = ''; FILTROS = []; PEND_CONT = []
CONT_H2 = 'Editorias, temas e peças fixas do perfil'; CONT_SUB = ''

if READY:
    TXT = open(P, encoding='utf-8').read()
    S2 = dict((t.split('.', 1)[0].strip(), (t, b)) for t, b in sections(TXT, 2))
    def sec(n): return S2.get(str(n), ('', ''))[1]

    # 0 · fontes
    STT = {'lido': ('ok', 'lido'), 'colado': ('ok', 'colado'), 'parcial': ('pa', 'parcial'), 'não acessado': ('no', 'não acessado'), 'nao acessado': ('no', 'não acessado')}
    for r in table(sec(0)):
        if len(r) < 3: continue
        st = r[1].lower()
        k, lab = next((v for key, v in STT.items() if key in st), ('pa', E(r[1].lower())))
        CONT_FONTES.append((E(r[0]), '', k, lab, E(r[2])))

    # 1 · editorias
    for t, body in sections(sec(1), 3):
        nome = re.sub(r'^E\d+\s*[·.\-–:]\s*', '', t).strip()
        v, l = kv(body)
        slot = pick(v, 'slot')
        sl = slot.strip()[:1].upper()
        conteudos = []
        for it in l.get('conteudos', []) or l.get('conteúdos', []):
            m = re.search(r'\s*\[condi[çc][ãa]o:\s*(.+?)\]\s*$', it)
            conteudos.append((it[:m.start()].strip() if m else it, m.group(1).strip() if m else ''))
        temas = []
        for it in l.get('temas', []):
            parts = [x.strip() for x in it.split('::')]
            while len(parts) < 3: parts.append('')
            flags = [f.strip() for f in re.split(r'[,;/]', parts[2]) if f.strip() in ('tema único', 'série recorrente')]
            temas.append((re.sub(r'^\d+\s*[·.\-–]\s*', '', parts[0]), parts[1], flags))
        ED.append(dict(nome=nome, slot=SLOT_NAME.get(sl, slot), objetivo=pick(v, 'objetivo'), pergunta=pick(v, 'pergunta').strip('"“”'),
                       ids=pick(v, 'fatos'), conteudos=conteudos, temas=temas))

    # 2 · datas
    body2 = sec(2)
    subs = dict((t.lower(), b) for t, b in sections(body2, 3))
    main2 = body2.split('\n### ', 1)[0]
    DATAS = [tuple(r[:4]) for r in table(main2) if len(r) >= 4]
    DATAS_OUT = [tuple(r[:2]) for r in table(next((b for k, b in subs.items() if 'descart' in k), '')) if len(r) >= 2]
    DATAS_NOTE = E(clean(' '.join(ln.strip() for ln in next((b for k, b in subs.items() if 'nota' in k), '').splitlines() if ln.strip())))
    DATAS_HEAD = f'{len(DATAS)} datas cruzam com um fato da Execon' if DATAS else 'Nenhuma data cruza com um fato da Execon'

    # 3 · destaques
    for t, body in sections(sec(3), 3):
        tl = t.lower()
        if tl.startswith('descart'):
            for ln in body.splitlines():
                m = re.match(r'^\s*[-*]\s+(.*)$', ln)
                if m:
                    a, _, b = clean(m.group(1)).partition('::')
                    HL_OUT.append((a.strip(), b.strip()))
            continue
        if tl.startswith('ordem'):
            HL_WHY = E(clean(' '.join(x.strip() for x in body.splitlines() if x.strip()))); continue
        titulo = re.sub(r'^D\d+\s*[·.\-–:]\s*', '', t).strip()
        v, l = kv(body)
        icon = pick(v, 'icone', 'ícone').lower().strip()
        HL.append(dict(titulo=titulo, funcao=pick(v, 'funcao', 'função'), slot=pick(v, 'slot'), icon=icon if icon in ICONS else 'sobre',
                       why=pick(v, 'porque', 'por_que'), dentro=l.get('dentro', []), nao=pick(v, 'nao_entra', 'não_entra')))
    HL_HEAD = 'Para quem vai construir uma casa de alto padrão, o perfil é conferido antes da conversa'

    # 4 · fixados
    for t, body in sections(sec(4), 3):
        funcao = re.sub(r'^F\d+\s*[·.\-–:]\s*', '', t).strip()
        v, l = kv(body)
        texto = []
        for it in l.get('texto_imagem', []) or l.get('texto_na_imagem', []):
            a, _, b = it.partition('::'); texto.append((a.strip(), b.strip()))
        FIX.append(dict(funcao=funcao, slot=pick(v, 'slot'), titulo=pick(v, 'titulo', 'título'), legenda=pick(v, 'legenda'),
                        imagem=l.get('imagem', []) or [pick(v, 'imagem')], texto=texto))

    # 5 · assinatura
    v, l = kv(sec(5))
    SIG_TEXT = pick(v, 'texto').strip('"“”')
    SIG_ROWS = [tuple(r[:4]) for r in table(sec(5)) if len(r) >= 4]
    wa = pick(v, 'whatsapp')
    SIG_HTML = E(SIG_TEXT)
    SIG_WHY = E(pick(v, 'porque', 'por_que', 'justificativa', default=''))

    # 6 · bio
    v, l = kv(sec(6))
    BIO = pick(v, 'texto').strip('"“”'); BIO_N = len(BIO.encode('utf-16-le')) // 2; BIO_WHY = pick(v, 'porque', 'por_que')

    # 7 · filtros, 8 · pendências
    FILTROS = [tuple(r[:2]) for r in table(sec(7)) if len(r) >= 2]
    PEND_CONT = [clean(m.group(1)) for m in re.finditer(r'^\s*[-*\d.)]+\s+(.*)$', sec(8), re.M)]

    CIDADES_HEAD = 'Capital, Grande SP, interior e litoral paulista. Ou aparece o alcance inteiro, ou nenhum lugar.'
    CIDADES_RULE = [
     ('Legenda do fixado 1</b> e <b>fixado 3', '<b>O alcance inteiro, por extenso</b><br><small>capital e Grande São Paulo, interior e litoral paulista, inclusive obras em condomínios do interior</small>', 'Legenda não tem limite apertado. Os nomes dos condomínios entram quando a lista inteira for confirmada'),
     ('Destaque de onde a Execon atende', 'O alcance, com os condomínios do interior sem nomes até a lista inteira chegar', 'Dois nomes num destaque fixo seriam meia lista'),
     ('Texto dentro da imagem', '<b>Nenhum lugar</b> — entra o alcance: "capital, interior e litoral de SP"', 'Não cabe lista em arte de 1080 px legível'),
     ('Bio (150 caracteres)', '<b>Nenhum condomínio</b> — entra o alcance', 'Dois condomínios na bio diriam que os outros não são atendidos'),
     ('Assinatura (~70 caracteres)', '<b>Nenhum lugar</b> — ver a seção 6', 'A peça mais fixa de todas'),
     ('Endereço', '<b>Nenhum</b> — só "São Paulo (SP)"', 'Três endereços em conflito, dois em prédio de escritório compartilhado'),
    ]
    CONT_NOTA = ''
    CONT_H2 = f'{len(ED)} editorias e {sum(len(e["temas"]) for e in ED)} temas, com o envelope enxuto e sem inventar nada'
    CONT_SUB = ('Tudo aqui sai do envelope de fatos que o verificador aprovou e das perguntas reais do público, levantadas pelo agente de reputação e conteúdo. '
                'O que depende de confirmação entra com a condição escrita, em amarelo. As peças fixas do perfil, os destaques, os fixados, a assinatura e a bio, '
                'são recomendação a partir do cadastro: o Instagram não foi aberto.')
