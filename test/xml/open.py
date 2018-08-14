#coding=utf-8
import  xml.dom.minidom

#打开xml文档
dom = xml.dom.minidom.parse('D:\\Cities.xml')

#得到文档元素对象
root = dom.documentElement

itemlist = root.getElementsByTagName('City')
# item = itemlist[0]
for item in itemlist:
    un=item.getAttribute("ID")
    print un
    pd=item.getAttribute("CityName")
    print pd

# ii = root.getElementsByTagName('item')
# i1 = ii[0]
# i=i1.getAttribute("id")
# print i
#
# i2 = ii[1]
# i=i2.getAttribute("id")
# print i