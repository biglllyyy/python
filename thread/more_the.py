from multiprocessing import Pool
import os, time, random

def open_file(path):
    with open(path,'r',encoding='utf-8') as f:
        for i in f.readlines():
            # print('line is :%s'%(i))
            return 'line is :%s'%(i)

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    print (open('/workspace/a.txt'))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')