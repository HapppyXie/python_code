# Athour:Mr Xie
# 开发时间:2021/11/21 20:46
'''

在Idle可以的
import wordcloud
from wordcloud import WordCloud
wordcloud.WordCloud()代表一个文本对应的词云
- 可以根据文本中词语出现的频率等参数绘制词云
- 词云的绘制形状、尺寸和颜色都可以设定

- 步骤1：配置对象参数
- 步骤2：加载词云文本
- 步骤3：输出词云文件

import wordcloud
c = wordcloud.WordCloud()
c.generate("wordcloud by Python")
c.to_file("pywordcloud.png")  默认在桌面

w = wordcloud.WordCloud(<参数>)
指定词云对象生成图片的宽度，默认400像素
  >>>w=wordcloud.WordCloud(width=600)
指定词云对象生成图片的高度，默认200像素
  >>>w=wordcloud.WordCloud(height=400)

指定词云中字体的最小字号，默认4号
w=wordcloud.WordCloud(min_font_size=10)
指定词云中字体的最大字号，根据高度自动调节
指定词云中字体字号的步进间隔，默认为1
w=wordcloud.WordCloud(font_step=2)

指定字体文件的路径，默认None
w=wordcloud.WordCloud(font_path="msyh.ttc")
指定词云显示的最大单词数量，默认200
w=wordcloud.WordCloud(max_words=20)
指定词云的排除词列表，即不显示的单词列表
from wordcloud import STOPWORDS
w=wordcloud.WordCloud(stop_words={"Python"})

指定词云形状，默认为长方形，需要引用imread()函数
from scipy.misc import imread
mk=imread("pic.png")
w=wordcloud.WordCloud(mask=mk)

指定词云图片的背景颜色，默认为黑色
w=wordcloud.WordCloud(background_color="white")

import wordcloud
txt = "life is short, you need python"
w = wordcloud.WordCloud( \
       background_color = "white")
w.generate(txt)
w.to_file("pywcloud.png")

import jieba
import wordcloud
txt = "程序设计语言是计算机能够理解和\
识别用户操作意图的一种交互体系，它按照\
特定规则组织计算机指令，使计算机能够自\
动进行各种运算处理。"
w = wordcloud.WordCloud( width=1000,\
    font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("pywcloud.png")

'''









