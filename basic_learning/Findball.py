#时间：2020.10.6 23点44分
#找小球:三个球A、B、C，大小形状相同且其中有一个球与其他球重量不同。要求找出这个不一样的球。

a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
result=""

#print("a=", a)
#print("b=", b)
#print("c=", c)

if(a==b):
    #print("a=",a)
    #print("b=",b)
    result +="C"
else:
    if(a==c):
        #print("a=",a)
        #print("c=",c)
        result +="B"
    else:
        result +="A"
print(result)


