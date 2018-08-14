def open_file(path,arr,fuhao,line_num):
    with open(path,'r') as f:
        for line in f.readlines:
            line = line.split(fuhao)
            arr.append(line[line_num])
    return arr

if __name__ == '__main__':
    arr_1 = []
    arr_2 = []
    all_vin = open_file('D:\\abc.txt', arr_1, '\t', 0)
    compar_vin = open_file('D:\\te_vin.txt', arr_2, ',', 1)
    print(all_vin)
    print (compar_vin)
