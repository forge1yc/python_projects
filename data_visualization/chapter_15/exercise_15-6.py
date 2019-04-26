from data_visualization.chapter_15.die import Die
# 15-6 自动生成标签，已经做完
import pygal
#创建两个骰子属于15-4-7,一个变为D10
#创建两个D6
die_1=Die(8)
die_2=Die(8)
die_3=Die(8)

#掷几次骰子，并将结果存储在一个列表中
results=[]
for roll_num in range(30000):#15-4-5分析结果
	result=die_1.roll()*die_2.roll()*die_3.roll()
	results.append(result)

#分析结果IK
frequencies=[]
max_result=die_1.num_sides*die_2.num_sides*die_2.num_sides
for value in range(2,max_result+1):
	frequency=results.count(value) #我曹，真的牛逼，这个函数这样用
	frequencies.append(frequency)

#15-4-6
#对结果进行可视化分析
hist=pygal.Bar()

hist.title='Results of rolling a 3*D8  30000 times'
# hist.x_labels=['2','3','4','5','6','7','8','9','10',"11",'12','13']
hist.x_labels=list(range(1,513))
hist.x_labels=[str(i) for i in hist.x_labels]#15-6

print(hist.x_labels)
hist.x_title="Result"
hist.y_title="Frequency of Result"

hist.add('D8*D8*D8',frequencies)#这里书中单词

hist.render_to_file('die_visual.svg')
#print(frequencies)

#print(results) 不要这行了

#15-7 两个D8骰子 会向绝对正太分布趋近
#15-8 同时掷三个筛子


#15-9 将点数相乘

#15-10 练习使用本章介绍的两个库

# 尝试使用 matplotlib 通过可视化来模拟掷骰子
# 的情况，并尝试使用 Pygal 通过可视化来模拟随机漫步的情况
#这个好像很难哦