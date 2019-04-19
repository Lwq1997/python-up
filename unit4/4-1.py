# -*- coding: utf-8 -*-
# @Time    : 2019/4/19 16:08
# @Author  : Lwq
# @File    : 4-1.py
# @Software: PyCharm
"""
可迭代对象Iterable(__iter__)和迭代器对象Iterator(__next__)
"""
from collections import Iterator, Iterable

import requests

# able = [0, 1, 2, 3]
# ator = able.__iter__()
# print(isinstance(able, Iterator))
# print(isinstance(able, Iterable))
# print(isinstance(ator, Iterable))
# print(isinstance(ator, Iterable))
# print(issubclass(list, Iterator))
# print(issubclass(list, Iterable))
# print(ator)
# print(ator is iter(able))
# print(ator is iter(ator))


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration

        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

    def get_weather(self, city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        r = requests.get(url)
        data = r.json()['data']['forecast'][0]
        return city, data['high'], data['low']


class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def show(w):
    for i in w:
        print(i)


if __name__ == '__main__':
    w = WeatherIterable(['北京', '西安', '海东', '哈尔滨'] * 10)
    show(w)
