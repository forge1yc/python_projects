from random import choice

class RandomWalk():
	'''一个生成随机漫步数据的类'''

	def __init__(self,num_points=5000):
		'''初始化随机漫步的属性'''
		self.num_points = num_points

		#所有的随机漫步都始于（0,0）
		self.x_values=[0]
		self.y_values=[0]

	def fill_walk(self):
		'''计算随机漫步包含的所有点'''

		# #不断进步，直到列表到指定的长度
		# while len(self.x_values)<self.num_points:
		# 	#决定前进方向以及沿这个方向前进的距离
		# 	x_direction = choice([1,-1])
		# 	#15 -4 改进随机漫步
		# 	x_distance = choice([0,1,2,3,4,5,6,7,8,9])
		# 	x_step = x_direction * x_distance
		#
		# 	y_direction = choice([1, -1])
		# 	y_distance = choice([0, 1, 2, 3, 4])
		# 	y_step = y_direction * y_distance
		#
		# 	#拒绝原地踏步
		# 	if x_step == 0 and y_step == 0:
		# 		continue
		while len(self.x_values) < self.num_points:
			x_step=self.get_step()
			y_step=self.get_step()
			#计算下一个点的x和y值
			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)

	#15 - 5 重构
	def get_step(self):
		active=True
		temp_step=-1
		while active:
			# 决定前进方向以及沿这个方向前进的距离
			temp_direction = choice([1, -1])
			# 15 -4 改进随机漫步
			temp_distance = choice([0, 1, 2, 3, 4])
			temp_step = temp_direction * temp_distance

			# y_direction = choice([1, -1])
			# y_distance = choice([0, 1, 2, 3, 4])
			# y_step = y_direction * y_distance

			# 拒绝原地踏步
			if temp_step == 0:
				continue
			else:
				active=False


		return temp_step
		# 计算下一个点的x和y值
		# next_x = self.x_values[-1] + x_step
		# next_y = self.y_values[-1] + y_step
		#
		# self.x_values.append(next_x)
		# self.y_values.append(next_y)

