# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt


#数据区域
# x_value = [1, 2, 3, 4, 5]
# y_value = [1,4,9,16,25]

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

#设置散点图数据和颜色
# plt.scatter(x_value, y_value, c='red', edgecolors='none', s=40)

#设置散点图颜色为蓝色渐变
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolors='none', s=40)

#设置图表标题并给坐标轴加上标签.
plt.title('Square Numbers', fontsize =24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

#显示图标
plt.show()

#自动保存图表
# plt.savefig('squares_plot.png', bbox_inches='tight')

