import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#17 -1 -4 处理API响应
#languages1=['JavaScript','Ruby','C','Java','C++']
#languages2=['Visual Basic .NET','SQL','Python','C#','Assembly language']
languages=['JavaScript','Ruby','C','Java','C++','Visual Basic .NET','SQL','Python','C#','Assembly language']
rs=[]
#执行API调用，并存储响应
#for index,language in enumerate(languages):
url='https://api.github.com/search/repositories?q=language:'+languages[-3]+'&sort=stars'
req=requests.get(url)
print(languages[-3]+': ',req.status_code)



#将API响应存储在一个变量中
# for index,r in enumerate(rs):
print(req)
response_dict=req.json()
print(response_dict)
print(languages[-3]+" Total repositories:",response_dict['total_count'])

repo_dicts=response_dict['items']
print(repo_dicts)


#探索有关仓库的信息
repo_dicts=response_dict['items']
print("Repositories returned:", len(repo_dicts))

#研究第一个仓库
repo_dict=repo_dicts[1]
print("\nKeys:", len(repo_dict))
for key in repo_dict.keys():
	print(key)


