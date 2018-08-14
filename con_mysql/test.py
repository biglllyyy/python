# import os
# def read_file(path):
#     with open(path,'r') as f:
#         line = f.readlines()
#         if line[0][0:17] == line[1][0:17]:
#             pass
#         else:
#             print(line[0][0:17])
#             print(line[1][0:17])
#             print(path)
#
# if __name__ == '__main__':
#     for root,dir,files in os.walk('/workspace/licheng/zong'):
#         for file in files:
#             path_pull = os.path.join(root,file)
#             # print(path_pull)
#             read_file(path_pull)
# a={1:'a',2:'b',3:'c'}
# b={2:'b',3:'c'}
# for key in a.keys():
#     if not b.get(key):
#         print(key)

# import datetime
# if int(datetime.datetime.now().strftime('%d')) < 7:
#     tableNum = datetime.datetime.now().strftime('%d')
# else:
#     tableNum = int(datetime.datetime.now().strftime('%d'))//7+1
# tableName = "t_raw_"+datetime.datetime.now().strftime('%Y_%m')+"_w0"+str(tableNum)
# print(tableName)
# print(tableNum)
# #   t_raw_2017_11_w02
#
# #   t_raw_2017_11_w02
# a ={1:'a'}
# print(len(a))

#
# import datetime
# import time
# print(datetime.datetime.now().strftime('%p'))
# print(time.time())
a='asd'
a=a.replace()
