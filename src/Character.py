import pygame
import random

from pygame import key
from src import Controller
from pygame.constants import K_LEFT, K_RETURN, K_RIGHT, KEYDOWN, KEYUP, K_l
class Hero(pygame.sprite.Sprite):
	
	def __init__(self,pos,name):
		"""
			creates a character object and sets instance variables
			args: self, int, str
			return: none
		"""
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((32,64))
		self.image.fill((70,40,60))
		self.rect = self.image.get_rect(topleft = pos)
		self.name = name
		self.direction = pygame.math.Vector2(0,0)

	

		
	def movement(self):
		"""
			shows the movement of the character
			args: self
			return: rectangle object
		"""
		# move_right = False
		# move_left = False
		# for event in pygame.event.get():
		# 	if event.type == KEYDOWN:
		# 		if event.key == K_RIGHT:
		# 			move_right == True
		# 		if event.key == K_LEFT:
		# 			move_left == True
		# 	if event.type == KEYUP:
		# 		if event.key == K_RIGHT:
		# 			move_right == False
		# 		if event.key == K_LEFT:
		# 			move_left == False
		# 	if move_right == True:
		# 		self.direction.x = 1
		# 	if move_left == False:
		# 		self.direction.y = -1
		keys = pygame.key.get_pressed()
		if keys[pygame.K_RIGHT]:
			self.direction.x = 1 
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
		else:
			self.direction.x = 0
	
	def update(self):
		self.movement()
		self.rect.x += self.direction.x 

	def swing_sword(self):
		"""
			returns true for if the character successfully swings sword with 2/5 chance of missing
			args: self
			return: bool
		"""
		swing_chance = random.randrange(5)
		if swing_chance == 0:
			print("Hit!")
			return True
		if swing_chance == 1:
			print("Hit!")
			return True
		if swing_chance == 2:
			print("Hit!")
			return True
		if swing_chance == 3:
			print("Miss!")
			return False
		if swing_chance == 4:
			print("Miss!")
			return False




