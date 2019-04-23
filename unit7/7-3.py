# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 21:25
# @Author  : Lwq
# @File    : 7-1.py
# @Software: PyCharm
"""
如何实现一个带参数的装饰器（实现一个参数类型绑定的装饰器）
"""
import inspect


def type_assert(*ty_args, **ty_kwargs):
    """
    根据传入的ty属性去判断func中的参数是不是ty中定义的。
    :param ty_args:
    :param ty_kwargs:
    :return:
    """

    def decorator(func):
        """
        在这里实现一个参数和类型的绑定
        :param func:函数type的值
        :return:函数type的值
        """
        func_sign = inspect.signature(func)
        bind_type_dict = func_sign.bind_partial(*ty_args, **ty_kwargs).arguments

        def wrap(*args, **kwargs):
            """
            在这里通过检查用户的真正输入的类型，看是否符合上面定义的绑定类型
            :param args:函数的传入值
            :param kwargs:函数的传入值
            :return:
            """
            real_type_dict = func_sign.bind(*args, **kwargs).arguments
            for name, real_type in real_type_dict.items():
                type_ = bind_type_dict.get(name)
                if type_:
                    if not isinstance(real_type, type_):
                        raise TypeError('%s must be %s' % (name, type_))
            return func(*args, **kwargs)
        return wrap
    return decorator


@type_assert(int, int, str)
def f(a, b, c):
    pass


f(1, 2, 3)
