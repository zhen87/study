#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/3 19:34
# @File    : 8xian.py
# @Function:

import pickle
import codecs

# 将xian.txt文件打开，并加载在mylist中
f = open('xian.txt', 'rb')
mylist = pickle.load(f)
f.close()
# 打开源数据
path = r'E:\study\python\python-python3.7\python-JB\学习\eight\kaifanglist.txt'
f = codecs.open(path, 'rb', encoding='utf-8', errors='ignore')
f1 = f.readlines()
# 遍历mylist，用list中的数据命名文件，
# 创建一个空list，放置文件名称
flist = []
for i in mylist:
    path = r'E:\study\python\python-python3.7\python-JB\学习\eight\xian\\' + i[1] + '.txt'
    f = codecs.open(path, 'wb', encoding='utf-8', errors='ignore')
    flist.append(f)
#将list数据与源数据对比
for line in f1:
    xianstr = line.split(',')[1][0:6] #将源数据进行切割成list，并取出前六位
    for i in range(len(mylist)):
        if str(mylist[i][0]) == xianstr: #数据对比
            flist[i].write(line)
            #print(line)

for m in flist:
    m.close




