import pygame, random, os
from pygame import key
from src import controller
class Hero(pygame.sprite.Sprite):
	
	def __init__(self,x,y):
		"""
			creates a character object and sets instance variables
			args: self, int, str
			return: none
		"""
		pygame.sprite.Sprite.__init__(self)
		image = pygame.image.load(os.path.join('assets','Vagabond.png'))
		self.image= image.convert_alpha()
		self.image = pygame.transform.scale(self.image,(64,64))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

	

#	def movement(self, x, interval):
#		x = x
#		#y = y
#		interval = interval
#		keys = pygame.key.get_pressed()
#		if keys[pygame.K_LEFT]:
#			x -= interval
#		if keys[pygame.K_RIGHT]:
#			x += interval
		#if keys[pygame.K_UP]:
		#	y -= interval
		#if keys[pygame.K_DOWN]
		#	y += interval






		
	def movement(self,direction):	
		"""
		move
		args: self
		return: rectangle object
		"""
		if direction == "Left":
			self.rect.x -= 3
		elif direction == "Right":
			self.rect.x += 3

		
		

	
	def update(self,screen):
		screen.blit(self.image, self.rect)

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




