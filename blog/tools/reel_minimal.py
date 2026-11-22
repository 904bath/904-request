import subprocess, os
from playwright.sync_api import sync_playwright
V='/mnt/user-data/uploads/Downloads/'
enc=['-c:v','libx264','-preset','slow','-crf','15','-pix_fmt','yuv420p','-r','30']
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
def smooth_photo(src,lp,n,zoom,o):
    # 서브픽셀 줌 (떨림 없음) + 화질 우선: 원본 해상도에서 바로 LANCZOS로 한 번만 리샘플, 약한 샤픈, 고화질 인코딩
    from PIL import Image, ImageOps, ImageEnhance, ImageFilter
    W,H=1080,1920
    im=ImageOps.exif_transpose(Image.open(src)).convert('RGB')
    iw,ih=im.size; r=W/H
    if iw/ih>r: cw,ch=ih*r,ih
    else: cw,ch=iw,iw/r
    ox,oy=(iw-cw)/2,(ih-ch)/2
    im=ImageEnhance.Color(im).enhance(0.9)
    lab=Image.open(lp).convert('RGBA').resize((W,H))
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r','30','-i','-',
        '-c:v','libx264','-preset','slow','-crf','15','-tune','film','-pix_fmt','yuv420p','-r','30',o],stdin=subprocess.PIPE)
    for k in range(n):
        z=1+zoom*k/max(n-1,1); w,h=cw/z,ch/z; x0,y0=ox+(cw-w)/2,oy+(ch-h)/2
        f=im.resize((W,H),Image.LANCZOS,box=(x0,y0,x0+w,y0+h)).filter(ImageFilter.UnsharpMask(radius=1.2,percent=45,threshold=2)).convert('RGBA')
        f.alpha_composite(lab); p.stdin.write(f.convert('RGB').tobytes())
    p.stdin.close(); p.wait()
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
                    smooth_photo(s['src'],lp,n,s.get('zoom',0.04),o)
            files.append(o)
        br.close()
    run(['ffmpeg','-y','-loglevel','error','-loop','1','-framerate','30','-t','3.2','-i',endcard,'-vf',"scale=1080:1920,format=yuv420p",'-frames:v','96']+enc+[f'{tmp}/end.mp4'])
    files.append(f'{tmp}/end.mp4')
    open(f'{tmp}/list.txt','w').write(''.join(f"file '{os.path.basename(f)}'\n" for f in files))
    run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',f'{tmp}/list.txt','-c','copy',f'{tmp}/v.mp4'])
    run(['ffmpeg','-y','-loglevel','error','-i',f'{tmp}/v.mp4','-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-c:v','copy','-c:a','aac','-shortest',out+'.tmp.mp4'])
    os.rename(out+'.tmp.mp4',out)
