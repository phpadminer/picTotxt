##python基础实战项目--将图片转化为字符串输出
>本文是知乎上推荐的[python实战项目](https://www.zhihu.com/question/29372574/answer/88624507?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io)的基础篇的开篇！
>首先声明一下：我不是知乎上面的文章的作者！我写这篇文章主要是想记录和分享一下我实践中的想法和心得！

###1.1 项目简介
本项目用 `50` 行 `Python `代码完成图片转字符画小工具。

###1.2 项目环境
- [x]python3.6.4
- [x]mac

###1.3 需要的第三方库
- [x] pillow 
- [x] argparse

###1.4 实现原理
图片可以看作是一个个像素块组成的，我们只需要将像素块替换成指定的文字就行了！
核心是：如何将彩色的图片转化为单色的图片 ，这里需要用到灰度转化公式：
```gray ＝ 0.2126 * r + 0.7152 * g + 0.0722 * b```

###1.5 业务逻辑图
```flow
st=>start: 开始
e=>end: 结束
op1=>operation: 获取图片
op2=>operation: 获取图片的宽高
op3=>operation: 依次获取图片的像素
op4=>operation: 将像素用灰度转化公式转化
op5=>operation: 依次替换像素块
op6=>operation: 输出图片到文本中
st->op1->op2->op3->op4->op5->op6->e
```

###1.6 代码实现
```
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
```

###1.7 结语
本次项目至此已经全部完成！如果您有什么疑问可以直接在下面留言或者在我github上issue我！




