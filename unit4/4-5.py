# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 16:08
# @Author  : Lwq
# @File    : 4-1.py
# @Software: PyCharm
"""
for循环遍历多个可迭代对象
"""
from itertools import chain
from random import randint

chinese = [randint(60, 100) for _ in range(0, 20)]
print('chinese:', chinese)
math = [randint(60, 100) for _ in range(0, 20)]
print('math:', math)
englist = [randint(60, 100) for _ in range(0, 20)]
print('englist:', englist)
print(list(zip(chinese, math, englist)))

t = []
for s1, s2, s3 in zip(chinese, math, englist):
    t.append(s1 + s2 + s3)

print('total1:', t)
print('total2:', [sum(s) for s in zip(chinese, math, englist)])
print('total3:', list(map(sum, zip(chinese, math, englist))))
print('total4:', list(map(lambda s1, s2, s3: s1 + s2 + s3, chinese, math, englist)))

print('zip:', list(zip([1, 2, 3], [4, 5])))
print('chain:', list(chain([1, 2, 3], [4, 5])))
