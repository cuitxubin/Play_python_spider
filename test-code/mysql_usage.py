#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2018/10/19 16:02
# @Author  : xubin
# @FileName: mysql_usage.py
# @Software: PyCharm
# @Mail    : 863813624@qq.com


# 主流数据库连接方式：
"""
Microsoft SQL Server mssql+pymysql://username:password@ip:port/dbname
Mysql                mysql+pymysql://username:password@ip:port/dbname
Oracle               cx_Orcle://username:password@ip:port/dbname
PostgreSQL           postgresql://username:password@ip:port/dbname
SQLLite              sqllite://file_path
"""

# 连接数据库
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:xubin,.QWE@localhost:3306/test?charset=utf8",
                       echo=True, pool_size = 5, max_overflow = 10, pool_recycle = 7200, pool_timeout = 30)

# 创建数据表
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
Base = declarative_base()

class mytable(Base):

    __tablename__ = 'mytable'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    age = Column(Integer)
    birth = Column(DateTime)
    class_name = Column(String(50))

# Base.metadata.create_all(engine)

from sqlalchemy import Column, MetaData, ForeignKey, Table
from sqlalchemy.dialects.mysql import (INTEGER, CHAR)
meta = MetaData()
myclass = Table('myclass', meta,
                Column('id', INTEGER, primary_key=True),
                Column('name', CHAR(50), ForeignKey(mytable.name)),
                Column('class_name', CHAR(50))
                )
# myclass.create(bind=engine)

#添加数据
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind=engine)
session = DBSession()
# new_data = mytable(name = 'ccc', age = 10, birth = "2017-10-01", class_name = "s年级一班")
# session.add(new_data)
# session.commit()
# session.close()

#更新数据
# session.query(mytable).filter_by(id=1).update({ mytable.age : 12})
# session.commit()
# session.close()
#
# get_data = session.query(mytable).filter_by(id=1).first()
# get_data.class_name = '三年级三班'
# session.commit()
# session.close()

#查询数据
# get_data = session.query(mytable).all()
# for i in get_data:
#     print("我的名字是： " + i.name)
#     print("我的班级是： " + i.class_name)
# session.close()


get_data = session.query(mytable.name, mytable.class_name).all()
print(get_data)
for i in get_data:
    print('我的名字是：' + i.name)
    print('我的班级是：' + i.class_name)
session.close()