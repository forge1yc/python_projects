# 16-2 制作世界人口地图：JSON模式

import json
from pygal_maps_world.i18n import COUNTRIES
import pygal_maps_world.maps as pm
import pygal
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle

def get_country_code(country_name):
	'''根据指定国家，返回pygal使用的两个字母的国家'''

	for code,name in COUNTRIES.items():
		if name == country_name:
			return code


	#如果没有找到指定的国家，返回none
	return None



#将数据加载到一个列表中
filename='gdp_json.json'
with open(filename) as f:
	pop_data = json.load(f)

gdps={}

#打印每个国家2010年的人口数量
for gdp_dict in pop_data:
	if gdp_dict['Year']==2016:
		country_name=gdp_dict['Country Name']
		gdp = int(float(gdp_dict['Value']))
		code=get_country_code(country_name)
		if  code:
			gdps[code]=gdp#这样就能直接添加进字典不需要append()方法,因为字典无序

#根据人口数量将所有国家分成三组
cc_pops_1,cc_pops_2,cc_pops_3={},{},{}
for cc,pop in gdps.items():
	if pop <100000000000:
		cc_pops_1[cc]=pop
	elif pop<1000000000000:
		cc_pops_2[cc]=pop
	else:
		cc_pops_3[cc]=pop

#分别显示每组有多少个国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))


#wm =pm.World()
wm_style=RotateStyle('#336699',base_style=LightColorizedStyle)
wm = pm.World(style=wm_style)
wm.title = 'The GDP of world in 2016,by Country'


wm.add('0-100bn',cc_pops_1,)
wm.add('100bn-1000bn',cc_pops_2)
wm.add('>1000bn',cc_pops_3)
wm.render_to_file('gdp_world.svg')

