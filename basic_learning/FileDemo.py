# 时间：2020.10.11 21点13分
# 要求：完成小甲鱼的文件分割要求

# 打开文件，读取方式r，路径：E:\\资料\\test.txt
f=open("E:\\资料\\test.txt","r")

fish_temp=[]    #存储每一段对话的小甲鱼列表
people_temp=[]  #存储每一段对话的小甲鱼列表
fish_all=[]     #存储所有对话的小甲鱼列表
people_all=[]   #存储所有对话的小甲鱼列表
count=1         #文件计数器

# 读取文件，根据内容作不同的处理
for each_line in f:
    print(each_line)
    # 根据分隔符的存在，将文本分割：======
    if each_line[:6]=="======":
        # 根据分割符的结束，将小甲鱼的内容输出到一个新的文件中
        for each_fish_temp in fish_temp:
            # 创建一个文件
            path="E:\\资料\\answer\\"+"fish_"+str(count) +".txt"
            f_fish_temp=open(path,"a")

            # 将内容写进新文件中
            f_fish_temp.write(each_fish_temp)

        # 小甲鱼文件写入结束，关闭文件
        f_fish_temp.close()

        # 根据分割符的结束，将小客服的内容输出到一个新的文件中
        for each_people_temp in people_temp:
            # 创建一个文件
            path = "E:\\资料\\answer\\" + "people_" +str(count) + ".txt"
            f_people_temp = open(path, "a")

            # 将内容写进新文件中
            f_people_temp.write(each_people_temp)

        # 小客服文件写入结束，关闭文件
        f_people_temp.close()

        # 文件写入成功，将每段对话单独列表的内容清空
        fish_temp.clear()
        people_temp.clear()
        count += 1  # 文件计数器加一
    else:
        # 每一个分隔符内读取小甲鱼和小客服的单独对话，对话内容保存在相应的列表中
        # 有两个列表，永远保存所有的小甲鱼和小客服的内容

        if each_line[:4]=="小客服:":
            people_temp.append(each_line[4:])
            people_all.append(each_line[4:])
        if each_line[:4]=="小甲鱼:":
            fish_temp.append(each_line[4:])
            fish_all.append(each_line[4:])


for each_fish_all in fish_all:
    # 创建一个文件
    path="E:\\资料\\answer\\"+"fish_all.txt"
    f_fish_all=open(path,"a")

    # 将内容写进新文件中
    f_fish_all.write(each_fish_all)

    # 小甲鱼文件写入结束，关闭文件
    f_fish_all.close()

# 根据分割符的结束，将小甲鱼的内容输出到一个新的文件中
for each_people_all in fish_all:
    # 创建一个文件
    path = "E:\\资料\\answer\\" + "people_all.txt"
    f_people_all = open(path, "a")

    # 将内容写进新文件中
    f_people_all.write(each_people_all)

    # 小甲鱼文件写入结束，关闭文件
    f_people_all.close()


# 将多处来的那个没有分隔符的保存
path = "E:\\资料\\answer\\" + "fish_" + str(count) + ".txt"
f_fish_temp = open(path, "a")

# 将内容写进新文件中
f_fish_temp.writelines(fish_temp)

# 小甲鱼文件写入结束，关闭文件
f_fish_temp.close()

 # 创建一个文件
path = "E:\\资料\\answer\\" + "people_" + str(count) + ".txt"
f_people_temp = open(path, "a")

# 将内容写进新文件中
f_people_temp.writelines(people_temp)

# 小客服文件写入结束，关闭文件
f_people_temp.close()

# 文件写入成功，将每段对话单独列表的内容清空
fish_temp.clear()
people_temp.clear()
count += 1  # 文件计数器加一

# 写入结束，关闭文件
f_fish_all.close()
f_people_all.close()
f.close()
