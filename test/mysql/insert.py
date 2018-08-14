

id_1=1
VIN='123'
pack_time_1='2017-01-12 12:09:23'
raw_1='1234567890'
pack_time_2='2017-01-12 12:09:23'
sql='insert into raw_data(id,VIN,pack_time,raw,send_time) value(%s,%s,%s,%s,%s)'%(id_1,VIN,pack_time_1,raw_1,pack_time_2)
print sql
sql1="insert into te(time) values(%s)"%(pack_time_2)
print sql1