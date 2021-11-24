import pygame

class Door(pygame.sprite.Sprite):
	def __init__(self, image, x, y):
		"""
			this inits sprite functions and sets instance variables for the rectangle of the door
			args: self, int, str
			return: none
		"""
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
