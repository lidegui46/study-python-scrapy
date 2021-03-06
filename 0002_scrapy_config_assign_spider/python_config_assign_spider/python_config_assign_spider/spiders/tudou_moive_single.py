# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from python_config_assign_spider.items.MovieItem import MoiveItem

"""
注：爬取“单个网页”数据继承父类“scrapy.Spider”,默认解析器“parse”
"""
class TudouMovieSingleSpider(scrapy.Spider):
    name = 'tudou_moive_single'
    allowed_domains = ['new.tudou.com']
    start_urls = [
        'http://new.tudou.com/category/c_100.html',  # 电影
    ]

    def parse(self, response):
        doc = response.xpath('//div[@class="td-col"]')
        sel = Selector(response)
        for x in doc:
            item = MoiveItem()
            item["title"] = x.css('div a.v-meta__title__link::text').extract_first()
            item["subtitle"] = x.css('div.v-meta__subtitle::text').extract_first()
            item["playNum"] = x.css('span.v-num::text').extract_first()

            # 获取dom标签的属性
            # item["playUrl"] = x.css('a.v-thumb__link').xpath('@href').extract_first()
            item["playUrl"] = x.css('a.v-thumb__link::attr(href)').extract_first()
            yield item
