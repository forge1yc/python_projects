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
filename='population_data.json'
with open(filename) as f:
	pop_data = json.load(f)


cc_populations={}

#打印每个国家2010年的人口数量
for pop_dict in pop_data:
	if pop_dict['Year']=='2010':
		country_name=pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code=get_country_code(country_name)
		if  code:
			cc_populations[code]=population#这样就能直接添加进字典不需要append()方法,因为字典无序

#根据人口数量将所有国家分成三组
cc_pops_1,cc_pops_2,cc_pops_3={},{},{}
for cc,pop in cc_populations.items():
	if pop <10000000:
		cc_pops_1[cc]=pop
	elif pop<100000000:
		cc_pops_2[cc]=pop
	else:
		cc_pops_3[cc]=pop

#分别显示每组有多少个国家
print(len(cc_pops_1),len(cc_pops_2),len(cc_pops_3))


#wm =pm.World()
wm_style=RotateStyle('#336699',base_style=LightColorizedStyle)
wm = pm.World(style=wm_style)
wm.title = 'World Population in 2010,by Country'


wm.add('0-10m',cc_pops_1,)
wm.add('10m-1bn',cc_pops_2)
wm.add('>1bn',cc_pops_3)
wm.render_to_file('world_population.svg')

