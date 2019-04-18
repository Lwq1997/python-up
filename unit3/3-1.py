# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 15:53
# @Author  : Lwq
# @File    : 3-1.py
# @Software: PyCharm
"""
拆分含有多种分隔符的字符串
"""
import re
from functools import reduce

s = 'ab/cd*efg,hijk\tlmn.opq'

print([ss.split('*') for ss in s.split('/')])
print(list(map(lambda ss: ss.split('*'), s.split('/'))))
t = []
print(list(map(t.extend, [ss.split('*') for ss in s.split('/')])))
print(t)


def my_split(s, seqs):
    res = [s]
    for seq in seqs:
        t = []
        list(map(lambda ss: t.extend(ss.split(seq)), res))
        res = t
    return res


print('方法一：', my_split(s, '*,/\t.'))

print('方法二(不推荐)：', list(reduce(lambda l, sep: sum(map(lambda ss: ss.split(sep), l), []), '*,/\t.', [s])))

print('方法三(推荐)：', re.split('[*,/\t.]+', s))
