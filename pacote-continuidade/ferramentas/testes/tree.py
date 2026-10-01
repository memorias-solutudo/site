import sys,re
from html.parser import HTMLParser
VOID={'br','img','input','meta','link','hr','wbr','source','col'}
class P(HTMLParser):
    def __init__(s,maxd):
        super().__init__(); s.d=0; s.out=[]; s.maxd=maxd; s.last=None; s.rep=0
    def handle_starttag(s,t,a):
        a=dict(a)
        if s.d<=s.maxd:
            key=' '*s.d*2+t+('.'+a['class'].replace(' ','.') if a.get('class') else '')+('#'+a['id'] if a.get('id') else '')
            extra=''
            for k in ('data-tip','onclick','data-k','href','data-tab'):
                if k in a: extra+=f' {k}="{(a[k] or "")[:40]}"'
            line=key+extra
            if line==s.last: s.rep+=1
            else:
                if s.rep: s.out.append(' '*s.d*2+f'  (x{s.rep+1})')
                s.rep=0; s.out.append(line); s.last=line
        if t not in VOID: s.d+=1
    def handle_endtag(s,t):
        if t not in VOID: s.d-=1
    def handle_data(s,d):
        d=d.strip()
        if d and s.d<=s.maxd+1:
            s.out.append(' '*s.d*2+'"'+d[:70]+'"'); s.last=None
h=open(sys.argv[1],encoding='utf-8').read()
a=h.find(sys.argv[2]); b=h.find(sys.argv[3],a+1) if len(sys.argv)>3 and sys.argv[3] else len(h)
p=P(int(sys.argv[4]) if len(sys.argv)>4 else 8); p.feed(h[a:b]); print('\n'.join(p.out))
