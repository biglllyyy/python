import pymysql.cursors
import time
import os


def con_mysql(sql):
    conn = pymysql.connect(host='10.99.6.41', port=63306, user='root', passwd='evm@daocloud',db='raw_data_storage')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur

def read_file(path,vin_list):
    with open(path,'r') as f:
        for line in f.readlines():
            vin_list.append(line)

if __name__ == '__main__':
    vin_list = []
    count = 0
    jingdu = 0
    read_file('/workspace/search/s_vin', vin_list)
    for vin in vin_list:
        sql = "select vin from t_raw_2017_08_w04 where vin='%s' " % (vin)
        for result in con_mysql(sql):
            if result[0] != 0:
                count += 1
                jingdu += 1
                print(jingdu)
                # print(result[0])
    print('count is :' + str(count))
