import pygame

class Character(pygame.sprite.Sprite):
	def __init__(self, direction, max_hit_points, char_speed):
		"""
			creates a character object
			args: 3 integers, self
			return: none
		"""
		super().__init__()
		self.max_hit_points = max_hit_points
		self.image = pygame.image.load("assets/[character file name].png").convert_alpha()
		self.char_speed = char_speed
		self.image.get_rect().x = 10
		self.image.get_rect().y = 10
		self.direction = direction
	def movement(self):
		"""
			shows the movement of the character
			args: self
			return: rectangle object
		"""
		if self.direction == "Up":
			self.image.get_rect().y = self.image.get_rect().y - self.char_speed
		elif self.direction == "Down":
			self.image.get_rect().y = self.image.get_rect().y + self.char_speed
		elif self.direction == "Left":
			self.image.get_rect().x = self.image.get_rect().x - self.char_speed
		elif self.direction == "Right":
			self.image.get_rect().x = self.image.get_rect().x + self.char_speed
	def shoot(self):
		"""
			returns true for if the character shoots
			args: self
			return: bool
		"""
		return True
