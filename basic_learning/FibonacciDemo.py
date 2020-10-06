#时间：2020.10.4 22点15分
#Fibonacci数列
#输入包含一个整数n。
#输出一行，包含一个整数，表示Fn除以10007的余数。
#Fibonacci数列的递推公式为：Fn=Fn-1+Fn-2，其中F1=F2=1。

def Fibonacci(n):
    if(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return  Fibonacci(n-1)+Fibonacci(n-2)

#number=int(input("请输入数字n："))
number=int(input())
number_Fi=Fibonacci(number)

#print("当前的斐波拉列数列数字是：",number_Fi)
#print(number_Fi)

number_mod=number_Fi%10007
#print("当前对10007取余的结果为：",number_mod)
print(number_mod)
