# 904 첫 화면(커버) 통일 규칙 (2026-11-21 토론 확정)
# - 사진 전체 + 똑같은 어둡기(검정 30%), 글씨 테두리·말풍선 없음
# - 가운데 정렬, 그리드(3:4)에서 잘리지 않는 화면 정중앙
# - 1줄: 현장명 (Noto Sans CJK Bold 100px, 흰색, 한 줄)
# - 2줄: 시공 내용/숫자 훅 (Medium 42px, "A · B · C")
# - 3줄: 작은 영문 세리프 "90.4 bath" (Lora 28px)
from playwright.sync_api import sync_playwright
def block(name,sub,scale=1.0):
    s=lambda v:int(v*scale)
    return (f'<div style="font-family:\'Noto Sans CJK KR\';font-weight:700;font-size:{s(100)}px;line-height:1.15;letter-spacing:-1px">{name}</div>'
            f'<div style="font-family:\'Noto Sans CJK KR\';font-weight:500;font-size:{s(42)}px;margin-top:{s(22)}px;letter-spacing:1px">{sub}</div>'
            f'<div style="font-family:Lora,serif;font-size:{s(28)}px;letter-spacing:6px;margin-top:{s(48)}px;opacity:.85">90.4 bath</div>')
def html(src,name,sub,w,h,pos='center'):
    return f'''<html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body><div style="width:{w}px;height:{h}px;position:relative;overflow:hidden">
<img src="file://{src}" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:{pos};filter:saturate(.85)">
<div style="position:absolute;inset:0;background:rgba(0,0,0,.30)"></div>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#fff;text-shadow:0 2px 16px rgba(0,0,0,.35)">{block(name,sub)}</div></div></body></html>'''
def render(items,size=(1080,1920)):
    with sync_playwright() as p:
        b=p.chromium.launch(); pg=b.new_page(viewport={'width':size[0],'height':size[1]})
        for src,name,sub,out,pos in items:
            open('/tmp/cu.html','w').write(html(src,name,sub,size[0],size[1],pos)); pg.goto('file:///tmp/cu.html'); pg.wait_for_timeout(250)
            pg.screenshot(path=out,type='jpeg',quality=92)
        b.close()
