import pygame, sys
from src import controller

class MakeButton:
    def __init__(self,x,y,image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.click = False
    
    def render(self,screen_obj):
        screen_obj.blit(self.image, (self.rect.x, self.rect.y))
    
    def start_button(self, mouse_pos):
        event = False
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                event = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False
        return event

    def exit_button(self, mouse_pos):
        event = False
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                event = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False
        return event




