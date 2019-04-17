# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 15:33
# @Author  : Lwq
# @File    : 2-1.py
# @Software: PyCharm
"""
如何在列表，字典，集合中根据某些条件过滤数据
"""
from random import randint

'''
过滤掉负数
'''
L = [randint(-10, 10) for _ in range(10)]
print(L)
print([i for i in L if i >= 0])
print(list(filter(lambda x: x >= 0, L)))

'''
过滤掉90以下的学生
'''
D = {'student%d' % i: randint(50, 100) for i in range(1, 21)}
print(D)
print({key: value for key, value in D.items() if value >= 90})
print(dict(filter(lambda item: item[1] >= 90, D.items())))

'''
过滤掉集合中不能被3整除的数
'''
S = {randint(0, 20) for _ in range(20)}
print(S)
print({i for i in S if i % 3 == 0})
print(list(filter(lambda x: x % 3 == 0, S)))
