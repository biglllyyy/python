#coding=utf8

"""
接入层redis监控

"""
import redis

r=redis.Redis(host='10.99.5.5',port=6379,db=0)
for i in r.keys('*'):
    print (i)


# 10.99.5.6

# r.set('test','test')
# print r.keys('*')
# print r.type('online')
# print r.hgetall('online')
# for i,m in r.hgetall('online'):
#     if i=='LDP53A930GC101395':
#         print i,m
# p=r.pipeline()
# p.set('b',2)
# p.incr('num')
# print (p.execute())


