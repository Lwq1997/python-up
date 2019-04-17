# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 15:52
# @Author  : Lwq
# @File    : 2-2.py
# @Software: PyCharm
"""
如何排序字典中的value
"""
from random import randint

'''
将字典转换为列表[元组]的形式
'''
D = {k: randint(60, 100) for k in 'abcdefghijklmn'}
print(D)
L = [(v, k) for k, v in D.items()]
print('L:', L)
print(sorted(L))
print(sorted(L, reverse=True))

'''
使用zip
'''
L = list(zip(D.values(), D.keys()))
print('L:', L)
print(sorted(L))
print(sorted(L, reverse=True))

'''
使用sorted的key属性
'''
p = sorted(D.items(), key=lambda item: item[1], reverse=True)
print('sorted,key', p)
for i, item in enumerate(p, 1):
    print(i, item[0], item[1])

'''
使用sorted
'''
p = sorted(((v, k) for k, v in D.items()), reverse=True)
print('sorted,key', p)
for i, item in enumerate(p, 1):
    print(i, item[0], item[1])
