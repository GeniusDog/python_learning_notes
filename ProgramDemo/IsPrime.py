#IsPrime.py

'''
    描述：
    时间：2020年1月14日11:28:48
    作者：Dragon
    思路：素数指的是只能被1和自身整除的大于1的整数
          通过循环看其有没有其他因子
'''

number=int(input("请输入要判断的数字："))
flag=0;
for x in range(2,number):
    #print("进入循环，当前x为：",x)
    #print("number%x==0   为：",number/x==0)
    if(number%x==0):
        print("不是素数！")
        flag=1
        break

if flag==0:
    print("是素数！")
