# coding:utf-8
import pygame
from sys import exit

bg_file_name = 'bg.jpg'
cursor_file_name = 'cursor.png'

# init hardware
pygame.init()

# set display mode -fixed
screen = pygame.display.set_mode((640,480),0,32)

# set caption 
pygame.display.set_caption('Hello,world')

# background_image and mousr_cursor_image
bg = pygame.image.load(bg_file_name).convert()
mouse_cursor_image = pygame.image.load(cursor_file_name).convert_alpha()

# infinite game loop
while True:
	# handle event -- main framework
	for event in pygame.event.get():
		# QUIT event 
		if pygame.QUIT == event.type:
			pygame.quit()
			exit()
		# mouse button down event 
		if pygame.MOUSEBUTTONDOWN == event.type:
			# change background_image
			bg = pygame.image.load('bg2.jpg').convert()
	# 
	screen.blit(bg,(0,0))
	x,y = pygame.mouse.get_pos()
	x -= mouse_cursor_image.get_width() / 2
	y -= mouse_cursor_image.get_height() / 2
	screen.blit(mouse_cursor_image,(x,y))
	pygame.display.update()
	