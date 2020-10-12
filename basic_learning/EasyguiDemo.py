# 时间：2020.10.12 12点08分
# 导入easygui模块，测试导入是否成功
# 学习该段代码，自己设计喜欢的逻辑

import easygui as g
import sys

#显示进入界面
g.msgbox('恭喜你，打开了绝密资料档案！')


#显示第一个选择性窗口
msg = '你想了解我哪些方面呢?'
title = '绝密资料！'
choices = ['爱好', '专业技能', '梦中情狗','黑历史']
choice = g.choicebox(msg, title, choices)

#注意，选择了字符串，以防用户取消了chioce，我们得到None

if choice!=None:
    # 给出选择提示窗口
    g.msgbox('你的选择是: ' + str(choice), '结果')

    #显示第二个选择性窗口
    msg = '你真希望深入了解我？不会后悔？'
    title = '请选择'
    #显示Continue和Cancel的选择窗口
    if g.ccbox(msg, title):
        #用户选择了Continue
        g.msgbox("对不起，我还没做好心理准备！")
    else:
        #用户选择了Cancel
        g.msgbox("你原来没有那么喜欢我......一腔真情终究是错付了~")
        sys.exit(0)
else:
    g.msgbox("再见！")
    sys.exit(0)
