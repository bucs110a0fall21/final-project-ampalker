import pygame
import random
class Hero(pygame.sprite.Sprite):
	
	def __init__(self, rect_x, rect_y, name, image, speed, max_hit_points):
		"""
			creates a character object and sets instance variables
			args: self, int, str
			return: none
		"""
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(image).convert_alpha()
		self.max_hit_points = max_hit_points
		self.name = name
		self.speed = speed
		self.rect = self.image.get_rect()
		self.rect.x = rect_x
		self.rect.y = rect_y
		self.spawn = [50,50]
		
	def movement(self):
		"""
			shows the movement of the character
			args: self
			return: rectangle object
		"""
		if self.direction == "Left":
			self.rect.x = self.rect.x - self.speed
		elif self.direction == "Right":
			self.rect.x = self.rect.y + self.speed
		elif self.direction == "Up":
			self.rect.y = self.rect.y - self.speed
		elif self.direction == "Down":
			self.rect.y = self.rect.y + self.speed
	def swing_sword(self):
		"""
			returns true for if the character successfully swings sword with 2/5 chance of missing
			args: self
			return: bool
		"""
		swing_chance = random.randrange(5)
		if swing_chance == 0:
			print("Hit!")
			return True
		if swing_chance == 1:
			print("Hit!")
			return True
		if swing_chance == 2:
			print("Hit!")
			return True
		if swing_chance == 3:
			print("Miss!")
			return False
		if swing_chance == 4:
			print("Miss!")
			return False




