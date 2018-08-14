#coding=utf8
class Vehicle(object):
    """
    整车数据
    """

    def __init__(self):
        self.vehicle_status = None  # 车辆状态
        self.charge_state = None  # 充电状态
        self.run_model = None  # 运行模式
        self.speed = None  # 车速
        self.accu_mile = None  # 累计里程
        self.total_voltage = None  # 总电压
        self.total_current = None  # 总电流
        self.SOC = None  # SOC
        self.DC_DC_status = None  # DC-DC状态
        self.gear = None  # 档位
        self.IR = None  # 绝缘电阻
        self.accel_pedal_travel = None  # 加速踏板行程值
        self.brake_pedal_status = None  # 制动踏板状态


class DriveMotor(object):
    """
    驱动电机数据：驱动电机总数(N) + 驱动电机序号为1的电机数据 + ... + 驱动电机序号为N的电机数据
    """

    def __init__(self, total_drive_motor):
        self.total_drive_motor = total_drive_motor  # 驱动电机个数
        self.info_list = []  # 驱动电机总成信息列表
        self._init_info_list()

    def _init_info_list(self):
        """
        根据实际的<驱动电机个数>来构造实际的<驱动电机总成信息列表>
        """
        for _ in range(self.total_drive_motor):
            self.info_list.append(
                dict(DM_serial=None,  # 驱动电机序号
                     DM_status=None,  # 驱动电机状态
                     DM_CON_TEMP=None,  # 驱动电机控制器温度
                     DM_speed=None,  # 驱动电机转速
                     DM_torque=None,  # 驱动电机转矩
                     DM_TEMP=None,  # 驱动电机温度
                     motor_CON_in_V=None,  # 电机控制器输入电压
                     motor_CON_DC_bus_C=None  # 电机控制器直流母线电流
                     )
            )


class FuelCell(object):
    """
    燃料电池数据
    """

    def __init__(self):
        self.voltage = None  # 燃料电池电压
        self.current = None  # 燃料电池电流
        self.consumption_rate = None  # 燃料电池消耗率

        self.total_TEMP_probe = None  # 燃料电池温度探针总数
        self.probe_TEMP = None  # 探针温度值

        self.H_sys_max_TEMP = None  # 氢系统中最高温度
        self.H_sys_max_TEMP_probe = None  # 氢系统中最高温度探针代号

        self.H2_max_CONC = None  # 氢气最高浓度
        self.H2_max_CONC_sensor = None  # 氢气最高浓度传感器代号

        self.H2_max_P = None  # 氢气最高压力
        self.H2_max_P_sensor = None  # 氢气最高压力传感器代号

        self.high_P_DC_DC_state = None  # 高压DC/DC状态


class Engine(object):
    """
    发动机数据
    """

    def __init__(self):
        self.engine_state = None  # 发动机状态
        self.crankshaft_speed = None  # 曲轴转速
        self.fuel_consumption_rate = None  # 燃料消耗率


class VehicleLocation(object):
    """
    车辆位置数据
    """

    def __init__(self):
        self.location_state = None  # 定位状态
        self.longitude = None  # 经度
        self.latitude = None  # 纬度


class Extreme(object):
    """
    极值数据
    """

    def __init__(self):
        self.max_V_bat_subsys_serial = None  # 最高电压电池子系统号
        self.max_V_bat_mer_code = None  # 最高电压电池单体代号
        self.max_bat_mer_V = None  # 电池单体电压最高值

        self.min_V_bat_subsys_serial = None  # 最低电压电池子系统号
        self.min_V_bat_mer_code = None  # 最低电压电池单体代号
        self.min_bat_mer_V = None  # 电池单体电压最低值

        self.max_TEMP_subsys_serial = None  # 最高温度子系统号
        self.max_TEMP_probe_serial = None  # 最高温度探针序号
        self.max_TEMP = None  # 最高温度值

        self.min_TEMP_subsys_serial = None  # 最低温度子系统号
        self.min_TEMP_probe_serial = None  # 最低温度探针序号
        self.min_TEMP = None  # 最低温度值


class Alarm(object):
    """
    报警数据
    """

    def __init__(self):
        self.max_level = None  # 最高报警等级
        self.general_sign = None  # 通用报警标志
        self.total_device_fault = None  # 可充电储能装置故障总数N1
        self.total_DM_fault = None  # 驱动电机故障总数N2
        self.total_engine_fault = None  # 发动机故障总数N3
        self.total_other_fault = None  # 其他故障总数N4


class Voltage(object):
    """
    可充电储能系统电压数据：可充电储能子系统个数(N) + 可充电储能子系统号为1的系统数据 + ... + 可充电储能子系统号为N的系统数据
    """

    def __init__(self, total_subsys):
        self.total_subsys = total_subsys  # 可充电储能子系统个数
        self.info_list = []  # 可充电储能子系统电压信息列表
        self._init_info_list()

    def _init_info_list(self):
        """
        根据实际的<可充电储能子系统个数>来构造实际的<驱动电机总成信息列表>
        """
        for _ in range(self.total_subsys):  # 可充电储能子系统号为1~250
            self.info_list.append(
                dict(subsys_serial=None,  # 可充电储能子系统号
                     voltage=None,  # 可充电储能装置电压
                     current=None,  # 可充电储能装置电流
                     total_mer_battery=None,  # 单体电池总数
                     start_frame_bat_serial=None,  # 本帧起始电池序号
                     total_frame_mer_bat=None,  # 本帧单体电池总数
                     mer_bat_voltage=None  # 单体电池电压
                     )
            )


class Temperature(object):
    """
    可充电储能系统温度数据：可充电储能子系统个数(N) + 可充电储能子系统号为1的系统数据 + ... + 可充电储能子系统号为N的系统数据
    """

    def __init__(self, total_subsys):
        self.total_subsys = total_subsys  # 可充电储能子系统个数
        self.info_list = []  # 可充电储能子系统温度信息列表
        self._init_info_list()

    def _init_info_list(self):
        """
        根据实际的<可充电储能子系统个数>来构造实际的<可充电储能子系统温度信息列表>
        """
        for _ in range(self.total_subsys):  # 可充电储能子系统号为1~250
            self.info_list.append(
                dict(subsys_serial=None,  # 可充电储能子系统号
                     total_TEMP_probe=None,  # 可充电储能温度探针个数
                     each_TEMP_probe_detect=None  # 可充电储能子系统各温度探针检测到的值
                     )
            )
