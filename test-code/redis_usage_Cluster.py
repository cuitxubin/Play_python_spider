#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/11/15 11:29
# @Author  : xubin
# @FileName: redis_usage_Cluster.py
# @Software: PyCharm
# @Mail    : 863813624@qq.com

from rediscluster import StrictRedisCluster

startup_nodes = [{"host": "172.20.17.170", "port": "6379"}]
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
rc.set("foo", "bar")

print(rc.get("foo"))