# @Time    : 2020/7/22 18:36
# @File    : 5.py
# @Function: 获取A文件与B文件的重复数据，保存至C文件

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
file = codecs.open('iist.txt', 'wb', encoding='utf-8', errors='ignore')
for x in f1:
    try:
        f2 = x.split(',')[5]
        if f2 == '-':
            continue
    except IndexError as i:
        continue
    for n in range(len(m1)):
        try:
            # print(f2)
            # print(m1[n][1:7])
            if f2 == m1[n][1:7]:
                # print(f2)
                # print(x)
                file.write(x)
        except IndexError as i:
            continue
file.close()