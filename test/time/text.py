import datetime
print datetime.datetime.now().__format__('%Y-%m-%d %H:%M:%S')
print (datetime.datetime.now()-datetime.timedelta(seconds=300)).__format__('%Y-%m-%d %H:%M:%S')