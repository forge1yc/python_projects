from data_visualization.chapter_15.die import Die

import pygal
#创建两个骰子属于15-4-7,一个变为D10
#创建两个D6
die_1=Die(10)
die_2=Die(10)

#掷几次骰子，并将结果存储在一个列表中
results=[]
for roll_num in range(50000):#15-4-5分析结果
	result=die_1.roll()+die_2.roll()
	results.append(result)

#分析结果IK
frequencies=[]
max_result=die_1.num_sides+die_2.num_sides
for value in range(2,max_result+1):
	frequency=results.count(value) #我曹，真的牛逼，这个函数这样用
	frequencies.append(frequency)

#15-4-6
#对结果进行可视化分析
hist=pygal.Bar()

hist.title='Results of rolling a D6 and D10 50000 times'
# hist.x_labels=['2','3','4','5','6','7','8','9','10',"11",'12','13']
hist.x_labels=list(range(1,5))
hist.x_labels=[str(i) for i in hist.x_labels]

print(hist.x_labels)
hist.x_title="Walk direction"
hist.y_title="Total steps of every direction"
#hist.title='random walk'
hist.add('D6+D10',frequencies)#

hist.render_to_file('die_visual.svg')
#print(frequencies)

#print(results) 不要这行了

