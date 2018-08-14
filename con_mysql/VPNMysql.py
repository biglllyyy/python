import pymysql
import datetime

def conMysql(tableName,firstTime,lastTime,vin):
    conn = pymysql.connect(host='10.99.6.40',port=63306,database='raw_data_storage',user='root',password='evm@daocloud')
    cur=conn.cursor()

    sql = "select * from %s where packet_time BETWEEN '%s' AND '%s' AND vin='%s'" % (
        str(tableName), firstTime, lastTime,vin)
    print(sql)

    cur.execute(sql)
    conn.commit()
    return cur

def readFile(readfile,arr):
    with open(readfile,'r') as f:
        for i in f.readlines():
            i=i.replace('\n','')
            arr.append(i)

def saveFile(savefile,content):
    with open(savefile,'a') as f:
        f.write(content)

if __name__ == '__main__':
    arr=[]
    readfile='/workspace/dataExport/vin'
    savefile='/workspace/dataExport/file'
    readFile(readfile,arr)
    for vin in arr:
        print(vin)
        savefile=savefile+'/'+vin
        for i in conMysql('t_raw_2017_11_w01','2017-11-01 00:00:00','2017-11-02 00:00:00',vin):
            saveFile(savefile,str(i)+'\n')
            print(i)





