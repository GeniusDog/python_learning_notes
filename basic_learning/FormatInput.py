#时间：2020.10.5 01点45分
#输入在一行中顺序给出浮点数1、整数、字符、浮点数2，其间以1个空格分隔。
#在一行中按照字符、整数、浮点数1、浮点数2的顺序输出，其中浮点数保留小数点后2位。

#输入
words=input().split()
f1=float(words[0])
inter=int(words[1])
char=words[2]
f2=float(words[3])
print("%c %d %.2f %.2f" %(char,inter,f1,f2))
