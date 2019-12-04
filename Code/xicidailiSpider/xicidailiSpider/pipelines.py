# -*- coding: utf-8 -*-

import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 为了让item在不同pipeline中都可以使用 ，所以必须返回item
class XicidailispiderPipeline(object):

    def process_item(self, item, spider):
        # print(item)
        # # item["hello"] = "world"
        for key, value in item.items():
            print(value)
            # print(key)
            # print(value)
            # print('{key}:{value}'.format(key=key, value=value))
        return item



# class XicidailispiderPipeline1(object):
#     def process_item(self, item, spider):
#         print(item)
#         return item


