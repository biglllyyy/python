import time
print (time.time())


import datetime
start_time=datetime.datetime.now()
def sleep():
    time.sleep(5)
    end_time=datetime.datetime.now()
    spend_time=(end_time-start_time).seconds
    return spend_time
if __name__ == '__main__':
    print(id(sleep()))
