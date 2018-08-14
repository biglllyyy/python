#coding=utf8
import binascii

a='232301FE4C44504141414B4230474330313032323801001E1108090D0C36000138393836303331363430323030323235353438300100EB'



def login_analysis(input):
    """
    起始符##
    16进制转字符
    """
    start= binascii.a2b_hex(input[0:4])

    """
    车辆登入
    """
    vehicle="\\x"+input[4:6]

    """
    主动发起方标志
    """
    source= "\\x"+input[6:8]

    """
    VIN:[8:42]
    """
    vin= binascii.a2b_hex(input[8:42])

    """
    加密方式
    """
    way= "\\x"+input[42:44]

    """
    数据单元长度
    """
    data_long= "\\x"+input[44:46]+"\\x"+input[46:48]

    """
    时间
    """
    data_time= "\\x"+input[48:50]+"\\x"+input[50:52]+"\\x"+input[52:54]+"\\x"+input[54:56]+"\\x"+input[56:58]+"\\x"+input[58:60]

    """
    登录流水号
    """
    number= "\\x"+input[60:62]+"\\x"+input[62:64]

    """
    车辆ICCID
    """
    ICCID=  binascii.a2b_hex(input[64:104])

    """
    可充电储能系统数
    """
    battery_num= "\\x"+input[104:106]

    """
    可充电储能系统编码长度
    """
    battery_long= "\\x"+input[106:108]

    """
    校验码
    """
    check_code= "\\x"+input[108:]

    print "登入信息："+start+vehicle+source+vin+way+data_long+data_time+number+ICCID+battery_num+battery_long+check_code

def logout_analysis(input):
    """
        起始符##
        16进制转字符
        """
    start = binascii.a2b_hex(input[0:4])

    """
    车辆登出
    """
    vehicle = "\\x" + input[4:6]

    """
    主动发起方标志
    """
    source = "\\x" + input[6:8]

    """
    VIN:[8:42]
    """
    vin = binascii.a2b_hex(input[8:42])

    """
    加密方式
    """
    way = "\\x" + input[42:44]

    """
    数据单元长度
    """
    data_long = "\\x" + input[44:46] + "\\x" + input[46:48]

    """
    时间
    """
    data_time= "\\x"+input[48:50]+"\\x"+input[50:52]+"\\x"+input[52:54]+"\\x"+input[54:56]+"\\x"+input[56:58]+"\\x"+input[58:60]

    """
    登录流水号
    """
    number = "\\x" + input[60:62] + "\\x" + input[62:64]

    """
    校验码
    """
    check_code = "\\x" + input[64:]

    print "登入信息：" + start + vehicle + source + vin + way + data_long + data_time + number + check_code


def realtime(input):
    """
        起始符##
        16进制转字符
        """
    start = binascii.a2b_hex(input[0:4])

    """
    车辆登出
    """
    vehicle = "\\x" + input[4:6]

    """
    主动发起方标志
    """
    source = "\\x" + input[6:8]

    """
    VIN:[8:42]
    """
    vin = binascii.a2b_hex(input[8:42])

    """
    加密方式
    """
    way = "\\x" + input[42:44]

    """
    数据单元长度
    """
    data_long = "\\x" + input[44:46] + "\\x" + input[46:48]

    """
    时间
    """

    """
    登录流水号
    """
    number = "\\x" + input[60:62] + "\\x" + input[62:64]

    """
    校验码
    """
    check_code = "\\x" + input[64:]

    print "登入信息：" + start + vehicle + source + vin + way + data_long + data_time + number + ICCID + battery_num + battery_long + check_code




if __name__ == '__main__':
    a = '232301FE4C44504141414B4230474330313032323801001E1108090D0C36000138393836303331363430323030323235353438300100EB'
    b='232304FE4C44504141414B423047433031303232380100081108090D0C380002F5'
    login_analysis(a)
