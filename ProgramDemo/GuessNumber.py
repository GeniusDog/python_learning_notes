#GuessNumber.py
import random   #导入random

'''
    描述：计算机出一个1~100之间的随机数由人来猜
          计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
    时间：2020年1月14日11:01:36
    作者：Dragon
    注意：生成随机数需要导入import random，random.randint（）函数的使用
'''

#系统生成1-100随机数字
randomNumber=random.randint(1,100)
print("我是作弊器：随机数是：",randomNumber)

#提示用户输入数字
while True:
    userNumber=int(input("请输入您的数字："))
    if(userNumber<randomNumber):
        print("再大一点！")
    elif userNumber>randomNumber:
        print("再小一点！")
    else:
        print("猜对了")
        break
