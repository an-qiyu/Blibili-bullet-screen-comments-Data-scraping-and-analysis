# 对已获取的弹幕数据分词，除去正则匹配未消除的乱码单字，词云、热度前20英雄柱状图
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
jieba.load_userdict('英雄名.txt')
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库

# 读取文件
def get_string():
    f = open('E:\爬取弹幕\B站弹幕.txt','r', encoding="utf-8") # 打开文件
    t = f.read() # 读出整个文件
    f.close() # 关闭文件

    # 文本分词
    string = jieba.lcut(t) # 精确模式分词
    string = [word for word in string if len(word)>1]# 排除单字，即获取弹幕时没分离出的乱码中文
    return string

def get_people_count(string):
    counts = {}  # 创建一个空字典
    excludes = {"啊啊啊"}

    for word in string:
        if len(word) == 1:
            continue
        elif word == "亮亮" or word == "诸葛":  # 列举排除相同情况
            rword = "诸葛亮"
        elif word == "昭君":
            rword = "王昭君"
        elif word == "阿离" or word == "离离":
            rword = "公孙离"
        elif word == "香香" or word == "大小姐":
            rword = "孙尚香"
        elif word == "百里" or word == "守约":
            rword = "百里守约"
        elif word == "信信":
            rword = "韩信"
        elif word == "李华" or word == "贵妃" or word == "玉环":
            rword = "杨玉环"
        elif word == "猴子" or word == "大圣":
            rword = "孙悟空"
        elif word == "子龙" or word == "赵子龙":
            rword = "赵云"
        elif word == "瑶瑶" or word == "阿瑶" or word == "公主":
            rword = "瑶"
        elif word == "小明":
            rword = "明世隐"
        elif word == "夫子":
            rword = "老夫子"
        elif word == "云云":
            rword = "云中君"
        elif word == "婉儿":
            rword = "上官婉儿"
        elif word == "东皇":
            rword = "东皇太一"
        elif word == "公瑾" or word == "都督" or word == "瑜瑜":
            rword = "周瑜"
        elif word == "元芳":
            rword = "李元芳"
        elif word == "奉先":
            rword = "吕布"
        elif word == "狄怀英":
            rword = "狄仁杰"
        elif word == "婵儿":
            rword = "貂蝉"
        elif word == "班爹":
            rword = "鲁班大师"
        elif word == "火舞":
            rword = "不知火舞"
        elif word == "木兰" or word == "兰兰":
            rword = "花木兰"
        elif word == "乔妹":
            rword = "小乔"
        else:
            rword = word
        counts[rword] = counts.get(rword, 0) + 1  # 若字典中没有则创建键值对，有则在原有值上加1

    for word in excludes:
        del counts[word]  # 删除非人名高频词

    items = list(counts.items())  # 将无序的字典类型转换为可排序的列表类型
    items.sort(key=lambda x: x[1], reverse=True)  # 以第二列值，从大到小进行排序
    for i in range(20):
        word, count = items[i]

        print("{0:<10}{1:>5}".format(word, count))  # 格式化输出前20个高频出现人物
    return items


def get_count(string):
    # 词频统计
    word_counts = collections.Counter(string) # 对分词做词频统计
    word_counts_top20 = word_counts.most_common(100) # 获取前20最高频的词
    print (word_counts_top20) # 输出检查
    return word_counts

def draw_cloud(word_counts): # 词频展示
    mask = np.array(Image.open('wordcloud.jpg')) # 定义词频背景
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simhei.ttf', # 设置字体格式
        mask=mask, # 设置背景图
        background_color='white',
        max_words=250, # 最多显示词数
    )

    wc.generate_from_frequencies(word_counts) # 从字典生成词云
    plt.imshow(wc) # 显示词云
    plt.axis('off') # 关闭坐标轴
    plt.show() # 显示图像


def draw_from_dict(items):
    items=dict(items)
    x_label = list(items.keys())[:20]#取前20个
    #print(x_label)
    x = np.arange(len(x_label))  # 确定柱状图数量,可以认为是x方向刻度
    y = list(items.values())[:20] # y方向刻度
    #print(y)


    color = ['blue']
    plt.figure(figsize=(15, 5), dpi=80)
    plt.rcParams["font.sans-serif"] = ['SimHei']#载入中文
    plt.xticks(x, x_label)  # 绘制x刻度标签

    plt.bar(x, y, color=color, width=0.7)  # 绘制y刻度标签
    plt.grid(True, linestyle=':', color='r', alpha=0.6)# 设置网格刻度

    plt.title("王者荣耀20年周年庆英雄热度")
    plt.xlabel("英雄")
    plt.ylabel("热度")

    plt.show()

def main():
    string = get_string()
    word_counts = get_count(string)
    items = get_people_count(string)
    x = '0'
    while x != '3':
        x = input('请输入:\n1（查看云图）\n2（查看柱状图）\n3(退出）')
        if x == '1':
            draw_cloud(word_counts)
        elif x == '2':
            draw_from_dict(items)
        else:
            print('请重新输入')


if __name__ == '__main__':
    main()
