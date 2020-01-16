#ScoreToLevel.py

'''
编程练习：百分制成绩转换为等级制成绩：
	     如果输入的成绩在90分以上（含90分）输出A；
	     80分-90分（不含90分）输出B；
	     70分-80分（不含80分）输出C；
	     60分-70分（不含70分）输出D；
	     60分以下输出E。
时间：2020年1月13日11:40:06
作者：Dragon
'''

score=float(input("请输入您的成绩："))
if score<60:
    print("成绩为E，您要再多多努力！")
elif score<70:
    print("成绩为D，您要再多多努力！")
elif score<80:
    print("成绩为c，加油！")
elif score<90:
    print("成绩为B，不错哦~")
else:
    print("成绩为A，学霸啊！")