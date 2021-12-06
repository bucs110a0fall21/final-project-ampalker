import os, pygame, sys

from pygame import mouse
from src import Character, Button #Enemy
from pygame.constants import K_LEFT, K_RETURN, K_RIGHT, KEYDOWN, KEYUP


class Controller:
    clock = pygame.time.Clock()
    clock.tick(60)
    def __init__(self):
        pygame.init()
        white = (255, 255, 255)
        self.size = ((800,500))
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill(white)
        self.vagabond = Character.Hero(7,10,"fortemps",'assets/Vagabond.png',10,4)
        self.title_img = pygame.image.load(os.path.join('assets', 'Vagrant Title.png'))
        self.start_button_img = pygame.image.load(os.path.join('assets', 'Vagrant Start.png')) 
        self.exit_button_img = pygame.image.load(os.path.join('assets', 'Vagrant Exit.png'))
       # self.enemy = enemy.Enemy()
        
    def mainloop(self):
        """
        menu code
        """
        
        self.title_img = self.title_img.convert_alpha()
        self.title = Button.MakeButton(195,25,self.title_img,1.5)  
        self.start_button_img = self.start_button_img.convert_alpha()
        self.start_button = Button.MakeButton(320, 350,self.start_button_img,1)
        self.exit_button_img = self.exit_button_img.convert_alpha()
        self.exit_button = Button.MakeButton(360,450,self.exit_button_img,1)
        run = True
        while run:
            self.screen.fill((49,50,51))
            self.title.render(self.screen)
            self.start_button.render(self.screen)
            self.exit_button.render(self.screen)
            mouse_pos = pygame.mouse.get_pos()
            if self.start_button.start_button(mouse_pos):
                print("start button")
                self.gameloop()
            if self.exit_button.exit_button(mouse_pos):
                print("exit button")
                self.exitloop()
            pygame.display.update()
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    run = False
        self.exitloop()


    def gameloop(self):
        self.screen.fill((250,250,250))
        for self.event in pygame.event.get():
            if self.event.type == pygame.QUIT:
                self.exitloop()
        pygame.display.update()

    def exitloop(self):
        pygame.quit()
        sys.exit()


    def keyboard(self):
        move_left = False
        move_right = False
        start_key = False
        back_key = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    move_right == True
                if event.key == K_LEFT:
                    move_left == True
                if event.key == K_RETURN:
                    start_key = True
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    move_right == False
                if event.key == K_LEFT:
                    move_left == False
                if event.key == K_RETURN:
                    start_key = False
                










