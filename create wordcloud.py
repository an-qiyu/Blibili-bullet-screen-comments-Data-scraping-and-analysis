import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.colors as colors  # 处理图片相关内容
import matplotlib.pyplot as plt # 图像展示库

# 读取文件
f = open('bullet chat.txt','r', encoding="utf-8") # 打开文件
t = f.read() # 读出整个文件
f.close() # 关闭文件


# 文本分词
string = jieba.lcut(t) # 精确模式分词
string = [word for word in string if len(word)>1]# 排除单字，即获取弹幕时没分离出的乱码中文


# 词频统计
word_counts = collections.Counter(string) # 对分词做词频统计
word_counts_top10 = word_counts.most_common(20) # 获取前20最高频的词
print (word_counts_top10) # 输出检查

# 词频展示
mask = np.array(Image.open('wordcloud.jpg')) # 定义词频背景
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simhei.ttf', # 设置字体格式
    mask=mask, # 设置背景图
    background_color='white',
    max_words=250, # 最多显示词数

)

wc.generate_from_frequencies(word_counts) # 从字典生成词云
#image_colors = wordcloud.ImageColorGenerator(mask, default_color=None)# 从背景图建立颜色方案
#wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
plt.imshow(wc) # 显示词云
plt.axis('off') # 关闭坐标轴
plt.show() # 显示图像
