import pygame

class Wall(pygame.sprite.Sprite):
	def __init__(self, lx, rx,ly, ry):
		"""
			creates a wall object
			args: 4 integers, self
			return: none
		"""
		super().__init__()
		self.image = pygame.image.load("assets/[wall image].png").convert_alpha()
		self.rect = self.image.get_rect()
		self.lx = lx
		self.rx = rx
		self.ly = ly
		self.ry = ry
	def hitByPlayer(self):
		"""
			returns true for if the player hits a wall
			args: self
			return: bool
		"""
		return True
