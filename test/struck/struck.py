from struct import *
import struct
import datetime
# s=Struct('hhl')
s=Struct('!BBBBBB')
# data=[1,2,3]
def get_time():
    return datetime.datetime.now().year - 2000, \
           datetime.datetime.now().month, \
           datetime.datetime.now().day, \
           datetime.datetime.now().hour, \
           datetime.datetime.now().minute, \
           datetime.datetime.now().second


# get_time=datetime.datetime.now()
data=struct.pack('!BBBBBB', *get_time())
pack_data=s.pack(*data)
print repr(pack_data)
print s.unpack(pack_data)