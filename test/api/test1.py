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
    return  response.json()

def saveFile(path,content):
    with open(path,'a',encoding='utf8') as f:
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
    # USERNAME = os.environ.get("USERNAME")
    # PASSWORD = os.environ.get("PASSWORD")
    user={'dc_rona':'123456','liul':'123'}
    for username,password in user.items():
        info = Get_APIINFO(username,password)
        print(str(info))
        dic ={}
        list = []
        savePath='/workspace/search/test'
        for key,value in city.items():
            if info['data']['prefectureCount'].get(value) != None:
                dic[key] = info['data']['prefectureCount'][value]
        result = sorted(dic.items(),key=lambda  asd:asd[1],reverse=True)
        content =''
        for i in result:
            chengshi=str(i[0])
            rihuo=str(i[1])
            content=content+(chengshi+":"+rihuo+'\n')
        saveFile(savePath,str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+'username is ：')
        saveFile(savePath, username+'\n')
        saveFile(savePath,content+'\n\n')
