#PrintMulTable.py

'''
    描述:输出乘法口诀表(九九表)
    时间：2020年1月14日11:11:19
    作者：Dragon
    思路：先思考一下乘法表长什么样，该怎么输出！
          一行一行输出，列成递增
          行：1-9
          列：1-9
          输出格式：a*b=c,不换行输出且制表
          考虑完毕，动手！
'''

for row in range(1,10):
    for cow in range(1,10):
        if cow <= row:
            print("%d * %d = %d \t" %(cow,row,row*cow),end="")
            #print("%d * %d = %d " %(cow,row,row*cow),end="\t"),两种方式皆可
        else:
            break
    print()     #换行
