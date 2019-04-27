#  第十六章 下载数据
'''
在本章中，你将从网上下载数据，并对这些数据进行可视化。网
上的数据多得难以置信，且大多未经过仔细检查。如果能够对这些数
据进行分析，你就能发现别人没有发现的规律和关联。
我们将访问并可视化以两种常见格式存储的数据： CSV和JSON。
我们将使用Python模块csv来处理以CSV（逗号分隔的值）格式存储
的天气数据，找出两个不同地区在一段时间内的最高温度和最低温
度。然后，我们将使用matplotlib根据下载的数据创建一个图表，展
示两个不同地区的气温变化：阿拉斯加锡特卡和加利福尼亚死亡谷。
在本章的后面，我们将使用模块json来访问以JSON格式存储的人口
数据，并使用Pygal绘制一幅按国别划分的人口地图。
阅读本章后，你将能够处理各种类型和格式的数据集，并对如何创建复杂的图表有更
深入的认识。要处理各种真实世界的数据集，必须能够访问并可视化各种类型和格式的在
线数据
'''
import csv
from matplotlib import pyplot as plt
from datetime import datetime


#filename='sitka_weather_2014.csv'
filename='death_valley_2014.csv'
with open(filename)as f:
	reader=csv.reader(f)
	header_row = next(reader)
	#print(header_row)

	# for index,column_header in enumerate(header_row):
	# 	print(index,column_header)

#16-1-3 提取并读取数据 ,日期和最高温，16-1-18 再绘制一个系列
	dates,highs,lows=[],[],[]
	for row in reader:
		try:
			#print(row)
			current_data = datetime.strptime(row[0],"%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_data,'missing data')
		else:
			dates.append(current_data)
			highs.append(high)
			lows.append(low)

	print(highs)
# 16-1-4 绘制气温图表
fig=plt.figure(dpi=75,figsize=(16,9))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)


#设置图形格式
title="Daily high and low temperature - 2014\nDeath Valley,CA"
plt.title(title,fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#斜着显示
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()


