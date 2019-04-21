import pygame
from pygame.sprite import Sprite
# import Part_II_Project.Alien_invasion.chapter_12.alien_invasion
# from pygame import *
class Ship(Sprite):

	def __init__(self,ai_settings,screen):# 这个screen 是一个
		'''初始化飞船并设置其初始位置'''
		super().__init__()
		self.screen=screen
		self.ai_settings=ai_settings

		# 加载飞船图像并获取其外接矩形
		self.image=pygame.image.load('images/ship.bmp')
		self.rect=self.image.get_rect()  #这个函数怎么不显示
		self.screen_rect=screen.get_rect()

		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom=self.screen_rect.bottom

		#在飞船的属性中存储小数值
		self.center=float(self.rect.centerx)

		# 移动标志
		self.moving_right = False
		self.moving_left =False

	def update(self):
		'''根据移动标志调整飞船的位置'''
		#更新飞船的center值，而不是rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			#self.rect.centerx += 1
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left>0:
			#self.rect.centerx -=1
			self.center -= self.ai_settings.ship_speed_factor

		#根据self.center更新rect对象
		self.rect.centerx=self.center


	def blitme(self):  #都是用这个函数绘制自己的图像
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		'''让飞船在屏幕上居中'''
		self.center = self.screen_rect.centerx




class Qiyu():
	'''这是我喜爱的琦玉老师'''

	def __init__(self,screen):
		'''初始化飞船并设置其初始位置'''
		self.screen = screen

		# 加载飞船图像并获取其外接矩形
		self.image = pygame.image.load('images/timg3.bmp')
		self.rect = self.image.get_rect()  # 这个函数怎么不显示
		self.screen_rect = screen.get_rect()

		# 将每艘新飞船放在屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.centerx



	def blitme(self):
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)




