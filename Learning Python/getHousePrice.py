from fake_useragent import UserAgent
import csv
import re
import time
from parsel import Selector
import httpx
import asyncio


class HomeLinkSpider(object):
    def __init__(self):
        self.ua = UserAgent()
        self.headers = {"User-Agent": self.ua.random}
        self.data = list()
        self.path = "/Users/tony/Tony/浦东_三房_500_800万.csv"
        self.url = "https://sh.lianjia.com/ershoufang/pudong/a3p5/"

    def get_max_page(self):
        response = httpx.get(self.url, headers=self.headers)
        if response.status_code == 200:
            # 创建Selector类实例
            selector = Selector(response.text)
            # 采用css选择器获取最大页码div Boxl
            a = selector.css('div[class="page-box house-lst-page-box"]')
            # 使用eval将page-data的json字符串转化为字典格式
            max_page = eval(a[0].xpath('//@page-data').get())["totalPage"]
            print("最大页码数:{}".format(max_page))
            return max_page
        else:
            print("请求失败 status:{}".format(response.status_code))
            return None

    # 异步 - 使用协程函数解析单页面，需传入单页面url地址
    async def parse_single_page(self, url):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            selector = Selector(response.text)
            ul = selector.css('ul.sellListContent')[0]
            li_list = ul.css('li')
            for li in li_list:
                detail = dict()
                detail['title'] = li.css('div.title a::text').get()

                #  2室1厅 | 74.14平米 | 南 | 精装 | 高楼层(共6层) | 1999年建 | 板楼
                house_info = li.css('div.houseInfo::text').get()
                house_info_list = house_info.split(" | ")

                detail['bedroom'] = house_info_list[0]
                detail['area'] = house_info_list[1]
                detail['direction'] = house_info_list[2]

                floor_pattern = re.compile(r'\d{1,2}')
                match1 = re.search(floor_pattern, house_info_list[4])  # 从字符串任意位置匹配
                if match1:
                    detail['floor'] = match1.group()
                else:
                    detail['floor'] = "未知"

                # 匹配年份
                year_pattern = re.compile(r'\d{4}')
                match2 = re.search(year_pattern, house_info_list[5])
                if match2:
                    detail['year'] = match2.group()
                else:
                    detail['year'] = "未知"

                # 文兰小区 - 塘桥    提取小区名和哈快
                position_info = li.css('div.positionInfo a::text').getall()
                detail['house'] = position_info[0]
                detail['location'] = position_info[1]

                # 650万，匹配650
                price_pattern = re.compile(r'\d+')
                total_price = li.css('div.totalPrice span::text').get()
                detail['total_price'] = re.search(price_pattern, total_price).group()

                # 单价64182元/平米， 匹配64182
                unit_price = li.css('div.unitPrice span::text').get()
                detail['unit_price'] = re.search(price_pattern, unit_price).group()

                self.data.append(detail)

    def parse_page(self):
        max_page = self.get_max_page()
        loop = asyncio.get_event_loop()

        # Python 3.6之前用ayncio.ensure_future或loop.create_task方法创建单个协程任务
        # Python 3.7以后可以用户asyncio.create_task方法创建单个协程任务
        tasks = []
        for i in range(1, max_page + 1):
            url = 'https://sh.lianjia.com/ershoufang/pudong/pg{}a3p5/'.format(i)
            tasks.append(self.parse_single_page(url))

        # 还可以使用asyncio.gather(*tasks)命令将多个协程任务加入到事件循环
        asyncio.create_task(asyncio.wait(tasks))
        loop.close()

    def write_csv_file(self):
        head = ["标题", "小区", "房厅", "面积", "朝向", "楼层",
                "年份", "位置", "总价(万)", "单价(元/平方米)"]
        keys = ["title", "house", "bedroom", "area", "direction",
                "floor", "year", "location",
                "total_price", "unit_price"]

        try:
            with open(self.path, 'w', newline='', encoding='utf_8_sig') as csv_file:
                writer = csv.writer(csv_file, dialect='excel')
                if head is not None:
                    writer.writerow(head)
                for item in self.data:
                    row_data = []
                    for k in keys:
                        row_data.append(item[k])
                    writer.writerow(row_data)
                print("Write a CSV file to path %s Successful." % self.path)
        except Exception as e:
            print("Fail to write CSV to path: %s, Case: %s" % (self.path, e))


if __name__ == '__main__':
    start = time.time()
    home_link_spider = HomeLinkSpider()
    home_link_spider.parse_page()
    home_link_spider.write_csv_file()
    end = time.time()
    print("耗时：{}秒".format(end - start))
