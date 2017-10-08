# -*- coding=utf-8 -*-
import pygal
from die import Die

#创建两个die 实例
die_1 = Die(6)
die_2 = Die(10)
#计算所有可能结果
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#分析结果的频率
frequency = []
max_result = die_1.num_sides +die_2.num_sides
for value in range(2, max_result+1):
    frequency.append(results.count(value))
#可视化结果
hist = pygal.Bar()

hist.title = 'Result of rolling die(6) and die(10) 50000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D10', frequency)
hist.render_to_file('2dice(D6 + D10)_visual.svg')
