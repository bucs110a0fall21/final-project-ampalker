import pygame
import random

class Enemy(pygame.sprite.Sprite, starting_dir1, starting_dir2, ending_dir1, ending_dir2):
	def __init__(self, direction):
		self.image = pygame.image.load("assets/[enemy image].png").convert_alpha()
		self.image.get_rect().x = random.randrange(starting_dir1,ending_dir1)
		self.image.get_rect().y = random.randrange(starting_dir2, ending_dir2)
		self.direction = direction
		self.kill = False
	def killed(self):
		return self.kill
