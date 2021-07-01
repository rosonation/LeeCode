# -*- coding: utf_8 -*-
# @Time     :2021年6月28日
# @File     :getMaoyan.py


import requests
# from fake_useragent import UserAgent
from lxml import etree
import time
# 加载数据分析常用库
import pandas as pd
# import numpy as np
# import jieba
from wordcloud import WordCloud
# import matplotlib.pyplot as ply
from matplotlib import pyplot as plt
import sys

# get_ipython().run_line_magic('matplotlib', 'inline')

# 随机请求头
# ua = UserAgent(use_cache_server=False)

# 构建请求 需要自己去网页上换一下  请求不到了就  去网页刷新   把验证码弄了


headers = {
    'Accept': '*/*',
    'Cookie': '220437415.1624896754816.1624970679849.1624970686314.17',
    # 'User-Agent': ua.random
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
}


def requestsTools(url):
    """
    爬虫请求工具函数
    :param url: 请求地址
    :return: HTML对象 用于xpath提取
    """
    response = requests.get(url, headers=headers).content.decode('utf-8')
    html = etree.HTML(response)
    return html


def index(page):
    """
    首页函数
    :param page: 页数
    :return:
    """

    url = 'https://maoyan.com/board/4?offset={0}'.format(page)
    html = requestsTools(url)
    # 详情页地址后缀
    urls_text = html.xpath('//a[@class="image-link"]/@href')
    print('urls_text:', urls_text)
    # 评分
    score1 = html.xpath('//i[@class="integer"]/text()')  # 评分整数
    score2 = html.xpath('//i[@class="fraction"]/text()')  # 评分小数
    # print('score1:', score1, 'score2', score2)
    for m, p1, p2 in zip(urls_text, score1, score2):
        score = p1 + p2
        print('score:', score)
        urs = 'https://maoyan.com' + m
        # 避免请求过于频繁
        time.sleep(2)
        details(urs, score)


def details(url, score):
    html = requestsTools(url)
    film = html.xpath('//h1[@class="name"]/text()')  # 电影名称
    print('film:', film)
    film_type = html.xpath('//li[@class="ellipsis"]/a/text()')  # 类型
    print('file_type:', film_type)
    area = html.xpath('/html/body/div[3]/div/div[2]/div/ul/li[2]/text()')  # 读取总和
    print('area', area)
    timedata = html.xpath('/html/body/div[3]/div/div[2]/div/ul/li[3]/text()')  # 时间
    print('timedata', timedata)
    for d, l, b, t in zip(film, film_type, area, timedata):
        country = b.replace('\n', '').split('/')[0]  # 地区
        runtime = b.replace('\n', '').split('/')[1]  # 时长
        country = country.replace(',', '|')
        runtime = runtime.replace(',', '|')
        f = open('/Users/tony/Tony/猫眼.csv', 'a')
        f.write('{0}, {1}, {2}, {3}, {4}, {5}, {6}\n'.format(d.strip(), score.strip(), url.strip(), l.strip(),
                                                             country.strip(), runtime.strip(), t.strip()))
        print(d.strip().ljust(10), score.strip().ljust(3), url.strip().ljust(50), l.strip().ljust(10),
              country.strip().ljust(15), runtime.strip().ljust(6), t.strip().ljust(20))


# 清空文件内容，否则会重复写入
# with open('/Users/tony/Tony/猫眼.csv', 'w') as file:
#     file.truncate()
# for page1 in range(0, 10):
#     page1 *= 10
#     index(page1)


path = '/Users/tony/Tony/猫眼.csv'
dataFrame = pd.read_csv(path, sep=',', encoding='utf-8', index_col=False)
dataFrame.drop(dataFrame.columns[0], axis=1, inplace=True)  # 删除第一列columns[0], axis=1为列模式，0为行模式，inplace是否就地替换
dataFrame.dropna(inplace=True)  # 就地删除空行Na
dataFrame.drop_duplicates(inplace=True)  # 就地删除重复数据
dataFrame.head(10)  # 返回10行数据

# 查看数据结构
dataFrame.info()
print('Column:', dataFrame.columns)

