"""
Settings file:

forrest_image = Image(ground_folder, 'Forrest', image_size1=tile_size-1, image_size2=tile_size-1).load_image()
mountain_image = Image(ground_folder, 'Mountain', image_size1=tile_size-1, image_size2=tile_size-1).load_image()
grass_image = Image(ground_folder, 'Grass', image_size1=tile_size-1, image_size2=tile_size-1).load_image()
woods_image = Image(ground_folder, 'Woods', image_size1=tile_size-1, image_size2=tile_size-1).load_image()


terrain = [forrest_image, mountain_image, grass_image, woods_image]


"""

"""
Board file:

class Tiles:

    def __init__(self, tile_id, image):
        self.tile_id = tile_id
        self.image = image
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

    def get_terrain(self):
        return self.image
"""

"""
    |   Instantiation of tiles   |

        - amount_tiles indicates amount of tiles
        - tile.append(i) adds amount of tiles to the tile list
        - tile[i] creates tile object

"""
"""
for i in range(amount_tiles):
    tile.append(i)
    tile[i] = Tiles(i, terrain[random.randrange(len(terrain))])
"""
"""
main page:

    def draw_tile(self):
        for t in range(amount_tiles):
            # loads the image
            # I expect the frame drop to be in here
            tile_image = tile[t].get_terrain()
            tile_rect = tile[t].get_rect()
            # to create a rect would be (coor1, coor2, size, size)
            self.screen.blit(tile_image, self.camera.apply_rect(tile_rect))

    def draw(self):
        # game loop draw

        self.draw_tile()

"""