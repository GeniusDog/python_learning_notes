#ChickProblem.py

'''
    描述：百元百鸡问题
          公鸡5元一只，母鸡3元一只，小鸡1元三只
		  用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
          直接输出其所有可能的结果集合
    作者：Dragon
    时间：2020年1月15日15:22:39
    思路：i公鸡从0-20，j母鸡从0-35，m小鸡作为补差价用的
          5i+3J<=100,m为100-5i-3j的个数
    注意：所有的鸡只有100只
          问题的要求一定要看清楚！
'''

print("-------------百元若干鸡问题所有的可能结果集合---------------")
for i in range(21):
    #print("当前的公鸡为：",i,end="")
    if(5*i<100):
        for j in range(35):
            #print("当前的母鸡为：", j)
            if (100-5*i-3*j > 0):
                m=100-5*i-3*j
                print("公鸡", i, "母鸡",j,"只，小鸡",3*m,"只")
            elif 100==5*i+3*j:
                print("公鸡",i,"母鸡",j,"只，小鸡0只")
            else:
                break

    else:
        print("公鸡",i,"只,母鸡0只，小鸡0只")

print("-------------百元百鸡问题所有的可能结果集合---------------")
for x in range(21):
    for y in range(35):
        z=100-x-y
        if (5*x+3*y+z/3 == 100):
            print("公鸡: %d只, 母鸡: %d只, 小鸡: %d只" % (x,y,z))