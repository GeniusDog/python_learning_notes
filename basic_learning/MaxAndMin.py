#时间：2020年10月3日23点23分
#练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
#最小公倍数=两整数的乘积÷最大公约数
#最大公约数：辗转相除法,相减法，穷举法（分解质因数法）：公共最大

def MaxNumber(a,b):
    '使用辗转相除法求最大公约数'
    if(a<b):
        temp=a
        a=b
        b=temp
    while a%b!=0:
        #print("***a=%d,b=%d" % (a, b))
        temp=b
        b=a%b
        a=temp
        #print("###a=%d,b=%d" % (a,b))
    return  b

def MinNumber(a,b):
    '最小公倍数=两整数的乘积÷最大公约数'
    max=MaxNumber(a,b)
    min=(a*b) / max
    return  min

a=int(input("请输入第一个数字："))
b=int(input("请输入第二个数字："))
print("%d 和 %d 的最大公约数是：%d" % (a,b,MaxNumber(a,b)))
print("%d 和 %d 的最小公倍数是：%d" % (a,b,MinNumber(a,b)))
