from scrapy.cmdline import execute

# 方式一：只会执行第一个execute spider
execute(['scrapy', 'crawl', 'tudou_moive_single'])