# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from request_single.items.MovieItem import MoiveItem
# from scrapy.http.request import Request

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

"""
注：爬取“单个网页”数据继承父类“scrapy.Spider”,默认解析器“parse”
"""


class TudouMovieSpider(scrapy.Spider):
    name = 'tudou_moive_single'
    allowed_domains = ['new.tudou.com']
    start_urls = [
        'http://new.tudou.com/category/c_100.html',  # 电影
    ]

    def start_requests(self):
        return super().start_requests()

    # 【电影】 单条返回，管道是一条一条的接收
    def parse(self, response):
        for item in self.download_item(response):
            yield item
        for url in self.download_redirect(response):
            yield scrapy.Request(url=url, method='GET', callback=self.parse, errback=TudouMovieSpider, dont_filter=True)

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want to do something special for some errors,
        # you may need the failure's type:

        if failure.check(HttpError):
            # these exceptions come from HttpError spider middleware
            # you can get the non-200 response
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            # this is the original request
            request = failure.request
            self.logger.error('DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

    # 下载数据
    def download_item(self, response):
        doc = response.xpath('//div[@class="td-col"]')
        items = []
        for x in doc:
            item = MoiveItem()
            item["title"] = x.css('div a.v-meta__title__link::text').extract_first()
            item["subtitle"] = x.css('div.v-meta__subtitle::text').extract_first()
            item["playNum"] = x.css('span.v-num::text').extract_first()

            # 获取dom标签的属性
            # item["playUrl"] = x.css('a.v-thumb__link').xpath('@href').extract_first()
            item["playUrl"] = x.css('a.v-thumb__link::attr(href)').extract_first()
            items.append(item)
            # yield item

        return items

    # 跳转到下一页
    def download_redirect(self, response):
        sel = Selector(response)
        nextPageUrl = sel.css("ul.yk-pages li.next a").xpath("@href").extract_first()
        urls = []
        if nextPageUrl != None:
            if nextPageUrl.find(self.allowed_domains[0]) == -1:
                nextPageUrl = "http://" + self.allowed_domains[0] + nextPageUrl
            urls.append(nextPageUrl)
            # 请求下一页
            # yield scrapy.Request(url=nextPageUrl, method='GET', callback=self.parse, errback=TudouMovieSpider, dont_filter=True)
        else:
            print("没有下一页了")

        return urls
