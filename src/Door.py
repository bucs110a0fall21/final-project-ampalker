import pygame

class Door(pygame.sprite.Sprite):
	def __init__(self, lx, ly, rx, ry):
		"""
			creates a door object
			args: 4 ints, self
			return: none
		"""
		super().__init__()
		self.image = pygame.image.load("assets/[door image].png").convert_alpha()
		self.rect = self.image.get_rect()
		self.lx = lx
		self.ly = ly
		self.rx = rx
		self.ry = ry
	def playerEntry(self):
		"""
			returns true for if the player object collides with the door
			args: self
			return: bool
		"""
		return True
