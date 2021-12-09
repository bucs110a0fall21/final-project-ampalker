import pygame
import random

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, image, speed):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.speed = speed
		self.rect.x = x
		self.rect.y = y


	def move(self):
		movement_chance = random.randrange(4)
		if movement_chance == 0:
			self.rect.x -= 1
			self.rect.y = self.rect.y
		elif movement_chance == 1:
			self.rect.x += 1
			self.rect.y = self.rect.y
		elif movement_chance == 2:
			self.rect.x = self.rect.x
			self.rect.y -= 1
		elif movement_chance == 3:
			self.rect.x = self.rect.x
			self.rect.y += 1







