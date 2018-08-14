#coding=utf8
import struct
from math import ceil

from VBase import VehiclePacket
from VRealTime import Alarm, DriveMotor, Engine, Extreme, FuelCell, Temperature, Vehicle, VehicleLocation, Voltage


class VehicleRealTime(VehiclePacket):
    """
    实时信息、补发信息上报的数据包：起始符 + 命令单元 + 识别码 + 数据加密方式 + 数据单元长度 + [数据单元] + 校验码
    [数据单元]：[数据采集时间] + [整车数据] + [驱动电机数据] + [燃料电池数据] + [发动机数据] + [车辆位置数据] + [极值数据] + [报警数据] + [可充电储能装置温度数据] + [可充电储能装置电压数据]
    """

    def __init__(self):
        super(VehicleRealTime, self).__init__()

        # 数据包第二部分：数据单元部分 + 校验码
        # 数据采集时间
        self.bj_year = None  # 北京时间：年(2位)
        self.bj_month = None  # 北京时间：月
        self.bj_day = None  # 北京时间：日
        self.bj_hour = None  # 北京时间：时
        self.bj_minute = None  # 北京时间：分
        self.bj_second = None  # 北京时间：秒

        # 整车数据
        self.vehicle = Vehicle()

        # 驱动电机数据
        self.total_drive_motor = None
        self.drive_motor = None

        # 燃料电池数据
        self.fuel_cell = FuelCell()

        # 发动机数据
        self.engine = Engine()

        # 车辆位置数据
        self.vehicle_location = VehicleLocation()

        # 极值数据
        self.extreme = Extreme()

        # 报警数据
        self.alarm = Alarm()

        # 可充电储能装置电压数据
        self.voltage_total_subsys = None  # 可充电储能子系统个数
        self.voltage = None

        # 可充电储能装置温度数据
        self.temp_total_subsys = None  # 可充电储能子系统个数
        self.temp = None

        self.type1 = None  # 第一类数据包（主包），可充电储能子系统电压数据中本帧单体电池总数为200
        self.type2 = None  # 整个数据包中只有0x08这类数据

    def handle_back(self, packet):
        """
        对数据包的后部进行处理
        处理顺序：
            先处理 数据采集时间
            将packet进行切片，去掉已处理的内容
            进入循环：
                取packet第一位，判断类型，处理对应的数据
                将packet进行切片，去掉已处理的数据
                直到packet长度为1，说明已到校验码，处理校验码并停止循环
        :param packet: 数据包的后部
        :type packet: bytes
        """
        # 处理数据采集时间
        self._unpack_time(packet[0:6])

        packet = packet[6:]

        packet_type = {0x01: False, 0x02: False, 0x03: False, 0x04: False, 0x05: False, 0x06: False, 0x07: False,
                       0x08: False, 0x09: False, 'count': 0}

        while True:
            if len(packet) == 1:
                break

            info_type, = struct.unpack('!B', packet[0:1])

            if info_type == 0x01:  # 处理整车数据
                self._unpack_vehicle(packet[1:21])
                packet = packet[21:]

                packet_type[info_type] = True
                packet_type['count'] += 1

            elif info_type == 0x02:  # 处理驱动电机数据
                self.total_drive_motor, = struct.unpack('!B', packet[1:2])  # 取得驱动电机个数
                self.drive_motor = DriveMotor(self.total_drive_motor)

                packet_drive_motor_start = 2
                packet_drive_motor_end = packet_drive_motor_start + 12
                packet_drive_motor = packet[packet_drive_motor_start:packet_drive_motor_end]

                for motor_iter in range(self.total_drive_motor):
                    self._unpack_drive_motor(motor_iter, packet_drive_motor)
                    if self.total_drive_motor - motor_iter > 1:
                        packet_drive_motor_start = packet_drive_motor_end
                        packet_drive_motor_end = packet_drive_motor_end + 12
                        packet_drive_motor = packet[packet_drive_motor_start: packet_drive_motor_end]

                packet = packet[packet_drive_motor_end:]

                packet_type[info_type] = True
                packet_type['count'] += 1

            elif info_type == 0x03:  # 处理燃料电池数据
                self._unpack_fuel_cell(packet)
                packet = packet[19 + self.fuel_cell.total_TEMP_probe:]

                packet_type[info_type] = True
                packet_type['count'] += 1

            elif info_type == 0x04:  # 处理发动机数据
                self._unpack_engine(packet[1:6])
                packet = packet[6:]

                packet_type[info_type] = True
                packet_type['count'] += 1

            elif info_type == 0x05:  # 处理车辆位置数据
                self._unpack_vehicle_location(packet[1:10])
                packet = packet[10:]

                packet_type[info_type] = True
                packet_type['count'] += 1

            elif info_type == 0x06:  # 处理极值数据
                self._unpack_extreme(packet[1:15])
                packet = packet[15:]

                packet_type[info_type] = True
                packet_type['count'] += 1

            elif info_type == 0x07:  # 处理报警数据
                self._unpack_alarm(packet[1:10])
                packet = packet[10:]

                packet_type[info_type] = True
                packet_type['count'] += 1

            elif info_type == 0x08:
                # 取得可充电储能装置电压数据中可充电储能子系统个数
                self.voltage_total_subsys, = struct.unpack('!B', packet[1:2])

                # bug
                # \x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00
                if self.voltage_total_subsys < 1 or self.voltage_total_subsys > 250:
                    raise Exception

                self.voltage = Voltage(self.voltage_total_subsys)

                # 处理可充电储能装置电压数据
                packet_voltage_start_1 = 2
                packet_voltage_end_1 = packet_voltage_start_1 + 10
                packet_voltage_start_2 = packet_voltage_end_1
                packet_voltage_end_2 = None

                for voltage_iter in range(self.voltage_total_subsys):
                    pack_voltage_1 = packet[packet_voltage_start_1:packet_voltage_end_1]  # 第一部分数据：子系统编号~本帧单体电池总数

                    self._unpack_voltage_1(voltage_iter, pack_voltage_1)  # 解包第一部分数据

                    packet_voltage_end_2 = \
                        packet_voltage_start_2 + 2 * self.voltage.info_list[voltage_iter]['total_frame_mer_bat']

                    packet_voltage_2 = packet[packet_voltage_start_2:packet_voltage_end_2]  # 第二部分数据：单体电池电压

                    self._unpack_voltage_2(voltage_iter, packet_voltage_2)  # 解包第二部分数据

                    if self.voltage_total_subsys - voltage_iter > 1:  # 当有超过1个子系统数时，进行循环来处理各子系统的信息
                        packet_voltage_start_1 = packet_voltage_end_2
                        packet_voltage_end_1 = packet_voltage_start_1 + 10
                        packet_voltage_start_2 = packet_voltage_end_1

                packet = packet[packet_voltage_end_2:]

                packet_type[info_type] = True
                packet_type['count'] += 1

            elif info_type == 0x09:
                # 取得可充电储能装置温度数据中可充电储能子系统个数
                self.temp_total_subsys, = struct.unpack('!B', packet[1:2])

                if self.temp_total_subsys < 1 or self.temp_total_subsys > 250:
                    raise Exception

                self.temp = Temperature(self.temp_total_subsys)

                # 处理可充电储能装置温度数据
                packet_temp_start_1 = 2
                packet_temp_end_1 = packet_temp_start_1 + 3
                packet_temp_start_2 = packet_temp_end_1
                packet_temp_end_2 = None

                for temp_iter in range(self.temp_total_subsys):

                    packet_temp_1 = packet[packet_temp_start_1:packet_temp_end_1]  # 第一部分数据：子系统号+温度探针个数

                    self._unpack_temp_1(temp_iter, packet_temp_1)  # 解包第一部分数据

                    packet_temp_end_2 = packet_temp_start_2 + self.temp.info_list[temp_iter]['total_TEMP_probe']

                    packet_temp_2 = packet[packet_temp_start_2:packet_temp_end_2]  # 第二部分数据：各温度探针检测到的温度值

                    self._unpack_temp_2(temp_iter, packet_temp_2)  # 解包第二部分数据

                    if self.temp_total_subsys - temp_iter > 1:  # 当有超过1个子系统数时，进行循环来处理各子系统的信息
                        packet_temp_start_1 = packet_temp_end_2
                        packet_temp_end_1 = packet_temp_start_1 + 2
                        packet_temp_start_2 = packet_temp_end_1

                packet = packet[packet_temp_end_2:]

                packet_type[info_type] = True
                packet_type['count'] += 1

            elif 0x80 <= info_type <= 0xFE:
                # 用户自定义数据
                user_defined_length, = struct.unpack('!H', packet[1:3])
                packet = packet[3 + user_defined_length:]

            else:
                raise Exception

        # 取得校验码
        self.check_code, = struct.unpack('!B', packet)

        # 判断是否为分过包的数据
        if packet_type[0x08] and packet_type['count'] == 1:  # 只有0x08这种包，可以判断为是第二类包
            self.type2 = True
        elif self.voltage:  # 不仅仅有0x08这类包，暂时作为第一类包怀疑对象
            for info_item in self.voltage.info_list:
                if info_item['total_mer_battery'] != info_item['total_frame_mer_bat']:  # 第一类包 单体电池总数 != 本帧单体电池总数
                    self.type1 = True
                    break

    def _unpack_time(self, packet):
        """
        解析共6字节数据包：数据采集时间
        """
        (self.bj_year,  # 北京时间：年(2位)
         self.bj_month,  # 北京时间：月
         self.bj_day,  # 北京时间：日
         self.bj_hour,  # 北京时间：时
         self.bj_minute,  # 北京时间：分
         self.bj_second  # 北京时间：秒
         ) = struct.unpack('!BBBBBB', packet)

    def _unpack_vehicle(self, packet):
        """
        解析共20字节数据包：整车数据
        """
        (self.vehicle.vehicle_status,  # 车辆状态
         self.vehicle.charge_state,  # 充电状态
         self.vehicle.run_model,  # 运行模式
         self.vehicle.speed,  # 车速
         self.vehicle.accu_mile,  # 累计里程
         self.vehicle.total_voltage,  # 总电压
         self.vehicle.total_current,  # 总电流
         self.vehicle.SOC,  # SOC
         self.vehicle.DC_DC_status,  # DC-DC状态
         self.vehicle.gear,  # 档位
         self.vehicle.IR,  # 绝缘电阻
         self.vehicle.accel_pedal_travel,  # 加速踏板行程值
         self.vehicle.brake_pedal_status,  # 制动踏板状态
         ) = struct.unpack('!BBBHlHHBBBHBB', packet)

    def _unpack_drive_motor(self, motor_iter, packet):
        """
        循环接收共self.total_drive_motor * 12字节数据
        """
        (self.drive_motor.info_list[motor_iter]['DM_serial'],  # 驱动电机序号
         self.drive_motor.info_list[motor_iter]['DM_status'],  # 驱动电机状态
         self.drive_motor.info_list[motor_iter]['DM_CON_TEMP'],  # 驱动电机控制器温度
         self.drive_motor.info_list[motor_iter]['DM_speed'],  # 驱动电机转速
         self.drive_motor.info_list[motor_iter]['DM_torque'],  # 驱动电机转矩
         self.drive_motor.info_list[motor_iter]['DM_TEMP'],  # 驱动电机温度
         self.drive_motor.info_list[motor_iter]['motor_CON_in_V'],  # 电机控制器输入电压
         self.drive_motor.info_list[motor_iter]['motor_CON_DC_bus_C'],  # 电机控制器直流母线电流
         ) = struct.unpack('!BBBHHBHH', packet)

    def _unpack_fuel_cell(self, packet):
        """
        解析共8+N+10字节数据包
        """
        (self.fuel_cell.voltage,  # 燃料电池电压
         self.fuel_cell.current,  # 燃料电池电流
         self.fuel_cell.consumption_rate,  # 燃料电池消耗率
         self.fuel_cell.total_TEMP_probe  # 燃料电池温度探针总数
         ) = struct.unpack('!HHHH', packet[1:9])

        # 探针温度值
        self.fuel_cell.probe_TEMP = struct.unpack('!{}B'.format(self.fuel_cell.total_TEMP_probe),
                                                  packet[9:9 + self.fuel_cell.total_TEMP_probe])
        (self.fuel_cell.H_sys_max_TEMP,  # 氢系统中最高温度
         self.fuel_cell.H_sys_max_TEMP_probe,  # 氢系统中最高温度探针代号
         self.fuel_cell.H2_max_CONC,  # 氢气最高浓度
         self.fuel_cell.H2_max_CONC_sensor,  # 氢气最高浓度传感器代号
         self.fuel_cell.H2_max_P,  # 氢气最高压力
         self.fuel_cell.H2_max_P_sensor,  # 氢气最高压力传感器代号
         self.fuel_cell.high_P_DC_DC_state  # 高压DC/DC状态
         ) = struct.unpack('!HBHBHBB', packet[9 + self.fuel_cell.total_TEMP_probe:19 + self.fuel_cell.total_TEMP_probe])

    def _unpack_engine(self, packet):
        """
        解析共5字节的数据包：发动机数据
        """
        (self.engine.engine_state,  # 发动机状态
         self.engine.crankshaft_speed,  # 曲轴转速
         self.engine.fuel_consumption_rate  # 燃料消耗率
         ) = struct.unpack('!BHH', packet)

    def _unpack_vehicle_location(self, packet):
        """
        解析共9字节数据包：车辆位置数据
        """
        (self.vehicle_location.location_state,  # 定位状态
         self.vehicle_location.longitude,  # 经度
         self.vehicle_location.latitude  # 纬度
         ) = struct.unpack('!Bll', packet)

    def _unpack_extreme(self, packet):
        """
        解析14字节数据包：极值数据
        """
        (self.extreme.max_V_bat_subsys_serial,  # 最高电压电池子系统号
         self.extreme.max_V_bat_mer_code,  # 最高电压电池单体代号
         self.extreme.max_bat_mer_V,  # 电池单体电压最高值

         self.extreme.min_V_bat_subsys_serial,  # 最低电压电池子系统号
         self.extreme.min_V_bat_mer_code,  # 最低电压电池单体代号
         self.extreme.min_bat_mer_V,  # 电池单体电压最低值

         self.extreme.max_TEMP_subsys_serial,  # 最高温度子系统号
         self.extreme.max_TEMP_probe_serial,  # 最高温度探针序号
         self.extreme.max_TEMP,  # 最高温度值

         self.extreme.min_TEMP_subsys_serial,  # 最低温度子系统号
         self.extreme.min_TEMP_probe_serial,  # 最低温度探针序号
         self.extreme.min_TEMP  # 最低温度值
         ) = struct.unpack('!BBHBBHBBBBBB', packet)

    def _unpack_alarm(self, packet):
        """
        解析9字节数据：报警数据
        """
        (self.alarm.max_level,  # 最高报警等级
         self.alarm.general_sign,  # 通用报警标志
         self.alarm.total_device_fault,  # 可充电储能装置故障总数N1
         self.alarm.total_DM_fault,  # 驱动电机故障总数N2
         self.alarm.total_engine_fault,  # 发动机故障总数N3
         self.alarm.total_other_fault,  # 其他故障总数N4
         ) = struct.unpack('!BlBBBB', packet)

    def _unpack_temp_1(self, temp_iter, packet):
        """
        解析可充电储能装置温度数据：可充电储能子系统号 + 可充电储能温度探针个数
        """
        (self.temp.info_list[temp_iter]['subsys_serial'],  # 可充电储能子系统号
         self.temp.info_list[temp_iter]['total_TEMP_probe']  # 可充电储能温度探针个数
         ) = struct.unpack('!BH', packet)

    def _unpack_temp_2(self, temp_iter, packet):
        """
        :param temp_iter: 可充电储能子系统序号
        :type temp_iter: int
        :param packet: 数据包
        :type packet: bytes
        :return: None
        :rtype: None
        """
        # 可充电储能子系统各温度探针检测到的值构成的元组(下标从0开始)
        self.temp.info_list[temp_iter]['each_TEMP_probe_detect'] = \
            struct.unpack('!{}B'.format(self.temp.info_list[temp_iter]['total_TEMP_probe']), packet)

    def _unpack_voltage_1(self, voltage_iter, packet):
        (self.voltage.info_list[voltage_iter]['subsys_serial'],  # 可充电储能子系统号
         self.voltage.info_list[voltage_iter]['voltage'],  # 可充电储能装置电压
         self.voltage.info_list[voltage_iter]['current'],  # 可充电储能装置电流
         self.voltage.info_list[voltage_iter]['total_mer_battery'],  # 单体电池总数
         self.voltage.info_list[voltage_iter]['start_frame_bat_serial'],  # 本帧起始电池序号
         self.voltage.info_list[voltage_iter]['total_frame_mer_bat'],  # 本帧单体电池总数
         ) = struct.unpack('!BHHHHB', packet)

    def _unpack_voltage_2(self, voltage_iter, packet):
        # 单体电池电压构成的元组(下标从0开始)
        self.voltage.info_list[voltage_iter]['mer_bat_voltage'] \
            = struct.unpack('!{}H'.format(self.voltage.info_list[voltage_iter]['total_frame_mer_bat']), packet)

    @staticmethod
    def response(packet, flag=0x02):
        """
         实时、补发应答
         flag的值：
             0x02 错误
         """
        temp_packet = bytearray(packet)

        temp_packet[3:4] = struct.pack('!B', flag)  # 修改应答标识

        # 计算新报文的校验码
        bcc = 0x00
        for _ in temp_packet[2:-1]:
            bcc ^= _

        temp_packet[-1:] = struct.pack('!B', bcc)  # 修改新报文的校验码

        return bytes(temp_packet)

    def instance_to_dict(self):
        """
        将类的实例属性处理为字典类型的数据
        :return: 实时信息所组成的字典
        :rtype: dict
        """
        return {
            'time': '20{0}-{1:0>2d}-{2:0>2d} {3:0>2d}:{4:0>2d}:{5:0>2d}'.format(self.bj_year, self.bj_month,
                                                                                self.bj_day, self.bj_hour,
                                                                                self.bj_minute, self.bj_second),

            'start_char': self.start_char.decode('utf-8'),  # 起始符
            'cmd_ID': self.cmd_ID,  # 命令单元-命令标识
            'response_flag': self.response_flag,  # 命令单元-应答标志
            'VIN': self.VIN,  # 车辆唯一标识码
            'data_enc': self.data_enc,  # 数据单元加密方式
            'data_unit_len': self.data_unit_len,  # 数据单元长度

            # 时间
            'bj_year': self.bj_year,
            'bj_month': self.bj_month,
            'bj_day': self.bj_day,
            'bj_hour': self.bj_hour,
            'bj_minute': self.bj_minute,
            'bj_second': self.bj_second,

            # 整车数据
            'vehicle': self.vehicle.__dict__ if self.vehicle else {},

            # 驱动电机数据
            'drive_motor': self.drive_motor.__dict__ if self.drive_motor else {},

            # 燃料电池数据
            'fuel_cell': self.fuel_cell.__dict__,

            # 发动机数据
            'engine': self.engine.__dict__,

            # 车辆位置数据
            'vehicle_location': self.vehicle_location.__dict__,

            # 极值数据
            'extreme': self.extreme.__dict__,

            # 报警数据
            'alarm': self.alarm.__dict__,

            # 可充电储能装置温度数据
            'temp': self.temp.__dict__ if self.temp else {},

            # 可充电储能装置电压数据
            'voltage': self.voltage.__dict__ if self.voltage else {},

            # 校验码
            'check_code': self.check_code
        }

    def status_to_dict(self):
        """
        车辆信息
        """
        return {
            'VIN': self.VIN,
            'vehicle_status': self.vehicle.vehicle_status,
            'charge_state': self.vehicle.charge_state,
            'max_level': self.alarm.max_level,
            'location_state': self.vehicle_location.location_state,
            'longitude': self.vehicle_location.longitude,
            'latitude': self.vehicle_location.latitude
        }

    def separate_info(self, packet):
        """
        给分包的数据包加上标识
        """
        sign = struct.pack('!2s', b'##')  # 标识这是分包数据

        total_mer_battery_int = self.voltage.info_list[0]['total_mer_battery']  # 电池总数

#################这个数组很奇怪

        total_mer_battery_bin = struct.pack('!H', ceil(total_mer_battery_int / 200))

        start_frame_bat_serial = self.voltage.info_list[0]['start_frame_bat_serial']  # 本帧起始电池序号

        relative_position = struct.pack('!H', start_frame_bat_serial // 200)  # 本帧相当于所有分包数据的位置，从0开始

        return packet + sign + total_mer_battery_bin + relative_position
