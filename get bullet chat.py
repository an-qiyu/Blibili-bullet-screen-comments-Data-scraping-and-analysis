# 获取B站指定的某视频某月的弹幕数据并存入TXT中
# 一次性爬取多页弹幕数据

import requests
import re


def get_response(html_url):
    headers = {
        # 身份
        'cookie': 'buvid3=82D82C78-6039-4E92-8744-77F3AE705B83167636infoc; b_nut=1642417589; LIVE_BUVID=AUTO4716424175997615; buvid_fp_plain=undefined; i-wanna-go-back=-1; DedeUserID=288162291; DedeUserID__ckMd5=e3f1432cd698ae8d; buvid4=2FA11B75-0C58-1530-13AB-839FE8C481E112797-022022519-551X6fL2lCne9Lftq0DAzw%3D%3D; blackside_state=0; CURRENT_BLACKGAP=0; is-2022-channel=1; CURRENT_FNVAL=4048; rpdid=0zbfVH9cu4|2DNcPYkH|3N3|3w1OZDq5; hit-new-style-dyn=0; hit-dyn-v2=1; b_ut=5; _uuid=DC1E5655-EE25-AFEC-5CBF-3D6B39551E8D59684infoc; header_theme_version=CLOSE; CURRENT_PID=b6e74de0-cee8-11ed-b05e-c5636cbe371d; FEED_LIVE_VERSION=V8; nostalgia_conf=-1; CURRENT_QUALITY=64; fingerprint=6d5c1de1aeae68a36736225dad6f0c53; buvid_fp=6d5c1de1aeae68a36736225dad6f0c53; home_feed_column=5; browser_resolution=1482-791; bp_video_offset_288162291=801079055293087700; PVID=2; b_lsid=C9B34477_1887C133989; SESSDATA=f88c70af%2C1701260817%2Cd5494%2A62; bili_jct=c252b9a8910baaecb64b252ab3c82131; sid=7cgaqqei',
        # 登录界面
        'origin': 'https://www.bilibili.com',
        # 目标视频
        'referer': 'https://www.bilibili.com/video/BV1ok4y1r7Cq',
        # 请求头
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
        with open('B站弹幕.txt', mode='a', encoding='utf-8') as f:
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
