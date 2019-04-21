# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 11:24
# @Author  : Lwq
# @File    : 6-1.py
# @Software: PyCharm
"""
更小的空间创建大量实例
"""
import tracemalloc


class People1:
    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level


class People2:
    __slots__ = ['id', 'name', 'level']

    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level


# p1 = People1(1, 'jim', 20)
# p2 = People2(1, 'jim', 20)
# print(p1.__dict__)
# print('p1:', sys.getsizeof(p1.__dict__))
# p1.x = 'x1231231231231'
# print(p1.x)
# p1.__dict__.pop('x')
# print(p1.__dict__)
# print('p1(x):', sys.getsizeof(p1.__dict__))

tracemalloc.start()
# f1 = [People1(1,2,3) for _ in range(100000)]
f2 = [People2(1,2,3) for _ in range(100000)]
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('filename')
for stat in top_stats[:10]:
    print(stat)