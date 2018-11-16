#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/31 18:15
# @Author  : xubin
# @FileName: redis_usage_Producer.py
# @Software: PyCharm
# @Mail    : 863813624@qq.com

import redis
import time

client = redis.StrictRedis(host='172.20.1.246', port=6379,db=1)

client.publish("codehole", "python comes")
client.publish("codehole", "java comes")
client.publish("codehole", "golang comes")