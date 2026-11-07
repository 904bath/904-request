from playwright.sync_api import sync_playwright
CSS="""body{margin:0}*{font-family:'Noto Sans CJK KR',sans-serif;box-sizing:border-box}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:#111;color:#fff}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.chip{position:absolute;left:60px;top:60px;background:#111;color:#fff;padding:18px 28px;font-weight:900;font-size:44px;line-height:1.25}
.num{position:absolute;right:60px;top:72px;background:#fff;color:#111;font-weight:900;font-size:26px;padding:8px 16px}
.band{position:absolute;left:0;right:0;bottom:0;background:#111;padding:44px 60px 52px;display:flex;align-items:flex-end;justify-content:space-between;gap:30px}
.band p{margin:0;font-size:34px;font-weight:500;line-height:1.5;color:#eee}
.band b{color:#fff;font-weight:900}
.mark{flex:none;font-size:24px;font-weight:900;letter-spacing:3px;color:#888}
.half{position:absolute;left:0;width:1080px;height:675px;overflow:hidden}
.half img{width:100%;height:100%;object-fit:cover}
.tag{position:absolute;left:40px;top:40px;background:#fff;color:#111;font-weight:900;font-size:32px;padding:10px 20px}
.tag.d{background:#111;color:#fff}"""
def photo(n,i,chip,text,pos='center'):
    return f'''<div class="s"><img class="bg" src="src/{n}.jpg" style="object-position:{pos}"><div class="chip">{chip}</div><div class="num">{i:02d}/10</div>
<div class="band"><p>{text}</p><span class="mark">90.4 BATH</span></div></div>'''
def ba(a,b,i,title,pa='center',pb='center'):
    return f'''<div class="s"><div class="half" style="top:0"><img src="src/{a}.jpg" style="object-position:{pa}"><div class="tag d">BEFORE</div></div>
<div class="half" style="top:675px"><img src="src/{b}.jpg" style="object-position:{pb}"><div class="tag">AFTER</div></div>
<div class="num">{i:02d}/10</div><div class="chip" style="top:auto;bottom:625px;left:auto;right:60px;font-size:40px">{title}</div></div>'''
slides=[
f'''<div class="s"><img class="bg" src="src/20261020_095011.jpg" style="filter:brightness(.55)"><div style="position:absolute;left:70px;top:110px">
<div style="font-size:36px;font-weight:500;letter-spacing:4px;color:#eee">DAEGU · 30평대</div>
<div style="font-size:96px;font-weight:900;line-height:1.15;margin-top:24px">욕실 2곳<br>주방·베란다·현관<br>타일 시공기</div>
<div style="font-size:38px;font-weight:500;margin-top:36px;color:#eee">철거 → 방수 → 대형타일 → 완성</div></div>
<div style="position:absolute;left:50px;bottom:60px"><div style="position:relative;width:380px;height:214px"><svg width="380" height="214" style="position:absolute;inset:0" aria-hidden="true"><defs><pattern id="tp380" width="90" height="90" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0H90" stroke="#fff" stroke-width="2"/><path d="M0 0V90" stroke="#fff" stroke-width="2" stroke-dasharray="6 6"/></pattern></defs><rect width="380" height="214" fill="url(#tp380)" opacity=".35"/></svg><img src="src/logo_line.png" style="position:absolute;left:53px;top:13px;width:274px;"></div></div><div style="position:absolute;right:70px;bottom:100px;font-size:34px;font-weight:900">넘겨서 보기 →</div></div>''',
photo('20261013_091638',2,'철거 후 베란다','기존 마감을 모두 걷어낸 상태에서<br><b>바탕부터 다시</b> 시작합니다.'),
photo('20261014_104659',3,'방수가 제일 중요','<b>액방 → 도막 1차 → 도막 2차</b><br>타일 붙이면 다시 못 보는 곳, 절대 안 건너뜁니다.'),
photo('20261014_104142',4,'레이저 기준선','붙이기 전에 수평·수직부터.<br><b>줄눈 라인이 딱 맞는 이유</b>입니다.'),
photo('20261016_180426',5,'대형 타일 + 평탄클립','큰 타일일수록 단차가 생기기 쉬워서<br><b>평탄클립</b>으로 이음새를 잡습니다.'),
photo('20261016_160820',6,'90년대생 시공팀','주방 벽까지 같은 대형 타일로.<br><b>젊은 감각, 꼼꼼한 마감.</b>','center 70%'),
photo('20261020_095011',7,'욕실 완성','벽·바닥 같은 톤으로 맞춰<br><b>넓어 보이는 욕실</b>로 마무리.'),
ba('20261013_091638','20261020_094853',8,'베란다'),
ba('20261014_104147','20261020_094941',9,'현관','center 70%','center 60%'),
f'''<div class="s" style="display:flex;flex-direction:column;justify-content:center;padding:0 90px;gap:40px">
<div style="position:relative;width:900px;height:506px"><svg width="900" height="506" style="position:absolute;inset:0" aria-hidden="true"><defs><pattern id="tp900" width="213" height="213" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0H213" stroke="#fff" stroke-width="3"/><path d="M0 0V213" stroke="#fff" stroke-width="3" stroke-dasharray="9 9"/></pattern></defs><rect width="900" height="506" fill="url(#tp900)" opacity=".35"/></svg><img src="src/logo_line.png" style="position:absolute;left:126px;top:30px;width:648px;"></div>
<div style="height:4px;background:#fff;width:100%"></div>
<div style="font-size:84px;font-weight:900;line-height:1.2">현장 사진만<br>보내주세요</div>
<div style="font-size:38px;font-weight:500;line-height:1.6;color:#ddd">욕실 리모델링 · 대형타일 · 방수<br>베란다 · 현관 · 주방 타일</div>
<div style="background:#fff;color:#111;padding:30px 36px;font-size:44px;font-weight:900">DM · 010-9459-9904</div>
<div style="font-size:32px;font-weight:500;color:#bbb">대구 · 구공사(90.4 BATH)</div></div>''',
]
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,s in enumerate(slides,1):
        open('/home/claude/insta/t.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{s}</body></html>')
        pg.goto('file:///home/claude/insta/t.html'); pg.wait_for_timeout(250)
        pg.screenshot(path=f'/home/claude/insta/out/{i:02d}.jpg',type='jpeg',quality=92)
    b.close()
