# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 21:25
# @Author  : Lwq
# @File    : 7-1.py
# @Software: PyCharm
"""
如何使用函数装饰器
"""
import time


def memo(func):
    cache = {}

    def wrap(*args):
        res = cache.get(args)
        if not res:
            res = cache[args] = func(*args)
        return res

    return wrap


# cache = {}
def fibonacci(n):
    # res = cache.get(n)
    # if res:
    #     return res
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
    # res = cache[n] = fibonacci(n-1)+fibonacci(n-2)
    # return res


# 有100层楼梯，一个人一次可以脉1-3层，有几种走法
@memo
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n - step, steps)
    return count


start = time.time()
fibonacci = memo(fibonacci)
print(fibonacci(100))
print(climb(50, (1, 2, 3)))
print((time.time() - start))
