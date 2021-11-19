import pygame
import random

class Enemy(pygame.sprite.Sprite, starting_dir1, starting_dir2, ending_dir1, ending_dir2):
	def __init__(self, direction):
		"""
			creates an enemy object
			args: int, self
			return: none
		"""
		self.image = pygame.image.load("assets/[enemy image].png").convert_alpha()
		self.image.get_rect().x = random.randrange(starting_dir1,ending_dir1)
		self.image.get_rect().y = random.randrange(starting_dir2, ending_dir2)
		self.direction = direction
		self.kill = False
	def killed(self):
		"""
			returns self.kill if the enemy is killed, which will return False
			args: self
			return: bool
		"""
		return self.kill
