#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/22 11:05
# @File    : 3年份划分.py
# @Function: 获取A文件与list的重复数据，并根据list数据进行分文件保存

import codecs

path = r'E:\study\python\python-python3.7\python-JB\学习\eight\kaifanglist.txt'
f = codecs.open(path, 'rb', encoding='utf-8', errors='ignore')
f1 = f.readlines()
f.close()
yearlist = []
#yearlist的方式一
# for i in range(1900, 2000):
#     yearlist.append(i)
# # print(yearlist)
#yearlist的方式二
for i in f1:
    print(i)
    line = i.split(',')[1][6:10]   #获取身份证中的年份
    #print(line)
    if int(line[0]) <= 2:          #进行除去干扰性，判断年份范围
        yearlist.append(line)   # 添加列表
yearlist = list(set(yearlist))  #去重
yearopen = []
for x in yearlist:
    path = r'E:\study\python\python-python3.7\python-JB\学习\eight\year\\' + str(x) + '.txt' # 创建文件
    f = codecs.open(path, 'wb', encoding='utf-8', errors='ignore') #打开文件
    yearopen.append(f) #添加

# print(yearlist)
# print(yearopen)
for i in f1:
    line = i.split(',')[1][6:10]  # 将文件中的信息的年份获取出来
    for x in range(len(yearlist)):
        # print(yearlist[x])
        if line == yearlist[x]: # 进行对比
            #print(line)
            yearopen[x].write(i)  #将相应年份写入

            break


for m in yearopen:
    m.close()


