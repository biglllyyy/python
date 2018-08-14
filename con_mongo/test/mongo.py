from pymongo import MongoClient

def save_file(path,content):
    with open(path,'a') as f:
        f.write(content)

def parse_mon(list_vin,collec='data'):
    client = MongoClient('10.99.6.8:8015,10.99.6.9:8013,10.99.6.11:8014')
    db = client.parsed_data_storage
    collention = db.parsed_real_data_w04
    first_time = None
    last_time = None
    for vin in list_vin:
        save_file('/workspace/dataExport/file/' + str(vin), str(collec)+'\n')
        for i in collention.find({'VIN':vin}):
            i = dict(i)

            m_time = i['time']

            if first_time == None:

                first_time = m_time
                last_time = m_time
            elif m_time > last_time:
                last_time = m_time
            elif m_time < first_time:
                first_time = m_time
        # if first_time !=  None:
        #     print('first_time is '+str(first_time)+'\n'+'last_time is '+str(last_time))


        for i in collention.find({'VIN': vin}):
            i = dict(i)
            if i['time'] == first_time:
                result1 = 'first_time is' + i['VIN'] + ',' + str(first_time) + ',' + str(i.get('vehicle').get('accu_mile'))+'\n'
                print(result1)
                save_file('/workspace/dataExport/file/'+str(vin),result1)

            if i['time'] == last_time:
                result2 = 'last_time is' + i['VIN'] + ',' + str(last_time) + ',' + str(i.get('vehicle').get('accu_mile'))+'\n'
                print(result2)
                save_file('/workspace/dataExport/file/'+str(vin), result2)

def read_file(path,list):
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
    # vin_list_2 = []
    # vin_list_3 = []
    path_1 = '/workspace/dataExport/vin.txt'
    # path_2 = '/workspace/licheng/vin_list_A6'
    # path_3 = '/workspace/licheng/vin_list_chengE3'
    read_file(path_1,vin_list_1)
    # read_file(path_2,vin_list_2)
    # read_file(path_3,vin_list_3)
    parse_mon(vin_list_1)
    # parse_mon(vin_list_2)
    # parse_mon(vin_list_3)



    # parse_mon(vin_list_1, 'myTestCollection')
    # parse_mon(vin_list_1, 'parsed_real_data_w01')
    # parse_mon(vin_list_1, 'parsed_real_data_w02')
    # parse_mon(vin_list_1, 'parsed_real_data_w03')
    # parse_mon(vin_list_1, 'parsed_real_data_w04')

    # parse_mon(vin_list_2, 'parsed_real_data_w01')
    # parse_mon(vin_list_2, 'parsed_real_data_w02')
    # parse_mon(vin_list_2, 'parsed_real_data_w03')
    # parse_mon(vin_list_2, 'parsed_real_data_w04')
    #
    # parse_mon(vin_list_3, 'parsed_real_data_w01')
    # parse_mon(vin_list_3, 'parsed_real_data_w02')
    # parse_mon(vin_list_3, 'parsed_real_data_w03')
    # parse_mon(vin_list_3, 'parsed_real_data_w04')

