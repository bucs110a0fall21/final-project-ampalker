import pygame
import random

class Enemy(pygame.sprite.Sprite):
	def __init__(self, image, x, x_movement, end_coord):
		"""
			this inits sprite functions and sets instance variables
			args: self, str, int
			return: none
		"""
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image).convert_alpha()
		self.enemy_tag = id(self)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.x_movement = x_movement
		self.end_coord = end_coord
		self.sprite_counter = 0
		self.speed = 5
#	def update(self):
#		"""
#			this dictates the movement of the enemy (up or down) left by chance, with 1/3 chance no movement occuring
#			args: self
#			return: int
#		"""
#		movement_chance = random.randrange(6)
#		if movement_chance == 0:
#			self.rect.x -= 1
#			self.rect.y = self.rect.y
#		elif movement_chance == 1:
#			self.rect.x += 1
#			self.rect.y = self.rect.y
#		elif movement_chance == 2:
#			self.rect.x = self.rect.x
#			self.rect.y -= 1
#		elif movement_chance == 3:
#			self.rect.x = self.rect.x
#			self.rect.y += 1
#		elif movement_chance == 4:
#			self.rect.x = self.rect.x
#			self.rect.y = self.rect.y
#		elif movement_chance == 5:
#			self.rect.x = self.rect.x
#			self.rect.y = self.rect.y



	def movement(self):
		if self.speed > 0:
			if self.x + self.speed < self.end_coord:
				self.x += self.speed
			else:
				self.speed *= -1
				self.sprite_counter = 0
		else:
			if self.x - self.speed > self.end_coord:
				self.x += self.speed
			else:
				self.speed *= -1
				self.sprite_counter = 0
		



	def kill(self):
		"""
			this returns false for when the enemy has been killed
			args: self
			return: bool
		"""
		return False














