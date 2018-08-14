#coding=utf8

import pymysql.cursors
import datetime
import os

# def con_mysql(file,spend_time_file):
#     conn = pymysql.connect(host='10.3.236.201', port=3306, user='root', passwd='root',db='test',charset = 'utf8')
#     cur = conn.cursor()
#
#     with open(file, 'r') as f:
#         start_time = datetime.datetime.now()
#         for line in f.readlines():
#             raw_data = line
#             line = line.split(',')
#             if len(line) == 4:
#                 packet_time = line[0]
#                 vin = line[1]
#                 raw = line[2]
#                 process_time = line[3].split('\n')[0]
#                 sql = "insert into t_raw_2017_08_w02(packet_time,vin,raw,process_time) \
#                                        values('%s','%s','%s','%s')" \
#                       % (packet_time, vin, raw, process_time)
#                 try:
#                     cur.execute(sql)
#
#                 except:
#                     print(raw_data)
#                     save_file('/workspace/mysql_data.txt', str(raw_data))
#
#             else:
#                 print('data parse errot')
#                 save_file('/workspace/data_parse.txt', str(raw_data))
#         conn.commit()
#         end_time = datetime.datetime.now()
#         spend_time = end_time-start_time
#         print('spend time is :'+str(spend_time))
#         save_file(spend_time_file,str(spend_time)+'\n')

    # cur.execute(sql)


def con_mysql():
    conn = pymysql.connect(host='10.2.208.171', port=3306, user='root', passwd='root',db='test',charset = 'utf8')
    cur = conn.cursor()
    num = 1
    while num < 100000:
        sql='insert into test.test(uid,uname) values(%d,"%s");'%(num,'232303FE4C4450474142414330484231303233313301012B110A1F0E26200101030100000000B0360E4E27105B011E0BB80064020101043B4E204E20410E562710050006CEDE5001D5C79C0601150F4601170F0E01034101023F070000000000000000000801010E4E2710005E00015E0F390F370F3B0F3E0F3D0F320F3F0F370F350F270F3E0F390F3E0F3A0F380F350F3B0F330F380F420F460F3F0F0E0F3D0F3A0F400F2F0F410F3A0F360F380F3F0F390F420F380F380F390F3E0F3C0F370F3E0F340F410F2B0F3C0F2F0F390F400F400F320F3B0F320F340F400F3B0F370F380F380F320F390F350F280F440F290F370F3C0F350F390F3C0F370F400F2D0F3A0F380F3C0F360F380F380F3D0F430F360F3D0F390F3A0F370F3F0F370F3C0F2D0F3B0F320F380F3A0F3E0901010012403F4141403F3F3F403F3F41413F3F3F3F4024 ')
        print(sql)
        try:
            cur.execute(sql)

        except:
            save_file('/workspace/mysql_data.txt', str(num))

        else:
            print('data parse errot')
            save_file('/workspace/data_parse.txt', str(num))
            conn.commit()
        num += 1

def save_file(path,content):
    with open(path,'a') as f :
        f.write(content)


if __name__ == '__main__':
        con_mysql()





#values(str_to_date('%s','%%Y-%%m-%%d %%H:%%M:%%S'),'%s','%s',str_to_date('%s','%%Y-%%m-%%d %%H:%%M:%%S'))"\

# sql="select * from raw_data limit 1"

# for i in  con_mysql(sql):
#     print (i)


