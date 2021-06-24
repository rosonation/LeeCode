import re

import jieba as jieba
import requests

param = {
    'id': 4650286486390483,
    'mid': 4650286486390483,
    'max_id_type': 0
}

headers = {
    # 'cookie': 'XSRF-TOKEN=a102b3; MLOGIN=0; M_WEIBOCN_PARAMS=uicode%3D20000061%26fid%3D4648381753067388%26oid%3D4648381753067388; WEIBOCN_FROM=1110006030; _T_WM=41346683383',
    'referer': 'https://m.weibo.cn/detail/4650286486390483/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
}

url = 'https://m.weibo.cn/comments/hotflow?id=4650286486390483&mid=4650286486390483&max_id_type=0'
resp = requests.get(url, headers=headers, params=param)
comments = resp.json()
print('Comments', comments)
print('response:', resp.status_code)

max_id = comments['data']['max_id']
wb_info = comments['data']['data']
nums = 0
for item in wb_info:
    nums += 1
    user_id = item.get('user')['id']  # 用户id
    author = item['user']['screen_name']  # 作者名称
    auth_sign = item['user']['description']  # 作者座右铭
    time = str(item['created_at']).split(' ')[1:4]
    rls_time = '-'.join(time)  # 发帖时间
    text = ''.join(re.findall('[\u4e00-\u9fa5]', item['text']))  # 发帖内容
    # print(max_id, user_id, author, auth_sign, rls_time, text)
    print(nums, ':', text)


# 爬虫可视化分析
def cut_word():
    with open('/Users/tony/Tony/打针.csv', encoding='utf-8') as file:
        comment_text = file.read()
        wordlist = jieba.lcut_for_search(comment_text)
        new_wordlist = ' '.join(wordlist)
        return new_wordlist


def create_word_cloud():
    mask = imread('zhen.jpg')
    wordcloud = WordCloud(font_path='msyh.ttc', mask=mask).generate(cut_word())
    wordcloud.to_file('zhen1.jpg')
    print('绘图成功！')
