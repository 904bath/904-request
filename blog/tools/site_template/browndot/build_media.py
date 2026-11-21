import sys, os, shutil, zipfile
sys.path.insert(0,'/home/claude/904-request/blog/tools')
from playwright.sync_api import sync_playwright
import insta_minimal as IM
R='/home/claude/904-request/'; SL='browndot-jukdo'; V='11211300'; M=R+f'media/{SL}/{V}/'; os.makedirs(M,exist_ok=True)
W='file:///home/claude/brown/work/'
LOGO='file://'+R+'blog/assets/logo-line-white.png'
def cover_html(src,pos,name):
    return f'''<html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body><div style="width:1080px;height:1080px;position:relative;overflow:hidden">
<img src="{src}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos}">
<div style="position:absolute;left:0;right:0;bottom:0;height:230px;background:linear-gradient(transparent,rgba(0,0,0,.6))"></div>
<div style="position:absolute;left:56px;bottom:52px;color:#fff"><div style="font-family:Lora,serif;font-size:28px;letter-spacing:1px">after ..</div><div style="font-family:'Noto Sans CJK KR';font-weight:700;font-size:44px;margin-top:4px">{name}</div></div>
<img src="{LOGO}" style="position:absolute;right:48px;bottom:46px;width:130px"></div></body></html>'''
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1080})
    for k,src,pos in [('A',W+'a_lobby.jpg','center 55%'),('B',W+'a_cafe2.jpg','center 60%')]:
        open('/tmp/c.html','w').write(cover_html(src,pos,'브라운도트 죽도점 바닥')); pg.goto('file:///tmp/c.html'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'{M}blog_cover_{k}.jpg',type='jpeg',quality=92)
    b.close()
N=15
sl=[IM.cover(W+'a_lobby.jpg','브라운도트 죽도점','영업 중 · 600각 바닥 시공','center 55%'),
IM.ba(W+'b_lobby.jpg',W+'a_lobby.jpg',2,N,'로비','center 55%','center 50%'),
IM.ba(W+'b_front.jpg',W+'a_front.jpg',3,N,'프런트','center 45%','center 45%'),
IM.ba(W+'b_cafe2.jpg',W+'a_cafe4.jpg',4,N,'조식 공간','center 50%','center 55%')]
L=[('p_entry','process ..','입구부터 한 줄씩'),('p_trowel','process ..','철거 없이 기존 바닥 위로','center 70%'),('p_lobby_clips','process ..','평탄클립으로 단차 잡기'),
('p_team','process ..','집기는 직접 옮겨가며','center 55%'),('p_hall','process ..','손님 동선은 비워두고'),('p_night','process ..','저녁까지 로비 완료','center 60%'),
('a_kiosk','after ..','로비에서 조식 공간까지','center 55%'),('a_cafe','after ..','조식 공간','center 60%'),('a_cafe5','after ..','테이블도 제자리로','center 60%'),('a_ev2','after ..','엘리베이터 바닥까지','center 65%')]
for i,t in enumerate(L,5): sl.append(IM.photo(W+t[0]+'.jpg',i,N,t[1],t[2],*(t[3:] or ['center'])))
sl.append('END')
tmp='/home/claude/brown/insta'; shutil.rmtree(tmp,ignore_errors=True)
IM.render(sl,tmp,R+'blog/assets/endcard_insta_light.jpg')
for f in sorted(os.listdir(tmp)): shutil.copy(f'{tmp}/{f}',f'{M}insta_{f}')
with zipfile.ZipFile(M+'insta_all.zip','w') as z:
    for f in sorted(os.listdir(tmp)): z.write(f'{tmp}/{f}',f'904_{SL}_{f}')
from PIL import Image
ims=[Image.open(f'{tmp}/{f}') for f in sorted(os.listdir(tmp))]
s=Image.new('RGB',(5*360,3*450),'white')
for i,im in enumerate(ims): s.paste(im.resize((360,450)),((i%5)*360,(i//5)*450))
s.save('/home/claude/brown/sheet.jpg',quality=85)
for k in 'AB': Image.open(f'{M}blog_cover_{k}.jpg').resize((540,540)).save(f'/home/claude/brown/cover_{k}.jpg')
print('done',len(ims))
