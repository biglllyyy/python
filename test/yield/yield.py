import tornado
def test():
    a=[1,2,3,4,5,6,7,1,2,3]
    for i in a:
        if i ==1:
            yield i
        if i==5:
            yield i
m=test()
print (type(m))
for i in m:
    print (i)