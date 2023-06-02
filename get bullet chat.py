
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
    }
    response = requests.get(url=html_url, headers=headers)
    return response

def get_date(html_url):
    response = get_response(html_url)
    json_data = response.json()
    date = json_data['data']
    print(date)
    return date


def save(content):#保存弹幕数据
    for i in content:
        with open('bullet chat.txt', mode='a', encoding='utf-8') as f:
            f.write(i)
            f.write('\n')
            print(i)


def main(html_url):
    data = get_date(html_url) #按照日期获得数据进行循环，可直接获得一月的弹幕数据
    for date in data:
        url = f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=185697359&date={date}'  # 弹幕地址
        html_data = get_response(url).text# 字符串形式获得内容
        result = re.findall("[\u4E00-\u9FA5]+", html_data)#获取数据进行正则表达匹配，排除乱码,存为list

    # [\u4e00-\u9fa5]+ 提取中文词
    # [\u4e00-\u9fa5] 提取中文字
        save(result)


if __name__ == '__main__':
    #下载地址（弹幕日期文件地址）
    date_url = 'https://api.bilibili.com/x/v2/dm/history/index?month=2020-05&type=1&oid=185697359'#日期地址
    main(date_url)

