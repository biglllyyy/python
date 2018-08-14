city={
"北京":"京",
"天津":"津",
"黑龙江":"黑",
"吉林":"吉",
"辽宁":"辽",
"河北":"冀",
"河南":"豫",
"山东":"鲁",
"山西":"晋",
"陕西":"陕",
"内蒙古":"蒙",
"宁夏":"宁",
"甘肃":"甘",
"新疆":"新",
"青海":"青",
"西藏":"藏",
"湖北":"鄂",
"安徽":"皖",
"江苏":"苏",
"上海":"沪",
"浙江":"浙",
"福建":"闵",
"湖南":"湘",
"江西":"赣",
"四川":"川",
"重庆":"渝",
"贵州":"贵",
"云南":"云",
"广东":"粤",
"广西":"桂",
"海南":"琼",
"香港":"港",
"澳门":"澳",
"台湾":"台",
}
list =[2,3,4,61,1,23,543,65,45,6]
list.reverse()
print(list)

    # print(type(info))
    # print("激活车辆"+str(info['data']['vehicleCount'])+'\n'
    #       ""+str(info['data']['onlineCount'])+'\n'
    #       ""+str(info['data']['activeCount'])+'\n'
    #       ""+str(info['data']['unActiveCount'])+'\n'
    #       ""+str(info['data']['inChargeCount']) + '\n'
    #       ""+str(info['data']['warnCount']) + '\n'
    #       ""+str(info['data']['offlineCount']) + '\n'
    #       ""+str(info['data']['prefectureCount']['冀']) + '\n'
    #       ""+str(info['data']['prefectureCount']['鲁']) + '\n'
    #       ""+str(info['data']['prefectureCount']['桂']) + '\n'
    #       ""+str(info['data']['prefectureCount']['鄂']) + '\n'
    #       ""+str(info['data']['prefectureCount']['赣']) + '\n'
    #       ""+str(info['data']['prefectureCount']['粤']) + '\n'
    #       ""+str(info['data']['prefectureCount']['津']) + '\n'
    #       ""+str(info['data']['prefectureCount']['吉']) + '\n'
    #       ""+str(info['data']['prefectureCount']['晋']) + '\n'
    #       ""+str(info['data']['prefectureCount']['豫']) + '\n'
    #       ""+str(info['data']['prefectureCount']['苏']) + '\n'
    #       ""+str(info['data']['prefectureCount']['云']) + '\n'
    #       ""+str(info['data']['prefectureCount']['贵']) + '\n'
    #       ""+str(info['data']['prefectureCount']['陕']) + '\n'
    #       ""+str(info['data']['prefectureCount']['皖']) + '\n'
    #       ""+str(info['data']['prefectureCount']['甘']) + '\n'
    #       ""+str(info['data']['prefectureCount']['湘']) + '\n'
    #       ""+str(info['data']['prefectureCount']['浙']) + '\n'
    #       ""+str(info['data']['prefectureCount']['琼']) + '\n'
    #       ""+str(info['data']['prefectureCount']['川']) + '\n'
    #       ""+str(info['data']['prefectureCount']['辽']) + '\n'



import datetime
import time
time.time()

print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))