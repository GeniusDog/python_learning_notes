#UserValid.py

'''
    编程练习 if-else语句
    描述：用户身份验证
          正确的账号 admin 和密码 0000
    验证成功输出：welcome admin!
    验证失败输出：
        a.user name is fail
        b.password is fail
    加强版：循环验证，直到验证正确
    作者：Dragon
'''

username=input("please input your username:")
if (username!="admin"):
    print("user name is fail")
else:
    password=input("please input your password:")
    if password!="0000":
        print("password is fail")
    else:
        print("welcome admin!")