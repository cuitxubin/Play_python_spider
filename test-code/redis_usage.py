#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/23 10:34
# @Author  : xubin
# @FileName: redis_usage.py
# @Software: PyCharm
# @Mail    : 863813624@qq.com

import redis

# HyperLogLog测试代码
# client = redis.StrictRedis(host='172.20.1.246', port=6379,db=0)
# for i in range(5000):
#     client.pfadd("codehole", "user%d" % i)
#     total = client.pfcount("codehole")
# print(client.pfcount("codehole"), "5000")

client = redis.StrictRedis(host='172.20.1.246', port=6380,db=0)
for i in range(5000):
    client.execute_command("bf.add", "df:userss", "user%d" % i)
    ret = client.execute_command("bf.exists", "df:userss", "user%d" % i)
    if ret == 0:
        print(i)
        break
