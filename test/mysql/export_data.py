#coding=utf8
import datetime
import pymysql.cursors
def open_file(path,arr):
    with open(path,'r') as f:
        for line in f.readlines():
            arr.append(line)
    # return arr


def con_mysql():
    # 连接配置信息
    config = {
        'host': '219.139.176.3',
        'port': 3307,
        'user': 'root',
        'password': 'evm@daocloud',
        'db': 'raw_data_storage',
    }
    # 创建连接
    connection = pymysql.connect(**config)

    value = []
    count = 0
    # 执行sql语句
    open_file('/workspace/vin',value)
    try:
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            for vin in value:
                sql = 'SELECT vin,raw FROM raw_data_storage.raw_data where vin="%s"'%(vin)
                # open_file('D:\\teshang.txt',arr)
                cursor.execute(sql)
                # 获取查询结果
                for j in cursor.fetchall():
                    vin = vin.split('\n')[0]
                    sava_file('/workspace/%s'%(vin),str(j[0])+','+str(j[1])+'\n')
                    # print j[0]
                count += 1
                print (count)

        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()

    finally:
        connection.close()

def sava_file(path,context):
    with open(path,'a') as f:
        f.write(context)

if __name__ == '__main__':
    con_mysql()
