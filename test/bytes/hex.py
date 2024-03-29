#coding=utf8
def change_bytes_to_hex_str(bytes_data):
    """
    转换bytes类型为16进制的字符串
    input:
        b"##\x01\xfeLDPZYB3D3HF225509\x01\x00'\x11\x02\x08\x0e\x14\x0f\x00\x0e89860616020004766338\x01\t120625061\xb9"
    output:
        "232301FE4C44505A594233443348463232353530390100271102080E140F000E38393836303631363032303030343736363333380109313230363235303631B9"
    """
    result_str = ''
    for i in bytes_data:

        # if len(str(hex(i)).upper()) == 3:
        if len(str(i.encode('hex')).upper()) == 3:
            result_str += '0' + str(hex(i)).upper()[-1:]
        else:
            result_str += str(i.encode('hex')).upper()[-2:]
    return result_str

if __name__ == '__main__':
    data='''##\x02\xfeLGHB2VH94HD171467\x01\x01\x19\x11\x08\t\x0b:\x1b\x01\x01\x03\x01\x00\x00\x00\x00\x00X\x0c\x16'\x10*\x01\x0e\x0b\xb8\x00\x00\x02\x01\x01\x04GN N ?\x0c\x16'\x10\x05\x00\x06\x1e0Q\x01~qA\x06\x011\x0e\x10\x01\x01\x0e\x0c\x01\x05<\x01\x0c:\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x01\x01\x0c\x16'\x10\x00V\x00\x01V\x0e\x0c\x0e\x0c\x0e\x0c\x0e\r\x0e\x0e\x0e\x0e\x0e\x0e\x0e\r\x0e\x0f\x0e\x0c\x0e\x0f\x0e\x0e\x0e\r\x0e\x0e\x0e\r\x0e\x0c\x0e\x0f\x0e\x0e\x0e\x0f\x0e\r\x0e\x0e\x0e\r\x0e\x0e\x0e\r\x0e\r\x0e\x0f\x0e\r\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0e\x0f\x0e\r\x0e\r\x0e\x0c\x0e\r\x0e\r\x0e\r\x0e\r\x0e\r\x0e\r\x0e\x0e\x0e\r\x0e\r\x0e\r\x0e\x0f\x0e\r\x0e\x0f\x0e\x10\x0e\x0f\x0e\x0e\x0e\x0f\x0e\r\x0e\x0e\x0e\x0e\x0e\x0f\x0e\x0f\x0e\r\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0f\x0e\x0e\x0e\x0e\x0e\x10\x0e\x10\x0e\x0f\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0f\x0e\x0f\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0f\x0e\r\x0e\x0e\x0e\r\x0e\x0e\x0e\x0e\x0e\x0f\t\x01\x01\x00\x10;;;;<;;<<;;:;;;;u'''
    print change_bytes_to_hex_str(data)

