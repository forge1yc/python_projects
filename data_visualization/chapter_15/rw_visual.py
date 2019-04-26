import matplotlib.pyplot as plt

from data_visualization.chapter_15.random_walk import  RandomWalk

#创建一个RandomWaik实例，并将其包含的点都绘制出来
while True:
	rw=RandomWalk(5000)#此处没有用默认值，而是增加了点数
	rw.fill_walk()

	#设置绘图窗口的尺寸
	plt.figure(figsize=(16,9),dpi=75)
	plt.scatter(rw.x_values,rw.y_values,s=15)
	# plt.show()

	#指定颜色,+渐变色，注意列表和单点不同
	# point_numbers = list(range(rw.num_points))
	# plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Reds,
	#             # s=15,edgecolor='none',)

	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
	            edgecolor='none', s=20)#此处修改为1

	# 突出起点和终点
	plt.scatter(0,0,c='green',edgecolor='none',s=100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',
	            s=100)

	#隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()#show 一定要放在最后
	plt.tick_params(axis='both', which='major', labelsize=14)
	keep_running=input("Make another walk?(y/n): ")
	if keep_running =='n':
		break


