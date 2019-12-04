# -*- coding: utf-8 -*-
import scrapy
from xicidailiSpider.items import  XicidailispiderItem
import pymysql
from scrapy.utils.project import get_project_settings
from dbhelper import *


# 创建爬虫类，并且继承自scrapy.Spider --> 最基础的类
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'   # 爬虫名字 --> 必须唯一
    allowed_domains = ['xicidaili.com']   # 允许采集的网站
    # start_urls = ['https://www.xicidaili.com']  # 开始采集的网站
    start_urls = ['https://www.xicidaili.com/nn']  # 开始采集的网站


    def __init__(self):
        settings = get_project_settings()
        if not is_exist_database(settings): # 如果不存在对应的数据库，需要新建
            print("没有对应的数据库，要新建")
            res = create_database(settings)
            if res:
                print("创建数据库成功")
            else:
                print("创建数据库失败, 请联系管理员")
                return

        if not is_exist_table(settings): # 如果不存在对应的表，需要新建
            print("没有对应的数据表，要新建")
            res = create_table(settings)
            if res:
                print("创建数据表成功")
            else:
                print("创建数据表失败, 请联系管理员")
                return

        print("可以添加数据啦")







        # pass


    # 解析响应数据，提取数据，或者网址，response 就是网页源码
    def parse(self, response):
        pass
        print(response)

        # 提取数据 xicidaili的数据
        selectors = response.xpath("//tr")
        for selector in selectors:
            # item ={}
            # item["IP"] = selector.xpath("./td[2]/text()").extract_first()
            # item["Port"] = selector.xpath("./td[3]/text()").extract_first()

            IP = selector.xpath("./td[2]/text()").extract_first()
            Port = selector.xpath("./td[3]/text()").extract_first()

            item = XicidailispiderItem(IP=IP, Port=Port)

            # yield dict,
            yield item







