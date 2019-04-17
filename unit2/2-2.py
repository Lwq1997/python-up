# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 15:52
# @Author  : Lwq
# @File    : 2-2.py
# @Software: PyCharm
"""
如何给元组中的每个元素命名，提高程序的可读性
"""
from collections import namedtuple
from enum import IntEnum


class StudentItem(IntEnum):
    NAME = 0,
    AGE = 1
    SEX = 2,
    EMAIL = 3


class TeacherItem(IntEnum):
    NAME = 1,
    AGE = 0,
    SEX = 3,
    EMAIL = 2


'''
使用枚举
'''
student = ('JIM', 6, 'male', 'jim@qq.com')
teacher = (6, 'Bob', 'bob@qq.com', 'male')
print(student[StudentItem.NAME], student[StudentItem.AGE])
print(teacher[TeacherItem.NAME], teacher[TeacherItem.AGE])

'''
使用namedtuple
'''
Student = namedtuple('Student', ['name', 'age', 'sex', 'email'])
s = Student('JIM', 6, 'male', 'jim@qq.com')
print(isinstance(s, tuple))
print(s)
print(s.name, s.age, s.email)
