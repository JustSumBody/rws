import pygame
import numpy as np

#Time the player is stunned for after being hit in ticks
PLAYERSTUN = 5

#Class to handle the player character in the game world
class PlayerSprite(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		
		self.image = pygame.Surface([32,32])
		self.image.fill(BLACK)
		
		self.rect = pygame.Rect(300,100,32,32)
		
		#movement vector with x,y components
		self.moveV = np.array([0,0])
		
		self.jumping = False
		self.attacking = False
		self.onGround = False
		#last time player was hit according to game clock
		self.lastAttacked = 0 
		
		self.direction = DIR_RIGHT
		self.prevDirection = DIR_RIGHT
		self.health = 100
		
	#stunned if the last time of attack is less than the current time minus PLAYERSTUN
	def incapacitated(self):
		return lastAttacked < mainClock - PLAYERSTUN
		
	def handleJump(self):
		if self.jumping and not self.onGround:
			self.moveV