import pygal
from data_visualization.chapter_15.random_walk import  RandomWalk
from data_visualization.chapter_15.random_walk import  RandomWalk
#这是第二个扩展，我需要用pypal模拟走路的数据集
import matplotlib.pyplot as plt

rw=RandomWalk(5000)#此处没有用默认值，而是增加了点数

rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
# 	            edgecolor='none', s=20)#此处修改为1
#
# 	# 突出起点和终点
# plt.scatter(0,0,c='green',edgecolor='none',s=100)
# plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',
# 	            s=100)


#分析结果IK
frequencies=[]
num=0
while num<5001:
	

for x in rw.x_values:
	for y in range((-rw.num_points/2),(rw.num_points/2)):
		if x in rw.x_values and y in rw.y_values:

			frequency=results.count(value) #我曹，真的牛逼，这个函数这样用
			frequencies.append(frequency)

# hist.x_labels=['2','3','4','5','6','7','8','9','10',"11",'12','13']
hist=pygal.Bar()

hist.title='Results of rolling a D6 and D10 50000 times'
# hist.x_labels=['2','3','4','5','6','7','8','9','10',"11",'12','13']
hist.x_labels=list(range(-600,600))
hist.x_labels=[str(i) for i in hist.x_labels]

print(hist.x_labels)
hist.x_title="Walk direction"
hist.y_title="Total steps of every direction"
#hist.title='random walk'
hist.add('D6+D10',frequencies)#

hist.render_to_file('die_visual.svg')
