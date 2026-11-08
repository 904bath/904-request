from playwright.sync_api import sync_playwright
import shutil, os
CSS="""body{margin:0}*{box-sizing:border-box}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:#dcd6cd}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:saturate(.85)}
.shade{position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(transparent,rgba(20,18,16,.55))}
.lab{position:absolute;left:70px;bottom:90px;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.35)}
.en{font-family:Lora,serif;font-size:84px;letter-spacing:1px}
.ko{font-family:'Noto Sans CJK KR';font-weight:500;font-size:36px;letter-spacing:2px;margin-top:10px}
.pg{position:absolute;right:60px;top:56px;font-family:Lora,serif;font-size:30px;color:#fff;letter-spacing:3px;text-shadow:0 1px 8px rgba(0,0,0,.4)}
.half{position:absolute;left:0;width:1080px;height:670px;overflow:hidden}.half img{width:100%;height:100%;object-fit:cover;filter:saturate(.85)}
.hl{position:absolute;left:50px;bottom:34px;font-family:Lora,serif;font-size:60px;color:#fff;text-shadow:0 2px 12px rgba(0,0,0,.45)}"""
def photo(src,i,N,en,ko,pos='center'):
    return f'<div class="s"><img class="bg" src="{src}" style="object-position:{pos}"><div class="shade"></div><div class="pg">{i:02d} / {N}</div><div class="lab"><div class="en">{en}</div><div class="ko">{ko}</div></div></div>'
def cover(src,en,ko,pos='center'):
    return f'''<div class="s"><img class="bg" src="{src}" style="object-position:{pos};filter:saturate(.85) brightness(.82)"><div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#fff;text-shadow:0 2px 18px rgba(0,0,0,.4)">
<div style="font-family:Lora,serif;font-size:96px;line-height:1.1">{en}</div><div style="font-family:'Noto Sans CJK KR';font-weight:500;font-size:40px;letter-spacing:3px;margin-top:26px">{ko}</div>
<div style="font-family:Lora,serif;font-size:32px;letter-spacing:6px;margin-top:70px;opacity:.9">swipe →</div></div></div>'''
def ba(a,b,i,N,ko,pa='center',pb='center'):
    return f'''<div class="s"><div class="half" style="top:0"><img src="{a}" style="object-position:{pa}"><div class="hl">before</div></div>
<div class="half" style="top:680px"><img src="{b}" style="object-position:{pb}"><div class="hl">after</div></div>
<div class="pg">{i:02d} / {N}</div>
<div style="position:absolute;right:50px;top:618px;font-family:'Noto Sans CJK KR';font-weight:500;font-size:34px;color:#2b2824;background:#dcd6cd;padding:10px 24px;letter-spacing:2px">{ko}</div></div>'''
def render(slides,out,endcard):
    os.makedirs(out,exist_ok=True)
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
        for i,s in enumerate(slides,1):
            if s=='END': shutil.copy(endcard,f'{out}/{i:02d}.jpg'); continue
            open('/tmp/im.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{s}</body></html>')
            pg.goto('file:///tmp/im.html'); pg.wait_for_timeout(200); pg.screenshot(path=f'{out}/{i:02d}.jpg',type='jpeg',quality=92)
        b.close()
