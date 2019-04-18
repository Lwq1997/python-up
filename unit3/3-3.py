# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 15:53
# @Author  : Lwq
# @File    : 3-1.py
# @Software: PyCharm
"""
拼接字符串
"""
from functools import reduce

l = ['abc', 'def', 'ghi', 'jkl']
s = ''
for ss in l:
    s += ss
print(s)

print(reduce(str.__add__, l))

print(''.join(l))
