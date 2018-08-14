import time
import thread
import datetime

gen = None
def lo():
    global gen
    def lo_1():
        time.sleep(2)
        try:
            gen.send(datetime.datetime.now())
        except:
            pass
    thread.start_new_thread(lo_1,())

def a():
    print 'a'
    ret = yield lo()
    print ret

def b():
    print 'b'

if __name__ == '__main__':
    gen = a()
    gen.next()
    b()
    while a:
        pass



