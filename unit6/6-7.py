# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 14:06
# @Author  : Lwq
# @File    : 6-7.py·
# @Software: PyCharm
"""
通过实例方法名称调用方法
"""
from lib1 import Circle
from lib2 import Triangle
from lib3 import Rectangle
from operator import methodcaller


def get_area(shape, method_name=['area', 'get_area', 'getArea']):
    for name in method_name:
        if hasattr(shape, name):
            return methodcaller(name)(shape)
        # f = getattr(shape, name, None)
        # if f:
        #     return f()


shape1 = Circle(1)
shape2 = Triangle(3, 4, 5)
shape3 = Rectangle(4, 6)

shape_list = [shape1, shape2, shape3]
# 获得面积列表
area_list = list(map(get_area, shape_list))
print(area_list)
