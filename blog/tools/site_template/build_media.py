import sys, os, shutil, zipfile
sys.path.insert(0,'/home/claude/904-request/blog/tools')
from playwright.sync_api import sync_playwright
import insta_minimal as IM
R='/home/claude/904-request/'; M=R+'media/dongil-hibill/11192155/'; os.makedirs(M,exist_ok=True)
W='file:///home/claude/dong/work/'
LOGO='file://'+R+'blog/assets/logo-line-white.png'
def cover_html(src,pos,name):
    return f'''<html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body><div style="width:1080px;height:1080px;position:relative;overflow:hidden">
<img src="{src}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos}">
<div style="position:absolute;left:0;right:0;bottom:0;height:230px;background:linear-gradient(transparent,rgba(0,0,0,.6))"></div>
<div style="position:absolute;left:56px;bottom:52px;color:#fff"><div style="font-family:Lora,serif;font-size:28px;letter-spacing:1px">after ..</div><div style="font-family:'Noto Sans CJK KR';font-weight:700;font-size:44px;margin-top:4px">{name}</div></div>
<img src="{LOGO}" style="position:absolute;right:48px;bottom:46px;width:130px"></div></body></html>'''
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1080})
    for k,src,pos,name in [('A',W+'a_g_wide.jpg','center 62%','대구 동일하이빌 욕실'),('B',W+'a_b_wide.jpg','center 66%','대구 동일하이빌 욕실')]:
        open('/tmp/c.html','w').write(cover_html(src,pos,name)); pg.goto('file:///tmp/c.html'); pg.wait_for_timeout(300)
        pg.screenshot(path=f'{M}blog_cover_{k}.jpg',type='jpeg',quality=92)
    b.close()
N=15
L=[('p_wp3','before ..','도막방수부터 꼼꼼하게'),('p_laser2','process ..','레이저로 기준선 잡기'),('p_team','process ..','90년대생 시공팀','center 40%'),
('p_beige_first','process ..','첫 줄이 제일 중요해요'),('p_g_wall2','process ..','평탄클립으로 단차 0'),('p_jojeok','process ..','조적으로 젠다이 자리'),
('p_floor_team','process ..','바닥 수평 다시 잡기','center 45%'),('p_tub','process ..','욕조 앞판까지 한 톤'),('a_g_wide','after ..','그레이 톤 욕실','center 60%'),
('a_g_part','after ..','젠다이 · 파티션','center 60%'),('a_g_jendai','after ..','결 맞춘 젠다이'),('a_b_wide','after ..','베이지 톤 욕실 · 욕조','center 62%'),
('a_b_wide2','after ..','파티션으로 나눈 샤워 공간','center 60%')]
sl=[IM.cover(W+'a_g_wide2.jpg','대구 동일하이빌','욕실 2칸 · 3일 · 600각 타일','center 60%')]
for i,t in enumerate(L,2): sl.append(IM.photo(W+t[0]+'.jpg',i,N,t[1],t[2],*(t[3:] or ['center'])))
sl.append('END')
tmp='/home/claude/dong/insta'; shutil.rmtree(tmp,ignore_errors=True)
IM.render(sl,tmp,R+'blog/assets/endcard_insta_light.jpg')
for f in sorted(os.listdir(tmp)): shutil.copy(f'{tmp}/{f}',f'{M}insta_{f}')
with zipfile.ZipFile(M+'insta_all.zip','w') as z:
    for f in sorted(os.listdir(tmp)): z.write(f'{tmp}/{f}',f'904_dongil-hibill_{f}')
# 미리보기 시트
from PIL import Image
ims=[Image.open(f'{tmp}/{f}') for f in sorted(os.listdir(tmp))]
s=Image.new('RGB',(5*360,3*450),'white')
for i,im in enumerate(ims): s.paste(im.resize((360,450)),((i%5)*360,(i//5)*450))
s.save('/home/claude/dong/sheet.jpg',quality=85); print('done')
