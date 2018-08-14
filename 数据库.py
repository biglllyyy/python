import pymysql
import requests
from bs4 import BeautifulSoup
baseURL1 = 'http://www.eshow365.com/guonei/date-20170%d.html'
baseURL2= 'http://www.eshow365.com/guonei/date-2017%d.html'
def get_eshow(start):
     lists = []
     if start<10:
          url=baseURL1%start
     else:
          url=baseURL2%start
     html = requests.get(url)
     soup = BeautifulSoup(html.content, "html.parser")
     items = soup.find("div", "hyzhanhuilistweikai").find_all("li") 
     for i in items:
                eshow= {}
                eshow["category"] = i.find("span","hangyespan").text
                eshow["link"] ="http://www.eshow365.com"+i.find("a").get("href")
                eshow["tle"] = i.find("a").get("title")
                eshow["name"] = i.find("span", "guowaicityspan").text
                eshow["score"] = i.find("span", "guowaitime").text
                lists.append(eshow)
     return lists

if __name__ == "__main__":
    db = pymysql.connect(host="localhost",user="root",password="123456",db="test2",charset="utf8mb4")
    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS eshow")
    createTab = """CREATE TABLE eshow(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(20) NOT NULL,
        category VARCHAR(20) NOT NULL,
        link VARCHAR(50) NOT NULL,
        tle VARCHAR(40) NOT NULL,
        score VARCHAR(20) NOT NULL
    )"""
    cursor.execute(createTab)
    start=1
    while (start<13):
         lists = get_eshow(start)
         start+=1   
         for i in lists:
               sql = "INSERT INTO `eshow`(`name`,`category`,`score`,`link`,`tle`) VALUES(%s,%s,%s,%s,%s)"
               try:
                     cursor.execute(sql, (i["name"], i["category"],i["score"],i["link"],i["tle"]))
                     db.commit()
                     print(i["name"]+"      "+i["category"]+"      "+i["score"]+"      "+"http://www.eshow365.com"+i["link"]+"      "+i["tle"]+"      "+"       获取成功")
               except:
                     db.rollback()
                
    db.close()
