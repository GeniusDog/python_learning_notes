#AddByFor.py

'''
    用for循环实现1~100求和
    时间：2020年1月14日10:54:22
    作者：Dragon
    注意for-in的语法格式
    range的三种使用方法：
        range(101)可以产生一个0到100的整数序列。
        range(1, 100)可以产生一个1到99的整数序列。
        range(1, 100, 2)可以产生一个1到99的奇数序列，其中2是步长，即数值序列的增量。
'''

sum=0;
for x in range(0,101):
    sum+=x
print(sum)