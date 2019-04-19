# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 16:08
# @Author  : Lwq
# @File    : 4-1.py
# @Software: PyCharm
"""
使用反向迭代器
"""
from decimal import Decimal


class FloatRange():
    def __init__(self, a, b, step):
        self.a = Decimal(str(a))
        self.b = Decimal(str(b))
        self.step = Decimal(str(step))

    def __iter__(self):
        t = self.a
        while t <= self.b:
            yield float(t)
            t += self.step

    def __reversed__(self):
        t = self.b
        while t >= self.a:
            yield float(t)
            t -= self.step


if __name__ == '__main__':
    f = FloatRange(0.2, 1.8, 0.2)
    for i in f:
        print(i)
    print('-'*20)
    for i in reversed(f):
        print(i)
