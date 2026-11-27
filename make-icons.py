# 用法：python3 make-icons.py 你的圖.png  → 產生 icons/ 內所有尺寸
import sys
from PIL import Image
src = Image.open(sys.argv[1]).convert('RGB')
w, h = src.size; s = min(w, h)
src = src.crop(((w-s)//2, (h-s)//2, (w-s)//2+s, (h-s)//2+s))
for name, size in [('icon-192', 192), ('icon-512', 512), ('apple-touch-icon', 180)]:
    src.resize((size, size), Image.LANCZOS).save(f'icons/{name}.png')
bg = src.getpixel((5, 5))  # 用圖片角落顏色當 maskable 底色
m = Image.new('RGB', (512, 512), bg)
m.paste(src.resize((420, 420), Image.LANCZOS), (46, 46))
m.save('icons/maskable-512.png')
print('done')
