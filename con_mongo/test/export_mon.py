from pymongo import MongoClient


def save_file(path,context):
    with open(path,'a') as f:
        f.write(context)

def get_VIN(path,arr):
    with open(path,'r') as f:
        for line in f.readlines():
            line=line.split('\n')
            arr.append(line[0])

client = MongoClient('10.99.6.8:8015,10.99.6.9:8013,10.99.6.11:8014')

db = client.parsed_data_storage

collect = db.myTestCollection

arr = []
get_VIN('/workspace/yunqi', arr)
for j in arr:
    print(j)
    for i in collect.find({'VIN':j}):
        result = str(i.get('VIN')) + ',' + str(i.get('vehicle_location').get('latitude')) \
                 + ',' + str(i.get('vehicle_location').get('location_state')) \
                 + ',' + str(i.get('vehicle_location').get('longitude')) \
                 + ',' + str(i.get('time')) + ',' + str(i.get('vehicle').get('accu_mile')) + '\n'
        print(result)
        save_file('/workspace/yunqi_file',result)
        if result:
            break
    # print(i)



