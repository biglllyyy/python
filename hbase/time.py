import time
import sys
'''
hbase数据的时间戳为13位，需要手动删除后三位，然后进行时间戳的转换
'''
a = 1508263043
time1 = time.localtime(a)
print(time1)
time2 = time.strftime('%Y-%m-%d %H:%M:%S',time1)
print(time2)
