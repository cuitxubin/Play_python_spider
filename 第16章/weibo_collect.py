from bs4 import BeautifulSoup
import re
import urllib
import csv
import requests
import time
import datetime
from concurrent.futures import ThreadPoolExecutor

# 多线程爬取视频文件
def thread_video(get_video_value, video_path):
    if get_video_value:
        url = str(get_video_value).split('video_src=')[
            1].split('cover_img=')[0][0:-1]
        url = urllib.parse.unquote(url) + '=' + str(int(time.time() * 1000))
        if 'http:' not in url:
            url = 'http:' + url
        try:
            temp_value = requests.get(url)
            video = open('video/' + video_path, 'wb')
            video.write(temp_value.content)
            video.close()
        except BaseException:
            pass

# 多线程爬取图片
def thread_img(k, img_path):
    if 'http:' in k['src']:
        img_r = requests.get(k['src'])
    else:
        img_r = requests.get( 'http:'+ k['src'])
    img = open('image/' + img_path, 'wb')
    img.write(img_r.content)
    img.close()

# 采集微博
def collect(keyword, session, pagenumber=1):
    # 关键字编码
    keyword_change = urllib.parse.quote_plus(keyword)
    keyword_change = urllib.parse.quote_plus(keyword_change)
    now = datetime.datetime.now().strftime('%Y-%m-%d')
    # 构建URL，地区默认广东省广州市
    url = 'http://s.weibo.com/weibo/' + keyword_change + \
        '&region=custom:44:1&typeall=1&suball=1&page=%s' % (str(pagenumber))
    r = session.get(url)
    # 解决中文乱码
    get_value = r.content.decode('unicode_escape').replace('\/', '/')
    # 清洗多余数据
    index = get_value.find('<div class="face">')
    get_value = get_value[index::]
    soup = BeautifulSoup(get_value, 'html5lib')
    # 获取当页全部用户信息
    get_info = soup.find_all('div', re.compile('content clearfix'))

    for i in get_info:
        # 获取用户信息
        get_user = i.find('a', re.compile('W_texta W_fb'))
        user_name = get_user.getText().replace('\n', '').strip()
        # 获取文字全部内容
        get_comment = i.find('p', re.compile('comment_txt'))
        # 文字过长需要特殊处理获取
        get_long_comment = get_comment.find('a', href=re.compile('javascript'))
        if get_long_comment:
            get_url = 'http://s.weibo.com/ajax/direct/morethan140?' + \
                get_long_comment['action-data'] + '&_t=0&__rnd=' + str(int(time.time() * 1000))
            temp_value = session.get(get_url)
            get_comment_temp = temp_value.json()
            get_comment = get_comment_temp['data']['html']
            get_comment = BeautifulSoup(get_comment, 'html5lib')
        # 输出全部文字内容
        comment = get_comment.getText().replace('\n', '').strip()
        comment = comment.encode("utf-8", 'ignore').decode('UTF-8', 'ignore')

        # 获取图片
        img_path_list = ''
        get_img_value = i.find_all('img', re.compile('bigcursor'))
        # 输出多张图片
        for k in get_img_value:
            img_path = str(int(time.time() * 1000)) + '.jpg'
            img_path_list = img_path_list + img_path + '/'
            pool = ThreadPoolExecutor(max_workers=1)
            pool.submit(thread_img, k, img_path)

        # 输出视频
        video_path = ''
        get_video_value = i.find('a', re.compile('WB_video'))
        if get_video_value:
            pool = ThreadPoolExecutor(max_workers=1)
            video_path = str(int(time.time() * 1000)) + '.mp4'
            pool.submit(thread_video, get_video_value, video_path)

        # 生成csv
        f = open('data.csv', 'a', newline='', encoding='gb18030')
        writer = csv.writer(f)
        writer.writerow([user_name, comment, img_path_list, video_path, now])
        f.close()
