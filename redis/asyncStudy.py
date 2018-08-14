import redis
import asyncio
#
pool = redis.ConnectionPool(host='10.3.236.238', port=6379)
r = redis.Redis(connection_pool=pool)
r.set('name', 'zhangsan')   #添加
print (r.get('name').decode('utf8'))   #获取




# r = redis.Redis(host='192.168.0.209', port=6379,db=0)
# r.set('name', 'zhangsan')   #添加
# print (r.get('name'))   #获取

import asyncio
#
# @asyncio.coroutine
# def hello():
#     while True:
#         print("Hello world!")
#         # 异步调用asyncio.sleep(1):
#         r = yield from asyncio.sleep(1)
#         print("Hello again!")

@asyncio.coroutine
def hello():
    count = 0
    while True:
        print(count)
        count += 1
        print(count)



# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()