# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 16:08
# @Author  : Lwq
# @File    : 4-1.py
# @Software: PyCharm
"""
给迭代对象切片
"""
from itertools import islice

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l[2:8:2])
# print(l.__getitem__(slice(2, 8, 2)))
# print(isinstance(range(1, 10), Iterable))
# print(range(1, 10)[2:5])
# print('--------------------------')
f = open(r'F:\Workspaces\PycharmProjects\python-up\unit4\a.txt')
# for line in islice(f,1-1,5,2):
#     print(line)

# for x in f:
#     print(x)
# print('--------------------------')
# print(isinstance(f, Iterable))


# print(f[100:300]) 这个对象不能切片
def my_islice(iterable, start, stop, step=1):
    tmp = 0
    for index, item in enumerate(iterable):
        if index >= stop:
            break
        if index >= start:
            if tmp == 0:
                tmp = step
                yield item
            tmp -= 1


if __name__ == '__main__':
    f = open(r'F:\Workspaces\PycharmProjects\python-up\unit4\a.txt')
    for line in islice(f, 1 - 1, 5, 2):
        print(line)
    print('-' * 20)
    f = open(r'F:\Workspaces\PycharmProjects\python-up\unit4\a.txt')
    for x in my_islice(f, 1 - 1, 5, 2):
        print(x)
    print('-' * 20)
    for x in my_islice(range(0, 10), 5 - 1, 10):
        print(x)
    print('-' * 20)
    for x in islice(range(0, 10), 5 - 1, 10):
        print(x)
