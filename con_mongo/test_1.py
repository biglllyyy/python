# #coding=utf8
# import requests
# import  xml.dom.minidom
# def get_city_name(city_id):
#     #打开xml文档
#     dom = xml.dom.minidom.parse('D:\\Cities.xml')
#
#     #得到文档元素对象
#     root = dom.documentElement
#
#     itemlist = root.getElementsByTagName('City')
#     # item = itemlist[0]
#     for item in itemlist:
#         un=item.getAttribute("ID")
#         # print type(un)
#         pd=item.getAttribute("CityName")
#         # print pd
#         if int(city_id) == int(un):
#             return pd
#
# def locatebyAddr(address, city=None):
#     '''
#     根据地址确定经纬度，城市为可选项
#     '''
#     items = {'output': 'json', 'ak': 'A9f77664caa0b87520c3708a6750bbdb', 'address': address}
#     if city:
#         items['city'] = city
#     r = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
#     dictResult = r.json()
#     return dictResult['result']['location'] if not dictResult['status'] else None
#
# def locatebyLatLon(lat, lon, pois=0):
#     '''
#     根据经纬度确定地址
#     '''
#     items = {'location': str(lat) + ',' + str(lon), 'ak': 'A9f77664caa0b87520c3708a6750bbdb', 'output': 'json'}
#     if pois:
#         items['pois'] = 1
#     r = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
#     dictResult = r.json()
#     return dictResult['result'] if not dictResult['status'] else None
#
# def main():
#     # address = input('输入地址： ')
#     # city = input('输入城市：（可选）')
#     # result = locatebyAddr('北京')
#     result = locatebyLatLon(32.112888,112.251648)
#     # print(result)
#     # print result.get('cityCode')
#     return result.get('cityCode')
#
# if __name__ == '__main__':
#     print get_city_name(main())

from pymongo import  MongoClient

client = MongoClient('10.99.6.8:8015,10.99.6.9:8013,10.99.6.11:8014')
db = client.parsed_data_storage
coll="data"
collention = db.
print(str(collention))
first_time = None
last_time = None
# for vin in "LGHB2VH97GD161224":
#     print(vin)
for i in collention.find({'VIN':"LGHB2VH97GD161224"}):
    print(i)