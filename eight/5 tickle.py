#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/22 16:21
# @File    : 5 tickle.py
# @Function:


import pickle
f = open('iist.txt', 'wb')
mylist = [[1, 2, 3], [2, 3, 4]]
f.write(str(mylist).encode('utf-8'))
f.flush()
