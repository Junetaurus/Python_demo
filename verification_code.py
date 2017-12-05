# 使用 Python 生成字母验证码图片

#-*-coding: utf-8-*-

from PIL import Image, ImageFont, ImageDraw, ImageFilter
import string
import random

def make_rand_char():
    return random.choice(string.ascii_letters)

def generator_bgcolor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def generator_font_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def producer(number):

    if number <= 0:
        return

    height = 60
    width = number*height
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('ahronbd.ttf', 40)
    draw = ImageDraw.Draw(image)

    for x in  range(width):
        for y in  range(height):
            draw.point((x, y), fill=generator_bgcolor())

    rand_char = ''
    for i in range(number):
        char = make_rand_char()
        rand_char += char
        draw.text((i*60+10, 10), char, font=font, fill=generator_font_color())

    image = image.filter(ImageFilter.BLUR)
    image.show()
    print(rand_char)

if __name__ == '__main__':
    producer(4)