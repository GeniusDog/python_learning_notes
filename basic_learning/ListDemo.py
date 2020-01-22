#ListDemo.py

'''
    描述：列表知识的学习
    作者：Dragon
    时间：2020年1月21日17:24:28
    内容：列表的使用和常用操作
'''

list1=[1,2,3,4,5,6]
list2=[11,22,33,44]
print(list1)         #[1, 2, 3, 4, 5, 6]
print(list1+list2)  #[1, 2, 3, 4, 5, 6, 11, 22, 33, 44]
print(list1*2)      #[1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
print(list1[2])     #3
print(list1[2::])   #[3, 4, 5, 6]

#两种循环输出的结果一样：123456，注意第二种不需要range
for index in range(len(list1)):
    print(list1[index],end="")
print()
for val in list1:
    print(val,end="")
print()

#通过enumerate函数处理列表之后，再遍历可以同时获得元素索引和值
for index,val in enumerate(list1):
    print("index=%d,val=%d" % (index,val))

list1.append(1314)
print(list1)            #[1, 2, 3, 4, 5, 6, 1314]
list1.insert(0,520)
print(list1)            #[520, 1, 2, 3, 4, 5, 6, 1314]
list1.pop(-1)
print(list1)            #[520, 1, 2, 3, 4, 5, 6]
list1.sort()
print(list1)            #[1, 2, 3, 4, 5, 6, 520]





