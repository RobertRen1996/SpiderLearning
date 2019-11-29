# -*- coding: utf-8 -*-
import scrapy

# 创建爬虫类，并且继承自scrapy.Spider --> 最基础的类
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'   # 爬虫名字 --> 必须唯一
    allowed_domains = ['xicidaili.com']   # 允许采集的网站
    start_urls = ['https://www.xicidaili.com']  # 开始采集的网站

    # 解析响应数据，提取数据，或者网址，response 就是网页源码
    def parse(self, response):

        # 提取数据

