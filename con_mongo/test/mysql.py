#coding=utf8

import pymysql.cursors

def con_mysql(sql):
    conn = pymysql.connect(host='10.99.6.41', port=63306, user='root', passwd='evm@daocloud',db='raw_data_storage')
    cur = conn.cursor()
    try:
        cur.execute(sql)
# li=[]
# # print(cur.fetchall())
#         print(r)
#         #cur.close()
# print li
    except:
        pass
    conn.commit()
    return cur

def read_file(path,list):
    with open(path) as f:
        for line in f.readlines():
            line = line.split('\n')[0]
            list.append(line)

# sql = "insert into raw_data(id,VIN,packet_time,raw,send_time) values('%s','%s','%s','%s','%s')"%(id, vin, this_packet_time, raw_data, send_packet_time)
# sql="select * from raw_data limit 1"
#
# for i in  con_mysql(sql):
#     print (i)

def save_file(path,content):
    with open(path,'a') as f:
        f.write(content)

if __name__ == '__main__':
    vin_list_1 = []

    path_1 = '/workspace/licheng/list_all'

    read_file(path_1, vin_list_1)
    count = set ()
    for i in vin_list_1:
        sql = "select * from t_raw_2017_09_w02 where vin = '%s'"%(i)
        for m in con_mysql(sql):
            if m:
                count.add(i)

    for i in count:
        print(i)
        save_file('/workspace/licheng/mysql',str(i)+'\n')


            # save_file('/workspace/licheng/mysql',str(i))t_raw_2017_08_w01

