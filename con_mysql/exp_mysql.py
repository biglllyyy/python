#!/usr/bin/env python
#coding=utf-8
import xlwt
import pymysql
conn=pymysql.connect(host='10.3.236.223',port=3306,user='root',passwd='root',db='data')
cursor=conn.cursor()
count = cursor.execute('select * from EMP')
print ('has %s record' % count)
#重置游标位置
cursor.scroll(0,mode='absolute')
#搜取所有结果
results = cursor.fetchall()
#测试代码，print results
#获取MYSQL里的数据字段
fields = cursor.description
#将字段写入到EXCEL新表的第一行
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('emp',cell_overwrite_ok=True)
for ifs in range(0,len(fields)):
    sheet.write(0,ifs,fields[ifs][0])
ics=1
jcs=0
for ics in range(1,len(results)+1):
    for jcs in range(0,len(fields)):
        sheet.write(ics,jcs,results[ics-1][jcs])
wbk.save('c:\\test4.xlsx')