import pygame

class MakeButton:
    def __init__(self,x,y,image,scale):
        """
		sets up instance variables to create a button
		args: self, x (int) - topleft x cor, y (int) - topleft y cor, image - button image, scale (int) - scale to change image by
		return:
	"""
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.click = False
    
    def render(self,screen_obj):
        """ 
		makes the button images appear on screen
		args: screen_obj - pygame surface to display on
		return: none
	"""
        screen_obj.blit(self.image, (self.rect.x, self.rect.y))
    
    def clicked(self, mouse_pos):
        """
		event handler for the buttons
		args: mouse_pos (int) - mouse position
		return: event (bool)
	"""
        event = False
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
                self.click = True
                event = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.click = False
        return event




