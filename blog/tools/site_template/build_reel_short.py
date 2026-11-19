import sys; sys.path.insert(0,'/home/claude/904-request/blog/tools')
import reel_minimal as RM
R='/home/claude/904-request/'; W='/home/claude/dong/work/'
hook='<div style="font-family:\'Noto Sans CJK KR\';font-weight:700;font-size:96px;line-height:1.2">동일하이빌</div><div style="font-family:\'Noto Sans CJK KR\';font-weight:700;font-size:72px;margin-top:10px">욕실 2칸, 3일</div><div style="font-family:\'Noto Sans CJK KR\';font-weight:500;font-size:50px;margin-top:22px">대구 · 600각 타일</div>'
aft='<div style="font-family:Lora,serif;font-size:118px">after ..</div><div style="font-family:\'Noto Sans CJK KR\';font-weight:500;font-size:44px;margin-top:18px">조적 젠다이 · 파티션 · 600각 타일</div>'
ph=lambda f,d,l='',z=0.06:{'t':'photo','src':W+f,'d':d,'label':l,'zoom':z}
segs=[ph('a_g_wide2.jpg',1.8,hook,0.04),
ph('p_wp3.jpg',0.6,'before ..'),ph('p_wp1.jpg',0.6,'before ..'),
ph('p_laser2.jpg',0.65,'process ..'),ph('p_laser.jpg',0.65,'process ..'),ph('p_team.jpg',0.75,'process ..'),ph('p_beige_first.jpg',0.65,'process ..'),
ph('p_g_wall2.jpg',0.65,'process ..'),ph('p_jojeok.jpg',0.65,'process ..'),ph('p_floor_team.jpg',0.75,'process ..'),ph('p_tub.jpg',0.65,'process ..'),
ph('p_g_part2.jpg',0.65,'process ..'),ph('p_b_part2.jpg',0.65,'process ..'),
ph('a_g_wide.jpg',1.6,aft),ph('a_g_part.jpg',1.2),ph('a_g_jendai.jpg',1.1),ph('a_b_wide.jpg',1.4),ph('a_b_wide2.jpg',1.2),
{'t':'logo','d':1.0,'logo':'file://'+R+'blog/assets/90.4BATH_로고_투명_검정선(밝은배경용).png'}]
RM.build(segs,R+'media/dongil-hibill/11192155/reel.mp4',R+'blog/assets/endcard_light.png','/home/claude/dong/reeltmp2')
print('ok')
