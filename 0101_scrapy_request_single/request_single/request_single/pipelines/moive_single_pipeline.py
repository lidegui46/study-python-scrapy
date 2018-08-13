# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from request_single.utils import fileUtil
from scrapy.exceptions import DropItem

class MoiveSinglePipeline(object):
    def __init__(self):
        self.jsonFileUtil = fileUtil.fileUtil()
        # 怎么放到指定的文件夹下？
        self.jsonFileUtil.open_file('tudou_moive.json')

    # def from_crawler(cls, crawler):
    #     # 通过配置来实例化“SinglePpipeline”，如果有多个参数，cls()中应该带入参数
    #     return cls(crawler)
    #     pass

    def open_spider(self, spider):
        # print("打开爬虫了")
        print("spider pipeLine single...................................")
        pass

    # 处理结束后关闭 文件 IO 流
    def close_spider(self, spider):
        self.jsonFileUtil.close_file()
        print("spider closed ..............................")

    def process_item(self, item, spider):
        try:
            # title = item["title"]
            # subtitle = item["subtitle"]
            # playUrl = item["playUrl"]
            # print(title + "______" + subtitle + "____________" + playUrl)
            # return item

            # 写入文件
            self.jsonFileUtil.write_to_Json(item)
            return item
        except Exception as ex:
            # 丢弃当前 item
            raise DropItem("Missing price in %s" % item)
