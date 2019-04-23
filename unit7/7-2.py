# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 21:25
# @Author  : Lwq
# @File    : 7-1.py
# @Software: PyCharm
"""
如何为被装饰的函数保存元数据
"""
import functools

"""
def f():
    pass


print(f.__name__)
print(f.__module__)
print(f.__doc__)


def f(a: int, b: int) -> int:
    pass


print(f.__annotations__)


def f(a, b=1, c=[]):
    pass


print(f.__defaults__)

def f(a):
    return lambda n:a**n

g = f(3)
print(g(4))
print(g.__closure__)
c = g.__closure__[0]
print(c.cell_contents)
"""


def my_decorator(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        '''某功能的装饰器函数'''
        return func(*args, **kwargs)

    return wrap


@my_decorator
def xxx_func(a, b):
    '''xxx_func 函数文档'''
    pass


print(xxx_func.__name__)
print(xxx_func.__doc__)
