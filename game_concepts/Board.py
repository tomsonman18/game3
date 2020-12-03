from game_concepts.Settings import *
import math


class Camera:

    def __init__(self, width, height):
        # this is the offset
        self.camera = pygame.Rect(0, 0, width, height)
        # width and height is the camera size
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0

    def apply(self, entity):
        # this moves the sprites other than the target. the 0,0 in the self.camera in the init
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        # rect = pygame.Rect(x, y, tile_size, tile_size)
        return rect.move(self.camera.topleft)

    def update(self, target):
        # this follows the sprite 'target' but moves in opposite because the offset needs to be minus
        x = -target.rect.x + int(screen_width / 2)
        y = -target.rect.y + int(screen_height / 2)

        # the camera offset needs a min and a maximum:
        x = min(0, x)   # left
        y = min(0, y)   # top
        self.x = max(-(tiles_amount_width - visible_tiles_amount_width)*tile_size, x)   # right
        self.y = max(-(tiles_amount_height - visible_tiles_amount_height)*tile_size, y)   # bottom
        # the camera is set to have the x and y values and same width and height as before
        self.camera = pygame.Rect(self.x, self.y, self.width, self.height)

    # not used
    def x_y(self):
        return self.x, self.y


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((tile_size, tile_size))
        self.coor_x = x * tile_size
        self.coor_y = y * tile_size
        self.image = type
        self.rect = self.image.get_rect()
        self.rect.x = self.coor_x
        self.rect.y = self.coor_y
        self.tile_coordinates = self.coor_x, self.coor_y
        self.row = int(y)
        self.col = int(x)
        self.tile_id = self.row * tiles_amount_width + self.col

    def get_tile_coordinates(self):
        return self.tile_coordinates

    def get_tile_number(self):
        return self.tile_id


class Tiles:

    def __init__(self, tile_id):
        self.tile_id = tile_id
        self.tile_size = tile_size
        self.current_row = math.floor(self.tile_id / row)
        self.current_column = self.tile_id % row
        x = self.current_column * self.tile_size
        y = self.current_row * self.tile_size
        self.coordinates = (x, y)
        self.rect = pygame.Rect(x, y, tile_size, tile_size)

    def get_current_column_row(self):
        return self.current_column, self.current_row

    def get_coordinates(self):
        return self.coordinates

    def get_rect(self):
        return self.rect

"""
    |   Instantiation of tiles   |
        
        - amount_tiles indicates amount of tiles
        - tile.append(i) adds amount of tiles to the tile list
        - tile[i] creates tile object
        
"""
for i in range(amount_tiles):
    tile.append(i)
    tile[i] = Tiles(i)

if __name__ == '__main__':

    print(tile[10].get_current_column_row())
    print(tile[10].get_coordinates())



