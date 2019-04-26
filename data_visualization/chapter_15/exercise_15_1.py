import matplotlib.pyplot as plt

#15-1 立方
# x_values=[1,2,3,4,5]
# y_values=[x**3 for x in x_values]
#
# plt.plot(x_values,y_values,linewidth=5)
#
# plt.title("cube of x_values",fontsize=24,)
# plt.xlabel('x_values',fontsize=14)
# plt.ylabel('y_values',fontsize=14)
#
# plt.tick_params(axis='both',which='major',labelsize=14)
#
# plt.show()


# x_values=list(range(1,5001))
# y_values=[x**3 for x in x_values]
#
# plt.plot(x_values,y_values,linewidth=5)
#
# plt.title("cube of x_values",fontsize=24,)
# plt.xlabel('x_values',fontsize=14)
# plt.ylabel('y_values',fontsize=14)
#
# plt.tick_params(axis='both',which='major',labelsize=14)
# plt.axis([0,5010,0,125175015001])
# plt.show()
#plt.savefig(str(a)+'png',bbox_inches='tight')


#15-2 指定颜色映射
x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Reds,
            s=40,edgecolor='none')
#plt.plot(x_values,y_values,linewidth=5)

plt.title("cube of x_values",fontsize=24,)
plt.xlabel('x_values',fontsize=14)
plt.ylabel('y_values',fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,5010,0,125175015001])
plt.show()
#plt.savefig('这里可以保存名字',bbox_inches='tight')

