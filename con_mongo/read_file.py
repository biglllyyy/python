def read_file(path1,path2,vin_list):
    count = 0
    for vin in vin_list:
        with open(path1+str(vin),'r') as f:
            lines_1 = f.readlines()

        with open(path2+str(vin),'r') as f:
            lines_2 = f.readlines()
        try:
            line_1_2 = lines_1[1]
            print(line_1_2[18:37])
            line_last_1 = lines_1[-1]
            print(line_last_1[18:37])


            line_2_2 = lines_2[1]
            print(line_2_2[18:37])
            line_last_2 = lines_2[-1]
            print(line_last_2[18:37])
        except:
            print('erroe')




        if line_1_2[18:37] < line_2_2[18:37]:
            print('min is :'+str(line_1_2))
            save_file('/workspace/licheng/zong/'+str(vin),str(line_1_2))
        elif line_1_2[18:37] > line_2_2[18:37]:
            print('min is :'+str(line_2_2))
            save_file('/workspace/licheng/zong/'+str(vin), str(line_2_2))

        if line_last_1[18:37] > line_last_2[18:37]:
            print('last is :'+str(line_last_1))
            save_file('/workspace/licheng/zong/'+str(vin), str(line_last_1))
        elif line_last_1[18:37] < line_last_2[18:37]:
            print('last is :'+str(line_last_2))
            save_file('/workspace/licheng/zong/'+str(vin), str(line_last_2))



def save_file(path,content):
    with open(path,'a') as f:
        f.write(content)
def list_cha(path,vin_list):
    with open(path,'r') as f:
        for line in f.readlines():
            line = line.strip('\n')
            vin_list.append(line)

if __name__ == '__main__':
    vin_list = []
    list_cha('/workspace/licheng/vin_list',vin_list)
    read_file('/workspace/licheng/mon_file3/','/workspace/licheng/mon_file4_data/',vin_list)


