import csv
from matplotlib import pyplot as plt
from datetime import datetime

import json
from pygal_maps_world.i18n import COUNTRIES
import pygal_maps_world.maps as pm
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

#Agricultural irrigated land (% of total agricultural land)





def get_country_code(country_name):
	'''根据指定国家，返回pygal使用的两个字母的国家'''

	for code,name in COUNTRIES.items():
		if name == country_name:
			return code


	#如果没有找到指定的国家，返回none
	return None

#filename='sitka_weather_2014.csv'
filename='API_AG.LND.IRIG.AG.ZS_DS2_en_csv_v2_10578607.csv'
#filename2='API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_10580107.csv'
with open(filename,'r', encoding='utf-8')as f:
	reader=csv.reader(f)
	header_row = next(reader)
	print(header_row)
	#print(header_row)

	# for index,column_header in enumerate(header_row):
	# 	print(index,column_header)

#16-1-3 提取并读取数据 ,日期和最高温，16-1-18 再绘制一个系列
	cc_test={}
	#countries,scales=[],[]
	for row in reader:
		try:
			country_name=row[0]
			code=get_country_code(country_name)
			value=float(row[-9])
		except ValueError or NameError:	#if row[-1]=='' or code==None:
			print(country_name,code,row[-2],"miss ")
		else:
			cc_test[code]=value
print(cc_test)
cc_pops_1,cc_pops_2,cc_pops_3={},{},{}
for cc,pop in cc_test.items():
	if pop <0.5:
		cc_pops_1[cc]=pop
	elif pop<2:
		cc_pops_2[cc]=pop
	else:
		cc_pops_3[cc]=pop

#分别显示每组有多少个国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))


#wm =pm.World()
wm_style=RotateStyle('#336699',base_style=LightColorizedStyle)
wm = pm.World(style=wm_style)
wm.title = 'Agricultural irrigated land (% of total agricultural land)\n by country,2018'


wm.add('0-0.5',cc_pops_1,)
wm.add('0.5-2',cc_pops_2)
wm.add('>2',cc_pops_3)
wm.render_to_file('Agricultural irrigated land.svg')
