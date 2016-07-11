from PIL import ImageFont, ImageDraw, Image
import re

font = ImageFont.truetype(font='msyh.ttf', size=14)
pattern = re.compile(r'.{2}')
im = Image.new('1', (64, 32), (1))
draw = ImageDraw.Draw(im)
draw.text((0, -5), '你好世界\n你好世界', font=font)
res = []
for h in range(32):
    tmp = ''
    for w in range(64):
        if im.getpixel((w, h)):
            tmp += '0'
            print('○', end='')
        else:
            tmp += '1'
            print('●', end='')
    print('')
    res.append(','.join(map(lambda x: '0x' + x, pattern.findall("%016X" % int(tmp, 2)))) + ',')
res = ''.join(res)[:-1]
print(res)
