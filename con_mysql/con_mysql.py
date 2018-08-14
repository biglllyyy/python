#coding=utf8

import pymysql.cursors

def con_mysql(sql):
    conn = pymysql.connect(host='10.99.6.41', port=63307, user='root', passwd='evm@daocloud',db='raw_data_storage')
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

# sql = "insert into raw_data(id,VIN,packet_time,raw,send_time) values('%s','%s','%s','%s','%s')"%(id, vin, this_packet_time, raw_data, send_packet_time)


def saveFile(path,content):
    with open(path,'a') as f:
        f.write(content)

if __name__ == '__main__':
    sql = []
    sql0 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w03 where packet_time \
        BETWEEN '2018-02-15 15:00:00' AND '2018-02-16 15:00:00' "

    sql1 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w03 where packet_time \
        BETWEEN '2018-02-16 15:00:00' AND '2018-02-17 15:00:00' "
    sql2 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w03 where packet_time \
        BETWEEN '2018-02-17 15:00:00' AND '2018-02-18 15:00:00' "
    sql3 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w03 where packet_time \
        BETWEEN '2018-02-18 15:00:00' AND '2018-02-19 15:00:00' "
    sql4 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w03 where packet_time \
    BETWEEN '2018-02-20 15:00:00' AND '2018-02-21 15:00:00' "

    sql5 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w04 where packet_time \
            BETWEEN '2018-02-21 15:00:00' AND '2018-02-22 15:00:00' "
    sql6 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w04 where packet_time \
            BETWEEN '2018-02-16 15:00:00' AND '2018-02-17 15:00:00' "
    sql7 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w04 where packet_time \
            BETWEEN '2018-02-17 15:00:00' AND '2018-02-18 15:00:00' "
    sql8 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w04 where packet_time \
            BETWEEN '2018-02-18 15:00:00' AND '2018-02-19 15:00:00' "
    sql9 = "select count(distinct(vin)) from raw_data_storage.t_raw_2018_02_w04 where packet_time \
        BETWEEN '2018-02-20 15:00:00' AND '2018-02-21 15:00:00' "
    for i in con_mysql(sql1):
        print(i)
        saveFile('/workspace/rihuo.txt',str(i)+'\n')
    for i in con_mysql(sql2):
        print(i)
        saveFile('/workspace/rihuo.txt', str(i) + '\n')
    for i in con_mysql(sql3):
        print(i)
        saveFile('/workspace/rihuo.txt', str(i) + '\n')
    for i in con_mysql(sql4):
        print(i)
        saveFile('/workspace/rihuo.txt', str(i) + '\n')
    for i in con_mysql(sql5):
        print(i)
        saveFile('/workspace/rihuo.txt', str(i) + '\n')
    for i in con_mysql(sql6):
        print(i)
        saveFile('/workspace/rihuo.txt', str(i) + '\n')
    for i in con_mysql(sql7):
        print(i)
        saveFile('/workspace/rihuo.txt', str(i) + '\n')
    for i in con_mysql(sql8):
        print(i)
        saveFile('/workspace/rihuo.txt', str(i) + '\n')
    for i in con_mysql(sql9):
        print(i)
        saveFile('/workspace/rihuo.txt', str(i) + '\n')




    #
    # vin = [
    #     "LGHB2VH90GD161193",
    #     "LGHB2VH90GD161209",
    #     "LGHB2VH90GD161212",
    #     "LGHB2VH90GD161226",
    #     "LGHB2VH90GD161243",
    #     "LGHB2VH90GD161257",
    #     "LGHB2VH90GD161260"
    #     # "LGHC2V1A4FG200244"
    # ]
    # tableName='t_raw_2017_12_w04'
    # for vinNum in vin:
    #     sql="select raw from t_raw_2017_12_w04 where vin = '%s'  "%(vinNum)
    #     # print(sql)
    #     for i in  con_mysql(sql):
    #         # print(str(i[2])[0:6])
    #         if str(i[0])[0:6]=='232302' or str(i[0])[0:6]=='232303':
    #             saveFile('/workspace/dataExport/vin/'+tableName+'/'+vinNum,str(i[0])+'\n')
#+','+str(i[1])+','+str(i[2])
# for i in  con_mysql(sql):
#     print (i)


