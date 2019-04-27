# 16-2 制作世界人口地图：JSON模式

import json
from pygal_maps_world.i18n import COUNTRIES
import pygal_maps_world.maps as pm
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


#这段代码是为了找出格式不对的国家，回答课后题 16-5
for pop_dict in pop_data:
	if pop_dict['Year']=='2010':
		country_name=pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code=get_country_code(country_name)
		if  code==None:
			print(country_name)


#打印每个国家2010年的人口数量
for pop_dict in pop_data:
	if pop_dict['Year']=='2010':
		country_name=pop_dict['Country Name']
		population = int(float(pop_dict['Value']))
		code=get_country_code(country_name)
		if  code:
			cc_populations[code]=population#这样就能直接添加进字典不需要append()方法,因为字典无序
		# else:                             #这块没必要留着了
		# 	print("Error - "+country_name)

		#print(country_name+': '+str(population))

wm =pm.World()
wm.title = 'World Population in 2010,by Country'
# wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
# wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
# wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
# 			'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.add('2010',cc_populations)
wm.render_to_file('world_population.svg')

