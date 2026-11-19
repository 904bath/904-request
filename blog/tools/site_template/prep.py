from PIL import Image, ImageOps, ImageEnhance, ImageFilter
import os
S='/home/claude/dong/src/'; W='/home/claude/dong/work/'
for f in os.listdir(S):
    im=ImageOps.exif_transpose(Image.open(S+f)).convert('RGB')
    if f.startswith('a_b_'):  # 베이지 욕실 완성: 뿌연 기운만 걷고 밝기 조절
        im=ImageOps.autocontrast(im,cutoff=0.8)
        im=ImageEnhance.Brightness(im).enhance(1.06)
        im=im.filter(ImageFilter.UnsharpMask(radius=2,percent=60,threshold=3))
    im.save(W+f,quality=93)
    print(f,im.size)
