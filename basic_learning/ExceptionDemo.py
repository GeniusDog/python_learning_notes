# 时间：2020.10.12 11点02分
# 异常语法的练习

try:
    #尝试打开一个文件，并比如数据
    f=open("E:\\ExceptionTest.txt","a")
    f.write("我是新建的文件，用于测试异常语法的训练")
except:
    #文件打开失败，返回对应的句子
    print("不好意思，ExceptionTest.txt文件打开失败！")
else:
    #不发生异常时，程序处理的部分
    print("文件打开成功，请前往查看~")
    f.close()
