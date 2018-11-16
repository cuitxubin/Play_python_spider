# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy_download.items import ScrapyDownloadItem
from scrapy.spider import Spider
# 导入setting.py配置信息
from scrapy.conf import settings
class downspider(Spider):
    name = "downspider"
    allowed_domains = []
    start_urls = [
       'http://ws.stream.qqmusic.qq.com/C100001IqoFr2rNsGH.m4a?fromtag=38'
       ]

    def parse(self, response):
        # 下载方法一
        f = open(settings['FILES_STORE']+'MySong.m4a', 'wb')
        f.write(response.body)
        f.close()
        # 下载方法二
        item = ScrapyDownloadItem()
        item['FileName'] = ['PythonBook.zip', 'Python.jpg', 'MyMusic.m4a']
        item['FileUrl'] = ['http://d.1.didiwl.com/PYTHON_zryycl.zip',
                           'http://i0.hdslb.com/bfs/archive/9a8f816fdadd1b814c5ce51e7ead25319166eb92.jpg',
                           'http://ws.stream.qqmusic.qq.com/C100001IqoFr2rNsGH.m4a?fromtag=38']
        return item