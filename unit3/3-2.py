# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 15:53
# @Author  : Lwq
# @File    : 3-1.py
# @Software: PyCharm
"""
替换字符串
"""
import re
from functools import reduce

s = '2016-08-162016-08-162016-08-162016-08-162016-08-162016-08-162016-08-16'
print(re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\1/\2/\3', s))
