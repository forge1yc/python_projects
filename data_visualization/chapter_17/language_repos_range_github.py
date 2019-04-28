#使用API
'''
在本章中，你将学习如何编写一个独立的程序，并对其获取的数
据进行可视化。这个程序将使用Web应用编程接口（API）自动请求
网站的特定信息而不是整个网页，再对这些信息进行可视化。由于这
样编写的程序始终使用最新的数据来生成可视化，因此即便数据瞬息
万变，它呈现的信息也都是最新的。
'''

#17 - 1 使用 web API
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#17 -1 -4 处理API响应
#languages1=['JavaScript','Ruby','C','Java','C++']
languages2=['Visual Basic .NET','SQL','Python','C#','Assembly language']
rs=[]
#执行API调用，并存储响应
for index,language in enumerate(languages2):
	url='https://api.github.com/search/repositories?q=language:'+language+'&sort=stars'
	print(languages2[index]+': ',requests.get(url).status_code)
	rs.append(requests.get(url))


#将API响应存储在一个变量中
for index,r in enumerate(rs):
	response_dict=r.json()
	print(languages2[index]+" Total repositories:",response_dict['total_count'])

	#探索有关仓库的信息
	repo_dicts=response_dict['items']

	names,plot_dicts=[],[]
	for repo_dict in repo_dicts:
		names.append(repo_dict['name'])

		#stars.append(repo_dict['stargazers_count'])
		plot_dict={
			'value':repo_dict['stargazers_count'],
			'label':str(repo_dict['description']),
			'xlink':repo_dict['html_url'],
			'total_count':response_dict['total_count']
		}
		plot_dicts.append(plot_dict)





	#print("Repositories returned:",len(repo_dicts))

	#可视化
	my_style=LS('#333366',base_style=LCS)

	my_config = pygal.Config()
	my_config.x_label_rotation = 45
	my_config.show_legend = False
	my_config.title_font_size=24
	my_config.label_font_size=14
	my_config.major_label_font_size=18
	my_config.truncate_label=15
	my_config.show_y_guides = False
	my_config.width=1000




	chart=pygal.Bar(style=my_style,config=my_config)#x_label必须斜着
	chart.title='Most-starred '+str(languages2[index])+' Projects on Github'
	chart.x_labels=names

	chart.add('',plot_dicts)
	chart.render_to_file(str(languages2[index])+'_repos.svg')

# #研究第一个仓库
# repo_dict=repo_dicts[0]
# print("\nKeys:",len(repo_dict))
# for key in sorted(repo_dict.keys()):
# 	print(key)
#
# print("\nSelected information about each repository:")
# for repo_dict in repo_dicts:
# 	print('Name:', repo_dict['name'])
# 	print('Owner:', repo_dict['owner']['login'])
# 	print('Stars:', repo_dict['stargazers_count'])
# 	print('Repository:', repo_dict['html_url'])
# 	print('Created:', repo_dict['created_at'])
# 	print('Updated:', repo_dict['updated_at'])
# 	print('Description:', repo_dict['description'])


#处理结果
#print(response_dict.keys())




