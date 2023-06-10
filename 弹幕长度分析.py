# 分析弹幕长度，一键查询王者玩家精神状态
# 根据统计结果，很大一部分弹幕为超长弹幕，即发疯弹幕，玩家精神状况可观

import matplotlib.pyplot as plt  # 图像展示库

counts = {}  # 创建一个空字典
arr = []
words = []
result = [0, '']
with open('B站弹幕.txt', 'r', encoding="utf-8") as fp:
    for line in fp:
        t = len(line)
        if t > result[0]:
            result = [t, line]

        if t < 6:
            t = '1-5'
        elif t < 11:
            t = '6-10'
        elif t < 16:
            t = '11-15'
        elif t < 21:
            t = '16-20'
        elif t < 41:
            t = '21-40'
        else:
            t = '40+'
        counts[t] = counts.get(t, 0) + 1

items = list(counts.items())  # 将无序的字典类型转换为可排序的列表类型
items.sort(key=lambda x: x[1], reverse=True)  # 以第二列值，从大到小进行排序
for i in range(len(items)):
    word, count = items[i]
    words.append(word)
    arr.append(count)
    # print(arr)
    print("{0:<10}{1:>5}".format(word, count))

print('最长弹幕长度及内容：\n', result)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False  # 解决中文显示问题

plt.pie(arr, labels=words, autopct='%3.1f%%')  # 以弹幕长度为标签，总计成交笔数为数据绘制饼图，并显示3位整数一位小数
plt.title('弹幕长度')  # 加标题
plt.show()
