from PIL import Image
import html, os
R='/home/claude/904-request/'; SL='dongil-hibill'; D=R+'blog/'+SL+'/'+open(R+'blog/'+'dongil-hibill/version.json').read().split('"')[3]+'/'; os.makedirs(D,exist_ok=True)
W='work/'
# (파일, 자르기 박스 비율 l,t,r,b 또는 None, alt)
seq=[('p_wp3',None,'베이지 욕실 도막방수'),('p_wp1',None,'그레이 욕실 도막방수'),('p_wp2',None,'바닥·벽 하단 방수'),
('p_carry',None,'조적 블록 반입'),('p_laser2',None,'레이저 레벨기 설치'),('p_laser',None,'레이저 기준선'),('p_laser3',None,'첫 장 자리 잡기'),
('p_team',None,'90.4 시공팀 벽 타일 작업'),('p_epoxy',None,'에폭시 타일접착제 준비'),('p_clips',None,'600각 타일 벽 시공'),('p_g_wall2',None,'평탄클립으로 단차 잡기'),
('p_jojeok',None,'조적으로 젠다이 자리 쌓기'),('p_floor_team',None,'바닥 수평 잡기'),
('p_beige_first',None,'베이지 욕실 첫 줄'),('p_beige_wall2',None,'베이지 욕실 벽 시공'),('p_tub',None,'욕조 앞판·젠다이 조적'),('p_beige_wall',None,'베이지 욕실 벽 마무리'),
('p_g_part',None,'그레이 욕실 파티션'),('p_g_part2',None,'파티션 모서리 보양'),('p_b_part2',None,'욕조·파티션 시공'),('p_b_part',None,'베이지 욕실 바닥 시공'),
('a_g_wide',None,'그레이 욕실 완성'),('a_g_wide2',None,'그레이 욕실 완성'),('a_g_part',None,'파티션과 젠다이'),('a_g_jendai',None,'젠다이 디테일'),('a_g_floor',(0,0.25,1,0.78),'배수구 쪽 대각 재단'),
('a_b_wide',None,'베이지 욕실 완성'),('a_b_wide2',None,'베이지 욕실 파티션'),('a_b_tub',None,'샤워 공간'),('a_b_slot',(0,0,1,0.62),'일자 배수구 라인')]
for i,(f,box,alt) in enumerate(seq,1):
    im=Image.open(W+f+'.jpg')
    if box: w,h=im.size; im=im.crop((int(box[0]*w),int(box[1]*h),int(box[2]*w),int(box[3]*h)))
    im.thumbnail((1600,1600)); im.save(f'{D}{i:02d}.jpg',quality=88)
