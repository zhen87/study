#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/22 13:58
# @File    : 4县区列表.py
# @Function:

import codecs

# 源数据
path = r'E:\study\python\python-python3.7\python-JB\学习\eight\kaifanglist.txt'
f = codecs.open(path, 'rb', encoding='utf-8', errors='ignore')
f1 = f.readlines()
# 提供的数据
path = r'E:\study\python\python-python3.7\python-JB\学习\eight\县区列表list.txt'
m = codecs.open(path, 'rb', encoding='utf-8', errors='ignore')
# m = open(path,'rb',encoding='utf-8',errors='ignore')
m1 = m.readlines()

qvlist1 = []

# 源数据与提供的数据的对比数据存放文件
path = r'E:\study\python\python-python3.7\python-JB\学习\eight\list.txt'
file = codecs.open(path, 'wb', encoding='utf-8', errors='ignore')
qvlist1.append(file)

qvlist = []
# print(m1)
# newfile = codecs.open('qvlist.txt','wb',encoding='GBK',errors='ignore')
for i in m1:
    qvlist.append(i)
# print(qvlist)

for x in f1:
    # print(x)
    try:
        f2 = x.split(',')[5][0:7].replace('-', '').replace('\r\n', ' ')
    except:
        continue
    # print(f2)
    for n in range(len((qvlist))):
        #     #print(range(len(qvlist[n][1:7])))
        # print(qvlist[n][1:7])
        if f2 == qvlist[n][1:7]:
            # print(f2)
            # print(qvlist[n][1:7])
            # qvlist1[n].write(x)
            try:
                qvlist1[n].write(x)
            except IndexError as i:
                # print(qvlist1[n])
                continue
        #print(qvlist1)
