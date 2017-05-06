#TODO: everything

import pygame, sys
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 400
WINDOWHEIGHT = 400
WindowSurface = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
pygame.display.set_caption('Running With Scissors!')

BLACK = (0,0,0)
WHITE = (255,255,255)

player = pygame.Rect(300,100,50,50)
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6
#Main game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		#Keypress checks, TODO: NotLikeThis
		if event.type == KEYDOWN:
			if event.key == K_LEFT or event.key == K_a:
				moveRight = False
				moveLeft = True
			if event.key == K_RIGHT or event.key == K_d:
				moveRight = True
				moveLeft = False
			if event.key == K_DOWN or event.key == K_s:
				moveDown = True
				moveUp = False
			if event.key == K_UP or event.key == K_w:
				moveDown = False
				moveUp = True
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_LEFT or event.key == K_a:
				moveLeft = False
			if event.key == K_RIGHT or event.key == K_d:
				moveRight = False
			if event.key == K_DOWN or event.key == K_s:
				moveDown = False
			if event.key == K_UP or event.key == K_w:
				moveUp = False
				
	WindowSurface.fill(WHITE)
	
	#handle movement
	if moveDown and player.bottom < WINDOWHEIGHT:
		player.top += MOVESPEED
	if moveUp and player.top > 0:
		player.top -= MOVESPEED
	if moveLeft and player.left > 0:
		player.left -= MOVESPEED
	if moveRight and player.right < WINDOWWIDTH:
		player.right += MOVESPEED
		
	pygame.draw.rect(WindowSurface, BLACK, player)
	
	pygame.display.update()
	mainClock.tick(40)