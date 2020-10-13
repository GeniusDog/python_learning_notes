# 2020.10.13 23点50分
# 逆序的三位数
# 程序每次读入一个正3位数，然后输出按位逆序的数字。
# 注意：当输入的数字含有结尾的0时，输出不应带有前导的0。比如输入700，输出应该是7。

numbers=input()
list_result=[]
for x in numbers[::-1]:
    list_result.append(x)
    #print(x)

flag=1
if list_result[0]=="0":
    flag=0
else:
    print(list_result[0],end="")

if list_result[1]=="0" and flag==0:
    pass
else:
    print(list_result[1],end="")

if list_result[2]=="0":
    pass
else:
    print(list_result[2],end="")
