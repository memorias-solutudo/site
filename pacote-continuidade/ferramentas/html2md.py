# -*- coding: utf-8 -*-
"""Converte uma central HTML em texto legível (Markdown simples), preservando as dicas data-tip
das marcações (fonte e justificativa de cada frase). Uso: python3 html2md.py entrada.html saida.md"""
import sys, re, html
from html.parser import HTMLParser

SKIP = {'script', 'style', 'svg', 'noscript', 'template', 'head'}
BLOCK = {'p', 'div', 'section', 'article', 'header', 'footer', 'main', 'aside', 'nav', 'ul', 'ol',
         'table', 'tr', 'blockquote', 'pre', 'figure', 'figcaption', 'details', 'summary', 'dl', 'dt', 'dd', 'br', 'hr'}

class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []; self.skip = 0; self.cell = None; self.row = None; self.tips = []; self.pre = 0
    def w(self, s): self.out.append(s)
    def handle_starttag(self, t, a):
        a = dict(a)
        if t in SKIP: self.skip += 1; return
        if self.skip: return
        if re.fullmatch(r'h[1-6]', t): self.w('\n\n' + '#' * min(int(t[1]) + 1, 6) + ' ')
        elif t == 'li': self.w('\n- ')
        elif t == 'tr': self.row = []
        elif t in ('td', 'th'): self.cell = []
        elif t == 'pre': self.pre += 1; self.w('\n\n```\n')
        elif t == 'br': self.w('\n')
        elif t in BLOCK: self.w('\n')
        if t == 'img' and a.get('alt'): self.w(f' [imagem: {a["alt"]}] ')
        if t == 'a' and a.get('href', '').startswith('http'): self.tips.append(('a', a['href']))
        elif t == 'a': self.tips.append(('a', None))
        tip = a.get('data-tip')
        if tip and t != 'a': self.tips.append((t, tip))
    def handle_endtag(self, t):
        if t in SKIP: self.skip = max(0, self.skip - 1); return
        if self.skip: return
        if t == 'a':
            for i in range(len(self.tips) - 1, -1, -1):
                if self.tips[i][0] == 'a':
                    _, href = self.tips.pop(i)
                    if href: self._emit(f' ({href})')
                    break
        else:
            for i in range(len(self.tips) - 1, -1, -1):
                if self.tips[i][0] == t:
                    _, tip = self.tips.pop(i); self._emit(f' ⟨nota: {tip}⟩'); break
        if t in ('td', 'th') and self.cell is not None and self.row is not None:
            self.row.append(re.sub(r'\s+', ' ', ''.join(self.cell)).strip().replace('|', '/')); self.cell = None
        elif t == 'tr' and self.row is not None:
            if any(self.row): self.w('\n| ' + ' | '.join(self.row) + ' |')
            self.row = None
        elif t == 'pre': self.pre = max(0, self.pre - 1); self.w('\n```\n')
        elif re.fullmatch(r'h[1-6]', t) or t in BLOCK: self.w('\n')
    def _emit(self, s):
        if self.cell is not None: self.cell.append(s)
        else: self.w(s)
    def handle_data(self, d):
        if self.skip: return
        if not self.pre: d = re.sub(r'\s+', ' ', d)
        self._emit(d)

def convert(src):
    p = P(); p.feed(src)
    txt = ''.join(p.out)
    txt = re.sub(r'[ \t]+\n', '\n', txt)
    txt = re.sub(r'\n[ \t]+', '\n', txt)
    txt = re.sub(r'\n{3,}', '\n\n', txt)
    return txt.strip() + '\n'

if __name__ == '__main__':
    s = open(sys.argv[1], encoding='utf-8').read()
    open(sys.argv[2], 'w', encoding='utf-8').write(convert(s))
