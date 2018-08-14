import pymysql
import redis
from pymongo import MongoClient

# Test MySQL Server
'''
mihsa's mysql 
'''
try:
    conn= pymysql.connect(
        host='10.99.6.11 ',
        # host='192.168.0.1 ',
        port = 8000,
        user='root',
        passwd='evm@daocloud',
        db ='test'
    )
    conn.close()
    print ("Success to connect to orig MySQL")
except:
    print ("Failed to connect to orig MySQL")


try:
    conn= pymysql.connect(
        host='10.99.6.12 ',
        # host='192.168.0.2 ',
        port = 8002,
        user='root',
        passwd='evm@daocloud',
        db ='test'
    )
    conn.close()
    print ("Success to connect to mgmt MySQL")
except:
    print ("Failed to connect to mgmt MySQL")

# Test MongoDB Server
'''
解析之后的数据存储
'''
try:
    client = MongoClient('mongodb://10.99.6.8:8015/,mongodb://10.99.6.9:8013/,mongodb://10.99.6.11:8014/')
    # client = MongoClient('mongodb://192.168.0.2:8015/,mongodb://192.168.0.3:8013/,mongodb://192.168.0.4:8014 /')
    db = client.test
    collection = db.test
    collection.insert({'name':'LiuPeng','age':22,'addr':'DaoCloud'})
    text = collection.find_one()
    collection.remove()
    client.close()
    print ("Success to connect to Mongodb")
except:
    print ("Failed to connect to Mongodb")

# Test Redis Server
try:
    r = redis.Redis(host='10.99.6.11', port=8008, db=1)
    # r = redis.Redis(host='192.168.0.7 ', port=8008)
    r.set('foo','bar')
    if r.get('foo') == "bar":
        print ("Success to connect to haproxy_redis_01")
    else:
        print ("Failed to connect to haproxy_redis_01")
except:
    print ("Failed to connect to haproxy_redis_01")

try:
    r = redis.Redis(host='10.99.6.11', port=8011, db=1)
    # r = redis.Redis(host='192.168.0.9 ', port=8011)
    r.set('foo','bar')
    if r.get('foo') == "bar":
        print ("Success to connect to haproxy_redis_02")
    else:
        print ("Failed to connect to haproxy_redis_02")
except:
    print ("Failed to connect to haproxy_redis_02")

# Test Kafka Server