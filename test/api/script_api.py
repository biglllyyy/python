#encoding:utf-8
import json,os,requests
import datetime

global Token
global Info

def Get_Token(username,password):
    url = "http://telematics.dfmc.com.cn:9100//user-centre/oauth/token"
    headers = {
        'Authorization': 'Basic Y2xpZW50YXBwOjEyMzQ1Ng==',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'scope': 'read',
        'client_secret': '123456',
        'client_id': 'clientapp'
    }
    response = requests.post(url, data=payload, headers=headers)
    data = json.loads(response.text)
    try:
        return data['access_token']
    except:
        return None

def Get_APIINFO(username,password):
    TOKEN = Get_Token(username,password)
    URL="http://telematics.dfmc.com.cn:9100/real-time/vehicle/statistics"
    headers = {
        'Authorization': 'Bearer %s' % (TOKEN),
    }
    response = requests.request("GET", URL, headers=headers)
    return  response.text

def saveFile(path,content):
    with open(path,'a',encoding='utf-8') as f:
        f.write(content)

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

if __name__ == '__main__':
    user = {'dongfengcyc': ['123','东风乘用车'],
            'dongfengkeche': ['123','东风客车'],
            'dongfengliuqi':['123','东风柳汽'],
            'dongfengteshang':['123','东风十堰特商'],
            'dongfengtezhuan':['123','东风十堰特专'],
            'dongfengsuizhuan':['123','东风随专'],
            'dongfengteqi':['123','东风特汽'],
            'dongfengxianglv':['123','东风襄旅'],
            'dongfengyunqi':['123','东风云汽'],
            }
    dic = {}
    list = []
    savePath = '/workspace/search/'+datetime.datetime.now().strftime('%Y-%m-%d')
    saveFile(savePath, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + '\n')
    for username, password in user.items():
        print(password[1])
        info = Get_APIINFO(username,password[0])
        print(info)
        info=json.loads(info)
        print(info)
        vehicleCount="总车辆"+" : "+str(info['data']['vehicleCount'])
        onlineCount="在线车辆"+" : "+str(info['data']['onlineCount'])
        activeCount="激活车辆"+" : "+str(info['data']['activeCount'])
        unActiveCount="没激活车辆"+" : "+str(info['data']['unActiveCount'])
        inChargeCount="充电中"+" : "+str(info['data']['inChargeCount'])
        warnCount="报警车辆"+" : "+str(info['data']['warnCount'])
        offlineCount="下线车辆"+" : "+str(info['data']['offlineCount'])
        saveFile(savePath,'   车场是 : '+password[1]+'\n')
        content=vehicleCount+'\n'+onlineCount+'\n'+activeCount+'\n'+unActiveCount+'\n'+inChargeCount+'\n'+warnCount+'\n'+offlineCount+'\n'
        print(content)
        saveFile(savePath, content+'\n')
    saveFile(savePath, '========================================================')
    saveFile(savePath,'\n\n\n')



        # for key,value in city.items():
        #     if info['data']['prefectureCount'].get(value) != None:
        #         dic[key] = info['data']['prefectureCount'][value]
        # result = sorted(dic.items(),key=lambda  asd:asd[1],reverse=True)
        # content =''
        # for i in result:
        #     chengshi=str(i[0])
        #     rihuo=str(i[1])
        #     content=content+(chengshi+":"+rihuo)+'\n'
        # saveFile(savePath, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + 'username is :')
        # saveFile(savePath, username + '\n')
        # saveFile(savePath,content+'\n\n')
        # print(content)