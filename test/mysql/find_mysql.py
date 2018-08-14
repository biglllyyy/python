import pymysql
# Test MySQL Server
'''
mihsa's mysql 
'''
try:
    conn= pymysql.connect(
        host='10.99.6.11  ',
        # host='192.168.0.1  ',
        port = 8000,
        user='root',
        passwd='evm@daocloud',
        db ='test'
    )
except:
    print  "except"
cursor = conn.cursor()
cursor.execute("select raw from raw_data_storage.raw_data WHERE VIN='LDPGAAAB7HB105453'")
conn.close()