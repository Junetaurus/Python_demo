# 图像右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
#-*-coding: utf-8-*-
from PIL import Image, ImageDraw, ImageFont

def imageWriter(filePath, number):
    img = Image.open(filePath)
    size = img.size
    fontSize = size[1] / 4
    draw = ImageDraw.Draw(img)
    ttFont = ImageFont.truetype('ahronbd.ttf', 50)
    draw.text((size[0]-fontSize, 0), str(number),fill=(255, 0, 0) ,font=ttFont)
    img.show()

print(imageWriter('0.png', 8))