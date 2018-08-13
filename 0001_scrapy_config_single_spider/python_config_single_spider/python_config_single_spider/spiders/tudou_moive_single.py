# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from python_config_single_spider.items.MovieItem import MoiveItem

"""
注：爬取“单个网页”数据继承父类“scrapy.Spider”,默认解析器“parse”
"""
class TudouMovieSpider(scrapy.Spider):
    name = 'tudou_moive_single'
    allowed_domains = ['new.tudou.com']
    start_urls = [
        'http://new.tudou.com/category/c_100.html',  # 电影
    ]

    # 多条一起返回，但管道是一条一条的接收
    # def parse(self, response):
    # doc = response.xpath('//div[@class="td-col"]')
    # sel = Selector(response)
    # items = []
    # for x in doc:
    #     item = StudypythonItem()
    #     item["title"] = x.css('div a.v-meta__title__link::text').extract_first()
    #     item["subtitle"] = x.css('div.v-meta__subtitle::text').extract_first()
    #     items.append( item)
    # return items

    # 【电影】 单条返回，管道是一条一条的接收
    def parse(self, response):
        doc = response.xpath('//div[@class="td-col"]')
        sel = Selector(response)
        for x in doc:
            print("--------------------------------------- tudou_moive_single begin -------------------------------")
            item = MoiveItem()
            item["title"] = x.css('div a.v-meta__title__link::text').extract_first()
            item["subtitle"] = x.css('div.v-meta__subtitle::text').extract_first()
            item["playNum"] = x.css('span.v-num::text').extract_first()

            # 获取dom标签的属性
            # item["playUrl"] = x.css('a.v-thumb__link').xpath('@href').extract_first()
            item["playUrl"] = x.css('a.v-thumb__link::attr(href)').extract_first()
            yield item
