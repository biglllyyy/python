import pymysql.cursors
import datetime

def connectionMysql(sql):
    conn = pymysql.connect(host='10.99.6.41', port=63306, user='root', passwd='evm@daocloud',db='raw_data_storage')
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
        tableNum = datetime.datetime.now().strftime('%d')
    else:
        tableNum = int(datetime.datetime.now().strftime('%d')) // 7 + 1
    tableName = "t_raw_" + datetime.datetime.now().strftime('%Y_%m') + "_w0" + str(tableNum)

    sql0="select count(distinct(vin)) from %s where packet_time BETWEEN '%s' AND '%s'"%(str(tableName),dayNow,tomorrow)
    print(sql0)
    # sql0 = "select count(distinct(vin)) from t_raw_2017_11_w02 where packet_time BETWEEN '2017-11-07 00:00:00' AND '2017-11-08 00:00:00'"
    for result0 in connectionMysql(sql0):
        print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"："+str(result0[0]))
        # saveFile('/workspace/search/mysql/rihuo.txt','2017-11-07 00:00:00 :'+str(result0[0])+'\n')
        saveFile('/workspace/search/mysql/rihuo.txt',str(datetime.datetime.now().strftime('%Y-%m-%d')) +":"+ str(result0[0]) + '\n')

