import asyncio

@asyncio.coroutine
def hello():
    print('hello')
    print('1')
    print('2')
    print('3')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()