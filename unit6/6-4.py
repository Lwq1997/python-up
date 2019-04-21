# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 11:24
# @Author  : Lwq
# @File    : 6-1.py
# @Software: PyCharm
"""
让类支持比较操作
"""
from abc import ABCMeta
from functools import total_ordering


@total_ordering
class Shape(metaclass=ABCMeta):
    @classmethod
    def area(self):
        pass

    def __lt__(self, other):
        print('__lt__', self, other)
        return self.area() < other.area()


class Ract(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

    def __str__(self):
        return 'Rect(%s, %s)' % (self.l, self.w)


r1 = Ract(6, 8)
r2 = Ract(6, 9)
print(r1)
print(r2)
print(r1 < r2)
print(r1 > r2)
