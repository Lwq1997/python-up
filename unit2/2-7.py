# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 15:52
# @Author  : Lwq
# @File    : 2-2.py
# @Software: PyCharm
"""
猜数字的小游戏，完成一个记录输入历史记录的功能
"""
from collections import deque
from random import randint


def guess(k, n):
    if k == n:
        print('恭喜你猜对了，这个数字是%d' % k)
        return True
    elif k > n:
        print('你猜错了，这个数比%d小' % k)
    elif k < n:
        print('你猜错了，这个数比%d大' % k)
    return False


def main():
    n = randint(1, 100)
    i = 0
    hq = deque([], 5)
    while True:
        line = input('[%d] 请输入一个1-100之间的数字:' % i)
        if line.isdigit():
            k = int(line)
            hq.append(k)
            i += 1
            if guess(k, n):
                break
        elif line == 'quit':
            break
        elif line == 'history':
            print(list(hq))


if __name__ == '__main__':
    main()
