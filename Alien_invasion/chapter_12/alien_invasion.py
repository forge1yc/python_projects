#encoding=utf-8
#import sys 别的文件间接导入了

import pygame

from Part_II_Project.Alien_invasion.chapter_12.settings import Settings
from Part_II_Project.Alien_invasion.chapter_12.ship import Ship
from Part_II_Project.Alien_invasion.chapter_13.game_stats import GameStats
from Part_II_Project.Alien_invasion.chapter_14.scoreboard import Scoreboard
#from Part_II_Project.Alien_invasion.chapter_13.alien import Alien
#from Part_II_Project.Alien_invasion.chapter_12.ship import Qiyu
import Part_II_Project.Alien_invasion.chapter_12.game_functions as gf
from Part_II_Project.Alien_invasion.chapter_14.button import Button


from pygame.sprite import Group



def run_game():
	#初始化游戏，并创建一个屏幕对象
	pygame.init()
	ai_settings=Settings()  #创建实例
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#set mode也是一个类吗
	pygame.display.set_caption("Alien Invasion")

	#创建Play按钮
	play_button = Button(ai_settings,screen,'play')

	#创建一个用于存储游戏统计信息的实例,并创建记分牌
	stats=GameStats(ai_settings)
	sb=Scoreboard(ai_settings,screen,stats)

	# 创建一艘飞创
	ship=Ship(ai_settings,screen)
	#qiyu=Qiyu(screen)
	#创建一个用于存储子弹的编组
	bullets=Group()

	#创建一群外星人编组
	aliens=Group()

	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)



	#开始游戏主循环
	while True:


		#监视键盘和鼠标事件
		gf.check_events(ai_settings, screen, stats,sb,play_button,ship,
		                aliens,bullets)

		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens, bullets)
			gf.update_aliens(ai_settings, screen,stats,sb,ship, aliens, bullets)

		gf.update_screen(ai_settings, screen,stats,sb,ship,aliens,bullets,play_button)


		#bullets.update()

		# #删除已经消失的子弹
		# for bullet in bullets.copy():
		# 	if  bullet.rect.bottom <=0:
		# 		bullets.remove(bullet)
		#print(len(bullets)) #验证是否删除，这个输出写入到终端而花费的时间比将图形绘制到窗口还多

		#gf.update_screen(ai_settings, screen, qiyu)
		# #每次循环时都重新绘制屏幕
		# screen.fill(ai_settings.bg_color)
		# ship.blitme()
		#
		# # 让最近绘制的屏幕可见
		# pygame.display.flip() #这里管理屏幕更新

run_game()

