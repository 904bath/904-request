import subprocess, os
from playwright.sync_api import sync_playwright
V='/mnt/user-data/uploads/Downloads/'
enc=['-c:v','libx264','-preset','veryfast','-crf','19','-pix_fmt','yuv420p','-r','30']
def run(c): subprocess.run(c,check=True)
CSS="body{margin:0;background:transparent}*{box-sizing:border-box}"
def label_png(path,text):
    inner=text if text.startswith('<') else f'<div style="font-family:Lora,serif;font-size:118px;letter-spacing:2px">{text}</div>'
    h=f'<div style="width:1080px;height:1920px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;color:#fff;text-shadow:0 2px 18px rgba(0,0,0,.45)">{inner}</div>' if text else '<div style="width:1080px;height:1920px"></div>'
    PG.set_viewport_size({'width':1080,'height':1920})
    open('/tmp/m.html','w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>')
    PG.goto('file:///tmp/m.html'); PG.wait_for_timeout(100); PG.screenshot(path=path,omit_background=True)
def logo_png(path,logo):
    h=f'<div style="width:1080px;height:1920px;background:#dcd6cd;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:40px"><img src="{logo}" style="width:720px"><div style="font-family:Lora,serif;font-size:46px;color:#3a3631;letter-spacing:6px">daegu tile &amp; bath</div></div>'
    open('/tmp/m.html','w').write(f'<html><head><meta charset="utf-8"><style>body{{margin:0}}</style></head><body>{h}</body></html>')
    PG.goto('file:///tmp/m.html'); PG.wait_for_timeout(150); PG.screenshot(path=path)
def build(segs,out,endcard,tmp):
    global PG
    os.makedirs(tmp,exist_ok=True); files=[]
    with sync_playwright() as p:
        br=p.chromium.launch(); PG=br.new_page(viewport={'width':1080,'height':1920})
        labels={}
        for i,s in enumerate(segs):
            d=s['d']; n=int(round(d*30)); o=f'{tmp}/{i:02d}.mp4'
            if s['t']=='logo':
                lp=f'{tmp}/logo.png'; logo_png(lp,s['logo'])
                run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-t',str(d),'-i',lp,'-vf',"scale=1080:1920,format=yuv420p",'-frames:v',str(n)]+enc+[o])
            else:
                lab=s.get('label','')
                if lab not in labels:
                    lp=f'{tmp}/lab{len(labels)}.png'; label_png(lp,lab); labels[lab]=lp
                lp=labels[lab]
                if s['t']=='video':
                    sp=s.get('speed',1)
                    fc=f"[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setpts=PTS/{sp},fps=30,eq=saturation=0.85,format=yuv420p[b];[1:v]format=rgba[o];[b][o]overlay=0:0:format=auto,format=yuv420p"
                    run(['ffmpeg','-y','-loglevel','error','-ss',str(s.get('ss',0)),'-t',f'{d*sp+0.3:.2f}','-i',V+s['src'],'-loop','1','-framerate','30','-t',str(d),'-i',lp,'-filter_complex',fc,'-an','-frames:v',str(n)]+enc+[o])
                else:
                    z=f"zoompan=z='1+{s.get('zoom',0.06)}*on/{n}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={n}:s=1080x1920:fps=30"
                    fc=f"[0:v]scale=2160:-1,{z},eq=saturation=0.85,format=yuv420p[b];[1:v]format=rgba[o];[b][o]overlay=0:0:format=auto,format=yuv420p"
                    run(['ffmpeg','-y','-loglevel','error','-i',s['src'],'-loop','1','-framerate','30','-t',str(d),'-i',lp,'-filter_complex',fc,'-frames:v',str(n)]+enc+[o])
            files.append(o)
        br.close()
    run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-t','3.2','-i',endcard,'-vf',"scale=1080:1920,format=yuv420p",'-frames:v','96']+enc+[f'{tmp}/end.mp4'])
    files.append(f'{tmp}/end.mp4')
    open(f'{tmp}/list.txt','w').write(''.join(f"file '{os.path.basename(f)}'\n" for f in files))
    run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',f'{tmp}/list.txt','-c','copy',f'{tmp}/v.mp4'])
    run(['ffmpeg','-y','-loglevel','error','-i',f'{tmp}/v.mp4','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-c:v','copy','-c:a','aac','-shortest',out+'.tmp.mp4'])
    os.rename(out+'.tmp.mp4',out)
