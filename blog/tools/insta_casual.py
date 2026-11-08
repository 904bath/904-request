from playwright.sync_api import sync_playwright
import shutil
OUT='/home/claude/chim/out_c'; SRC='src'
CSS="""body{margin:0}*{font-family:'Noto Sans CJK KR',sans-serif;box-sizing:border-box}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:#111}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.cap{position:absolute;left:50px;right:50px;bottom:110px;text-align:center;color:#fff;font-weight:900}
.main{font-size:78px;line-height:1.18;-webkit-text-stroke:13px #111;paint-order:stroke fill}
.sub{display:inline-block;margin-top:24px;background:#ffe14d;color:#111;font-size:42px;padding:10px 24px;transform:rotate(-2deg)}
.pg{position:absolute;left:50px;top:50px;background:#ffe14d;color:#111;font-weight:900;font-size:30px;padding:6px 16px;border-radius:30px}
.mark{position:absolute;right:50px;top:56px;color:#fff;font-weight:900;font-size:28px;letter-spacing:4px;-webkit-text-stroke:6px #111;paint-order:stroke fill}
.half{position:absolute;left:0;width:1080px;height:675px;overflow:hidden}.half img{width:100%;height:100%;object-fit:cover}
.tag{position:absolute;left:40px;top:40px;font-weight:900;font-size:40px;padding:8px 22px;transform:rotate(-3deg)}"""
def photo(n,i,N,main,sub,pos='center'):
    return f'<div class="s"><img class="bg" src="/home/claude/chim/src/{n}.jpg" style="object-position:{pos}"><div class="pg">{i}/{N}</div><div class="mark">90.4 BATH</div><div class="cap"><div class="main">{main}</div><div class="sub">{sub}</div></div></div>'
def ba(a,b,i,N,label,pa='center',pb='center'):
    return f'''<div class="s"><div class="half" style="top:0"><img src="/home/claude/chim/src/{a}.jpg" style="object-position:{pa}"><div class="tag" style="background:#111;color:#fff;border:4px solid #fff">BEFORE</div></div>
<div class="half" style="top:675px"><img src="/home/claude/chim/src/{b}.jpg" style="object-position:{pb}"><div class="tag" style="background:#ffe14d;color:#111">AFTER</div></div>
<div class="pg" style="left:auto;right:50px">{i}/{N}</div>
<div style="position:absolute;left:0;right:0;top:620px;text-align:center"><span style="display:inline-block;background:#fff;color:#111;font-weight:900;font-size:50px;padding:10px 30px;border:5px solid #111;transform:rotate(2deg)">{label}</span></div></div>'''
def render(slides,endcard):
    import os; os.makedirs(OUT,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(slides,1):
            if s=='END': shutil.copy(endcard,f'{OUT}/{i:02d}.jpg'); continue
            open('/tmp/c.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{s}</body></html>')
            pg.goto('file:///tmp/c.html'.replace('/tmp/c.html','/tmp/c.html')); pg.wait_for_timeout(200)
            pg.screenshot(path=f'{OUT}/{i:02d}.jpg',type='jpeg',quality=92)
        b.close()
