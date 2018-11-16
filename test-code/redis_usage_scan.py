#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/29 18:24
# @Author  : xubin
# @FileName: redis_usage_scan.py
# @Software: PyCharm
# @Mail    : 863813624@qq.com

import redis

client = redis.StrictRedis(host='172.20.1.246', port=6379,db=0)
for i in range(1000):
    client.set("key%d" % i, i)
