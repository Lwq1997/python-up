# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 21:25
# @Author  : Lwq
# @File    : 7-1.py
# @Software: PyCharm
"""
如何实现属性可修改的函数装饰器（定义一个time，运行超过这个time，就记录到log，运行中可以动态的修改time）
"""
import inspect
import logging
import random
import time


def warn_timeout(timeout):
    def decorator(func):
        def wrap(*args, **kwargs):
            start = time.time()
            res = func(*args,**kwargs)
            used = time.time()-start
            if used>timeout:
                logging.warning('%s, %s > %s'% (func.__name__,used,timeout))
            return res
        def set_timeout(new_timeout):
            nonlocal timeout
            timeout = new_timeout

        wrap.set_timeout = set_timeout
        return wrap
    return decorator


@warn_timeout(1.5)
def f(i):
    print('in f[%s]' %i)
    while random.randint(0,1):
        time.sleep(0.6)

for i  in range(30):
    f(i)
f.set_timeout(1)
for i  in range(30):
    f(i)