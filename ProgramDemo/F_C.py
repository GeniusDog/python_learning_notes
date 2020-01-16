#F_C.py

'''
    练习1：华氏温度转换为摄氏温度
    提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
'''

#提示用户输入华氏温度,并转化为对应的数值
f=float(input("请输入华氏温度："))
#print(f)

#对温度进行转化
c=(f-32)/1.8

'''
    数据的输出
    错误输出：print("当前华氏温度:%f,对应的摄氏温度为：%f",f,c)
    Python中数据的输入与输出
    输入：input函数
    输出：print函数，使用占位符语法：百分号代替逗号，输出的变量要用括号
'''
print("当前华氏温度:%.2f,对应的摄氏温度为：%f" % (f,c))