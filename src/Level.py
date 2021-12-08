import pygame
from src.Tiles import Tile
from src.Constants import tile_size

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.create_level(level_data)
        self.world_shift = 0
    
    def create_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for col_index,column in enumerate(row):
                if column == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)

    def render(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
