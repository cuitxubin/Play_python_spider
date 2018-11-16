# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import json
import math
from scrapy_music.items import ScrapyMusicItem
from scrapy.spider import Spider

class QQMusic(Spider):
    name = 'QQMusic'
    allowed_domains = ['qq.com']
    # start_urls是歌手列表URL，并使用%s设置可控变量
    start_urls = [
        'https://c.y.qq.com/v8/fcg-bin/v8.fcg?channel=singer&page=list&key=all_all_%s&pagesize=100&pagenum=%s&loginUin=0&hostUin=0&format=jsonp'
    ]

    # 重写start_requests，遍历歌手字母分类A-Z
    def start_requests(self):
        for i in range(65, 66):
            key = chr(i)
            url = self.start_urls[0] %(key, 1)
            yield scrapy.Request(url, dont_filter=True, callback=self.get_genre_singer, meta={'key': key})

    # 获取每个字母分类下的每页歌手
    def get_genre_singer(self, response):
        # 通过参数传递获取字母
        key = response.meta['key']
        # 从函数start_requests得出响应内容，获取总页数
        pagenum = json.loads(str(response.body.decode('utf-8')))['data']['total_page']
        # 生成列表
        page_list = [x for x in range(pagenum)]
        for p in page_list[0:1]:
            url = self.start_urls[0] % (key, p+1)
            # dont_filter取消重复请求。
            yield scrapy.Request(url, dont_filter=True, callback=self.get_singer_songs)

    # 获取每一个歌手信息
    def get_singer_songs(self, response):
        # 获取每个字母分类下的每页歌手的全部信息
        singermid_list = json.loads(response.body.decode('utf-8'))['data']['list']
        for k in singermid_list[0:2]:
            url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?loginUin=0&hostUin=0&singermid=%s' \
                  '&order=listen&begin=0&num=30&songstatus=1' % (k['Fsinger_mid'])
            yield scrapy.Request(url, dont_filter=True, callback=self.get_singer_info, meta={'singermid': k['Fsinger_mid']})

    # 获取歌手的每一页歌曲
    def get_singer_info(self, response):
        # 参数传递获取singermid
        singermid = response.meta['singermid']
        # 获取歌手的名字，总页数
        singer_info = json.loads(response.body.decode('utf-8'))
        song_singer = singer_info['data']['singer_name']
        songcount = singer_info['data']['total']
        pagecount = math.ceil(int(songcount) / 30)
        for p in range(1):
            url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_singer_track_cp.fcg?loginUin=0&hostUin=0&singermid=%s' \
                  '&order=listen&begin=%s&num=30&songstatus=1' % (singermid, p * 30)
            yield scrapy.Request(url, dont_filter=True, callback=self.get_song_info, meta={'song_singer': song_singer})

    # 获取每一页的每一首歌曲信息
    def get_song_info(self, response):
        # 参数传递获取歌手名字
        song_singer = response.meta['song_singer']
        music_data = json.loads(response.body.decode('utf-8'))['data']['list']
        for i in music_data:
            # 设置请求参数
            filename = 'C400' + i['musicData']['songmid']
            # 获取下载歌曲的vkey
            url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?loginUin=0&hostUin=0' \
                  '&cid=205361747&uin=0&songmid=%s&filename=%s.m4a&guid=0' % (i['musicData']['songmid'], filename)
            yield scrapy.Request(url, dont_filter=True, callback=self.get_data, meta={'filename': filename, 'i': i, 'song_singer': song_singer})

    # 每一首歌曲信息
    def get_data(self, response):
        # 参数传递
        # song_singer为歌手名字
        # filename为请求参数
        # i为歌曲信息
        song_singer = response.meta['song_singer']
        filename = response.meta['filename']
        i = response.meta['i']
        # items.py文件的类的实例化，用于传递数据给pipelines.py实现存储
        items = ScrapyMusicItem()
        # 获取下载歌曲的vkey
        vkey = json.loads(response.body.decode('utf-8'))['data']['items'][0]['vkey']
        # 数据写入items，用于传递数据给pipelines.py实现存储
        items['song_url'] = 'http://dl.stream.qqmusic.qq.com/%s.m4a?vkey=%s&guid=0&uin=0&fromtag=66' % (
            filename, vkey)
        items['song_singer'] = song_singer
        items['song_name'] = i['musicData']['songname']
        items['song_ablum'] = i['musicData']['albumname']
        items['song_interval'] = i['musicData']['interval']
        items['song_songmid'] = i['musicData']['songmid']
        yield items
