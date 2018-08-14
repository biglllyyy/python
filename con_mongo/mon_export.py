# #coding=utf8
# from pymongo import MongoClient
#
# def get_VIN(path,arr):
#     with open(path,'r') as f:
#         for line in f.readlines():
#             line=line.split(',')
#             arr.append(line[0])
#             # save_file(line)
#             # print line[0]
#
# def save_file(path,context):
#     with open(path,'a') as f:
#         f.write(context)
#
# # for i in collection.find({'time': {'$gte':"2017-08-01 00:01:00", '$lt':"2017-09-15 00:01:00"}}):
# #LDPAAAKB0HC003751
# def sear(VIN):
#     client = MongoClient('10.99.6.8:8015,10.99.6.9:8013,10.99.6.11:8014')
#     db=client.parsed_data_storage
#     # collection=db.myTestCollection
#     # collection = db.data
#     collection = db.parsed_real_data_w02
#
#     rs_map = {}
#     for j in VIN:
#         print (type(j))
#         print (j)
#
#         try:
#             for i in collection.find({"VIN":j}):
#                     #,'time': '2017-09-05 10:41'
#                 try:
#                     result = str(i.get('VIN'))+','+str(i.get('vehicle_location').get('latitude')) \
#                            + ','+str(i.get('vehicle_location').get('location_state')) \
#                            + ','+str(i.get('vehicle_location').get('longitude'))\
#                            +','+str(i.get('time'))+','+str(i.get('vehicle').get('accu_mile'))+'\n'
#                     print (result)
#                 except:
#                     print ('parse error')
#
#                 print (result)
#                 save_file('/workspace/teshang_file', result)
#                 if result:
#                     break
#         except:
#             print ('VIN error')
#             print (j)
#
#
#
#
# if __name__ == '__main__':
#     arr_v = []
#     get_VIN('/workspace/teshang',arr_v)
#     sear(arr_v)
#


from pymongo import MongoClient

def save_file(path, content):
    with open(path, 'a') as f:
        f.write(content)


def parse_mon(list_vin):
    client = MongoClient('10.99.6.8:8015,10.99.6.9:8013,10.99.6.11:8014')
    db = client.parsed_data_storage
    first_time = None
    last_time = None
    for vin in list_vin:
        collention = db.parsed_real_data_w01
        for i in collention.find({'VIN':vin}):
            i = dict(i)
            m_time = i['time']
            print(type(i.get('vehicle').get('accu_mile')))
            if str(i.get('vehicle').get('accu_mile')) != None and 0<i.get('vehicle').get('accu_mile')<100000:
                result1 = i['VIN'] + ',' + str(m_time) + ',' + str(i.get('vehicle').get('accu_mile')) + '\n'
                print(result1)
                count=0
                save_file('/workspace/dataExport/file/vinLicheng',result1 + '\n')
                list_vin.remove(vin)
                if result1:
                    break
    # for vin in list_vin:
    #     collention = db.parsed_real_data_w01
    #     for i in collention.find({'VIN':vin}):
    #         i = dict(i)
    #         m_time = i['time']
    #         print(type(i.get('vehicle').get('accu_mile')))
    #         if i.get('vehicle').get('accu_mile') :
    #             if str(i.get('vehicle').get('accu_mile')) != None and 0<i.get('vehicle').get('accu_mile')<100000:
    #                 result1 = i['VIN'] + ',' + str(m_time) + ',' + str(i.get('vehicle').get('accu_mile')) + '\n'
    #                 print(result1)
    #                 save_file('/workspace/dataExport/file/vinLicheng',result1 + '\n')
    #                 list_vin.remove(vin)
    #                 if result1:
    #                     break
    # for vin in list_vin:
    #     collention = db.parsed_real_data_w02
    #     for i in collention.find({'VIN':vin}):
    #         i = dict(i)
    #         m_time = i['time']
    #         print(type(i.get('vehicle').get('accu_mile')))
    #         if i.get('vehicle').get('accu_mile') :
    #             if str(i.get('vehicle').get('accu_mile')) != None and 0<i.get('vehicle').get('accu_mile')<100000:
    #                 result1 = i['VIN'] + ',' + str(m_time) + ',' + str(i.get('vehicle').get('accu_mile')) + '\n'
    #                 print(result1)
    #                 save_file('/workspace/dataExport/file/vinLicheng',result1 + '\n')
    #                 list_vin.remove(vin)
    #                 if result1:
    #                     break
    # for vin in list_vin:
    #     collention = db.parsed_real_data_w03
    #     for i in collention.find({'VIN':vin}):
    #         i = dict(i)
    #         m_time = i['time']
    #         print(type(i.get('vehicle').get('accu_mile')))
    #         if i.get('vehicle').get('accu_mile') :
    #             if str(i.get('vehicle').get('accu_mile')) != None and 0<i.get('vehicle').get('accu_mile')<100000:
    #                 result1 = i['VIN'] + ',' + str(m_time) + ',' + str(i.get('vehicle').get('accu_mile')) + '\n'
    #                 print(result1)
    #                 save_file('/workspace/dataExport/file/vinLicheng',result1 + '\n')
    #                 list_vin.remove(vin)
    #                 if result1:
    #                     break
    # for vin in list_vin:
    #     collention = db.parsed_real_data_w04
    #     for i in collention.find({'VIN':vin}):
    #         i = dict(i)
    #         m_time = i['time']
    #         print(type(i.get('vehicle').get('accu_mile')))
    #         if i.get('vehicle').get('accu_mile') :
    #             if str(i.get('vehicle').get('accu_mile')) != None and 0<i.get('vehicle').get('accu_mile')<100000:
    #                 result1 = i['VIN'] + ',' + str(m_time) + ',' + str(i.get('vehicle').get('accu_mile')) + '\n'
    #                 print(result1)
    #                 save_file('/workspace/dataExport/file/vinLicheng',result1 + '\n')
    #                 list_vin.remove(vin)
    #                 if result1:
    #                     break

def read_file(path, list):
    with open(path) as f:
        for line in f.readlines():
            line = line.split('\n')[0]
            list.append(line)


if __name__ == '__main__':
    dic = {}
    list_time = []
    first_time = None
    last_time = None
    vin_list_1 = []

    path_1 = '/workspace/dataExport/vin.txt'

    read_file(path_1, vin_list_1)
    parse_mon(vin_list_1)