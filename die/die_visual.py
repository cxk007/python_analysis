# -*- coding=utf-8 -*-
import pygal
from die import Die



die = Die()
# 算出筛子结果
result = []
for roll_num in range(50000):
    result.append(die.roll())
#算出各个点数的频率
frequency = []
for value in range(1, die.num_sides):
    frequency.append(result.count(value))


hist = pygal.Bar()

hist.title = 'Result of rolling one dice(6) 50000 times'
hist.x_labels = ['1', '2', '3', '4', '5', '6' ]
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequency)
hist.render_to_file('die_visual.svg')
