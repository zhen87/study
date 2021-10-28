#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/22 19:22
# @File    : 6pickle.py
# @Function  列表写入文件，文件可被读取


import pickle
f = open('iist.txt','wb')
mylist = [['a,b'],[1,2]]
pickle.dump(mylist,f) #将列表写入文件
f.close()

f = open('iist.txt','rb')
print(pickle.load(f)) #将列表数据读取出来




