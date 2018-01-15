#! /usr/local/bin/python3.6
# -*- coding : utf-8 -*-

from PIL import Image
import argparse

# 命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')  # 输入文件
parser.add_argument('-o', '--output')  # 输出文件

# 获取参数
args = parser.parse_args()

IMG = args.file

OUTPUT = args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    # 为了不能超过列表的长度,我们必须给她一个系数 这个系数是根据列表的长度算出来的！
    unit = (256 + 1) / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':

    im = Image.open(IMG)
    # 获取图片的长和宽
    WIDTH, HEIGHT = im.size
    # 缩放图片 (以最高质量输出)
    im = im.resize((WIDTH, HEIGHT), Image.ANTIALIAS)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j, i)))
        txt += '\n'

    print(txt)

    # 字符画输出到文件
    with open(OUTPUT and OUTPUT or 'output.txt', 'w') as f:
        f.write(txt)
