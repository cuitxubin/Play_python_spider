import csv
def get_auctions_info(response_auctions_info, file_name,auctions_distinct):
    with open(file_name,"a",newline='') as csvfile:
        #生成csv对象，用于写入csv文件
        writer = csv.writer(csvfile)
        for i in response_auctions_info:
            #判断是否数据已经记录
            if str(i['raw_title']) not in auctions_distinct:
                #写入数据
                writer.writerow([i['raw_title'],i['view_price'],i['view_sales'],i['nick'],i['item_loc']])
                auctions_distinct.append(str(i['raw_title']))
        csvfile.close()
    return auctions_distinct