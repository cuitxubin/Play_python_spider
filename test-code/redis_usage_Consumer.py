#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/31 18:14
# @Author  : xubin
# @FileName: redis_usage_Consumer.py
# @Software: PyCharm
# @Mail    : 863813624@qq.com

import redis
import time

client = redis.StrictRedis(host='172.20.1.246', port=6379,db=1)

p = client.pubsub()
p.subscribe("codehole")
for msg in p.listen():
    print(msg)