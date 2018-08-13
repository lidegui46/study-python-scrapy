# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from python_config_spider_rule.items import MoiveItem, EducationItem, DocumentItem

"""
    注：爬取“多个网页”数据继承父类“CrawlSpider”,解析器按指定的rule设定
"""


class TudouMovieMultipleSpider(CrawlSpider):
    name = 'tudou_moive_multiple'
    allowed_domains = ['new.tudou.com']
    start_urls = [
        'http://new.tudou.com/category/c_100.html',  # 电影
        'http://new.tudou.com/category/c_87.html',  # 教育
        'http://new.tudou.com/category/c_84.html',  # 纪实
    ]
    rules = [
        Rule(LinkExtractor(allow=("/category/c_100.*.html$")), callback='parse_category_moive', follow=True),  # 电影
        Rule(LinkExtractor(allow=("/category/c_87.*.html$")), callback='parse_category_education', follow=True),  # 教育
        Rule(LinkExtractor(allow=("/category/c_84.*.html$")), callback='parse_category_documentary', follow=True),  # 纪实
    ]

    # 【电影】 单条返回，管道是一条一条的接收
    def parse_category_moive(self, response):
        print("--------------------------------------- parse_category_moive multile begin -------------------------------")
        doc = response.xpath('//div[@class="td-col"]')
        sel = Selector(response)
        for x in doc:
            item = MoiveItem.MoiveItem()
            item["title"] = x.css('div a.v-meta__title__link::text').extract_first()
            item["subtitle"] = x.css('div.v-meta__subtitle::text').extract_first()
            item["playNum"] = x.css('span.v-num::text').extract_first()

            # 获取dom标签的属性
            # item["playUrl"] = x.css('a.v-thumb__link').xpath('@href').extract_first()
            item["playUrl"] = x.css('a.v-thumb__link::attr(href)').extract_first()
            yield item

    # 【教育】 单条返回，管道是一条一条的接收
    def parse_category_education(self, response):
        print("--------------------------------------- parse_category_education multile begin -------------------------------")
        doc = response.xpath('//div[@class="td-col"]')
        sel = Selector(response)
        for x in doc:
            item = EducationItem.EducationItem()
            item["title"] = x.css('div a.v-meta__title__link::text').extract_first()
            item["subtitle"] = x.css('div.v-meta__subtitle::text').extract_first()
            item["playNum"] = x.css('span.v-num::text').extract_first()

            # 获取dom标签的属性
            # item["playUrl"] = x.css('a.v-thumb__link').xpath('@href').extract_first()
            item["playUrl"] = x.css('a.v-thumb__link::attr(href)').extract_first()
            yield item

    # 【纪实】 单条返回，管道是一条一条的接收
    def parse_category_documentary(self, response):
        print("--------------------------------------- parse_category_documentary multile begin -------------------------------")
        doc = response.xpath('//div[@class="td-col"]')
        sel = Selector(response)
        for x in doc:
            item = DocumentItem.DocumentItem()
            item["title"] = x.css('div a.v-meta__title__link::text').extract_first()
            item["subtitle"] = x.css('div.v-meta__subtitle::text').extract_first()
            item["playNum"] = x.css('span.v-num::text').extract_first()

            # 获取dom标签的属性
            # item["playUrl"] = x.css('a.v-thumb__link').xpath('@href').extract_first()
            item["playUrl"] = x.css('a.v-thumb__link::attr(href)').extract_first()
            yield item
