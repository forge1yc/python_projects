# 12-5 重构：模块game_functions
'''在大型项目中，经常需要在添加新代码前重构既有代码。重构旨在简化既有代码的结构，使
其更容易扩展。在本节中，我们将创建一个名为game_functions的新模块，它将存储大量让游戏
《外星人入侵》运行的函数。通过创建模块game_functions，可避免alien_invasion.py太长，并使
其逻辑更容易理解。'''

#12-5-1 函数check_events()+ #12-6-1 相应按键
import sys
from Part_II_Project.Alien_invasion.chapter_12.bullet import Bullet
from Part_II_Project.Alien_invasion.chapter_13.alien import Alien
from random import randint
import pygame
from time import sleep

def check_keydown_events(event,ai_settings,screen,ship,bullets):
	'''响应按键'''
	if event.key==pygame.K_RIGHT:
		#print(event.key)  #这里本质是映射 对比，向右键是 字符串’‘275

		ship.rect.centerx+=1
		ship.moving_right=True
	elif event.key ==pygame.K_LEFT:
		#print(event.key)   #这里是276
		ship.moving_left=True
	elif event.key==pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key==pygame.K_q: #这里可以随时退出
		sys.exit()



def fire_bullet(ai_settings,screen,ship,bullets):
	'''如果还没有到达限制，就发射一颗子弹'''
	# 创建一颗子弹，并将其加入到编组bullets中
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event,ship):
	'''按键松开'''
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False



