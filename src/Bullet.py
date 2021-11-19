import pygame

class Bullet(pygame.sprite.Sprite):
	def __init__(self, speed):
		super().__init__()
		self.image = pygame.image.load("assets/[bullet file name].png").convert_alpha()
		self.speed = speed
	def update(self):
		self.image.get_rect() = self.image.get_rect() + self.speed
