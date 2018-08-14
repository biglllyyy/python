import threading
import os

def open_file(path):
    with open(path) as f:
        for line in f.readlines():
            print (line)

if __name__ == '__main__':
    theads = []
    t1 = threading.Thread(target=open_file,args=('/workspace/a.txt'))
    theads.append(t1)
    t2 = threading.Thread(target=open_file, args=('/workspace/b.txt'))
    theads.append(t2)
    for t in theads:
        t.setDaemon(True)
        t.start()
    for t in theads:
        t.join()
os.system()