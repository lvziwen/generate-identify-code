
# coding:utf-8
'''
利用python图像处理包PIL生成验证码
Centos安装相关依赖库
yum install libjpeg libjpeg-devel zlib zlib-devel freetype freetype-devel lcms lcms-devel
yum install python-imaging
'''

import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('/usr/share/fonts/liberation/LiberationSerif-Bold.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
char_list = [rndChar() for i in range(4)]
print char_list
for t in range(4):
    draw.text((60 * t + 10, 10), char_list[t], font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg');
