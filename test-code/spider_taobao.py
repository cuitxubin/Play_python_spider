#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/22 19:23
# @Author  : xubin
# @FileName: spider_taobao.py
# @Software: PyCharm
# @Mail    : 863813624@qq.com

import json
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

url = "https://s.taobao.com/api?&callback=jsonp254&m=customized&q=%E5%9B%9B%E4%BB%B6%E5%A5%97&s=36"
response = requests.get(url, headers= headers).text
print(response)
