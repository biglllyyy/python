#!/usr/local/bin/python3
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
    tomorrow=datetime.datetime.now().strftime('%Y-%m-%d 00:00:00')
    dayNow=(datetime.datetime.now()+datetime.timedelta(days=-1)).strftime('%Y-%m-%d 00:00:00')

    if int(datetime.datetime.now().strftime('%d')) < 7:
        tableNum = datetime.datetime.now().strftime('%d')
    else:
        tableNum = int(datetime.datetime.now().strftime('%d')) // 7 + 1
    tableName = "t_raw_" + datetime.datetime.now().strftime('%Y_%m') + "_w0" + str(tableNum)
    if int(tableName[-1]) > 4:
        tableName ="t_raw_" + datetime.datetime.now().strftime('%Y_%m') + "_w04"
    else:
        tableName = tableName

    sql0="select count(distinct(vin)) from %s where packet_time BETWEEN '%s' AND '%s'"%(str(tableName),dayNow,tomorrow)
    for result0 in connectionMysql(sql0):
        print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+" : "+str(result0[0]))
        # saveFile('/home/liulin/rihuo/rihuo.txt',str(datetime.datetime.now().strftime('%Y-%m-%d')) +":"+ str(result0[0]) + '\n')





'''
2323起始符
02命令标识
FE应答标志
4C44唯一识别码
504741414143354842313038363231
01
0142110B1C112213010203010000000001360E8F2710490200B46E000002010103344E204E203B0000271003001B0014025800023639383001000001003001020500069BC9A801F13B1406012D0F2E010C0F24010136010935070000000000000000000801010E8F271000600001600F280F250F2A0F250F250F280F270F280F280F280F280F240F270F270F270F270F2B0F280F280F280F2A0F2B0F280F280F270F2AF250F280F270F240F270F240F240F240F250F250F2B0F280F2D0F2A0F2D0F2A0F2B0F2A0F2E0F2B0F2B0F2D0F270F2B0F270F2D0F250F250F270F270F270F2B0F2D0F240F270F2A0F270F2B0F240F2B0F2A0F2D0F2A0F280F280F270F2A0F280F2A0F270F280F280F280F2A0F270F270F280F250F2B0F270F280F2D0F280F2B0F2B0F250F250F2A0F2A0F2A0901010010363636363636363635353535353535355C



001B电压

0014电流

0258消耗率

0002电池温度探针总数

3639探针温度值

3830氢系统中最高温度

01氢系统中最高温度探针代号

0000氢气最高浓度

01氢气最高浓度传感器代号

0030氢气最高压力

01氢气最高压力传感器代号

02高压DC/DC状态（断开）








##
\x02#实时上报数据
\xfe#主动发起方应答标志
LDPGAAAB0GG105585
\x01#加密方式

\x01B
B=0x42#数据单元长度


\x11\x07\x14\x17;\x0e#时间

\x01#信息数据标志，整车数据
\x02\x03\x00\x00\x00\x00\x00\x05\xbe\r\xb8'\x10-

\x02
\x00\xc3P\x00\x00\x02\x01\x01\x03DN N E\x00\x00'\x10

\x03
\x00\x00\x009\x00\x14\x00\x02FFF\xb2\x01\x00\x00\x01\x00M\x01\x02

\x05
\x00\x06\x9b\xd8\xd0\x01\xf19\xaa

\x06
\x01\x0c\x0eP\x01%\x0e=\x01\x01H\x01\tG

\x07
\x00\x00\x00\x00\x00\x00\x00\x00\x00

\x08
\x01\x01\r\xb8'\x10\x00`\x00\x01`\x0eO\x0eD\x0eF\x0eI\x0eG\x0eG\x0eJ\x0e@\x0eF\x0eL\x0eO\x0eP\x0eG\x0eF\x0eC\x0eA\x0eD\x0eC\x0eF\x0eL\x0eJ\x0eM\x0eI\x0eF\x0eG\x0eF\x0eF\x0eJ\x0eF\x0eD\x0eJ\x0eG\x0eG\x0eI\x0eG\x0eG\x0e=\x0eI\x0e>\x0eA\x0e>\x0eC\x0eF\x0eG\x0eA\x0eF\x0eD\x0eC\x0eM\x0eL\x0eI\x0eM\x0eI\x0eJ\x0eF\x0eI\x0eJ\x0eL\x0eI\x0eL\x0eL\x0eG\x0eO\x0eI\x0eL\x0eL\x0eP\x0eG\x0eO\x0eG\x0eO\x0eF\x0eA\x0eD\x0eF\x0eG\x0eD\x0eD\x0eI\x0eI\x0eD\x0eG\x0eC\x0eG\x0eI\x0eF\x0eG\x0eM\x0eC\x0eJ\x0eG\x0eM\x0e@\x0eL\x0eA\x0eJ\t\x01\x01\x00\x10HHHHHHHHGGHHHHHH\xcc



##\x02\xfeLDPGAAAB0GG105585\x01\x01B\x11\x07\x14\x17;\x0e

\x01\x02\x03\x00\x00\x00\x00\x00\x05\xbe\r\xb8'\x10-\x02\x00\xc3P\x00\x00\x02\x01\x01\x03DN N E\x00\x00'\x10\x03\x00\x00\x009\x00\x14\x00\x02FFF\xb2\x01\x00\x00\x01\x00M\x01\x02\x05\x00\x06\x9b\xd8\xd0\x01\xf19\xaa\x06\x01\x0c\x0eP\x01%\x0e=\x01\x01H\x01\tG
\x07
\x00\x00\x00\x00\x00
\x00
\x00\x00\x00\x08\x01\x01\r\xb8'\x10\x00`\x00\x01`\x0eO\x0eD\x0eF\x0eI\x0eG\x0eG\x0eJ\x0e@\x0eF\x0eL\x0eO\x0eP\x0eG\x0eF\x0eC\x0eA\x0eD\x0eC\x0eF\x0eL\x0eJ\x0eM\x0eI\x0eF\x0eG\x0eF\x0eF\x0eJ\x0eF\x0eD\x0eJ\x0eG\x0eG\x0eI\x0eG\x0eG\x0e=\x0eI\x0e>\x0eA\x0e>\x0eC\x0eF\x0eG\x0eA\x0eF\x0eD\x0eC\x0eM\x0eL\x0eI\x0eM\x0eI\x0eJ\x0eF\x0eI\x0eJ\x0eL\x0eI\x0eL\x0eL\x0eG\x0eO\x0eI\x0eL\x0eL\x0eP\x0eG\x0eO\x0eG\x0eO\x0eF\x0eA\x0eD\x0eF\x0eG\x0eD\x0eD\x0eI\x0eI\x0eD\x0eG\x0eC\x0eG\x0eI\x0eF\x0eG\x0eM\x0eC\x0eJ\x0eG\x0eM\x0e@\x0eL\x0eA\x0eJ\t\x01\x01\x00\x10HHHHHHHHGGHHHHHH\xcc

\x01#信息数据标志，整车数据
\x02#车辆状态：熄火
\x03#充电状态：未充电状态
\x00#运行模式：
\x00\x00：#车速
\x00\x00\x05\xbe#累计里程
\r\xb8#总电压
'\x10#总电流
-#SOC
\x02#DC-DC状态
\x00#档位
\xc3P#绝缘电阻
\x00\x00#预留

\x02#驱动电机数据
\x01#驱动电机个数
\x01#驱动电机序号
\x03#驱动电机状态
D#驱动电机控制器温度
N #驱动电机转速（“ ”：0x20，N：0x4e）
N #驱动电机转矩（“ ”：0x20，N：0x4e）
E#驱动电机温度
\x00\x00#电机控制器输入电压
'\x10#电机控制器直流母线电流（‘：0x27）

\x03#燃料电池数据
\x00\x00#燃料电池电压
\x009#燃料电池电流（9：0x39）
\x00\x14#燃料消耗率
\x00\x02#燃料电池温度探针总数
FF#探针温度值（F:0x46）
F\xb2#氢系统中最高温度
\x01#氢系统中最高温度探针代号
\x00\x00#氢气最高浓度
\x01#氢气最高浓度传感器代号
\x00M#氢气最高压力(M:0x4d)
\x01#氢气最高压力传感器代号
\x023#高压DC/DC状态

\x05#车辆位置数据
\x00#定位状态
\x06\x9b\xd8\xd0#经度
\x01\xf19\xaa#纬度

\x06#极值数据
\x01#最高电压电池子系统号
\x0c#最高电压电池单体代号
\x0eP#电池单体电压最高值
\x01#最低电压电池子系统号
%#最低电压电池单体代号（%：0x25）
\x0e=#电池单体电压最低值（#：0x23）
\x01#最高温度子系统号
\x01#最高温度探针序号
H#最高温度值（H:0x48）
\x01#最低温度子系统号
\t#最低温度探针（\t:0x9）
G#最低温度值(G:0x47)

\x07#报警数据
\x00#最高报警等级
\x00\x00\x00\x00#通用报警标志
\x00#可充电储能装置故障总数N1
\x00#驱动电机故障总数N2
\x00#发动机故障总数N3
\x00#其他故障总数N4

\x08#可充电储能装置电压数据
\x01#可充电储能子系统个数
\x01#可充电储能子系统号
\r\xb8#可充电储能装置电压
'\x10#可充电储能装置电流
\x00`#单体电池总数
\x00\x01#本帧起始电池序号
`#本帧单体电池总数
\x0e
O
\x0e
D
\x0e
F
\x0e
I
\x0e
G
\x0e
G
\x0e
J
\x0e
		15
@
\x0e
F
\x0e
L
\x0e
O
\x0e
P
\x0e
G
\x0e
F
\x0e
C
		30
\x0e
A
\x0e
D
\x0e
C
\x0e
F
\x0e
L
\x0e
J
\x0e
M
\x0e
		45
I
\x0e
F
\x0e
G
\x0e
F
\x0e
F
\x0e
J
\x0e
F
\x0e
D
\x0e
J
\x0e
G
\x0e
G
\x0e
I
\x0e
G
		70
\x0e
G
\x0e
=
\x0e
I
\x0e
>
		78
\x0e平台交换协议数据
A
\x0e
>
\x0e
C
\x0e
F
\x0e
G
\x0e
A
\x0e
F
\x0e
D
\x0e
C
\x0e
M
\x0e
L
\x0e
I
\x0e
M
\x0e
I
\x0e
J
\x0e
F
\x0e
I
\x0e
J
\x0e
L
\x0e
I
\x0eL\x0eL\x0eG\x0eO\x0eI\x0eL\x0eL\x0eP\x0eG\x0eO\x0eG\x0eO\x0eF\x0eA\x0eD\x0eF\x0eG\x0eD\x0eD\x0eI\x0eI\x0eD\x0eG\x0eC\x0eG\x0eI\x0eF\x0eG\x0eM\x0eC\x0eJ\x0eG\x0eM\x0e@\x0eL\x0eA\x0eJ\t\x01\x01\x00\x10HHHHHHHHGGHHHHHH\xcc


'''




