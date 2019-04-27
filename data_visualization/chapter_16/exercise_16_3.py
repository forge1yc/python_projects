#16-3 降雨量
# print(header_row)
import csv
from matplotlib import pyplot as plt
from datetime import datetime
filename='death_valley_2014.csv'
with open(filename)as f:
	reader=csv.reader(f)
	header_row = next(reader)
	print(header_row)

	dates1, highs1, lows1 = [], [], []
	for row in reader:
		try:
			# print(row)
			current_data = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[7])
			low = int(row[9])
		except ValueError:
			print(current_data, 'missing data')
		else:
			dates1.append(current_data)
			highs1.append(high)
			lows1.append(low)

fig=plt.figure(dpi=75,figsize=(16,9))
plt.plot(dates1,highs1,c='red',alpha=0.5)
plt.plot(dates1,lows1,c='blue',alpha=0.5)
plt.fill_between(dates1,highs1,lows1,facecolor='blue',alpha=0.1)

title="Daily high and low temperature - 2014\nSitka,CA"
plt.title(title,fontsize=24)
plt.xlabel('',fontsize=16)
fig.autofmt_xdate()#斜着显示
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)
#plt.ylim([0,120])

plt.show()
