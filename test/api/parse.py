import requests
import os
import _thread

url = 'http://58.49.84.92:1511/parse'

# data = '232301024C44504141414B423948463136333532380100291109120F092000B63839383630363137303230303239373334383830010B5A42414B42503130313338AA'



def get_parse(data_path,save_f):
    with open(data_path,'r') as f:
        for line in f.readlines():
            line = line.split('\n')
            print('i is ' + line)
            try:
                r = requests.post(url , line)
                print (r.json())
                time = r.json().get('time')
                vin = r.json().get('VIN')
                raw = line
                result = str(time)+','+str(vin)+','+str(raw)+','+str(time)+'\n'
                print(result)
                save_file(save_f,result)
            except:
                print ('error')



def save_file(path,context):
    with open(path,'a') as f:
        f.write(context)

if __name__ == '__main__':
    n = 0
    arr = []
    # if n < 10:
        # filename = '00000'+str(n)+'_0.txt'
        # path = os.path.join('/workspace','000011_0.txt')
        # get_data('path',arr)
        # for i in arr:
        #     get_parse(i)
    while True:
        _thread.start_new_thread(get_parse,('/workspace/000011_0.txt','/workspace/mysql1'))
        _thread.start_new_thread(get_parse, ('/workspace/000000_0.txt', '/workspace/mysql2'))