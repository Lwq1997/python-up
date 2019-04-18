# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 15:53
# @Author  : Lwq
# @File    : 3-1.py
# @Software: PyCharm
"""
删除无用字符
"""
import re

s = '  \n   abc   \t  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = '   \n abc \n \n 123 \t   '
print(re.sub('[\s]+', '', s))

s = '  abc  123'
print(s[2:5]+s[7:])

s = 'abcxyzaaxxyybbcczz'
print(s.maketrans('abcxyz', 'XYZABC'))
print(s.translate({ord('a'): 'X'}))
print(s.translate({ord('a'): None}))
print(s.translate(s.maketrans('abcxyz', 'XYZABC')))