U=lambda n,a:f'<p style="text-align:center"><img src="https://904bath.github.io/904-request/blog/{SL}/11192155/{n:02d}.jpg" alt="{a}" style="max-width:100%"></p>'
P=lambda t:f'<p>{t}</p>'; H=lambda t:f'<h3><b>{t}</b></h3>'; E='<p><br></p>'
I=lambda *ns:''.join(U(n,seq[n-1][2]) for n in ns)
tags='#대구욕실리모델링 #대구욕실타일 #대구화장실리모델링 #동일하이빌 #동일하이빌욕실 #욕실리모델링 #화장실리모델링 #600각타일 #욕실타일 #욕실방수 #젠다이 #욕실파티션 #욕조 #대구타일시공 #구공사 #904BATH'
body=[P('안녕하세요, 대구 욕실리모델링 · 타일 시공팀 <b>구공사(90.4 BATH)</b>입니다.'),E,
P('오늘은 <b>대구 동일하이빌</b> 욕실 2칸 리모델링 현장이에요.'),
P('시공 기간은 <b>3일</b>, 두 욕실 모두 <b>600각 타일</b>로 벽과 바닥을 새로 마감했습니다.'),E,
P('✔ 이런 분들께 도움이 될 거예요'),
P('· 대구에서 욕실 리모델링 업체를 알아보고 계신 분'),
P('· 600각 같은 큰 타일로 넓어 보이는 욕실을 원하시는 분'),
P('· 욕조를 두면서 샤워 공간도 따로 나누고 싶으신 분'),E,
P('방수부터 완성까지 순서대로 보여드릴게요.'),E,
H('1. 방수 — 욕실 리모델링에서 제일 중요한 단계'),
P('파란색으로 보이는 부분이 방수층(도막방수)이에요.'),
P('바닥까지 철거한 욕실은 <b>액체방수 → 도막 1차 → 도막 2차</b> 순서로 방수를 다시 잡고, 물이 닿는 벽 아래쪽까지 올려 바릅니다.'),
P('타일을 붙이고 나면 다시는 볼 수 없는 곳이라 절대 건너뛰지 않아요.'),I(1,2,3),E,
H('2. 레이저로 기준선부터'),
P('젠다이(세면대·수전 쪽 선반)를 쌓을 블록부터 팀원들이 같이 올렸습니다.'),
P('타일을 붙이기 전에는 레이저 레벨기로 수평·수직 기준선을 먼저 잡아요. 줄눈 라인이 벽과 바닥에서 딱 맞아떨어지려면 이게 기본입니다.'),I(4,5,6,7,8),E,
H('3. 600각 타일 벽 시공'),
P('600각 타일은 크고 무게가 있어서 에폭시 타일접착제로 단단하게 붙였어요.'),
P('타일끼리 높이 차이(단차)가 생기지 않도록 이음새마다 평탄클립을 촘촘하게 끼웠습니다.'),I(9,10,11),E,
H('4. 젠다이 · 파티션 만들기'),
P('세면대와 수전이 들어갈 자리는 블록을 쌓아(조적) 젠다이를 만들고, 샤워 공간은 파티션으로 나눴어요.'),
P('수전 배관 위치에 맞춰 쌓고 그 위로 타일을 감쌌습니다.'),
I(12,13),P('바닥은 레벨기로 수평을 다시 잡은 뒤에 타일을 깔았어요.'),I(14),E,P('욕조가 들어가는 욕실은 욕조 앞판과 젠다이 자리까지 블록으로 쌓고 타일로 감쌌습니다.'),I(15,16,17),E,P('파티션은 모서리가 깨지기 쉬워서 테이프로 보양하고, 클립으로 높이를 맞춰 고정했어요.'),I(18,19,20,21),E,
H('5. 완성 — 그레이 톤 욕실'),
P('벽은 밝은 그레이, 젠다이와 파티션 아래쪽은 결이 진한 그레이 타일로 포인트를 줬습니다.'),
P('바닥은 배수구 쪽으로 물이 잘 빠지도록 기울기(구배)를 주고, 그에 맞춰 타일을 대각선으로 잘라 붙였어요.'),I(22,23,24,25,26),E,
H('6. 완성 — 욕조 있는 베이지 톤 욕실'),
P('욕조가 있는 욕실은 결이 살아 있는 베이지 600각 타일로 벽·바닥·욕조 앞판까지 한 톤으로 맞췄습니다.'),
P('샤워 공간은 일자 배수구로 라인을 깔끔하게 정리했어요.'),I(27,28,29,30),E,
H('자주 물어보시는 것'),
P('<b>Q. 욕실 2칸 리모델링, 기간은 얼마나 걸리나요?</b>'),
P('A. 현장마다 다르지만, 이번 동일하이빌 현장은 욕실 2칸을 3일 만에 마무리했어요.'),E,
P('<b>Q. 600각 타일, 좁은 욕실에도 괜찮나요?</b>'),
P('A. 줄눈이 적어서 오히려 넓어 보이고 청소도 편해요. 대신 타일이 크고 무거워서 접착제와 평탄 작업을 제대로 해야 단차 없이 나옵니다.'),E,
P('<b>Q. 방수는 꼭 다시 해야 하나요?</b>'),
P('A. 바닥까지 철거하면 방수층도 같이 없어지기 때문에 반드시 다시 합니다.'),E,
P('<b>Q. 견적은 어떻게 받나요?</b>'),
P('A. 욕실 사진 몇 장과 평수만 보내주시면 편하게 상담 도와드려요.'),E,
P('저희 팀은 90년대생 젊은 시공자들이 직접 현장에 들어갑니다.'),
P('철거부터 마감까지 한 팀이 끝까지 책임지고 있어요.'),E,
P('<b>상담은 편하게, 시공은 확실하게.</b>'),E,
P('<b>90.4 BATH INTERIOR DESIGN</b> · 대구 욕실리모델링 · 타일 시공'),P('문의 010-9459-9904'),
P('네이버 플레이스 <a href="https://map.naver.com/p/entry/place/2018592692">https://map.naver.com/p/entry/place/2018592692</a>'),E,P(tags)]
title='대구 동일하이빌 욕실리모델링 | 욕실 2칸 3일, 600각 타일 (욕조·젠다이·파티션)'
tpl=open(R+'blog/daon-cafe/index.html').read()
head=tpl[:tpl.index('<div class="paper">')].replace('구미 카페 현장','대구 동일하이빌').replace('안 붙으면 아래 본문을 마우스로 드래그해서 복사해 보세요.','안 붙으면 아래 본문을 마우스로 드래그해서 복사해 보세요. <b>④ 완성 사진 바로 위에 「블로그용 영상」을 동영상으로 올려주세요</b> (네이버 동영상 검색에도 같이 떠요).')
tail=tpl[tpl.index('<script>'):]
page=head+f'<div class="paper"><div class="ttl" id="title">{html.escape(title)}</div><div id="post">{"".join(body)}</div>\n<div id="tags" style="display:none">{html.escape(tags)}</div></div>\n'+tail
open(R+'blog/'+SL+'/index.html','w').write(page.replace('</head>','<script>(function(){var PV="'+'11192155'+'";fetch("version.json?"+Date.now(),{cache:"no-store"}).then(function(r){return r.json()}).then(function(j){if(j.v&&j.v!==PV){location.replace(location.pathname+"?v="+j.v+location.hash)}}).catch(function(){})})();</script></head>',1)); print('ok',len(page))
