import pygame.font
from pygame.sprite import Group

from Part_II_Project.Alien_invasion.chapter_12.ship import Ship


class Scoreboard():
	"""显示得分信息的类"""

	def __init__(self,ai_settings,screen,stats):
		'''初始化显示得分涉及的属性'''
		self.screen = screen
		self.screen_rect=screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		#显示得分信息使用的字体设置
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)

		#准备初始得分图像
		self.prep_images()
		# self.prep_score()
		# self.prep_high_score()
		# self.prep_level()
		# self.prep_ships()

	def prep_images(self):
		'''准备初始得分图像'''
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_ships(self):
		'''显示余下还有多少艘飞船'''
		self.ships=Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)

	def prep_level(self):
		'''将等级转换为渲染的图像'''
		self.level_image = self.font.render("Level: "+str(self.stats.level),True,
		                                    self.text_color,self.ai_settings.bg_color)

		#将等级放在得分下方
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom+10



	def prep_high_score(self):
		'''将最高得分转换为渲染的图像'''
		high_score = int(round(self.stats.high_score, -1))
		high_score_str ="{:,}".format(high_score)
		self.high_score_image = self.font.render("HS: "+high_score_str, True,
						self.text_color, self.ai_settings.bg_color)

		#将最高得分放在屏幕顶部中央
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.centerx = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top#这里是说明和得分的高度一样

	def prep_score(self):
		'''将得分转换为一副渲染的图像'''
		round_score = int(round(self.stats.score,-1))
		score_str = "{:,}".format(round_score)
		self.score_image = self.font.render("CS: "+score_str,True,self.text_color,
		                                    self.ai_settings.bg_color)

		#将得分放在屏幕右上角
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		'''在屏幕上显示得分'''
		self.screen.blit(self.score_image,self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image,self.level_rect)
		#绘制飞船
		self.ships.draw(self.screen)

#这条是为了测试用