# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 15:53
# @Author  : Lwq
# @File    : 3-1.py
# @Software: PyCharm
"""
对齐字符串
"""

s = 'abc'
print(s.ljust(10))
print(s.ljust(10, '*'))
print(s.rjust(10))
print(s.rjust(10, '*'))
print(s.center(10))
print(s.center(10, '*'))
print('-----------format-----------------------')
print(format(s, '<10'))
print(format(s, '*<10'))
print(format(s, '>10'))
print(format(s, '*>10'))
print(format(s, '^10'))
print(format(s, '*^10'))
print('--------format数字--------------------')
print(format(123, '+'))
print(format(-123, '+'))
print(format(123, '<10'))
print(format(123, '>10'))
print(format(123, '=10'))
print(format(123, '<+10'))
print(format(123, '>+10'))
print(format(123, '=+10'))
print(format(123, '0=+10'))
print(format(-123, '0=+10'))
