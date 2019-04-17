# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 15:52
# @Author  : Lwq
# @File    : 2-2.py
# @Software: PyCharm
"""
如何让字典保持有序（进去的顺序和出来的顺序是一样的）
"""
from collections import OrderedDict
from itertools import islice
from random import shuffle

players = list('abcdefg')
print('原始顺序：', players)
shuffle(players)
print('打乱顺序：', players)
od = OrderedDict()
for i, p in enumerate(players, 1):
    od[p] = i
print('出字典的顺序：', od)


def query_by_order(d, a, b=None):
    a -= 1
    if b is None:
        b = a + 1
    return list(islice(d, a, b))


print('查询出第3-6进入字典的player：', query_by_order(od, 3, 6))
print('查询出第3个进入字典的player：', query_by_order(od, 3))
