import sys
from html.parser import HTMLParser
VOID={'br','img','input','meta','link','hr','wbr','source','col','area','base','embed','param','track','path','circle','rect'}
class V(HTMLParser):
    def __init__(s): super().__init__(); s.st=[]; s.err=[]; s.ids={}
    def handle_starttag(s,t,a):
        d=dict(a)
        if 'id' in d:
            if d['id'] in s.ids: s.err.append(f'dup id {d["id"]} @{s.getpos()}')
            s.ids[d['id']]=1
        if t not in VOID: s.st.append((t,s.getpos()))
    def handle_startendtag(s,t,a):
        d=dict(a)
        if 'id' in d: s.ids[d['id']]=1
    def handle_endtag(s,t):
        if t in VOID: return
        if not s.st: s.err.append(f'stray </{t}> @{s.getpos()}'); return
        if s.st[-1][0]==t: s.st.pop(); return
        # find
        for i in range(len(s.st)-1,-1,-1):
            if s.st[i][0]==t:
                s.err.append(f'unclosed {[x[0] for x in s.st[i+1:]]} before </{t}> @{s.getpos()}'); del s.st[i:]; return
        s.err.append(f'stray </{t}> @{s.getpos()}')
v=V(); v.feed(open(sys.argv[1],encoding='utf-8').read())
print('errors', len(v.err)); [print(' ',e) for e in v.err[:15]]
print('open at end', [x for x in v.st][:5])
