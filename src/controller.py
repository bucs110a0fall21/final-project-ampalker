import pygame 
import sys
from src import character
#from src import enemy
from pygame.constants import K_LEFT, K_RIGHT, KEYDOWN, KEYUP


class Controller:
    clock = pygame.time.Clock()
    def __init__(self):
        pygame.init()
        self.window = (500,500)
        self.screen = pygame.display.set_mode(self.window)
        self.background = pygame.Surface(self.window)
        self.background.fill((250,250,250))
        self.vagabond = character.Hero(7,10,"fortemps",'assets/Vagabond.png',10,4)
       # self.enemy = enemy.Enemy()

    def mainLoop(self):
        while self.state:
            if self.state == "MENU":
                self.menuloop()
            elif self.state == "GAME":
                self.gameloop()
            elif self.state == "GAMEOVER":
                self.endloop()
    
    def menuloop():
        """
        menu code
        """

    def gameloop(self):
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


    def keyboard(self):
        self.move_left = False
        self.move_right = True
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.move_right == True
                if event.key == K_LEFT:
                    self.move_left == True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    self.move_right == False
                if event.key == K_LEFT:
                    self.move_left == False










