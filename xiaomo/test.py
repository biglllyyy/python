import csv


# Mileage as 里程,
# StartingTime as 报文开始时间,
# EndTime as 报文结束时间,
# Duration as 持续时间,
# LastMessageEndTime as 上一条报文结束时间,
# TLastMessageEndTime as 上上条报文结束时间,
# TheLastMile as 上一条里程,
# TTheLastMile as 上上条里程,
# TTimeDifference as 与上上条报文时间差值,
# TimeDifference as 与上一条报文时间差值,
# TheDifferenceBetweenTheLastMile as 上一条里程差值,
# TTheDifferenceBetweenTheLastMile as 上上条里程差值,
# Segmentation as 是否分段
# 里程,报文开始时间,报文结束时间,持续时间,上一条报文结束时间,上上条报文结束时间,上一条里程,上上条里程,与上一条报文时间差值,与上上条报文时间差值,上一条里程差值,上上条里程差值,是否分段

csv_reader = csv.reader(open('test.csv', encoding='utf-8'))
num = 0
ch = ""
m = {}
for raw in csv_reader:
    if num == 0:
        num += 1
        pass
    else:
        ch = raw[2]
        m["StartingTime"] = raw[0]
        m["startMileage"] = raw[1]
        m["EndTime"] = raw[0]
        break

for raw in csv_reader:
    if num == 0:
        num += 1
        pass
    else:
        pacNum = 1
        if raw[2] == ch:
            if pacNum ==1:
                m["EndTime"] = raw[0]
                m["endMileage"] = raw[1]

                pacNum += 1
            else:
                m["EndTime"] = raw[0]
                m["endMileage"] = raw[1]

        else:
            ch = raw[2]

            print(m["StartingTime"],m["EndTime"],m["startMileage"],m["endMileage"],   \
                  int(m["endMileage"])-int(m["startMileage"]))

            m["startMileage"] = raw[1]
            m["StartingTime"] = raw[0]


print(m["StartingTime"], m["EndTime"], m["startMileage"], m["endMileage"], \
                  int(m["endMileage"]) - int(m["startMileage"]))


#i["youxiaolicheng"]-m["youxiaolicheng"]







# for raw1 in csv_reader:
#     if num == 0:
#         num += 1
#         pass
#     else:





# r = []
# info = {}
# info['StartingTime'] = ""
# info['EndTime'] = ""
# info['StartingMileage'] = ""
# info['EndMilage'] = ""
# info['EffectiveMileage'] = ""
# EffectiveMileage = 0
# for row in csv_reader:
#     Time = row[0]
#     Mileage = row[1]
#     FenDuan = row[2]
#     LastMessageEndTime = row[3]
#     TheLastMile = row[4]
#     youxiaolicheng = row[5]
#     EffectiveMileage = EffectiveMileage + int(youxiaolicheng)
#     if info['StartingTime'] == "":
#         info['StartingTime'] = Time
#         info['StartingMileage'] = Mileage
#         continue
#     if FenDuan == "F":
#         info['EffectiveMileage'] = EffectiveMileage
#     if FenDuan == "T":
#
#
#         info['EndTime'] = Time
#         info['EndMilage'] = Mileage
#         # info['EffectiveMileage'] = EffectiveMileage
#         print(info)
#         r.append(info)
#         info['StartingTime'] = ""
#         info['EndTime'] = ""
#         info['StartingMileage'] = ""
#         info['EndMilage'] = ""
#         info['EffectiveMileage'] = ""
#         EffectiveMileage = 0