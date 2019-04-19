# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 16:08
# @Author  : Lwq
# @File    : 4-1.py
# @Software: PyCharm
"""
使用生成器代替迭代器来实现可迭代对象
"""
from collections import Iterable


class PrimeNumbers(Iterable):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __iter__(self):
        # 这块原本是返回一个迭代器，但是我们现在使用生成器
        for k in range(self.a, self.b + 1):
            if self.is_prime(k):
                yield k

    def is_prime(self, k):
        # if k < 2:
        #     return False
        # for i in range(2, k - 1):
        #     if k % i == 0:
        #         return False
        return False if k < 2 else all(map(lambda x: k % x, range(2, k)))


if __name__ == '__main__':
    p = PrimeNumbers(1, 30)
    for i in p:
        print(i, end=' ')
