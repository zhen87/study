#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 19:28
# @File    : 1区域划分.py
# @Function:
# E:\study\python\python-python3.7\python-JB\学习\eight\area
import codecs

path = r'E:\study\python\python-python3.7\python-JB\学习\eight\kaifanglist.txt'
f = codecs.open(path, 'rb', encoding='utf-8', errors='ignore')
f1 = f.readlines() #读取所有的行以列表数据返回
f.close()
# print(f1)
# 创建地区的列表
arealist = [[1, '华北'], [2, '东北'], [3, '华东'], [4, '中南'], [5, '西南'], [6, '西北']]
areaopen = [] #创建空列表，用来装打开文件返回的f
arealistlen = len(arealist)  #计算长度，用于计算相应的索引值
# 根据地区对应创建文件
for i in arealist:
    areapath = r'E:\study\python\python-python3.7\python-JB\学习\eight\area\\' + i[1] + '.txt'
    f = codecs.open(areapath, 'wb', encoding='utf-8', errors='ignore')  #根据文件的名称进行创建
    areaopen.append(f)#将每个文件对应的f添加到列表里

for line in f1:
    #l = line
    l = (line.split(','))#将字符串以逗号进行分割成列表
    #print(l)
    areastr = l[1][0]  #取出身份证号的第一位
    for i in range(arealistlen):
        if int(areastr) == arealist[i][0]: #判断我地区列表数据是否与身份证号想匹配
            areaopen[i].write(line)  #将用户对应地区的信息写入文件中
            break #跳出循环体

for f in areaopen:
    f.close() #便利循环体

f.close()
