#!
# 图片转字符画

"""
使用公式：gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b, 将RGB色值转换为灰度值。
每个灰度值对应一个字符，透明度为0时灰度值为255（白色）
"""

from PIL import Image

def convert_rgb2char(r, g, b, alpha = 256):
    #if 254 <= alpha: return ' ';

    grayChars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'  "
    grayValue = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    shrinkRate = len(grayChars) / 256
    return grayChars[int(grayValue * shrinkRate)]

imgFile = '/data/python/python-practice-80/resources/dlam.jpg'
width, height = 80, 100

if '__main__' == __name__:
    img = Image.open(imgFile, 'r')
    img = img.resize((width, height), Image.NEAREST)
    chars = ''
    for j in range(height):
        for i in range(width):
            chars += convert_rgb2char(*img.getpixel((i, j)))
        chars += "\n"
    print(chars)

