#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/19 16:39
# @Author  : xubin
# @FileName: mysql_usage01.py
# @Software: PyCharm
# @Mail    : 863813624@qq.com

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://root:xubin,.QWE@localhost:3306/test?charset=utf8",
                       echo=True, pool_size = 5, max_overflow = 10, pool_recycle = 7200, pool_timeout = 30)

DBSession = sessionmaker(bind=engine)
session = DBSession()
new_data = mytable(name = 'Li Lei', age = 10, birth = "2017-10-01", class_name = "一年级一班")
session.add(new_data)
session.commit()
session.close()