def check_events(ai_settings, screen, stats,sb, play_button, ship,aliens, bullets,):
	'''响应按键和鼠标事件'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#stats.write_high_score()      这句话放这没用不知道为什么
			sys.exit()

		elif event.type==pygame.KEYDOWN:
			# if event.key==pygame.K_RIGHT:
			#
			# 	# ship.rect.centerx+=1
			# 	ship.moving_right=True
			# elif event.key ==pygame.K_LEFT:
			# 	ship.moving_left=True
			check_keydown_events(event,ai_settings,screen,ship,bullets)#这是重构完的
		elif event.type ==pygame.KEYUP:
			# if event.key ==pygame.K_RIGHT:
			# 	ship.moving_right=False
			# elif event.key ==pygame.K_LEFT:
			# 	ship.moving_left=False
			check_keyup_events(event,ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y=pygame.mouse.get_pos()
			check_play_button(ai_settings,screen,stats,sb,play_button,ship,
			                  aliens,bullets,mouse_x,mouse_y)


def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,
                      bullets,mouse_x,mouse_y):
	"""在玩家单击Play按钮时开始新游戏"""
	button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		#重置游戏设置
		ai_settings.initialize_dynamic_settings()
		#隐藏光标
		pygame.mouse.set_visible(False)

		#重置游戏统计信息
		stats.reset_stats()
		stats.game_active = True

		#重置记分牌图像
		sb.prep_images()
		# sb.prep_score()
		# sb.prep_high_score()
		# sb.prep_level()
		# sb.prep_ships()

		#清空外星人和子弹列表
		aliens.empty()
		bullets.empty()

		#创建一群新的外星人，并让飞船居中
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()





#12-5-2 update_screen()
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):# ship 和 screens 都是对象
	'''更新屏幕上的图像，并切换到新屏幕'''
	# 每次循环时都重新绘制屏幕
	screen.fill(ai_settings.bg_color)

	# 在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():# 方 法bullets.sprites()返回一个列表
		bullet.draw_bullet()

	ship.blitme()
	aliens.draw(screen)
	#alien.blitme()

	#显示得分
	sb.show_score()

	# 如果游戏处于非活动状态，就绘制Play按钮
	if not stats.game_active:
		play_button.draw_button()

	# 让最近绘制的屏幕可见
	pygame.display.flip()


def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
	'''更新子弹的位置，并删除已经消失的子弹'''
	#更新子弹的位置
	bullets.update()

	# 删除已经消失的子弹
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	check_bullet_alien_collisions(ai_settings, screen,stats,sb,ship, aliens, bullets)
	# stats.file_high_score=stats.score              #放这里也是可行的
	# stats.write_high_score()
	# 检查是否有子弹击中了外星人
	# # 如果是这样，就删除相应的子弹和外星人
	# collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
	# if  len(aliens)==0:
	# 	#删除现有的子弹并新建一群外星人
	# 	bullets.empty()
	# 	create_fleet(ai_settings,screen,ship,aliens)


def check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens, bullets):
	"""响应子弹和外星人的碰撞"""
	# 删除发生碰撞的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	if collisions:
		for aliens in collisions.values():
			stats.score += ai_settings.alien_points*len(aliens)
			sb.prep_score()
		check_high_score(stats,sb)
	start_new_level(ai_settings,bullets,stats,sb,aliens,screen,ship)
	# if len(aliens) == 0:
	# 	# 删除现有的所有子弹,加快游戏节奏，并创建一群新的外星人,并提高了一个等级
	# 	bullets.empty()
	# 	ai_settings.increase_speed()
	#
	# 	# 提高等级
	# 	stats.level += 1
	# 	sb.prep_level()
	#
	# 	create_fleet(ai_settings, screen, ship, aliens)

def start_new_level(ai_settings,bullets,stats,sb,aliens,screen,ship):
	if len(aliens) == 0:
		# 删除现有的所有子弹,加快游戏节奏，并创建一群新的外星人,并提高了一个等级
		bullets.empty()
		ai_settings.increase_speed()

		# 提高等级
		stats.level += 1
		sb.prep_level()

		create_fleet(ai_settings, screen, ship, aliens)



def get_number_aliens_x(ai_settings, alien_width):
	"""计算每行可容纳多少个外星人"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
	"""创建一个外星人并将其放在当前行"""
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def get_numbers_rows(ai_settings,ship_height,alien_height):
	'''计算屏幕可容纳多少外星人'''
	available_space_y=(ai_settings.screen_height -
	                   (3*alien_height)-ship_height)
	number_rows = int(available_space_y/(2*alien_height))
	return number_rows

def create_fleet(ai_settings,screen,ship,aliens):
	'''创建外星人群'''
	#创建一个外星人，并计算一行可容纳多少个外星人
	#外星人间距为外星人宽度

	alien =Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows=get_numbers_rows(ai_settings,ship.rect.height,
	                             alien.rect.height)
	# 创建外星人群
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings, screen, aliens, alien_number,
			             row_number)

	#这里是为了随机显示
	# for row_number in range(number_rows):
	# 	random_number=randint(1,number_aliens_x)
	# 	create_alien(ai_settings, screen, aliens, random_number,
	# 	            row_number)

def check_fleet_edges(ai_settings, aliens):
	"""有外星人到达边缘时采取相应的措施"""
	for alien in aliens.sprites():
		if  alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""将整群外星人下移，并改变它们的方向"""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction*=-1

def ship_hit(ai_settings, screen, stats,sb, ship, aliens, bullets):
	"""响应被外星人撞到的飞船"""
	if stats.ships_left >0:
		#将ships_left减1
		stats.ships_left -= 1

		#更新记分牌
		sb.prep_ships()

		# 清空外星人列表和子弹列表
		aliens.empty()
		bullets.empty()

		#创建一群新的外星人，并将飞船放到屏幕底端中央
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

		# 暂停
		sleep(0.5)
	else:
		stats.game_active =False
		pygame.mouse.set_visible(True)



def check_aliens_bottom(ai_settings, screen, stats,sb, ship, aliens, bullets):
	"""检查是否有外星人到达了屏幕底端"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			#像飞船被撞到一样进行处理
			ship_hit(ai_settings,stats,screen,sb,ship,aliens,bullets)
			break



def update_aliens(ai_settings, screen, stats,sb, ship, aliens, bullets):
	'''更新外星人群中所有外星人的位置'''
	check_fleet_edges(ai_settings,aliens)
	aliens.update()

	#检测外星人和飞船之间的碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		#print('Ship hit!!!')
		ship_hit(ai_settings, screen, stats,sb, ship, aliens, bullets)

	#检查是否有外星人到达屏幕底端
	check_aliens_bottom(ai_settings, screen, stats,sb, ship, aliens, bullets)

def check_high_score(stats,sb):
	'''检查是否诞生了新的最高分'''
	#stats.read_high_score()
	if stats.score > stats.high_score:
		stats.file_high_score=stats.score            #在这块添加就不会发生回0的情况，原因是没有检测>的条件，
		stats.write_high_score()                     #只有这里添加永远不会归零，或者改成stats.file_high_score=stats.score
		stats.high_score=stats.score                  #移到 stats.high_score=stats.score这个下面
		sb.prep_high_score()                           #永远让file_high_score=high_score













