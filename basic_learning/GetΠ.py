#时间：10.7 01点17分
#根据公式计算圆周率：https://pintia.cn/problem-sets/14/problems/795
import math

def getNumber(n):
    up=math.factorial(n)
    down=1
    for i in range(3,2*n+3,2):
        #print("1.当前的分数为：",i)
        down *=i
    up=float(up)
    down=float(down)
    result=float(up/down)
    #print("2.n=",n,"result=",result)
    return  result

yu=float(input())
sum=1
i=1
while 1:
    right=getNumber(i)
    if right>=yu:
        sum +=right
        i+=1
    else:
        break

pi=sum*2
print("%.6f" %pi)


