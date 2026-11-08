import subprocess, os, sys
from playwright.sync_api import sync_playwright
V='/mnt/user-data/uploads/Downloads/'
enc=['-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p','-r','30']
CSS="""body{margin:0;background:transparent}*{font-family:'Noto Sans CJK KR',sans-serif;box-sizing:border-box}
.cap{position:absolute;left:40px;right:40px;top:1180px;text-align:center;color:#fff;font-weight:900}
.main{font-size:92px;line-height:1.15;-webkit-text-stroke:14px #111;paint-order:stroke fill}
.sub{display:inline-block;margin-top:26px;background:#ffe14d;color:#111;font-size:50px;padding:10px 26px;transform:rotate(-2deg)}
.badge{position:absolute;left:60px;top:140px;background:#111;color:#ffe14d;font-weight:900;font-size:46px;padding:10px 22px;border:4px solid #ffe14d}
.mark{position:absolute;right:60px;top:150px;color:#fff;font-weight:900;font-size:32px;letter-spacing:4px;-webkit-text-stroke:6px #111;paint-order:stroke fill}
.tag{position:absolute;left:60px;font-weight:900;font-size:56px;padding:10px 26px;transform:rotate(-3deg)}"""
def overlay(path,main,sub='',badge='',ba=None):
    b=f'<div class="badge">{badge}</div>' if badge else ''
    s=f'<div class="sub">{sub}</div>' if sub else ''
    extra=''
    if ba:
        extra=('<div class="tag" style="top:120px;background:#111;color:#fff;border:5px solid #fff">BEFORE</div>'
               '<div class="tag" style="top:1000px;background:#ffe14d;color:#111">AFTER</div>'
               '<div style="position:absolute;left:0;right:0;top:954px;height:12px;background:#111"></div>')
        cap=f'<div style="position:absolute;left:0;right:0;top:880px;text-align:center"><span style="display:inline-block;background:#fff;color:#111;font-weight:900;font-size:64px;padding:10px 34px;border:6px solid #111;transform:rotate(2deg)">{ba}</span></div>'
    else:
        cap=f'<div class="cap"><div class="main">{main}</div>{s}</div>'
    h=f'<div style="width:1080px;height:1920px;position:relative">{extra}{b}<div class="mark">90.4 BATH</div>{cap}</div>'
    open('/tmp/r.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>')
    PG.goto('file:///tmp/r.html'); PG.wait_for_timeout(120); PG.screenshot(path=path,omit_background=True)
def run(c): subprocess.run(c,check=True)
def build(segs,out,endcard='/home/claude/reel/ov2/08.png',tmp='seg'):
    global PG
    os.makedirs(tmp,exist_ok=True); files=[]
    with sync_playwright() as p:
        br=p.chromium.launch(); PG=br.new_page(viewport={'width':1080,'height':1920})
        for i,s in enumerate(segs):
            ov=f'{tmp}/{i:02d}.png'; overlay(ov,s.get('main',''),s.get('sub',''),s.get('badge',''),s.get('ba'))
            d=s['d']; n=int(round(d*30)); o_=f'{tmp}/{i:02d}.mp4'
            first=(i==0)
            ovf="[1:v]format=rgba[o];[b][o]overlay=0:0:format=auto" if first else "[1:v]format=rgba,fade=in:st=0:d=0.15:alpha=1[o];[b][o]overlay=x=0:y='if(lt(t,0.25),50*pow(1-t/0.25,2),0)':format=auto"
            if s['t']=='video':
                sp=s.get('speed',1)
                fc=f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setpts=PTS/{sp},fps=30,format=yuv420p[b];{ovf},format=yuv420p"
                run(['ffmpeg','-y','-loglevel','error','-ss',str(s.get('ss',0)),'-t',f'{d*sp+0.3:.2f}','-i',V+s['src'],'-loop','1','-framerate','30','-t',str(d),'-i',ov,'-filter_complex',fc,'-an','-frames:v',str(n)]+enc+[o_])
            else:
                z=f"zoompan=z='1+{s.get('zoom',0.07)}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30"
                fc=f"[0:v]scale=2160:-1,{z},format=yuv420p[b];{ovf},format=yuv420p"
                run(['ffmpeg','-y','-loglevel','error','-i',s['src'],'-loop','1','-framerate','30','-t',str(d),'-i',ov,'-filter_complex',fc,'-frames:v',str(n)]+enc+[o_])
            files.append(o_)
        br.close()
    run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-t','3','-i',endcard,'-filter_complex',"color=c=0x111111:s=1080x1920:r=30:d=3[b];[0:v]format=rgba,fade=in:st=0:d=0.3:alpha=1[o];[b][o]overlay=0:0:format=auto,format=yuv420p",'-frames:v','90']+enc+[f'{tmp}/end.mp4'])
    files.append(f'{tmp}/end.mp4')
    open(f'{tmp}/list.txt','w').write(''.join(f"file '{os.path.basename(f)}'\n" for f in files))
    run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',f'{tmp}/list.txt','-c','copy',f'{tmp}/v.mp4'])
    run(['ffmpeg','-y','-loglevel','error','-i',f'{tmp}/v.mp4','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-c:v','copy','-c:a','aac','-shortest',out+'.tmp.mp4'])
    os.rename(out+'.tmp.mp4',out)
