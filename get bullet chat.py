import requests
import re


def get_response(url):
    headers = {
        # 身份
        'cookie': 'buvid3=82D82C78-6039-4E92-8744-77F3AE705B83167636infoc; b_nut=1642417589; LIVE_BUVID=AUTO4716424175997615; buvid_fp_plain=undefined; i-wanna-go-back=-1; DedeUserID=288162291; DedeUserID__ckMd5=e3f1432cd698ae8d; buvid4=2FA11B75-0C58-1530-13AB-839FE8C481E112797-022022519-551X6fL2lCne9Lftq0DAzw%3D%3D; blackside_state=0; CURRENT_BLACKGAP=0; is-2022-channel=1; CURRENT_FNVAL=4048; rpdid=0zbfVH9cu4|2DNcPYkH|3N3|3w1OZDq5; hit-new-style-dyn=0; hit-dyn-v2=1; b_ut=5; _uuid=DC1E5655-EE25-AFEC-5CBF-3D6B39551E8D59684infoc; header_theme_version=CLOSE; CURRENT_PID=b6e74de0-cee8-11ed-b05e-c5636cbe371d; FEED_LIVE_VERSION=V8; nostalgia_conf=-1; CURRENT_QUALITY=64; fingerprint=6d5c1de1aeae68a36736225dad6f0c53; buvid_fp=6d5c1de1aeae68a36736225dad6f0c53; home_feed_column=5; b_lsid=6A839A5F_188671458F7; browser_resolution=1482-791; SESSDATA=29a26a08%2C1700908569%2C24f1b%2A52; bili_jct=cc9c1d290701690f628eb99b84978676; sid=6szmjf0o; bp_video_offset_288162291=801079055293087700; PVID=2',
        # 登录界面
        'origin': 'https://www.bilibili.com',
        # 目标视频
        'referer': 'https://www.bilibili.com/video/BV1eo4y1G7iJ',
        # 请求头
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
    }
    response = requests.get(url=url, headers=headers)
    return response



def save(content):#保存弹幕数据
    for i in content:
        with open('bullet chat.txt', mode='a', encoding='utf-8') as f:
            f.write(i)
            f.write('\n')
            print(i)


def main(url):#运行
    html_data = get_response(url).text
    result = re.findall("[\u4E00-\u9FA5]+", html_data)#获取数据进行正则表达匹配，排除乱码
    # [\u4e00-\u9fa5]+ 提取中文词
    # [\u4e00-\u9fa5] 提取中文字
    save(result)


if __name__ == '__main__':
    #下载地址（弹幕信息文件地址）
    url = 'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid=1139019885&pid=398903694&segment_index=1&pull_mode=1&ps=120000&pe=360000'#b站api
    main(url)
