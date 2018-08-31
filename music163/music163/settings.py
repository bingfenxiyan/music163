# -*- coding: utf-8 -*-

# Scrapy settings for music163 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'music163'

SPIDER_MODULES = ['music163.spiders']
NEWSPIDER_MODULE = 'music163.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'music163 (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'iuqxldmzr_=32; _ntes_nnid=be765bd0e57aeb4c38d79e8fc3343f30,1534927931146; _ntes_nuid=be765bd0e57aeb4c38d79e8fc3343f30; __utma=94650624.1573893119.1534927931.1534927931.1534927931.1; __utmc=94650624; __utmz=94650624.1534927931.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=de4NZ5npCUco%2B%2BtoQi35f0QPluGl4Wm1BuUGMGrDk3aqZ1pgQUPIM8EsiLajCrKqbn8sGBxth4PI%2Fkhx%2BUgtdK5O8mx%2FRhaOXby3C3dovL%2FRdJSlcW4Zr7%2B8Ug%2Be0AdAZFg%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed6d443baece1abca5991eca6d2b544f7b48ea3cc3a8be7feb6f76bf4aa9caed02af0fea7c3b92aa8bbfcafd93faeb08db6e265e9f5bc90d463f1ebaad1d45cb0ab898db75dafef8e96d84d8f99bea5ea39a3af96d2f36d938ba0aad03487ada7ade46281ae8592e166fcad89a3fb80aceca0aaae61aca8e5b6e680a895fbb0bb67bcf19e89e4459cbeb7d4c239a8b1baadae5aa8969d8de25df886bed8aa3497b9e586b34ba89f96a7e637e2a3; WM_TID=Db21fFJEoII%2FxGnJ%2BzZI0Io0fW538tql; JSESSIONID-WYYY=EwZdrncFl6TybF4jFkeJ0anOPMurp1I7daW%2FGmXtlAzBnWhx693%5Cek3MQNcMNG82aT4HqtlFcNFxmcpGqkb%2Fe9Zq3FWUX5%2FUceTRG8MSMZkYDhw4%2B24%5CIbBwxm0uzNZNY3wTpzo3X%2BQYIuTMlPklCDDG4vkECU2IRPYPF7kU4GhnbWdx%3A1534931472043; playerid=80967244; __utmb=94650624.34.10.1534927931',
    'Host':'music.163.com',
    'Referer': 'https://music.163.com/',
    'Upgrade-Insecure-Requests': 1,
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'music163.middlewares.Music163SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'music163.middlewares.Music163DownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'music163.pipelines.Music163Pipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MAX_COUNT = 20


MONGO_URL = 'localhost'
MONGO_PORT = 27017
MONGO_DB = 'test'

