import time
import thread

def f():
    def th():
        time.sleep(5)
        print ('sleep5')
    thread.start_new_thread(th, ())

def pr():
    print ('hello')

if __name__ == '__main__':
    f()
    pr()