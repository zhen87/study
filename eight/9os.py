#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/3 20:02
# @File    : 9os.py
# @Function: os

import os

# 操作系统 nt 代表windows
# print(os.name)
# 创建文件夹
# os.mkdir('新的文件夹')
# 删除文件夹
# os.rmdir('新的文件夹')
# 获取当前的工作目录
# print(os.getcwd())
# 重命名
# print(os.rename('2、省份划分.py', '2省份划分.py'))
path = r'www\x\y'
# 拼接路径
print(os.path.join(path, 'a.txt'))
# 判断是否为目录
print(os.path.isdir('xxx'))
# 判断是否为文件
print(os.path.isfile(r'E:\study\python\python-python3.7\python-JB\学习\eight\kaifanglist.txt'))

# 判断文件的带下
print(os.path.getsize(r'E:\study\python\python-python3.7\python-JB\学习\eight\kaifanglist.txt'))

