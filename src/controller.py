import os, pygame, sys
from pygame import *
# from pygame.constants import K_LEFT, K_RETURN, K_RIGHT, KEYDOWN, KEYUP
from src import Character, Button, Enemy
from src.Constants import *
from src.Character import Hero
from src.Tiles import Tile
import requests



class Controller:
    def __init__(self):
        """
		    creates instance variables and loads in important images
		    args: self
		    return: none
	    """
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.title_img = pygame.image.load(os.path.join('assets', 'Vagrant Title.png'))
        self.start_button_img = pygame.image.load(os.path.join('assets', 'Vagrant Start.png')) 
        self.exit_button_img = pygame.image.load(os.path.join('assets', 'Vagrant Exit.png'))
        self.enemy = Enemy.Enemy(300,300,3)
        self.Vagabond = Character.Hero(48,500)
        self.miss_count = 0
        self.hit_count = 0
        
    def mainloop(self):
        """
        	code for the menu and handles game and exit loops
		    args: self
		    return: none
        """
        self.title_img = self.title_img.convert_alpha()
        self.title = Button.MakeButton(235,25,self.title_img,2.5)  
        self.start_button_img = self.start_button_img.convert_alpha()
        self.start_button = Button.MakeButton(465, 420,self.start_button_img,1.5)
        self.exit_button_img = self.exit_button_img.convert_alpha()
        self.exit_button = Button.MakeButton(525,570,self.exit_button_img,1.5)
        while True:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.exitloop()
            self.screen.fill((49,50,51))
            self.title.render(self.screen)
            self.start_button.render(self.screen)
            self.exit_button.render(self.screen)
            mouse_pos = pygame.mouse.get_pos()
            if self.start_button.clicked(mouse_pos):
                print("start button")
                self.gameloop()
            elif self.exit_button.clicked(mouse_pos):
                print("exit button")
                self.exitloop()
            pygame.display.flip()       
            self.clock.tick(60)     
            
    def gameloop(self): 
        """
		    handles rendering the screen after being called in mainloop, gameloop
		    args: self
		    return: none
	    """       
        while True:
            self.level(level_map,self.screen) 
            self.screen.fill((0,0,0))
            self.render_level()
            self.Vagabond.update(self.screen)
            self.enemy.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitloop()
                #print(self.miss_count)
                #print(self.hit_count)
            
            result = self.Vagabond.collision(self.enemy)
            
            if result == True:
                self.hit_count += 1
                try:
                    result = requests.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")
                except:
                    print("try again later")
                    setdefaultvalues()
                if result.status_code == 200:
                    response = result.json()
                    print(response)
                else:
                    print("no internet")
            elif result == False:
                self.miss_count += 1
            
	    #enemy movement
            self.enemy.move()

            #keyboard inputs
            key = pygame.key.get_pressed()
            if key[pygame.K_a]:
                self.Vagabond.movement("Left")
            if key[pygame.K_d]:
                self.Vagabond.movement("Right")
            if key[pygame.K_SPACE]:
                self.Vagabond.movement("Up")
            if key[pygame.K_SPACE] == False:
                self.Vagabond.movement("None")
            else:
                self.Vagabond.movement("None")
                
                
            pygame.display.update()
    
    def level(self, level_data, surface):
        """
		    handles background GUI elements
		    args: level_data (str) - layout for tiles, surface - screen obj
		    return: none
	    """
        self.display_surface = surface
        self.create_level(level_data)
        self.world_shift = 0
    
    def create_level(self, layout):
        """
		    creates a renderable layout for tiles
		    args: layout (str) - layout of the level within Constants
		    return: none
	    """
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,column in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if column == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)

    def render_level(self):
        """
		    draws the tiles onto the surface
		    args: self
		    return: none
	    """
        self.tiles.draw(self.display_surface)                    

    def exitloop(self):
        """
		    exit loop, exits out of the program
		    args: self
		    return: none
	    """
        pygame.quit()
        sys.exit()
    












