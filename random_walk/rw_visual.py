# -*- coding=utf-8 -*-
from random_walk import RandomWalk
import matplotlib.pyplot as plt


while True:
    rw = RandomWalk(50000)
    rw.fill_walk()

    # plt.figure(figsize=(16,9))
    plt.figure(dpi=, figsize=(10,6))


    point_numbers = list(range(rw.num_points))

    #随机漫步由深到浅着色
    plt.scatter(rw.x_value,rw.y_value,c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=1)
    #正常随机漫步
    # plt.scatter(rw.x_value, rw.y_value, s=5)

    #突出起点和终点
    #设置起点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    #设置终点
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=100)

    #隐藏坐标轴
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)


    plt.show()

    keep_running = input('Make another walk, (y/n):')
    if keep_running == 'n':
        break



