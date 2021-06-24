import urllib.parse
import requests
# from pyquery import PyQuery as pq
from urllib.parse import urlencode
from urllib.parse import urlparse
import re

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
#     'referer': 'https://so.toutiao.com/search?keyword=%E8%A1%97%E6%8B%8D&pd=synthesis&source=search_subtab_switch&dvpf=pc&aid=4916&page_num=0',
#     # 'cookie': 'tt_webid=6970268611437856264; _S_DPR=1; _S_IPAD=0; MONITOR_WEB_ID=6970268611437856264; ttwid=1%7CobYZC0vIyDzWzgZETeBnLXiczCSfyj93HRpnKzDmjv0%7C1623254627%7C0320a1f1cb08676972a90f718fbd310044d6554255abcf4aa2e226f2262a7a9f; _S_WIN_WH=171_657',
# }


# 获取首页
def get_page(page_num):
    global headers
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'  # ,
        # 'Content-Type': 'application/json; charset=utf-8'
    }
    datas = {
        'keyword': '街拍',
        'pd': 'atlas',
        'dvpf': 'pc',
        'aid': 4916,
        'page_num': page_num,
        'search_json': '%22from_search_id%22:%22202106241923590101501370353E40FD0C%22',
        # 'img_url': 'https://sf3-ttcdn-tos.pstatp.com/obj/pgc-image/1532670355471e9914cbbbb'
        # 'rawJSON': 1,
        # 'search_id': '202106100004290101500200495C05B763'
    }
    # datas = urllib.parse.urlencode(datas).encode('utf-8')
    keyword = urllib.parse.unquote('%E8%A1%97%E6%8B%8D')
    print('keyword', keyword)
    data = urlencode(datas)
    print('data', data)
    img_url = urllib.parse.unquote('https://so.toutiao.com/search?keyword=街拍&pd=atlas&dvpf=pc&aid=4916&page_num=0&search_json=%7B%22from_search_id%22%3A%22202106240206490101501390122038F5E6%22%2C%22origin_keyword%22%3A%22街拍%22%2C%22image_keyword%22%3A%22街拍%22%7D&image_keyword=街拍&image=https%3A%2F%2Fsf3-ttcdn-tos.pstatp.com%2Fobj%2Fpgc-image%2F8dfc137f846a46618afbf6654bec70a3')
    img_http = img_url.split('=')[8]
    try:
        response = requests.get(img_http, headers=headers)
    #     print("hello world.")
        print(response.status_code)
        if response.status_code == 200:
            print('json', response.text)
            return response.json()
    except requests.ConnectionError:
        return None


# 获取图片链接
def get_images(json):
    images = json.get('rawData').get('data')
    for image in images:
        link = image.get('img_url')
        yield link


# 下载图片
name = 1


def saving_img(link):
    global name
    print(f'-------正在打印第{name}张图片')
    data = requests.get(link, headers=headers).content
    with open(f'/Users/tony/Tony/image1/{name}.jpg', 'wb') as f:
        f.write(data)
        name += 1


def main(paga_num):
    json = get_page(paga_num)
    for link in get_images(json):
        saving_img(link)


if __name__ == '__main__':
    for i in range(0, 2):
        main(i)
