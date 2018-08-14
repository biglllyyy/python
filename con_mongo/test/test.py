import tarfile
import os

#解压tar.gz文件
# tar = tarfile.open('/workspace/test/abc.tar.gz','r:gz')
# file_names = tar.getnames()
# for file_name in file_names:
#     tar.extract(file_name,'/workspace/test')
# tar.close()

#压缩
tar = tarfile.open('/workspace/test/abc','w:gz')
if os.path.isfile('/workspace/test/abc'):
    tar.add('/workspace/test/abc',arcname='/workspace/test/abc.tar.gz')
elif os.path.isdir('/workspace/test/abc'):
    for root,dir,files in os.walk('/workspace/test/abc'):
        for file in files:
            fullpath = os.path .join(root,file)
            tar.add(fullpath,arcname=file)
tar.close()

#遍历文件下的全部文件
# for root,dir,files in os.walk('/workspace/test'):
#     # print('root is '+str(root))
#     # print(dir)
#     # print(files)
#     for file in files:
#         print(os.path.join(root,file))



