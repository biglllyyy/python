#coding=utf-8
from pymongo import MongoClient

#建立MongoDB数据库连接
# client = MongoClient('10.99.6.9',8013)
client = MongoClient('10.99.6.8:8015,10.99.6.9:8013,10.99.6.11:8014')

#连接所需数据库,test为数据库名
# db=client.test
db=client.parsed_data_storage


#连接所用集合，也就是我们通常所说的表，test为表名
# collection=db.data
# collection=db.myTestCollection
collection=db.parsed_real_data_w04
count =0
# for i in collection.find():
#     count +=1
#     print i
# print count
# print db['a']
# for i in collection.find({'time': {'$gte':"2017-09-05 00:01:00", '$lt':"2017-09-08 00:01:00"}}):
for i in collection.find({'VIN':'LGJE13EA0GM417415','time':'2017-09-21 00:00:00'}):
# for i in collection.find({'VIN':'LGJE13EA2GM454207'}):

# for i in collection.find({'VIN':'LGJE13EA4HM616257','time':{'$lt':'2017-11-29 00:00:00','$gt':'2017-11-28 00:00:00'}}):

# for i in collection.find({'VIN':'LDPGAAAB9HB101503'}):
#     print i
# for i in collection.distinct("VIN",{"time": {'$gte':"2017-09-06 00:00:00",'$lt':"2017-09-08 00:00:00"}}):

    # if i=='LDPGABAC1HB101817':
    # if i =='LDP53A935GC10474':
    #    for f in  collection.find({'VIN':'LDPGABAC1HB101817'}):
    #        print f
    print (i)
    if count == 1:
        break
    count += 1


print (count)