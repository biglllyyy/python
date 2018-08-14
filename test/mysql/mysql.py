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
    conn.close()
    print ("Success to connect to orig MySQL")
except:
    print ("Failed to connect to orig MySQL")


try:
    conn= pymysql.connect(
        host='10.99.6.12  ',
        # host='192.168.0.2',
        port = 8002,
        user='root',
        passwd='evm@daocloud',
        db ='test'
    )
    conn.close()
    print ("Success to connect to mgmt MySQL")
except:
    print ("Failed to connect to mgmt MySQL")