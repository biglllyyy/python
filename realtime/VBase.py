#coding=utf8
import struct


class VehiclePacket(object):
    """
    作为 车辆登入、实时信息上报、补发数据上报、车辆登出、心跳、终端校时 的父类，包含：
    1. 共同的字段：起始符、命令标识、应答标识、VIN、数据单元加密方式、数据单元长度、校验码
    2. 共同的方法：对数据包前24字节的处理
    """
    HEAD_24BYTES = 24  # 将数据包分为两部分，第一部分部分为24字节

    def __init__(self):
        # 以下为所有数据包共有的第一部分：数据包前24字节
        self.start_char = None  # 起始符
        self.cmd_ID = None  # 命令单元-命令标识
        self.response_flag = None  # 命令单元-应答标志
        self.VIN = None  # 车辆唯一标识码
        self.data_enc = None  # 数据单元加密方式
        self.data_unit_len = None  # 数据单元长度

        # 以下为所有数据包共有的第二部分
        self.check_code = None  # 校验码

    def unpack_head(self, head_24bytes):
        """
        对24字节的数据包(头部)进行处理，可以得到：
        起始符、命令单元-命令标识、命令单元-应答标志、唯一识别码、数据单元加密方式、数据单元长度
        """
        (self.start_char,
         self.cmd_ID,
         self.response_flag,
         self.VIN,
         self.data_enc,
         self.data_unit_len) = struct.unpack('!2sBB17sBH', head_24bytes)

        if self.response_flag != 0xfe:
            raise Exception


class VehicleFunction(VehiclePacket):
    """
    作为 终端校时、心跳 的父类
    """

    def __init__(self):
        super(VehicleFunction, self).__init__()

    def unpack_back(self, back_packet):
        """
        对数据包第二部分进行解包
        :param back_packet: 数据包第二部分，即校验码
        :type back_packet: bytes
        :return: None
        :rtype: None
        """
        self.check_code = struct.unpack('!B', back_packet)
