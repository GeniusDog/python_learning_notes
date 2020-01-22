#StrDemo.py

'''
    描述：字符串和常用数据结构
    作者：Dragon
    时间：2020年1月21日16:59:42
    内容：字符串的常用表示、字符串的运算、内置函数的使用
'''

str1="123abc"
str2='，123abcdefg'
print(str1+str2)    #123abc，123abcdefg
print(str1*2)       #123abc123abc
print(str1 in str2) #True
print(str1[2])      #3
print(str2[2:5])    #23a
print(str2[2:])     #23abcdefg
print(str2[2::2])   #2aceg
print(str2[::2])    #，2aceg
print(str2[::-1])   #gfedcba321，
print(str2[-3:-1])  #ef

str3="\'hello Drgon!\'"
print(str3)         #'hello Drgon!'
str4=r"\'hello Drgon!\'"
print(str4)         #\'hello Drgon!\'

#内置函数的使用
print("#######内置函数的使用#######")
# 通过内置函数len计算字符串的长度
print(len(str3))            #str3="\'hello Drgon!\'",长度为14

# 获得字符串 首字母 大写的拷贝
print(str3.capitalize())    # 'hello drgon!'

# 获得字符串 每个单词 首字母大写的拷贝
print(str3.title())         # 'Hello Drgon!'

# 获得 字符串 变大写后的拷贝
print(str3.upper())         # 'HELLO DRGON!'

# 从字符串中查找子串所在位置
print(str3.find('lo'))      # 4

# 与find类似但找不到子串时会引发异常
print(str3.index('lo'))     # 4

# 检查字符串是否以指定的字符串开头
print(str3.startswith('He'))    # False

# 检查字符串是否以指定的字符串结尾
print(str3.endswith('!'))       # False

# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str3.center(30, '*'))     #********'hello Drgon!'********

# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str3.rjust(30, ' '))      #                'hello Drgon!'

str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())       # False
# 检查字符串是否以字母构成
print(str2.isalpha())       # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())       # True
str3 = '  jackfrued@126.com '

print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())         #jackfrued@126.com