from scrapy.cmdline import execute

# 方式三：通过命令方式执行，详见：  https://www.cnblogs.com/lei0213/p/7900340.html
#     1、在spiders同级创建任意目录，如：commands
#     2、在“commands”文件夹下创建 crawlall.py 文件 （此处文件名就是自定义的命令）
#     3、在 “settings.py”配置文件增加“COMMANDS_MODULE = ‘项目名称.目录名称’”,如：“COMMANDS_MODULE = 'zhihuuser.commands'”。
#     4、执行命令“execute(['scrapy', 'crawlall'])”

execute(['scrapy', 'crawlall'])