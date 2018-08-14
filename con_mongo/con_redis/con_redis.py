#coding=utf8
import redis

# r=redis.StrictRedis(host='10.2.23.3',port=4301,db=0)
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



'''
验证10.99.6.11的可用性
'''
# try:
#     r=redis.Redis(host='10.99.6.11',port=8008,db=1)
#     r.set('foo','test')
#     if r.get('test') == 'test':
#         print 'success'
#     else:
#         print 'fause'
# except:
#     print 'except'
# r.keys('*')

#    StrictRedis(host='10.99.6.8', port=8011, db=0)


'''
验证10.99.6.8:8011的可用性
'''
# try:
r=redis.Redis(host='10.99.6.8',port=8011,db=1)
print (r.keys('*'))
#     r.set('foo','test')
#     if r.get('test') == 'test':
#         print 'success'
#     else:
#         print 'fause'
# except:
#     print 'except'
# r.keys('*')