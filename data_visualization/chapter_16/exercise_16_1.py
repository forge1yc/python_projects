#16-2 比较洗卡特和死亡谷的气温



import csv
from matplotlib import pyplot as plt
from datetime import datetime


filename1='sitka_weather_2014.csv'
filename2='death_valley_2014.csv'
with open(filename1)as f:
	reader=csv.reader(f)
	header_row = next(reader)
	#print(header_row)

	# for index,column_header in enumerate(header_row):
	# 	print(index,column_header)

#16-1-3 提取并读取数据 ,日期和最高温，16-1-18 再绘制一个系列
	dates1,highs1,lows1=[],[],[]
	for row in reader:
		try:
			#print(row)
			current_data = datetime.strptime(row[0],"%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_data,'missing data')
		else:
			dates1.append(current_data)
			highs1.append(high)
			lows1.append(low)

with open(filename2)as f:
	reader = csv.reader(f)
	header_row = next(reader)
	# print(header_row)

	# for index,column_header in enumerate(header_row):
	# 	print(index,column_header)

	# 16-1-3 提取并读取数据 ,日期和最高温，16-1-18 再绘制一个系列
	dates2, highs2, lows2 = [], [], []
	for row in reader:
		try:
			# print(row)
			current_data = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_data, 'missing data')
		else:
			dates2.append(current_data)
			highs2.append(high)
			lows2.append(low)

#print(highs)
# 16-1-4 绘制气温图表
fig=plt.figure(dpi=75,figsize=(16,9))
plt.plot(dates1,highs1,c='red',alpha=0.5)
plt.plot(dates1,lows1,c='red',alpha=0.5)
plt.fill_between(dates1,highs1,lows1,facecolor='blue',alpha=0.1)

#这是为了画两个图准备的
title="Daily high and low temperature - 2014\nSitka,CA"
plt.title(title,fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#斜着显示
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
plt.ylim([0,120])


fig2=plt.figure(dpi=75,figsize=(16,9))#这句话可以多加一个图
plt.plot(dates2,highs2,c='blue',alpha=0.5)
plt.plot(dates2,lows2,c='blue',alpha=0.5)
plt.fill_between(dates2,highs2,lows2,facecolor='blue',alpha=0.1)
plt.ylim((0,120))# 列表和元组都可以


#设置图形格式
title="Daily high and low temperature - 2014\nDeath Valley,CA"
plt.title(title,fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#斜着显示
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)

plt.show()

#