# 年份&上映电影的数目  2018及以后的上映数目只是目前猫眼上公布的，具有不确定性，就先把2018及之后的剔除
fig, ax = plt.subplots(figsize=(9, 6), dpi=70)  # nrows : 行数  ncols: 列数 sharex: 是否共享x轴  sharey: 是否共享y轴
dataFrame[dataFrame[u'上映时间'] < 2018][u'上映时间'].value_counts().sort_index().plot(kind='line', ax=ax)
ax.set_xlabel(u'时间（年）')
ax.set_ylabel(u'上映数量')
ax.set_title(u'上映时间&上映的电影数目')

# 基于上图， 再弄一个上映时间&上映数量&评分的关系图
# 但是由于1980年以前的数据量较少，评分不准确，将主要的分析区域集中在1980-2017
x = dataFrame[dataFrame[u'上映时间'] < 2018][u'上映时间'].value_counts().sort_index().index
y = dataFrame[dataFrame[u'上映时间'] < 2018][u'上映时间'].value_counts().sort_index().values
y2 = dataFrame[dataFrame[u'上映时间'] < 2018].sort_values(by=u'上映时间').groupby(u'上映时间').mean()[u'评分'].values
fig, ax = plt.subplots(figsize=(10, 5), dpi=70)
ax.plot(x, y, label='上映数量')
ax.set_xlim(1980, 2017)
ax.set_xlabel(u'上映时间')
ax.set_ylabel(u'上映数量')
ax.set_title(u'时间&上映数量&评分均值')
ax2 = ax.twinx()
ax2.plot(x, y2, c='y', ls='--', label=u'评分')
ax.legend(loc=1)
ax2.legend(loc=2)


# 解决中文乱码， 坐标轴显示不出负值的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 世界&上映时间&均值评分
fig, ax = plt.subplots(figsize=(10, 7), dpi=60)
dataFrame[dataFrame[u'评分'] > 0].groupby(u'上映时间').mean()[u'评分'].plot(kind='line', ax=ax)
ax.set_ylabel(u'评分')
ax.set_title(u'世界&上映时间&均值评分')

# 世界各类型影片所占的数目
# 对类型进行切割成最小单位， 然后统计
types = []
for tp in dataFrame[u'类型']:
    ls = tp.split(',')
    for x in ls:
        types.append(x)

tp_df = pd.DataFrame({u'类型': types})
fig, ax = plt.subplots(figsize=(9, 6), dpi=60)
tp_df[u'类型'].value_counts().plot(kind='bar', ax=ax)
ax.set_xlabel(u'类型')
ax.set_ylabel(u'数量')
ax.set_title(u'世界&类型&数目')

# 影片时长与评分的分布
# 有个问题: 其实有一些影片未进行评分，在这里要将这些取缔
x = dataFrame[dataFrame[u'评分'] > 0].sort_values(by=u'时长(min)')[u'时长(min)'].values
y = dataFrame[dataFrame[u'评分'] > 0].sort_values(by=u'时长(min)')['评分'].values
fig, ax = plt.subplots(figsize=(9, 6), dpi=70)
ax.scatter(x, y, alpha=0.6, marker='o')
ax.set_xlabel(u'时长(min)')
ax.set_ylabel(u'数量')
ax.set_title(u'影片时长&评分分布图')
# 可以看出评分
plt.show()

i = 0
c0 = []
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []
c6 = []
c7 = []

for x in dataFrame[u'地区']:
    if u'中国大陆' in x:
        c0.append(dataFrame.iat[i, 0])
        c1.append(dataFrame.iat[i, 1])
        c2.append(dataFrame.iat[i, 2])
        c3.append(dataFrame.iat[i, 3])
        c4.append(dataFrame.iat[i, 4])
        c5.append(dataFrame.iat[i, 5])
        c6.append(dataFrame.iat[i, 6])
        c7.append(dataFrame.iat[i, 7])
    i += 1

china_df = pd.DataFrame(
    {u'电影': c0, u'评分': c1, u'链接': c2, u'类型': c3, u'地区': c4, u'上映地点': c5, u'时长(min)': c6, u'上映时间': c7})

# 中国&世界均值评分比较 时间范围在1980-2017
x1 = dataFrame[dataFrame[u'评分'] > 0].groupby(u'上映时间').mean()[u'评分'].index
y1 = dataFrame[dataFrame[u'评分'] > 0].groupby(u'上映时间').mean()[u'评分'].values

