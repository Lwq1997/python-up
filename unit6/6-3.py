# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 11:24
# @Author  : Lwq
# @File    : 6-1.py
# @Software: PyCharm
"""
创建可管理的对象属性
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def R(self):
        return round(self.radius, 1)

    @R.setter
    def R(self, radius):
        if isinstance(radius, int):
            raise Exception('wrong type')
        self.radius = radius

    @property
    def S(self):
        return round(self.radius ** 2 * math.pi, 2)

    @S.setter
    def S(self, s):
        self.radius = math.sqrt(s / math.pi)


c = Circle(12.9683)
# c.R = 12.56
print(c.R)
print(c.S)
