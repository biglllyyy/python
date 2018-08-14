#coding=utf8
import binascii
import datetime
import sys

def read_file(file_name,file_log,write_path):
    """
    读取文件，提取文件每一行的数据
    :param file_name: './hbase.txt'
    :type file_name: str
    :return: [(b'170606GB06CZH0045', '2017-07-21 17:31:39', '232302FE31373036303647423036435A4830303435010010110715111F270500069BD42001F13C685A')]
    :rtype: list
    """
    id_a = 0
    id_b=0
    start_time=datetime.datetime.now()
    with open(file_name, 'r') as f:
        for line in f.readlines():
            try:
                hex_data = get_hex_data(line[3:])
                vin = get_packet_vin(hex_data[8:42])
#                packet_time = get_packet_time(hex_data[48:60])
                result_data=str(vin)+','+str(hex_data)+'\n'
                save_file(write_path,result_data)
#                print id
                id_a += 1
            except:
                id_b += 1
                print file_name+'data_erro num :'+id_b
                log=file_name+'data_erro num :'+id_b
                save_log(file_log,log)
                hex_data = get_hex_data(line[3:])
                result_data=''+str(hex_data)
                save_log(write_path,result_data)
                continue
    save_log(str(id_a)+":正常解析条数",file_log)
    save_log(str(id_b)+":异常解析条数",file_log)
            # # 返回格式：(VIN, 报文时间，16进制数据)
            # result_data.append((vin, packet_time, hex_data))
    end_time=datetime.datetime.now()
    spend_time=end_time-start_time
    print "处理"+file_name+"所花时间："+str(spend_time)


def get_hex_data(str_data):
    """
    从字符串数据中提取16进制字符串数据
    :param str_data: '\\N,23 23 02 FE 31 37 30 36 30 36 47 42 30 36 43 5A 48 30 30 34 35 01 00 10 11 07 15 11 1F 27 05 00 06 9B D4 20 01 F1 3C 68 5A\n'
    :type str_data: str
    :return: '232302FE31373036303647423036435A4830303435010010110715111F270500069BD42001F13C685A'
    :rtype: str
    """
    temp_hex_data = str_data.replace(' ', '')
    hex_data = temp_hex_data.replace('\n', '')
    return hex_data


def get_packet_vin(hex_data):
    """
    从16进制数据中提取vin
    :param hex_data: '31373036303647423036435A4830303435'
    :type hex_data: str
    :return: b'170606GB06CZH0045'
    :rtype: bytes
    """
    return str(binascii.a2b_hex(hex_data))


def get_packet_time(hex_data):
    """
    从16进制数据中提取时间
    :param hex_data: '110715111F27'
    :type hex_data: str
    :return: '2017-07-21 17:31:39'
    :rtype: str
    """
    year = int(hex_data[0:2], 16)
    month = int(hex_data[2:4], 16)
    day = int(hex_data[4:6], 16)
    hour = int(hex_data[6:8], 16)
    minute = int(hex_data[8:10], 16)
    second = int(hex_data[10:12], 16)
    packet_time = '20{0}-{1:0>2d}-{2:0>2d} {3:0>2d}:{4:0>2d}:{5:0>2d}'.format(year, month, day, hour, minute, second)
    return packet_time

def save_file(write_path, context):
    with open(write_path, 'a') as f:
        f.write(context)

def save_log(write_path, context):
    with open(write_path, 'a') as f:
        f.write(context)

if __name__ == '__main__':
    num=1
    for i in sys.stdin:
        print "正在处理"+i
#        print i
        read_file(i,'all.log',str(i)+'.txt')
#     read_file('000002_0','all.log','./hbase_2.txt')
        print "处理完成"+i

        num+=1