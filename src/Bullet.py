import pygame

class Bullet(pygame.sprite.Sprite):
	"""
		creates a bullet object
		args: self, int
		return: none
	"""
	def __init__(self, speed):
		super().__init__()
		self.image = pygame.image.load("assets/[bullet file name].png").convert_alpha()
		self.speed = speed
	def update(self):
	"""
		updates the bullet
		args: self
		return: rectangle object
	"""
		self.image.get_rect() = self.image.get_rect() + self.speed
