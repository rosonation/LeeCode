import json
import os
import time
import requests
import plotly.express as px
import pandas as pd
from openpyxl import Workbook


def get_tp_data(year, code):
    tim = int(time.time())
    url = f'https://d1.weather.com.cn/typhoon/typhoon_data/{year}/{code}.json?callback=getData&_={tim}'
    print('url:\n', url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print('r-------------:\n', r.text)
    datas = json.loads(r.text[8:-1])  # delete 'getData('[8] and ')'[-1]
    # print('datas--------------:\n', datas)
    tp_name = datas['typhoon'][2]  # 台风名字黄蜂
    detail_datas = datas['typhoon'][8]
    print('detail_datas:----------\n', detail_datas)
    # 台风信息
    allinfo = []
    for data in detail_datas:
        # 时间
        tp_time = data[1]
        # 经度
        tp_lon = data[4]
        # 纬度
        tp_lat = data[5]
        # 中心气压
        central_pressure = data[6]
        # 风速
        tp_speed = data[7]
        # 移向
        tp_direction = data[8]
        # 去除台风登陆时的空行
        if tp_direction is None:
            continue
        # 移速
        move_speed = data[9]
        tp_info = [f'{code}-' + tp_name, tp_time, tp_lon, tp_lat, central_pressure, tp_speed, tp_direction, move_speed]
        allinfo.append(tp_info)
    print(str(year1) + '_' + str(code1) + '_' + tp_name + '_轨迹数据')
    insert2excel(file_path + str(year1) + '_' + str(code1) + '_' + tp_name + '_轨迹数据', allinfo)
    print('allinfo:---------\n', allinfo)


def insert2excel(filepath, allinfos):
    try:
        # 表头
        table_title = ['名称', '时间', '经度', '纬度', '中心气压(hPa)', '风速(m/s)', '移向', '移速(m/s)']
        wb = Workbook()
        ws = wb.active
        ws.title = '台风'
        ws.append(table_title)
        for info in allinfos:
            ws.append(info)
        wb.save(filepath)
        return True
    except():
        return False


def trace_point_shows(filenames):
    # df = pd.DataFrame()
    lsts = []
    for filename in filenames:
        df0 = pd.read_excel(filename)
        lsts.append(df0)
    df = pd.concat(lsts)
    token = 'pk.eyJ1Ijoicm9zb25hdGlvbiIsImEiOiJja3FzZHVvaWIxeWVpMnZsMTA1dG50ajBzIn0.PAqISsqIQAGYNPIB2-SS6w'
    fig = px.scatter_mapbox(df,
                            hover_data=['时间'],
                            lon='经度',
                            lat='纬度',
                            color='风速(m/s)',
                            hover_name='名称',
                            size_max=14,
                            color_continuous_scale=px.colors.carto.Temps
                            )
    fig.update_layout(mapbox={'accesstoken': token,  # 官网注册token
                              'center': {'lon': 121.54, 'lat': 25.00},  # 地图中心
                              'zoom': 8,
                              'style': 'dark',  # 显示地图类型
                              },
                      margin={'l': 1, 'r': 1, 't': 1, 'b': 1})  # 地图边界
    fig.write_html('/Users/tony/Tony/trace_point_shows.html')


if __name__ == '__main__':
    year1 = 2020
    file_path = '/Users/tony/Tony/'
    for code1 in range(2001, 2011):
        get_tp_data(year1, code1)
    filenames1 = []
    for root, dirs, files in os.walk(file_path):
        for name in files:
            if name.startswith("2020_20"):
                filenames1.append(f'{root}/{name}')
    print("filenames:--------", filenames1)
    trace_point_shows(filenames1)
