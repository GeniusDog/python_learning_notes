#VariateType.py

''''
    变量类型的使用以及Type函数的使用
    扩展：变量转化函数的使用（综合使用）
    变量类型：整型，浮点型，布尔型
    时间：2020年1月13日10:36:07
'''

a=23;
print('1.a=23,对应的类型为>>>',type(a))

a=23.45
print('2.a=23.45,对应的类型为>>>',type(a))

a=2+5j
print('3.a=2+j,对应的类型为>>>',type(a))

b='123dfg'
print("4.b='123dfg',对应的类型为>>>",type(b))

c=True
print('5.c=True,对应的类型为>>>',type(c))

'''
- `int()`：将一个数值或字符串转换成整数，可以指定进制。
           int将数值转化为整数，会下取整
- `float()`：将一个字符串转换成浮点数。
            小数点后一位，如1234转化的结果为1234.0
- `str()`：将指定的对象转换成字符串形式，可以指定编码。
- `chr()`：将整数转换成该编码对应的字符串（一个字符）。
           将对应的整数转化成对应ASCII编码对应的字符
- `ord()`：将字符串（一个字符）转换成对应的编码（整数）。
'''

a_数值_多位=234;
a_数值_小数位=234.7;
a_数值_一位=56;
b_字符串_字母型='hello'
b_字符串_数字型='12345'

print()
print("1.int()将一个数值或字符串转换成整数")
print("a.将一个数值转化为整数：数值",a_数值_小数位,'转化结果：',int(a_数值_小数位))
a_数值_小数位_int=int(a_数值_小数位);
print("转化之前的类型：",type(a_数值_小数位))
print("转化后的类型：",type(a_数值_小数位_int))
print("b.将一个字符串转化为整数：字符串",b_字符串_数字型,'转化结果：',int(b_字符串_数字型))
b_字符串_数字型_int=int(b_字符串_数字型);
print("转化之前的类型：",type(b_字符串_数字型))
print("转化后的类型：",type(b_字符串_数字型_int))
print()

print("2.float()：将一个字符串转换成浮点数")
print("将一个字符串转化为浮点数：字符串",b_字符串_数字型,'转化结果：',float(b_字符串_数字型))
b_字符串_数字型_float=float(b_字符串_数字型);
print("转化之前的类型：",type(b_字符串_数字型))
print("转化后的类型：",type(b_字符串_数字型_float))
print()

print("3.str()：将指定的对象转换成字符串形式，可以指定编码。")
print("将一个数值转化为字符串：数值",a_数值_小数位,'转化结果：',str(a_数值_小数位))
a_数值_小数位_str=str(a_数值_小数位);
print("转化之前的类型：",type(a_数值_小数位))
print("转化后的类型：",type(a_数值_小数位_str))
print()

print("4.chr()：将整数转换成该编码对应的字符串（一个字符）")
print("将一个数值转化为字符串：数值",a_数值_一位,'转化结果：',chr(a_数值_一位))
a_数值_一位_chr=chr(a_数值_一位);
print("转化之前的类型：",type(a_数值_一位))
print("转化后的类型：",type(a_数值_一位_chr))
