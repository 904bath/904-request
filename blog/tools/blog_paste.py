from PIL import Image, ImageOps
import base64, io, html
def img(n, alt):
    im=ImageOps.exif_transpose(Image.open(f'photos/{n}.jpg')).convert('RGB'); im.thumbnail((1000,1000))
    b=io.BytesIO(); im.save(b,'JPEG',quality=80)
    return f'<p style="text-align:center"><img src="data:image/jpeg;base64,{base64.b64encode(b.getvalue()).decode()}" alt="{alt}" style="max-width:100%;height:auto"></p>'
P=lambda t:f'<p>{t}</p>'
H=lambda t:f'<h3><b>{t}</b></h3>'
E='<p><br></p>'
body=[
P('안녕하세요, 욕실·타일 시공 전문 <b>구공사(90.4 BATH)</b>입니다.'),E,
P('오늘은 대구 30평대 현장 시공기를 들고 왔어요.'),
P('이번 현장은 욕실 두 곳과 주방 벽, 베란다·현관 바닥까지 한 번에 새로 바꾼 현장입니다.'),E,
P('밝은 톤의 대형 타일로 통일해서 좁은 공간도 훨씬 넓고 깔끔해 보이게 잡았는데요.'),
P('철거 후 상태부터 방수, 시공 과정, 완성 모습까지 순서대로 보여드릴게요.'),E,
H('1. 철거 후 현장 상태'),
P('기존 마감을 모두 철거한 상태에서 시작했습니다.'),
P('베란다는 예전 바닥을 걷어내고 바탕면이 드러난 상태였고, 현관도 바닥을 전부 덜어낸 모습이에요.'),
img('20261013_091638','베란다 철거 후'), img('20261014_104147','현관 철거 후'),E,
H('2. 방수 — 보이지 않는 곳이 제일 중요합니다'),
P('욕실은 바닥까지 철거한 현장이라 방수를 처음부터 다시 잡았습니다.'),
P('저희는 <b>액체방수 → 도막 1차 → 도막 2차</b> 순서로 진행하고, 한 단계씩 충분히 굳힌 뒤에 다음으로 넘어갑니다.'),E,
P('파란색으로 보이는 부분이 도막방수층이에요.'),
P('바닥은 물론이고 물이 튀는 벽 하단까지 올려서 꼼꼼하게 덮었습니다.'),
P('타일을 붙이고 나면 다시는 볼 수 없는 곳이라, 이 단계는 절대 건너뛰지 않습니다.'),
img('20261014_104659','욕실 도막방수 완료'), img('20261014_104634','방수층'),E,
H('3. 레이저로 기준선 잡기'),
P('타일을 붙이기 전에 레이저 레벨기로 수평·수직 기준선을 먼저 잡습니다.'),
P('줄눈 라인이 벽과 바닥에서 딱 맞아떨어지려면 이 작업이 기본이에요.'),
P('수전 위치와 타일 분할도 이때 미리 맞춰 둡니다.'),
img('20261014_104142','레이저 기준선 작업'), img('20261014_104233','첫 장 자리 잡기'),E,
H('4. 대형 타일 시공'),
P('이번 현장은 벽·바닥 모두 밝은 톤의 대형 타일을 썼습니다.'),
P('대형 타일은 줄눈이 적어 공간이 넓어 보이고 청소도 편한 대신, 타일끼리 단차가 생기기 쉽습니다.'),E,
P('그래서 파란 <b>평탄클립(레벨링 클립)</b>을 촘촘하게 끼워서 이음새 단차를 잡았어요.'),
P('욕실 바닥은 배수구 쪽으로 물이 잘 빠지도록 구배를 주고, 그에 맞춰 타일을 대각으로 재단했습니다.'),
P('모서리는 테이프로 보양해서 깨짐 없이 마무리했어요.'),E,
P('주방 벽도 같은 방식으로 레이저 기준선을 잡고 대형 타일을 시공했습니다.'),
img('20261016_160820','주방 벽 타일 시공'), img('20261016_180426','욕실 벽 시공'), img('20261016_180508','욕조 쪽 벽·바닥 시공'),E,
H('5. 베란다·현관'),
P('베란다 바닥도 같은 방식으로 평탄클립을 쓰면서 깔았습니다.'),
P('현관도 같은 톤의 대형 타일로 단차 부분까지 깔끔하게 맞춰 마무리했어요.'),
img('20261016_180556','베란다 바닥 시공 중'),E,
H('6. 줄눈과 마감'),
P('타일이 자리 잡은 뒤 클립을 제거하고 줄눈과 마감 작업을 했습니다.'),
P('저희 팀은 90년대생 젊은 시공자들이 직접 현장에 들어갑니다.'),
P('요즘 스타일을 잘 알고, 그만큼 마감 디테일에 예민합니다.'),
img('20261020_085737','마감 작업'), img('20261020_094602','샤워실 마감 작업'),E,
H('7. 완성'),
P('<b>욕실</b> — 벽과 바닥을 같은 톤으로 맞춰 통일감 있게 마무리했습니다. 벽면 선반(젠다이)까지 줄눈 라인을 맞춰서 깔끔하게 이어집니다.'),
img('20261020_095011','욕실 완성'),E,
P('<b>베란다</b> — 어둡고 거칠었던 바닥이 환하게 바뀌었습니다.'),
img('20261020_094831','베란다 완성'), img('20261020_094853','베란다 완성'),E,
P('<b>현관</b> — 바닥 전체를 밝은 톤의 대형 타일로 새로 깔았습니다.'),
img('20261020_094941','현관 완성'),E,
P('철거부터 방수, 타일, 마감까지 저희 팀이 현장을 끝까지 책임집니다.'),
P('욕실 리모델링이나 베란다·현관·주방 타일 고민 중이시라면, 현장 사진 몇 장만 보내주세요. 편하게 상담 도와드릴게요.'),E,
P('<b>90.4 BATH INTERIOR DESIGN</b>'),
P('문의 010-9459-9904'),
P('네이버 플레이스 <a href="https://map.naver.com/p/entry/place/2018592692">https://map.naver.com/p/entry/place/2018592692</a>'),E,
P('#대구욕실리모델링 #대구타일시공 #대구주방타일 #욕실리모델링 #화장실리모델링 #욕실타일 #대형타일 #타일시공 #욕실방수 #도막방수 #베란다타일 #현관타일 #욕실인테리어 #구공사 #904BATH'),
]
title='대구 30평대 욕실 2곳 + 주방 + 베란다 + 현관 타일 시공기 | 방수부터 대형타일 마감까지'
tags='#대구욕실리모델링 #대구타일시공 #대구주방타일 #욕실리모델링 #화장실리모델링 #욕실타일 #대형타일 #타일시공 #욕실방수 #도막방수 #베란다타일 #현관타일 #욕실인테리어 #구공사 #904BATH'
page=f'''<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>블로그 붙여넣기용 — 대구 30평대 시공기</title>
<style>
body{{margin:0;background:#f2f2f0;font-family:-apple-system,"Apple SD Gothic Neo","Malgun Gothic",sans-serif;color:#222}}
.bar{{position:sticky;top:0;z-index:5;background:#111;color:#fff;padding:14px 16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center}}
.bar b{{margin-right:auto;font-size:15px}}
button{{border:0;border-radius:8px;padding:10px 14px;font-size:14px;font-weight:700;cursor:pointer;background:#fff;color:#111}}
button.main{{background:#03c75a;color:#fff}}
.msg{{width:100%;font-size:13px;color:#9fe3b9;min-height:1em}}
.how{{max-width:760px;margin:16px auto 0;padding:0 16px;font-size:14px;line-height:1.6;color:#555}}
.paper{{max-width:760px;margin:12px auto 40px;background:#fff;padding:32px 28px;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.08)}}
.ttl{{font-size:20px;font-weight:700;margin:0 0 20px;padding-bottom:14px;border-bottom:1px solid #eee}}
#post{{font-size:16px;line-height:1.8}} #post h3{{font-size:18px;margin:28px 0 8px}} #post p{{margin:0}}
</style></head><body>
<div class="bar"><b>네이버 블로그 붙여넣기용</b>
<button onclick="cp('title')">① 제목 복사</button><button class="main" onclick="cp('post')">② 본문 전체 복사 (사진 포함)</button><button onclick="cp('tags')">③ 태그 복사</button>
<div class="msg" id="msg"></div></div>
<div class="how">네이버 블로그 글쓰기 → 제목 칸에 ① 붙여넣기 → 본문 칸에 ② 붙여넣기 → 태그 칸에 ③ 붙여넣기. 사진이 안 붙으면 아래 본문을 마우스로 드래그해서 복사해 보세요.</div>
<div class="paper"><div class="ttl" id="title">{html.escape(title)}</div><div id="post">{"".join(body)}</div>
<div id="tags" style="display:none">{html.escape(tags)}</div></div>
<script>
async function cp(id){{
  const el=document.getElementById(id), m=document.getElementById('msg');
  const plain = id==='post'? el.innerText : el.textContent;
  let ok=false;
  try{{
    if(id==='post' && window.ClipboardItem){{
      await navigator.clipboard.write([new ClipboardItem({{'text/html':new Blob([el.innerHTML],{{type:'text/html'}}),'text/plain':new Blob([plain],{{type:'text/plain'}})}})]); ok=true;
    }} else {{ await navigator.clipboard.writeText(plain); ok=true; }}
  }}catch(e){{}}
  if(!ok){{
    try{{ const hidden=el.style.display==='none'; if(hidden) el.style.display='block';
      const r=document.createRange(); r.selectNodeContents(el); const s=getSelection(); s.removeAllRanges(); s.addRange(r);
      ok=document.execCommand('copy'); s.removeAllRanges(); if(hidden) el.style.display='none'; }}catch(e){{}}
  }}
  m.textContent = ok ? ({{title:'제목',post:'본문(사진 포함)',tags:'태그'}}[id]+' 복사됨 — 네이버 블로그에 붙여넣기 하세요') : '복사가 막혔어요. 아래 내용을 드래그해서 Ctrl+C 해주세요.';
}}
</script></body></html>'''
open('blog_paste.html','w').write(page)
import os; print(os.path.getsize('blog_paste.html')/1e6)
