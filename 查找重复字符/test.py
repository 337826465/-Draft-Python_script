import os

path = r"F:\Code\Python_Project\查找重复字符"  # 文件路径

filenames = os.listdir(path)

T = []
f = open("Record.txt", "w", encoding="utf-8")  # 打开txt文件，进行写入
for name in filenames:
    name = name.split(".")[0]  # 去后缀名
    print(name)  # 查看是否去后缀名成功
    T.append(name)  # 得到文件名列表
    f.write(name + "\n")  # 写入txt文件中
f.close()


f = open("Output.txt", "w", encoding="utf-8")  # 打开txt文件，进行写入
filelist = set(T)  # 去除list中重复的字符串
file = []
for i in filelist:  # 循环新得到的去重的list，得到i
    if T.count(i) > 1:
        file.append(str(i) + "  " + "出现了" + str(T.count(i)) + "次")  # i出现的次数
for j in file:
    f.write(j + "\n")  # 写入txt文件中
f.close()
