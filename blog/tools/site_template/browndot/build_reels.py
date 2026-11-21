import sys; sys.path.insert(0,'/home/claude/904-request/blog/tools')
import reel_minimal as RM
RM.V='/home/claude/brown/vids/'
R='/home/claude/904-request/'; W='/home/claude/brown/work/'; M=R+'media/browndot-jukdo/11211300/'
K="font-family:'Noto Sans CJK KR';font-weight:700"
hook=f'<div style="{K};font-size:92px;line-height:1.2">브라운도트 죽도점</div><div style="{K};font-size:76px;margin-top:14px">촬영 D-3, 영업 중</div><div style="font-family:\'Noto Sans CJK KR\';font-weight:500;font-size:50px;margin-top:22px">600각 바닥 시공</div>'
aft='<div style="font-family:Lora,serif;font-size:118px">after ..</div><div style="font-family:\'Noto Sans CJK KR\';font-weight:500;font-size:44px;margin-top:18px">로비 · 조식 공간 · 엘리베이터 · 600각 타일</div>'
ph=lambda f,d,l='',z=0.06:{'t':'photo','src':W+f+'.jpg','d':d,'label':l,'zoom':z}
logo={'t':'logo','d':1.0,'logo':'file://'+R+'blog/assets/90.4BATH_로고_투명_검정선(밝은배경용).png'}
short=[ph('a_lobby',1.8,hook,0.04),ph('b_lobby',0.6,'before ..'),ph('b_front',0.6,'before ..'),ph('b_cafe2',0.6,'before ..'),
ph('p_entry',0.65,'process ..'),ph('p_trowel',0.65,'process ..'),ph('p_mortar',0.65,'process ..'),ph('p_lobby_clips',0.65,'process ..'),
ph('p_corr',0.65,'process ..'),ph('p_team',0.75,'process ..'),ph('p_hall',0.65,'process ..'),ph('p_lobby_done',0.65,'process ..'),
{'t':'video','src':'v26.mp4','d':1.0,'label':'process ..','speed':2},ph('p_night',0.65,'process ..'),
ph('a_lobby',1.6,aft),ph('a_front',1.2),ph('a_kiosk',1.1),ph('a_cafe',1.2),ph('a_cafe5',1.1),ph('a_ev2',1.1),logo]
RM.build(short,M+'reel.mp4',R+'blog/assets/endcard_light.png','/home/claude/brown/rt1')
long=[ph('a_lobby',1.8,hook,0.04),{'t':'video','src':'v25.mp4','d':1.6,'label':'before ..','speed':2},ph('b_lobby',0.6,'before ..'),ph('b_front',0.6,'before ..'),ph('b_hall',0.6,'before ..'),
ph('p_start',0.8,'process ..'),ph('p_entry',0.8,'process ..'),ph('p_mortar',0.8,'process ..'),ph('p_trowel2',0.8,'process ..'),ph('p_trowel',0.8,'process ..'),ph('p_lobby_clips',0.8,'process ..'),
ph('p_corr',0.8,'process ..'),ph('p_team',0.9,'process ..'),ph('p_team2',0.8,'process ..'),ph('p_hall',0.8,'process ..'),ph('p_lobby_done',0.8,'process ..'),ph('p_clean',0.8,'process ..'),
{'t':'video','src':'v26.mp4','d':1.4,'label':'process ..','speed':2},ph('p_night',0.8,'process ..'),
ph('a_lobby',1.6,aft),ph('a_front',1.0),ph('a_kiosk',1.0),ph('a_cafe',1.0),ph('a_cafe2',1.0),ph('a_cafe5',1.0),ph('a_cafe4',1.0),ph('a_ev2',1.0),
{'t':'logo','d':1.2,'logo':logo['logo']}]
RM.build(long,M+'blog_video.mp4',R+'blog/assets/endcard_light.png','/home/claude/brown/rt2')
print('ok')
