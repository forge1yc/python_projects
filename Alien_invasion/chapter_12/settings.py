#12-3-3 创建设置类

class Settings():
	'''存储《外星人入侵》的所有设置的类'''

	def __init__(self):
		'''初始化游戏的静态设置'''
		#屏幕设置
		self.screen_width=900
		self.screen_height=600
		self.bg_color=(230,230,230)

		#飞船的设置
		self.ship_speed_factor=1.5
		self.ship_limit=3

		#子弹设置
		self.bullet_speed_factor=1
		self.bullet_width =900
		self.bullet_height=15
		self.bullet_color=60,60,60# python 竟然支持这种格式
		self.bullets_allowed = 7  #玩家最多能在屏幕能够同时发送子弹的数量

		#外星人设置
		self.alien_speed_factor=1
		self.fleet_drop_speed=10
		# fleet_direction为1表示向右移，为-1表示向左移
		self.fleet_direction=1

		# 以什么样的速度加快游戏
		self.speedup_scale = 1.1

		#外星人点数的提高速度
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		'''初始化随游戏进行而变化的设置'''
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor=1

		#fleet_direction 为1表示向右，为-1 表示向左
		self.fleet_direction = 1

		#计分
		self.alien_points=50

	def increase_speed(self):
		'''提高速度设置,和外星人点数'''
		self.ship_speed_factor*=self.speedup_scale
		self.bullet_speed_factor*=self.speedup_scale
		self.alien_speed_factor*=self.speedup_scale

		self.alien_points = int(self.alien_points*self.score_scale)
		#print(self.alien_points) #这条是为了看点数的分值是多少









