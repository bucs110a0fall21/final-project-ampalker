import pygame

class Character(pygame.sprite.Sprite):
	def __init__(self, direction, max_hit_points, char_speed):
		super().__init__()
		self.max_hit_points = max_hit_points
		self.image = pygame.image.load("assets/[character file name].png").convert_alpha()
		self.char_speed = char_speed
		self.image.get_rect().x = 10
		self.image.get_rect().y = 10
		self.direction = direction
	def movement(self):
		if self.direction == "Up":
			self.image.get_rect().y = self.image.get_rect().y - self.char_speed
		elif self.direction == "Down":
			self.image.get_rect().y = self.image.get_rect().y + self.char_speed
		elif self.direction == "Left":
			self.image.get_rect().x = self.image.get_rect().x - self.char_speed
		elif self.direction == "Right":
			self.image.get_rect().x = self.image.get_rect().x + self.char_speed
	def shoot:
		return True
