import json
class GameStats():
	'''跟踪游戏的统计信息'''

	def __init__(self,ai_settings):
		'''初始化统计信息'''
		self.ai_settings=ai_settings
		self.reset_stats()    #为了调用方法初始化
		#游戏启动时处于非活动状态
		self.game_active=False
		# 在任何情况下都不应重置最高得分
		self.read_high_score()
		self.high_score=self.file_high_score

		#self.read_high_score()


	def reset_stats(self):
		'''初始化在游戏运行期间可能变化的统计信息'''
		self.ships_left = self.ai_settings.ship_limit #这也是一个属性吗,答案是，是的
		self.score=0
		self.level =1

	def read_high_score(self):
		filename='username.json'
		try:
			with open(filename) as f_obj:
				self.file_high_score = json.load(f_obj)
		except FileNotFoundError:
			self.file_high_score=0
			temp_high_score=self.file_high_score
			with open(filename,'w')as f_obj:
				json.dump(temp_high_score,f_obj)

	def write_high_score(self):
		filename='username.json'
		with open(filename,'w') as f_obj:
			json.dump(self.file_high_score,f_obj)

		# except FileNotFoundError:
		# 	temp_high_score=str(self.high_score)
		# 	with open(filename,'w')as f_obj:
		# 		json.dump(temp_high_score,f_obj)












