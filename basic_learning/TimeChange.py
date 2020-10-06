#时间：2020.10.6 22点35分
#编写一个程序，要求用户输入24小时制的时间，然后显示12小时制的时间。

# 输入在一行中给出带有中间的:符号（半角的冒号）的24小时制的时间，如12:34表示12点34分。
# 当小时或分钟数小于10时，均没有前导的零，如5:6表示5点零6分。

#在一行中输出这个时间对应的12小时制的时间，数字部分格式与输入的相同，
# 然后跟上空格，再跟上表示上午的字符串AM或表示下午的字符串PM。
# 如5:6 PM表示下午5点零6分。
# 注意，在英文的习惯中，中午12点被认为是下午，
# 所以24小时制的12:00就是12小时制的12:0 PM；而0点被认为是第二天的时间，所以是0:0 AM。

t,m=input().split(":")
t=int(t)
m=int(m)

str=""

if(t>12):
    #print("t=",t)
    t=t-12
    str+="PM"
elif t==12:
    #print("t=", t)
    str += "PM"
elif t<12:
    #print("t=", t)
    str += "AM"

print("%d:%d %s" % (t,m,str))