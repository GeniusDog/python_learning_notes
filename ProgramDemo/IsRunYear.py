#IsRunYear.py

'''
    编程练习：输入年份判断是不是闰年,如果是闰年输出True 否则输出False
    时间：2020年1月13日11:10:46
    作者：Dragon
    提示：能被4且不能被100或者400整除的数
'''

year=int(input("please input your year："))
if (year % 4 == 0 and year % 100 != 0) or \
           year % 400 == 0:
    print(year,"True")
else:
    print(year,"False")

