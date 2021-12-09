import os, pygame, sys
from pygame import mouse
from pygame.constants import K_LEFT, K_RETURN, K_RIGHT, KEYDOWN, KEYUP
from src import Character, Button, Tiles, Enemy
from src.Constants import *
from src.Character import Hero
from src.Tiles import Tile




class Controller:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screen_width,screen_height))
        self.Vagabond = Character.Hero
        self.title_img = pygame.image.load(os.path.join('assets', 'Vagrant Title.png'))
        self.start_button_img = pygame.image.load(os.path.join('assets', 'Vagrant Start.png')) 
        self.exit_button_img = pygame.image.load(os.path.join('assets', 'Vagrant Exit.png'))
        #self.enemy = enemy.Enemy()
        
    def mainloop(self):
        """
        menu code
        """
        self.title_img = self.title_img.convert_alpha()
        self.title = Button.MakeButton(235,25,self.title_img,2.5)  
        self.start_button_img = self.start_button_img.convert_alpha()
        self.start_button = Button.MakeButton(465, 420,self.start_button_img,1.5)
        self.exit_button_img = self.exit_button_img.convert_alpha()
        self.exit_button = Button.MakeButton(525,570,self.exit_button_img,1.5)
        run = True
        while run:
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
                run = False
            elif self.exit_button.clicked(mouse_pos):
                print("exit button")
                self.exitloop()
            pygame.display.flip()       
            self.clock.tick(60)     
            
        


    def gameloop(self):        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exitloop()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.Vagabond.movement("Right")
                    if event.key == pygame.K_d:
                        self.Vagabond.movement("Left")
            self.level(level_map,self.screen) 
            self.screen.fill((0,0,0))
            self.render()
            pygame.display.flip()

    def level(self, level_data, surface):
        self.display_surface = surface
        self.create_level(level_data)
        self.world_shift = 0
    
    def create_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.hero = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout):
            for col_index,column in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if column == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if column == 'P':
                    hero_sprite = Hero((x,y),"fortemps")
                    self.hero.add(hero_sprite)

    def render(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.hero.update()
        self.hero.draw(self.display_surface)                    
         
            

    def exitloop(self):
        pygame.quit()
        sys.exit()
    
    def keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1 
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0











