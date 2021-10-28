#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/3 20:19
# @File    : 10递归.py
# @Function: 递归

import os

# 递归输出所有的文件名

path = r'E:\study\python\python-python3.7\python-JB\学习\eight'
def myfile(path):
    sum = 0 #初始化文件大小
    myfilelist = os.listdir(path)  #返回当前文件夹目录和所有的文件
    for i in myfilelist: #便利
        newpath = os.path.join(path, i)  #将文件夹以及其目录进行拼接
        # print(newpath)
        if os.path.isdir(newpath): #判断是否为目录
            # myfile(newpath)# 为目录时进行递归查询
            # print(myfile(newpath))
            sum += myfile(newpath)  # 统计目录下的文件大小，如果是目录进入进行统计
        if os.path.isfile(newpath):# 如果是文件，直接统计
            #print('文件', i)
            sum += os.path.getsize(newpath) #累加文件的大小
    return sum
print(myfile(path))
