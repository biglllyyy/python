#!/usr/local/bin/python3
import pymysql.cursors
import datetime

def connectionMysql(sql):
    conn = pymysql.connect(host='10.99.6.40', port=63306, user='root', passwd='evm@daocloud',db='raw_data_storage')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur

def saveFile(path,content):
    with open(path,'a') as f:
        f.write(content)

if __name__ == '__main__':
    tomorrow=(datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d 00:00:00')
    dayNow=datetime.datetime.now().strftime('%Y-%m-%d 00:00:00')

    if int(datetime.datetime.now().strftime('%d')) < 7:
        tableNum = int(datetime.datetime.now().strftime('%d'))
    else:
        tableNum = int(datetime.datetime.now().strftime('%d')) // 7 + 1
    tableName = "t_raw_" + datetime.datetime.now().strftime('%Y_%m') + "_w0" + str(tableNum)
    if int(tableName[-1]) > 4:
        tableName ="t_raw_" + datetime.datetime.now().strftime('%Y_%m') + "_w04"
    else:
        tableName = tableName
    print(tableNum)
    print(tableName)
    sql0="select count(distinct(vin)) from %s where packet_time BETWEEN '%s' AND '%s'"%(str(tableName),dayNow,tomorrow)
    for result0 in connectionMysql(sql0):
        print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+" : "+str(result0[0]))
        saveFile('/home/liulin/rihuo/rihuo.txt',str(datetime.datetime.now().strftime('%Y-%m-%d')) +":"+ str(result0[0]) + '\n')