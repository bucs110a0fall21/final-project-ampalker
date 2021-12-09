import pygame
import random
from pygame import key
from src import controller
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

	

	def movement(self, x, interval):
		x = x
		#y = y
		interval = interval
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			x -= interval
		if keys[pygame.K_RIGHT]:
			x += interval
		#if keys[pygame.K_UP]:
		#	y -= interval
		#if keys[pygame.K_DOWN]
		#	y += interval






		
#	def movement(self,direction):	
#		"""
#		shows the movement of the character
#		args: self
#		return: rectangle object
#		"""
#		if direction == "Left":
#			self.rect.x = self.rect.x - 2
#		elif direction == "Right":
#			self.rect.x = self.rect.y + 2
		# elif direction == "Up":
		# 	self.rect.y = self.rect.y - self.speed
		# elif direction == "Down":
		# 	self.rect.y = self.rect.y + self.speed
		

	
	# def update(self):
	# 	self.movement()
	# 	self.rect.x += self.direction.x 

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




