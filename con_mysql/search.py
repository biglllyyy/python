#coding=utf8

import pymysql.cursors
import time
import os

def save_file(path,content):
    with open(path,'a') as f:
        f.write(content)

def con_mysql(sql):
    try:
        conn = pymysql.connect(host='10.99.6.41', port=63306, user='root', passwd='evm@daocloud',db='raw_data_storage')
        cur = conn.cursor()
        cur.execute(sql)
    except:
        print('error')
    conn.commit()
    return cur

def read_file(path,vin_list):
    with open(path,'r') as f:
        for line in f.readlines():
            line=line.split('\n')[0]
            vin_list.append(line)

if __name__ == '__main__':
    vin_list = []
    count = 0
    jingdu = 0
    read_file('/workspace/search/mysql/chexing/DFA7000L2ABEV1',vin_list)
    for vin in vin_list:
        sql="select vin,packet_time,process_time,raw from t_raw_2017_10_w04 where vin='%s' and packet_time > '2017-10-23 00:00:00' and packet_time < '2017-10-31 00:00:00'"%(vin)
        try:
            for result in con_mysql(sql):
                content='vin 是 ： '+str(result[0])+'数据报的时间是：'+str(result[1])+'处理时间是： '+str(result[2])+'原始报文是 ：'+str(result[3])+'\n'
                save_file('/workspace/search/mysql/chexing/DFA7000L2ABEV1.txt',content)
        except:
            print('conn errot')

    #count is :341
