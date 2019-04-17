# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 15:52
# @Author  : Lwq
# @File    : 2-2.py
# @Software: PyCharm
"""
如何多个字典中的公共key
"""
from functools import reduce
from random import randint, sample

d1 = {k: randint(1, 4) for k in sample('abcdefg', randint(3, 6))}
d2 = {k: randint(1, 4) for k in sample('abcdefg', randint(3, 6))}
d3 = {k: randint(1, 4) for k in sample('abcdefg', randint(3, 6))}
print('d1', d1)
print('d2', d2)
print('d3', d3)

d = [d1, d2, d3]
print('d', d)
'''
map函数来判断k这个元素是不是在d2和d3中。all函数说明两者都在
'''
print([k for k in d[0] if all(map(lambda d: k in d, d[1:]))])

'''
使用交集的概念
'''
print('使用map函数对d中的所有字典进行取key操作', list(map(dict.keys, d)))
print('使用reduce函数，对上面取出的所有key进行一个交集的判断', list(reduce(lambda a, b: a & b, map(dict.keys, d))))
