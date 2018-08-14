# from hdfs.client import Client
# import time
# import os
# client = Client('http://10.2.208.172:50070')
# # print(dir(client))
# try:
#     for root,dir,files in client.walk('/'):
#         for file in files:
#             print(os.path.join(root,file))
#             time.sleep(0.1)
# except:
#     pass




# from hdfs3 import HDFileSystem
#
# hdfs = HDFileSystem(host='10.2.208.171',port=9000)
# print(hdfs.ls('/'))


# import os
# import time
# for root,dir,files in os.walk('/workspace'):
#     for file in files:
#         print(os.path.join(root,file))
#         print(os.path.getsize(os.path.join(root,file)))
#         time.sleep(0.2)


