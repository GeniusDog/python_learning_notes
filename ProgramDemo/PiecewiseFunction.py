#PiecewiseFunction.py
'''
    编程实战：分段函数求值
	               3x - 5  (x > 1)
    分段函数f(x) =  x + 2   (-1 <= x <= 1)
               	   5x + 3  (x < -1)
    时间：2020年1月13日11:34:11
    作者：Dragon
'''

x=float(input("请输入你的数值："))
if x<-1:
    f=5*x+3;
elif x<=1:
    f=x+2;
else:
    f=3*x-5;
print("对应的结果为：",f)