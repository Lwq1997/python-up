# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 15:52
# @Author  : Lwq
# @File    : 2-2.py
# @Software: PyCharm
"""
如何统计列表中的元素频度
"""
from collections import Counter
from random import randint

'''
先把列表转换为字典（k是数据，V是频次），然后排序
'''
data = [randint(0, 10) for _ in range(30)]
print('data:', data)
l = dict.fromkeys(data, 0)
for i in data:
    l[i] += 1
print('l', l)
p = sorted(l.items(), key=lambda item: item[1], reverse=True)
for i, (k, v) in enumerate(p, 1):
    print('出现%d的次数是%d,排名%d' % (k, v, i))
print('p', p)
print('出现次数前三的是：', p[:3])

'''
使用Counter
'''
c = Counter(data)
print('c:', c)
print('出现次数前三的是：', c.most_common(3))
