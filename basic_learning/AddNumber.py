# 2020.10.13 00点21分
#  求整数段和
# 给定两个整数A和B，输出从A到B的所有整数以及这些数的和。

numbers=input().split(" ")
n1=int(numbers[0])
n2=int(numbers[1])
sum=0

count=0
for x in range(n1,n2+1):
    if count==5:
        count = 1
        print()
        print("%5d" % x,end="")
    else:
        print("%5d" % x, end="")
        count += 1

    sum += x
print("\nSum = %d" % sum)
