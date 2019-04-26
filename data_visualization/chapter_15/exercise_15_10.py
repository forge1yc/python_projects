# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pygal
from data_visualization.chapter_15.random_walk import  RandomWalk
from data_visualization.chapter_15.die import Die


#我这个用matplotlib 模拟了掷骰子

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')
die_1=Die(10)
die_2=Die(10)


#掷几次骰子，并将结果存储在一个列表中
results=[]
roll_numbers=50000
for roll_num in range(roll_numbers):#15-4-5分析结果
	result=die_1.roll()+die_2.roll()
	results.append(result)

#分析结果IK
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
	frequency=results.count(value) #我曹，真的牛逼，这个函数这样用
	frequencies.append(frequency)

x_values=list(range(2,max_result+1))
x_values=[str(i) for i in x_values]

point_numbers=list(range(1,roll_numbers+1))

plt.scatter(x_values, frequencies,c='Blue',
	            edgecolor='none', s=20)#此处修改为1
plt.xlabel("two D"+str(die_1.num_sides)+' sum of them',fontsize=14)
plt.ylabel('the values of die',fontsize=14,)
plt.title('result of die',fontsize=24,)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()#show 一定要放在最后
# # 突出起点和终点
# plt.scatter(0,0,c='green',edgecolor='none',s=100)
# plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolor='none',
#             s=100)
