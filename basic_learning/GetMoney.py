#时间：2020.10.7 00点30分
#计算工资

year,time=input().split(" ")
year=int(year)
time=int(time)


money=0

'''
extra=1.5*(time-40)
if( year >=5):
    if( time <=40):
        money=50*time
    else:
        money=50*extra+40*50
else:
    if(time<=40):
        money=30*time
    else:
        money=30*extra+30*40

print("%.2f" % money)

'''
exp=30
if year>=5:
    exp=50

if time<=40:
    money=exp*time
else:
    money=exp*1.5*(time-40)+exp*40
print("%.2f" % money)
