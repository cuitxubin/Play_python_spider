import requests
import json
import csv
from taobao_m import get_auctions_info
def get_info(get_keyword_list,get_page,auctions_distinct):
    for k in get_keyword_list:
        #新建csv文件
        file_name = k+".csv"
        with open(file_name,"w",newline='') as csvfile:
            writer = csv.writer(csvfile)
            #写入数据
            writer.writerow(['标题','价格','销量','店铺','区域'])
            csvfile.close()
        for p in range(get_page):
            url='https://s.taobao.com/api?callback=jsonp804&m=customized&q=%s&s=%s' %(k,p)
            r = requests.get(url)
            response = r.text
            response = response.split('(')[1].split(')')[0]
            response_dict=json.loads(response)
            response_auctions_info = response_dict['API.CustomizedApi']['itemlist']['auctions']
            #数据存储
            auctions_distinct=get_auctions_info(response_auctions_info,file_name,auctions_distinct)