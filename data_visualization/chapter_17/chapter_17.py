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
#17 -1 -4 处理API响应

#执行API调用，并存储响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r=requests.get(url)
print("Status code:",r.status_code)

#将API响应存储在一个变量中
response_dict=r.json()
print("Total repositories:",response_dict['total_count'])

#探索有关仓库的信息
repo_dicts=response_dict['items']
print("Repositories returned:",len(repo_dicts))

#研究第一个仓库
repo_dict=repo_dicts[0]
print("\nKeys:",len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
	print('Name:', repo_dict['name'])
	print('Owner:', repo_dict['owner']['login'])
	print('Stars:', repo_dict['stargazers_count'])
	print('Repository:', repo_dict['html_url'])
	print('Created:', repo_dict['created_at'])
	print('Updated:', repo_dict['updated_at'])
	print('Description:', repo_dict['description'])


#处理结果
#print(response_dict.keys())




