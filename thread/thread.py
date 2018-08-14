#coding=utf8
import binascii
import datetime
from multiprocessing import Pool


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
    :return: '170606GB06CZH0045'
    :rtype: str
    """
    return binascii.a2b_hex(hex_data).decode('utf-8')


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


def process(line_data):
    hex_data = get_hex_data(line_data[3:])
    vin = get_packet_vin(hex_data[8:42])
    packet_time = get_packet_time(hex_data[48:60])

    return vin + ',' + packet_time + ',' + hex_data + ',' + packet_time + '\n'


def run(process_num, source_file, target_file):
    """
    以多进程的方式，从源文件(source_file)中读取数据，转换到目标文件(target_file)中
    :param process_num: 进程数
    :type process_num: int
    :param source_file: 源文件
    :type source_file: str
    :param target_file: 目标文件
    :type target_file: str
    :return: None
    :rtype: None
    """
    start_time = datetime.datetime.now()
    print('开始时间: {}'.format(start_time))

    pool = Pool(process_num)

    with open(target_file, 'a') as f_target:
        with open(source_file, 'r') as f_source:
            result_list = pool.map(process, f_source, 150)

            read_time = datetime.datetime.now()
            print('读源文件耗时: {}'.format(read_time - start_time))

            for each_one in result_list:
                f_target.write(each_one)

    end_time = datetime.datetime.now()
    print('结束时间: {}'.format(end_time))
    print('写文件耗时: {}'.format(end_time - read_time))
    print('转换总耗时: {}'.format(end_time - start_time))


if __name__ == '__main__':
    run(4, 'D:\\application_program\\python\\123.txt','D:\\application_program\\python\\hbase.txt')  # 以4个进程的方式来做文件转换
