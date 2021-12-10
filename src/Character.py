import pygame, random, os
from pygame import key
from src import controller
from src.Constants import screen_height
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
		self.image = pygame.transform.scale(self.image,(48,48))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.y_vel = 0
		self.jump = False

	def movement(self,direction):	
		"""
			movement of the character
			args: self, direction
			return: none
		"""
		#horizontal movement
		if direction == "Left":
			self.rect.x -= 1
		if direction == "Right":
			self.rect.x += 1
		#vertical movemnt
		if direction == "Up" and self.jump == False:
			self.y_vel = -1
			self.jump = True
		#gravity
		if direction == "None":
			self.jump = False
			self.y_vel += .5
			if self.y_vel > 2:
				self.y_vel = 2
		self.rect.y += self.y_vel
		
		
		#bottom test
		if self.rect.bottom > screen_height:
			self.rect.bottom = screen_height
			self.y_vel = 0
	def update(self,screen):
		"""
			makes the character show up on screen
			args: self
			return: none
		"""
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




