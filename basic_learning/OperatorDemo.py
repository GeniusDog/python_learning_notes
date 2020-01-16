#OperatorDemo.py

'''
    作者：Dragon
    时间：2020年1月5日17:48:06
    描述：熟悉掌握python中运算符的用法
'''

#1.+:不支持字符与数字相加，python将True当做1，False当做0
print("算术加法3+4：",3+4)
print("列表合并[1,2,3]+[4,5,6]：",[1,2,3]+[4,5,6])
print("元组合并(1,2,3)+(4,5)：",(1,2,3)+(4,5))
print("字符串拼接hello+Dragon!："+"hello"+"Dragon!")
print()

#2.-
print("算数减法3-4：",3-4)
print("集合差集{1,2,3}-{1}:",{1,2,3}-{1})
print("相反数-4：",-4)
print()

#3.*:乘法，序列与整数的乘法、生成新的序列对象，不支持字典和集合
print("乘法3*4：",3*4)
print("列表乘法[1,2,3]*4：",[1,2,3]*4)
print("元组乘法(1,2,3)*4：",(1,2,3)*4)
print("字符串乘法Dragon-*4:","Dragon-"*4)
print()

#4./:真除法
print("除法3/4:",3/4)
print("除法8/4:",8/4)
print("除法3/2:",3/2)
print("除法8.0/4:",8.0/4)
print()

#5.//：下取整
print("除法3//4:",3//4)
print("除法8//4:",8//4)
print("除法3//2:",3//2)
print("除法8.0//4:",8.0//4)
print()

#6.%:取余，字符串格式化
print("取余 3%4:",3%4)
print("取余 123.45 % 3:",123.45%3)
print("取余 123 % 3.2:",123%3.2)
print("取余 -15 % 4:",-15%4)
print("取余 -15 % -4:",-15%-4)
print("取余 15 % -4:",15%-4)
print("把65分别格式化为字符和整数 '%c,%d' % (65,65):",'%c,%d' % (65,65))
print("把65分别格式化为实数和字符串 '%f,%s' % (65,65):",'%f,%s' % (65,65))
print()

#7.**：幂运算
print("幂运算 2**4:",2**4)
print("幂运算 pow(2,4):",pow(2,4))
print("平方根 9**0.5:",9**0.5)
print("平方根 9**0.5:",9**0.5)
print("负数的平方根 -9**0.5:",(-9)**0.5)      #-9有无括号结果不同！
print()

#8.关系运算符：返回bool结果
print("2>4>7:",2>4>7)
print("等价：2>4 and 4>7:",2>4>7)
print("3<5>2:",3<5>2)
print("等价：3<5 and 5>2:",3<5>2)
print()

#9.in:成员测试运算符
print("成员测试运算符 3 in [1,2,3]:",3 in [1,2,3])
print("成员测试运算符 'abc' in 'abcdefg':",'abc' in 'abcdefg')
print()

#10.is：同一性测试运算符:同一个对象或相同的地址
print("Python采用内存管理模式，变量并不存值，而是地址或引用")
print("同一性测试运算符 3 is 3:", 3 is 3)
x=[1,2,3]
y=[1,2,3]
print("当前的x：",x)
print("当前的y：",y)
print("不同对象 x is y:", x is y)
print("同一个值内存中只有一份 x[0] is y[0]:", x[0] is y[0])
x.append(4)
print("当前的x：",x)    #此时y无影响
x=y     #x，y指向同一个对象
print("x，y指向同一个对象 x is y:",x is y)
x.append(4)
print("当前的x：",x)
print("当前的y：",y)
print()



