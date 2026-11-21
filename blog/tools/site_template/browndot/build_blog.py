from PIL import Image
import html, os
R='/home/claude/904-request/'; SL='browndot-jukdo'; V='11211300'
D=R+'blog/'+SL+'/'+V+'/'; os.makedirs(D,exist_ok=True); W='/home/claude/brown/work/'
seq=[('b_out','브라운도트 죽도점 입구'),('b_lobby','시공 전 로비'),('b_front','시공 전 프런트'),('b_hall','시공 전 복도'),('b_cafe','시공 전 조식 공간'),
('b_entry','시공 준비'),('p_start','벽 쪽 첫 줄'),('p_entry','입구부터 600각 타일 시공'),('p_mortar','타일 접착제 준비'),('p_trowel2','접착제 고르게 펴기'),('p_trowel','기존 바닥 위로 시공'),
('p_lobby_clips','로비 평탄클립'),('p_corr','복도 쪽 시공'),('p_team','90.4 시공팀'),('p_team2','집기 옮겨가며 작업'),('p_hall','엘리베이터 앞 복도'),
('p_lobby_done','로비 바닥 완료'),('p_clean','작업 끝나면 바로 정리'),('p_night','저녁 마감 후 입구'),
('a_lobby','로비 완성'),('a_front','프런트 완성'),('a_kiosk','키오스크·복도 완성'),('a_cafe','조식 공간 완성'),('a_cafe2','조식 공간 완성'),('a_cafe5','테이블 제자리'),('a_cafe4','조식 공간 전경'),('a_ev2','엘리베이터 바닥까지')]
for i,(f,alt) in enumerate(seq,1):
    im=Image.open(W+f+'.jpg'); im.thumbnail((1600,1600)); im.save(f'{D}{i:02d}.jpg',quality=88)
