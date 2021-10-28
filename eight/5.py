#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/22 18:36
# @File    : 5.py
# @Function:

import codecs
# 源数据
path = r'E:\study\python\python-python3.7\python-JB\学习\eight\kaifanglist.txt'
f = codecs.open(path, 'rb', encoding='utf-8', errors='ignore')
f1 = f.readlines()
# 提供的数据
f.close()
path = r'E:\study\python\python-python3.7\python-JB\学习\eight\县区列表list.txt'
m = codecs.open(path, 'rb', encoding='utf-8', errors='ignore')
# m = open(path,'rb',encoding='utf-8',errors='ignore')
m1 = m.readlines()
m.close()
for i in f1:
    try:
        f2 = i.split(',')[5][0:7].replace('-','')
    except IndexError as i:
        continue

    #print(f2)
    # f2 = i.split(',')[5][0:7].replace('-', '')
    # print(f2)

for x in m1:
    m2 = x.split(',')[0][1:7]
    #print(m2)
    for n in range(len(m1)):
        print(m2[n])
        print(f2)
    # try:
    #     if m2 == f2[n]:
    #         print(m2)
    # except IndexError as i:
    #     continue
    #     if m2 == f2:
    #         print(m2)
#print(m2)
    #sum += 1
# print(sum)






