#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/22 9:41
# @File    : 2、省份划分.py
# @Function:

import codecs

path = r'E:\study\python\python-python3.7\python-JB\学习\eight\kaifanglist.txt'
f = codecs.open(path, 'rb', encoding='utf-8', errors='ignore')
f1 = f.readlines()

provicelist = [[11, '北京'], [12, '天津'], [13, '河北'], [13, '山西'], [15, '内蒙古'], [21, '辽宁']]
prov = []

for i in provicelist:
    path = r'E:\study\python\python-python3.7\python-JB\学习\eight\pro\\' + i[1] + '.txt'
    f = codecs.open(path, 'wb', encoding='utf-8', errors='ignore')
    prov.append(f)

for x in f1:
    line = x.split(',')[1][0:2]
    for i in range(len(provicelist)):
        if int(line) == provicelist[i][0]:
            prov[i].write(x)
            break
for x in prov:
    x.close()


