import pymongo
import datetime
import re
# 创建对象
client = pymongo.MongoClient()
# 连接DB数据库
db = client['DB']
# 连接集合user，集合类似关系数据库的数据表
# 如果集合不存在，会新建集合user
user_collection = db.user
# 设置文档格式（文档即我们常说的数据）
user_info = {
	    "_id": 100,
	    "author": "小黄",
         "text": "Python爬虫开发",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

# 使用insert_one单条添加文档，inserted_id获取写入后id
# 添加文档时，如果文档尚未包含"_id"键，则会自动添加"_id"。 "_id"的值在集合中必须是唯一。
# inserted_id是获取添加后的id，若不需要可去掉。
user_id = user_collection.insert_one(user_info).inserted_id
print ("user id is ", user_id)

#批量添加
user_infos = [{
	    "_id": 101,
	    "author": "小黄",
         "text": "Python爬虫开发",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()},
	 {
	    "_id": 102,
	    "author": "小黄_A",
         "text": "Python爬虫开发_A",
         "tags": {"db":"Mongodb", "lan":"Python", "modle":"Pymongo"},
         "date": datetime.datetime.utcnow()},
		 ]
# inserted_ids是获取添加后的id，若不需要可直接去掉。
user_id = user_collection.insert_many(user_infos).inserted_ids
print ("user id is ", user_id)
