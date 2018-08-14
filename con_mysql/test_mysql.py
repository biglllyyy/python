#coding=utf8

import pymysql.cursors
import time
import os

def save_file(path,content):
    with open(path,'a') as f:
        f.write(content)

def con_mysql(sql,save_path):
    try:
        conn = pymysql.connect(host='10.2.23.8', port=4300, user='root', passwd='dangerous',db='nev_user_centre')
        cur = conn.cursor()
        cur.execute(sql)
    except:
        i = time.time()
        timeStamp = float(i)
        timeArray = time.localtime(timeStamp)
        time_1 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        print(time_1)
    conn.commit()
    return cur
if __name__ == '__main__':
    sql="select user_id from sys_user limit 1"
    for i in con_mysql(sql,'/workspace/abc'):
        print(i[0])
    # while True:
    #     try:
    #         for i in  con_mysql(sql,'/workspace/abc'):
    #             print (i)
    #         time.sleep(10)
    #     except:
    #         pass
