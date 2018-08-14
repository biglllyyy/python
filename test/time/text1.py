import time
# i=time.time()
# timeStamp = float(i)
# timeArray = time.localtime(timeStamp)
#
# time_1 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
# print (time_1)

i = time.time().__float__()
i=time.localtime(i)
print(i)
ti = time.localtime()
print(ti)
time1 = time.strftime('%Y-%m-%d %H:%M:%S',ti)
print(time1)


#float:1508468211.208629
#1508468226.056999
