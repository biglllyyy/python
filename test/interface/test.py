import threading
import time

def action(arg):
    time.sleep(2)
    print('time is %s\t'%(arg))

theads = []
for i in range(5):
    t = threading.Thread(target=action,args=(i,))
    t1 = threading.Thread(target=action,args=(i,))
    theads.append(t)
    theads.append(t1)
for i in theads:
    i.setDaemon(True)
    i.start()
for l in theads:
    t.join()