N={f:i for i,(f,a) in enumerate(seq,1)}
U=lambda f:f'<p style="text-align:center"><img src="https://904bath.github.io/904-request/blog/{SL}/{V}/{N[f]:02d}.jpg" alt="{seq[N[f]-1][1]}" style="max-width:100%"></p>'
P=lambda t:f'<p>{t}</p>'; H=lambda t:f'<h3><b>{t}</b></h3>'; E='<p><br></p>'
I=lambda *fs:''.join(U(f) for f in fs)
tags='#상가타일시공 #호텔타일 #로비타일 #바닥타일시공 #600각타일 #600각바닥 #영업중시공 #상업공간인테리어 #브라운도트 #브라운도트죽도점 #타일시공 #대구타일시공 #구공사 #904BATH'
body=[P('안녕하세요, 욕실 · 타일 시공팀 <b>구공사(90.4 BATH)</b>입니다.'),E,
P('오늘은 <b>브라운도트 죽도점</b> 로비 바닥 시공 현장이에요.'),
P('로비 · 프런트 · 조식 공간 · 복도 · 엘리베이터 바닥까지 <b>600각 타일</b>로 새로 깔았습니다.'),E,
P('이번 현장은 조건이 조금 특별했어요.'),
P('· <b>홍보영상 촬영 3일 전</b>이라 일정이 빠듯했고'),
P('· <b>영업 중</b>이라 손님이 오가는 상태에서 최대한 빠르고 조용하게 해야 했고'),
P('· 테이블·의자·냉장고 같은 집기가 그대로 있어서 <b>저희가 직접 옮겨가며</b> 구역별로 작업했습니다.'),E,
P('✔ 이런 분들께 도움이 될 거예요'),
P('· 가게·숙소 문을 닫지 않고 바닥을 바꾸고 싶은 사장님'),
P('· 오픈·촬영·행사 날짜가 정해져 있어서 일정이 급한 분'),
P('· 600각 같은 큰 타일로 넓고 깔끔한 바닥을 원하시는 분'),E,
I('b_out'),
H('1. 시공 전 — 화이트 대리석 무늬 바닥'),
P('기존 바닥은 화이트 대리석 무늬 타일이었어요. 이번에 차분한 톤의 600각 타일로 분위기를 바꿨습니다.'),I('b_lobby','b_front','b_hall','b_cafe'),E,
H('2. 입구부터 한 줄씩'),
P('손님 동선이 끊기지 않게 구역을 나눠서, 벽 쪽 첫 줄과 입구부터 차례로 깔아 나갔어요.'),
P('첫 줄이 반듯해야 나머지 줄눈이 전부 맞아떨어지기 때문에 제일 신경 쓰는 단계입니다.'),I('b_entry','p_start','p_entry'),E,
H('3. 접착제 · 평탄클립'),
P('타일 접착제를 고르게 펴 바르고, 600각 타일을 한 장씩 눌러 붙였어요.'),
P('이번 현장은 기존 바닥을 걷어내지 않고 그 위로 바로 시공해서, 철거 소음·먼지 없이 빠르게 진행할 수 있었습니다.'),
I('p_mortar','p_trowel2','p_trowel'),
P('큰 타일일수록 이음새 높이 차이(단차)가 잘 보여요. 그래서 모든 이음새에 평탄클립을 촘촘하게 끼워 높이를 맞췄습니다.'),I('p_lobby_clips','p_corr'),E,
H('4. 집기는 직접 옮겨가며'),
P('조식 공간에는 테이블·의자·음료 냉장고·선반이 그대로 있었어요.'),
P('한쪽으로 옮겨두고 깔고, 다시 옮기고 깔고 — 구역별로 나눠서 작업했습니다.'),I('p_team','p_team2','p_hall'),E,
P('로비는 하루 만에 바닥 전체를 덮었고, 작업이 끝나면 바로바로 정리해서 손님 다니는 길을 비워뒀어요.'),I('p_lobby_done','p_clean','p_night'),E,
H('5. 완성 — 로비 · 프런트'),
P('밝은 그레이 베이지 톤 600각 타일로 넓은 로비가 한층 차분해졌어요. 줄눈이 적어서 공간이 더 넓어 보입니다.'),I('a_lobby','a_front','a_kiosk'),E,
H('6. 완성 — 조식 공간 · 복도 · 엘리베이터'),
P('옮겨뒀던 테이블과 의자도 제자리로. 촬영 전에 손님 맞을 준비까지 끝냈습니다.'),
I('a_cafe','a_cafe2','a_cafe5','a_cafe4'),P('엘리베이터 바닥까지 같은 타일로 맞춰서 동선이 하나로 이어져요.'),I('a_ev2'),E,
H('자주 물어보시는 것'),
P('<b>Q. 영업하면서 바닥 공사가 되나요?</b>'),
P('A. 구역을 나눠서 하면 가능해요. 이번 현장도 영업 중에 집기를 옮겨가며 순서대로 진행했습니다.'),E,
P('<b>Q. 기존 바닥을 꼭 철거해야 하나요?</b>'),
P('A. 기존 바닥 상태가 괜찮으면 그 위로 시공할 수 있어요. 철거가 없으니 소음·먼지·기간이 확 줄어듭니다. 상태는 현장을 보고 판단해요.'),E,
P('<b>Q. 600각 타일, 상업 공간 바닥에 괜찮나요?</b>'),
P('A. 줄눈이 적어 넓어 보이고 청소가 편해서 로비·매장에 잘 맞아요. 대신 평탄 작업을 제대로 해야 단차 없이 나옵니다.'),E,
P('<b>Q. 견적은 어떻게 받나요?</b>'),
P('A. 공간 사진 몇 장과 대략적인 면적만 보내주시면 편하게 상담 도와드려요.'),E,
P('저희 팀은 90년대생 젊은 시공자들이 직접 현장에 들어갑니다.'),
P('철거부터 마감까지 한 팀이 끝까지 책임지고 있어요.'),E,
P('<b>상담은 편하게, 시공은 확실하게.</b>'),E,
P('<b>90.4 BATH INTERIOR DESIGN</b> · 욕실 · 바닥 타일 시공'),P('문의 010-9459-9904'),
P('네이버 플레이스 <a href="https://map.naver.com/p/entry/place/2018592692">https://map.naver.com/p/entry/place/2018592692</a>'),E,P(tags)]
title='상가 바닥 타일 | 브라운도트 죽도점 600각 바닥 시공 (영업 중 · 촬영 3일 전)'
tpl=open(R+'blog/dongil-hibill/index.html').read()
head=tpl[:tpl.index('<div class="paper">')].replace('대구 동일하이빌','브라운도트 죽도점').replace('"11192155"',f'"{V}"')
head=head.replace('../../media/','../../media/#'+SL) if False else head.replace('href="../../media/"',f'href="../../media/#{SL}"')
tail=tpl[tpl.index('</div>\n<script>')+7:] if '</div>\n<script>' in tpl else tpl[tpl.rindex('<script>'):]
page=head+f'<div class="paper"><div class="ttl" id="title">{html.escape(title)}</div><div id="post">{"".join(body)}</div>\n<div id="tags" style="display:none">{html.escape(tags)}</div></div>\n'+tail
open(R+'blog/'+SL+'/index.html','w').write(page); open(R+'blog/'+SL+'/version.json','w').write('{"v": "%s"}'%V)
print('ok',len(seq))
