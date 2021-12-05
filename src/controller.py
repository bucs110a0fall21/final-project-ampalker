import os 
import pygame
import sys
from src import character
#from src import enemy
from pygame.constants import K_LEFT, K_RETURN, K_RIGHT, KEYDOWN, KEYUP


class Controller:
    clock = pygame.time.Clock()
    def __init__(self):
        pygame.init()
        self.width = 900
        self.height = 500
        self.screen = pygame.display.set_mode(self.width,self.height)
        self.vagabond = character.Hero(7,10,"fortemps",'assets/Vagabond.png',10,4)
        self.state = "MENU"
       # self.enemy = enemy.Enemy()

    def mainloop(self):
        while self.state:
            if self.state == "MENU":
                self.menuloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "GAMEOVER":
                self.endloop()
            elif self.state == "EXIT":
                self.exitloop()
    
    def button(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    
    def render(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def menuloop(self):
        """
        menu code
        """
        self.title_img = pygame.image.load(os.path.join('assets', 'Vagrant Title.png'))
        self.start_button_img = pygame.image.load(os.path.join('assets', 'Vagrant Start.png'))
        self.exit_button_img = pygame.image.load(os.path.join('assets', 'Vagrant Exit.png'))
        run = True
        while run:
            #self.screen.fill(49,50,51)
            self.start_button = self.button(250,300,self.start_button_img)
            self.render()

            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    run = False
        self.exitloop()


    def gameloop(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.exitloop()
        pygame.display.update()

    def exitloop(self):
        pygame.quit()
        sys.exit()


    def keyboard(self):
        self.move_left = False
        self.move_right = False
        self.start_key = False
        self.back_key = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.move_right == True
                if event.key == K_LEFT:
                    self.move_left == True
                if event.key == K_RETURN:
                    self.start_key = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.move_right == False
                if event.key == K_LEFT:
                    self.move_left == False
                if event.key == K_RETURN:
                    self.start_key = False
                










