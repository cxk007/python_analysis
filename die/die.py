# -*- coding=utf-8 -*-
from random import randint


class Die():
    """表示一个筛子的类"""
    def __init__(self, num_sides=6):
        """
        设置筛子默认的面
        :param num_sides:
        """
        self.num_sides = num_sides

    def roll(self):
        """
        模拟掷筛子的随机数
        :return:
        """
        return randint(1, self.num_sides)

