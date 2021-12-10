import pygame, random, os
class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y, speed):
		"""
			sets up instance variables and loads in enemy image
			args: x (int) - x rect position, y (int) - y rect position, speed (int) - enemy speed
			return: none
		"""
		pygame.sprite.Sprite.__init__(self)
		image = pygame.image.load(os.path.join('assets','ghost.png'))
		image = pygame.transform.scale(image,(48,48))
		self.image = image.convert_alpha()
		self.rect = self.image.get_rect()
		self.speed = speed
		self.rect.x = x
		self.rect.y = y


	def move(self):
		"""
			handles movement of the enemy
			args: self
			return: none
		"""
		movement_chance = random.randrange(4)
		if movement_chance == 0:
			self.rect.x -= 1
			self.rect.y = self.rect.y
		elif movement_chance == 1:
			self.rect.x += 1
			self.rect.y = self.rect.y
		elif movement_chance == 2:
			self.rect.x = self.rect.x
			self.rect.y -= 1
		elif movement_chance == 3:
			self.rect.x = self.rect.x
			self.rect.y += 1
			
	def update(self,screen):
		"""
			makes the character show up on screen
			args: self
			return: none
		"""
		screen.blit(self.image, self.rect)






