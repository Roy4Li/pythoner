# coding:utf-8
"""
click or press arrow key to see next image
change log:
date         author     log
2014-4-9     Roy        added next and last
"""

import pygame
from pygame.locals import *
from sys import exit
import os
import random
import re


image_path = 'res/nice/'

pygame.init()

SCREEN_SIZE = (1024,768)

screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

file_list = os.listdir(image_path)

jpg_list = []

for i in file_list:
    jpg = re.findall(r'.*\.jpg',i)
    if jpg != []:
        jpg_list.append(jpg[0])
image_num = len(jpg_list)

def update_display(n,valid,fullscreen):
    if not valid:
        return
    image_file = image_path + jpg_list[n]
    bg = pygame.image.load(image_file).convert()
    width = bg.get_width()
    height = bg.get_height()
    x = (SCREEN_SIZE[0] - width) / 2
    y = (SCREEN_SIZE[1] - height) / 2
    if fullscreen:
        screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | FULLSCREEN, 32)
    else:
        screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
    screen.fill((0,0,0))
    pygame.display.flip()
    screen.blit(bg,(x,y))
    pygame.display.flip()

n = 0
fullscreen = False
while True:
    valid = 0
    event = pygame.event.wait()
    if (event.type == QUIT or 
        (event.type == KEYDOWN and 
            (event.unicode == 'q' or event.unicode == 'Q'))):
        print 'Quit'
        exit()
    if (event.type == MOUSEBUTTONDOWN or 
        (event.type == KEYDOWN and 
            (event.key == K_DOWN or event.key == K_RIGHT))):
        n += 1
        if n == image_num:
            n = 0
        valid = 1
    if (event.type == KEYDOWN and 
        (event.key == K_UP or event.key == K_LEFT)):
        n -= 1
        if n < 0:
            n = image_num - 1
        valid = 1
    if event.type == KEYDOWN and event.key == K_f:
        fullscreen = not fullscreen
        valid = 1
    if event.type == VIDEORESIZE:
        SCREEN_SIZE = event.size
        screen = pygame.display.set_mode(SCREEN_SIZE, RESIZABLE, 32)
        valid = 1
        
    update_display(n,valid,fullscreen)
        