x2 = china_df[china_df[u'评分'] > 0].groupby(u'上映时间').mean()[u'评分'].index
y2 = china_df[china_df[u'评分'] > 0].groupby(u'上映时间').mean()[u'评分'].values
fig, ax = plt.subplots(figsize=(12, 9), dpi=60)
ax.plot(x1, y1, ls='-', c='DarkTurquoise', label=u'世界')
ax.plot(x2, y2, ls='--', c='Gold', label=u'中国')
ax.set_title(u'中国&世界均值评分')
ax.set_xlabel(u'时间')
ax.set_xlim(1980, 2017)
ax.set_ylabel(u'评分')
ax.legend()

# 类型上映数目  中国&世界对比
# 因为类型是混合的，为了方便统计 先写一个函数用来对类型进行分割


# 写分割的函数  传入一个Sreies 类型对象 返回一个类型分割的DataFrame
# 这里传入的是一个 类型的Series
def Cuttig_type(typeS):
    types2 = []
    types1 = []

    for x3 in typeS:
        if len(x3) < 4:
            # print x
            types1.append(x3)
        ls1 = x3.split(',')
        for i1 in ls1:
            types2.append(i1)

    types2.extend(types1)
    df = pd.DataFrame({u'类型': types2})
    return pd.DataFrame(df[u'类型'].value_counts().sort_values(ascending=False))


# 中国&世界影片类型比较
df1 = Cuttig_type(china_df[u'类型'])
df2 = Cuttig_type(dataFrame[u'类型'])
trans = pd.concat([df1, df2], axis=1)
trans.dropna(inplace=True)
trans.columns = [u'中国', u'世界']
fig, ax = plt.subplots(figsize=(15, 9), dpi=80)
trans.plot(kind='bar', ax=ax)
fig.autofmt_xdate(rotation=30)
ax.set_title(u'中国&世界类型对比图')
ax.set_xlabel(u'类型')
ax.set_ylabel(u'影片的数目')

# 然后就是散点分布了，中国&世界&时长&评分分布
y = dataFrame[dataFrame[u'评分'] > 0].sort_values(by=u'时长(min)')[u'评分'].values
x = dataFrame[dataFrame[u'评分'] > 0].sort_values(by=u'时长(min)')[u'时长(min)'].values
y2 = china_df[china_df[u'评分'] > 0].sort_values(by=u'时长(min)')[u'评分'].values
x2 = china_df[china_df[u'评分'] > 0].sort_values(by=u'时长(min)')[u'时长(min)'].values

fig, ax = plt.subplots(figsize=(10, 7), dpi=80)
ax.scatter(x, y, c='DeepSkyBlue', alpha=0.6, label=u'世界')
ax.scatter(x2, y2, c='Salmon', alpha=0.7, label=u'中国')
ax.set_title(u'中国&世界评分分布情况')
ax.set_xlabel(u'时长(min)')
ax.set_ylabel(u'评分')
ax.legend(loc=4)

dfs = dataFrame[(dataFrame[u'上映时间'] > 1980) & (dataFrame[u'上映时间'] < 2019)]

# for x in range(0,len(dfs)):
#     print(dfs.iat[x,0],dfs.iat[x,-1])

df666 = dfs['电影'][:15]

wl = ",".join(df666.values)
# 把分词后的txt写入文本文件
# fenciTxt  = open("fenciHou.txt","w+")
# fenciTxt.writelines(wl)
# fenciTxt.close()

# 设置词云l
wc = WordCloud(background_color="white",  # 设置背景颜色
               # mask=imread('shen.jpg'),   #设置背景图片
               #                    max_words=2000,  #设置最大显示的字数
               # font_path="C:\\Windows\\Fonts\\simkai.ttf",  # 设置为楷体 常规
               font_path="/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/matplotlib/mpl-data/fonts/ttf/SimHei.ttf",
               # 设置中文字体，使得词云可以显示（词云默认字体是“DroidSansMono.ttf字体库”，不支持中文）
               max_font_size=60,  # 设置字体最大值
               random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
               )
myword = wc.generate(wl)  # 生成词云
wc.to_file('result.jpg')

# 展示词云图
plt.imshow(myword)
plt.axis("off")
plt.show()
