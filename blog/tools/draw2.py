from playwright.sync_api import sync_playwright
from PIL import Image, ImageOps
exec(open('scenes2.py').read())
CSS="body{margin:0;background:transparent}*{font-family:'Noto Sans CJK KR',sans-serif;box-sizing:border-box}"
def ov(k,b,s):
    return f'''<div style="width:1080px;height:1920px;position:relative">
<div style="position:absolute;left:0;right:0;bottom:0;height:820px;background:linear-gradient(transparent,rgba(0,0,0,.88) 50%)"></div>
<div style="position:absolute;left:80px;right:80px;bottom:300px;color:#fff">
<div style="display:inline-block;background:#fff;color:#111;font-weight:900;font-size:40px;padding:8px 20px;letter-spacing:2px">{k}</div>
<div style="font-size:110px;font-weight:900;line-height:1.12;margin-top:26px">{b}</div>
<div style="font-size:48px;font-weight:500;margin-top:22px;color:#eee">{s}</div></div>
<div style="position:absolute;right:80px;top:140px;color:#fff;font-weight:900;font-size:34px;letter-spacing:4px;opacity:.85">90.4 BATH</div></div>'''
END=f'''<div style="width:1080px;height:1920px;background:#111;color:#fff;display:flex;flex-direction:column;justify-content:center;padding:0 90px;gap:50px">
<img src="logo_line.png" style="width:800px">
<div style="height:5px;background:#fff"></div>
<div style="font-size:110px;font-weight:900;line-height:1.15">욕실,<br>이제 젊은 손으로</div>
<div style="font-size:48px;font-weight:500;color:#ddd;line-height:1.5">욕실 · 베란다 · 현관 · 주방 타일</div>
<div style="background:#fff;color:#111;font-size:60px;font-weight:900;padding:34px 40px">DM · 010-9459-9904</div></div>'''
with sync_playwright() as p:
    br=p.chromium.launch(); pg=br.new_page(viewport={'width':1080,'height':1920})
    for i,(ph,d,k,b,s,pos) in enumerate(S):
        html=END if ph is None else ov(k,b,s)
        open('t.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{html}</body></html>')
        pg.goto('file:///home/claude/reel/t.html'); pg.wait_for_timeout(200)
        pg.screenshot(path=f'ov2/{i:02d}.png',omit_background=True)
        if ph:
            im=ImageOps.exif_transpose(Image.open(f'{ph}.jpg')).convert('RGB')
            # cover-crop to 1080x1920 at 1.12x for zoom room
            W,H=int(1080*1.12),int(1920*1.12)
            r=max(W/im.width,H/im.height); im=im.resize((int(im.width*r)+1,int(im.height*r)+1))
            fy=pos
            x=(im.width-W)//2; y=int((im.height-H)*fy); im.crop((x,y,x+W,y+H)).save(f'bg2/{i:02d}.jpg',quality=92)
    br.close()
