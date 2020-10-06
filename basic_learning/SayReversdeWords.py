#时间：2020.10.5 00点38分
#说反话

#测试输入包含一个测试用例，在一行内给出总长度不超过500 000的字符串。
# 字符串由若干单词和若干空格组成，其中单词是由英文字母（大小写有区分）组成的字符串，单词之间用若干个空格分开。
#输出：每个测试用例的输出占一行，输出倒序后的句子，并且保证单词间只有1个空格。


words=(input().split())
lenth=len(words)
#print("lenth=",lenth)
for x in words[:-lenth:-1]:
    #print("x=",x)
    #print("lenth-x=",lenth-x)
    print(x,end=" ")
if lenth==0:
    print()
else:
    print(words[0])

'''
#使用异常处理是因为如果只读入空格，列表中不会存，导致数组越界
try:
    x = list(input().split())		#split()默认空格分隔（可以是多个）
    for i in x[:-len(x):-1]:		#循环到-len(x)，控制输出
        print(i,end=" ")
    print(x[0])
except IndexError:
    exit(0)
'''
