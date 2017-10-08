# -*- coding=utf-8 -*-
import csv
import matplotlib.pyplot as plt
from datetime import datetime

#设置csv file数据来源
# file_name = 'sitka_weather_07-2014.csv'
file_name = 'sitka_weather_2014.csv'

with open(file_name) as f:
    reader = csv.reader(f, delimiter=',')
    #读取表头数据，下面就不会再读取了
    header_row = next(reader)

    # 显示csv的表头记录
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, highs, lows =[], [], []
    for row in reader:
        highs.append(int(row[1]))
        lows.append(int(row[3]))
        dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
    print(highs)


#设置图形大小
fig = plt.figure(dpi=128, figsize=(10, 6))
#设置图形数据
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
#设置图形之间的填充
plt.fill_between(dates, highs, lows, facecolor='blue',alpha=0.3)
#设置y轴的取值范围
plt.ylim([0, 120])

#设置图形的格式
plt.title("Daily High and Low Temperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(F)', fontsize=16)
#设置斜的日期标签
fig.autofmt_xdate()
#设置坐标轴刻度样式
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
