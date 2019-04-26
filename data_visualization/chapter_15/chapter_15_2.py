import matplotlib.pyplot as plt

# #15-2 绘制简单的折线图
#
# input_values=[1,2,3,4,5]
# squares=[1,4,9,16,25]
#
# plt.plot(input_values,squares,linewidth=5)
#
# #设置图表标题，并给坐标轴加上标签
# plt.title("square Numbers",fontsize=24)
#
# plt.xlabel("value",fontsize=14)
# plt.ylabel("Square of value",fontsize=14)
#
# #设置刻度标记大小
# plt.tick_params(axis='both',labelsize=14)
#
#
# plt.show()

#修改标签文字和线条

# plt.scatter(2,4,s=200)
#plt.show()
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values,y_values,s=100)
#
#
# plt.title("Squares Numbers",fontsize=24)
# plt.xlabel("value",fontsize=14)
# plt.ylabel("squares of value",fontsize=14)
#
# #设置刻度标记大小
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.show()


# x_values = list(range(1, 1001))
# y_values = [x**2 for x in x_values]
#
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none', s=40)
#
# # Set chart title, and label axes.
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # Set size of tick labels.
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# # Set the range for each axis.
# #plt.axis([0, 1100, 0, 1100000])
#
# plt.show()

#scatter 是散点图
x_values=list(range(1,1001))
y_values=[x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40,)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0,1100,0,1100000])

#plt.show()

#自动保存列表
plt.savefig('squares_plot.png',bbox_inches='tight')


