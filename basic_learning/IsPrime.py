#time:2020年10月3日22点56分
#输入一个正整数判断是不是素数。
#素数指的是只能被1和自身整除的大于1的整数。

def IsPrime(num):
    flag = 1  # 素数标志

    for x in range(num):
        if(x==0 or x==1 or x==num):
            continue
        if (num % x == 0):
            flag = 0

    return  flag


number=int(input("请输入一个数字：")) #输入
flag=IsPrime(number)
if(flag==1):
    print("%d 是素数" % number)
else:
    print("%d 不是素数" % number)

