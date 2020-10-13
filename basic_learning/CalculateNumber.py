# 时间：2020.10.13 23点37分
# 两个数的简单计算器

# 获取输入，分别赋值
inputs=input().split(" ")
number1=int(inputs[0])
number2=int(inputs[2])
symbol=str(inputs[1])
result=0
symbols=["+","-","*","/","%"]


# 开始判断
if symbol in symbols:
    if symbol=="+":
        result=number1+number2
    if symbol=="-":
        result=number1-number2
    if symbol=="*":
        result=number1*number2
    if symbol=="/":
        result=int(number1/number2)
    if symbol=="%":
        result=number1%number2

    print(result)
else:
    print("ERROR")
