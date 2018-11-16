# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyMusicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_name = scrapy.Field()
    song_ablum = scrapy.Field()
    song_interval = scrapy.Field()
    song_songmid = scrapy.Field()
    song_singer = scrapy.Field()
    song_url = scrapy.Field()
    pass
