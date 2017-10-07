# -*- coding=utf-8 -*-
from random_walk import RandomWalk
import matplotlib.pyplot as plt


while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_value, rw.y_value, s=5)
    plt.show()

    keep_running = input('Make another walk, (y/n):')
    if keep_running == 'n':
        break



