#时间：2020.10.7 00点00分
#汉罗塔问题
#输入盘子的个数
#输出移动的过程与总次数

count=0

def Hanio(number,x,y,z):
    global count
    if number==1:
        print(x,"-->",z)
        count+=1
    else:
        Hanio(number-1,x,z,y)
        print(x, "-->", z)
        count+= 1
        Hanio(number - 1, y,x, z)

if __name__ == '__main__':
    number=int(input("请输入盘子的个数："))
    Hanio(number,"柱子1","柱子2","柱子3")
    print("总共移动了%d次" % count)
