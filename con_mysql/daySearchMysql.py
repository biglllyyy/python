import pymysql.cursors
import datetime
import os

###统计每天激活的车辆的厂家，VIN以及激活的数量

def con_mysql(sql):
    conn = pymysql.connect(host='10.99.6.12', port=8002, user='root', passwd='evm@daocloud',db='database_car')
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur

def saveFile(path,conent):
    with open(path,'a',encoding='utf-8') as f:
        f.write(conent)

def readYesterdayVin(path,dic):
    count = 0
    if os.path.exists(path):
        with open(path,'r',encoding='utf8') as f:
            print(path)
            for line in f.readlines():
                line=line.split(':')
                try:
                    dic[line[0]]=line[1].split('\n')[0]
                    count+=1
                except:
                    print(line)
                    print('yesterday line data error')
            return dic,count

if __name__ == '__main__':
    isActiveVinDic = {}
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    savaFilename = '/workspace/search/'+str(date)
    path = '/workspace/search/'+str((datetime.datetime.now() + datetime.timedelta(days=-1)).strftime('%Y-%m-%d'))

    sql0='select vin,vehicle_manufacturer from vehicle_info where is_activated =1'
    for isActiveVin in con_mysql(sql0):
        saveFile(savaFilename,isActiveVin[0]+":"+isActiveVin[1]+'\n')
        isActiveVinDic[isActiveVin[0]]=isActiveVin[1]
    yesterdayDic = {} 

    readYesterdayVin(path,yesterdayDic)
    print(isActiveVinDic)
    count = 0
    if len(yesterdayDic) != 0:
        for keyVIN in isActiveVinDic.keys():
            count += 1
            xinJiHuoFile = '/workspace/search/xinjihuo'+str(datetime.datetime.now().strftime('%Y-%m-%d'))
            # if not yesterdayDic.get(keyVIN):
                # saveFile(xinJiHuoFile,str(keyVIN)+':'+str(isActiveVinDic[keyVIN])+'\n')
        # saveFile('/workspace/search/vehiclemanager', str(date)+'：'+str(len(isActiveVinDic))+'\n')


