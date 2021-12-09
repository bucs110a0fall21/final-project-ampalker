import pygame
from src.Character import Hero
from src.Tiles import Tile
from src.Constants import tile_size

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.create_level(level_data)
        
    
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
        self.tiles.draw(self.display_surface)
        self.hero.update()
        self.hero.draw(self.display_surface)
        
