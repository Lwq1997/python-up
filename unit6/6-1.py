# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 11:24
# @Author  : Lwq
# @File    : 6-1.py
# @Software: PyCharm
"""
实现inttuple,过滤传进来的非int且小于0的字符
"""


class IntTuple(tuple):
    def __new__(cls, iteratable):
        i_filter = (i for i in iteratable if isinstance(i, int) and i >= 0)
        return super().__new__(cls, i_filter)


t = ('a', 'b', 1, 2, 3, -1, 0, -2, ['a', 'b', '1'])
i = IntTuple(t)
print(i)
