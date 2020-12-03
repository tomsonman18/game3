import os
import pygame
import random

"""colors"""
black = (10, 6, 8)
blue = (16, 52, 109)
red = (119, 0, 3)
yellow = (244, 195, 0)
white = (255, 255, 255)
grey = (186, 187, 188)

"""Main Settings"""
FPS = 60
screen_width = 1600
screen_height = 800

pygame.mixer.init()
pygame.font.init()
pygame.init()

"""dirs"""
game_folder = os.path.dirname(__file__)

img_folder = os.path.join(game_folder, 'images')
terrain_folder = os.path.join(img_folder, 'Terrain')
wall_folder = os.path.join(img_folder, 'Wall')
map_folder = os.path.join(img_folder, 'map')
boss_folder = os.path.join(img_folder, 'Boss')
knight_folder = os.path.join(img_folder, 'Knight')
backgrounds = os.path.join(img_folder, 'Backgrounds')
ground_folder = os.path.join(terrain_folder, 'ground')
trees_folder = os.path.join(terrain_folder, 'trees')
House_folder = os.path.join(terrain_folder, 'House')
Castle_folder = os.path.join(terrain_folder, 'Castle')
Well_folder = os.path.join(terrain_folder, 'Well')
Cart_folder = os.path.join(terrain_folder, 'Cart')
trees_05_folder = os.path.join(trees_folder, '_tree_05')
trees_03_folder = os.path.join(trees_folder, '_tree_03')
templar_folder = os.path.join(knight_folder, 'templar')
animated_knight_folder = os.path.join(knight_folder, 'animated_knight')
staying_motion_folder = os.path.join(animated_knight_folder, 'Staying')
attacking_motion_folder = os.path.join(animated_knight_folder, 'Attacking')
dying_motion_folder = os.path.join(animated_knight_folder, 'Dying')
walking_motion_folder = os.path.join(animated_knight_folder, 'Walking')

"""board"""
tile = []
obstacle = []

# tiles amount width must be able to divide by tile_size and screen width and screen height
# tile size is 80 x 80
tile_size = 80
half_tile_size = int(tile_size/2)
visible_tiles_amount_width = int(screen_width / tile_size)
visible_tiles_amount_height = int(screen_height / tile_size)
tiles_amount_width = 40
tiles_amount_height = 30
amount_tiles = tiles_amount_width * tiles_amount_height

grid_color = white

# 1 row is a complete width
row = tiles_amount_width
# 1 column is just 1 tile
column = 1

left = - column
up = - row
right = + column
down = + row
l_up = - row - column
r_up = - row + column
l_down = + row - column
r_down = + row + column

"""characters"""

"""Starting position"""
def tile_coor(x, y):
    y1 = row * y
    return y1 + x

# with tile_coor you can just fill in x and y tile
tile_start_players = [tile_coor(1,12), tile_coor(1,2), tile_coor(1,3), tile_coor(1,4)]
tile_start_mob = [tile_coor(30, 10)]

name1 = 'Mordred'
name2 = 'Dagos'
name3 = 'Tairyn'
name4 = 'Germaine'

moving_speed = 2
animation_frame_rate = 15

current_player_turn = []


# to stop the walking motion:
animation_walking_ongoing = [False]

"""images"""

class Image:

    def __init__(self, folder, image, file_type='jpg', image_size1=tile_size, image_size2=tile_size):
        self.folder = folder
        self.image = image
        self.file_type = file_type
        self.image_size1 = image_size1
        self.image_size2 = image_size2

    def load_image(self):
        loaded_image = pygame.image.load(os.path.join(self.folder, '{}.{}'.format(self.image, self.file_type)))
        loaded_image = pygame.transform.scale(loaded_image, (int(self.image_size1), int(self.image_size2)))
        return loaded_image


# folder, image_name, file_type, image_size_x, image_size_y
blue_knight = Image(templar_folder, 'templar_blue', 'png').load_image()
black_knight = Image(templar_folder, 'templar_black', 'png').load_image()
red_knight = Image(templar_folder, 'templar_red', 'png').load_image()
yellow_knight = Image(templar_folder, 'templar_yellow', 'png').load_image()
default_knight = Image(animated_knight_folder, 'default_knight', 'png').load_image()
default_l_knight = Image(animated_knight_folder, 'default_l_knight', 'png').load_image()
clear_image = Image(animated_knight_folder, 'clear', 'png').load_image()
boss_left = Image(boss_folder, 'boss2_8bit', 'png').load_image()
boss_right = Image(boss_folder, 'boss1_8bit', 'png').load_image()
sorcerer8bit = Image(boss_folder, 'sorcererfull', 'png', image_size1=1600, image_size2=900).load_image()
vert_wall_image = Image(wall_folder, 'vert', 'jpg').load_image()
hor_wall_image = Image(wall_folder, 'hor', 'jpg').load_image()
wall_image = Image(wall_folder, 'Wall_new', 'png').load_image()
Wall1 = Image(wall_folder, 'Wall1', 'png').load_image()
Wall2 = Image(wall_folder, 'Wall2', 'png').load_image()
Wall3 = Image(wall_folder, 'Wall3', 'png').load_image()
Wall4 = Image(wall_folder, 'Wall4', 'png').load_image()
Cart = Image(Cart_folder, 'cart_70000', 'png').load_image()
House = Image(House_folder, 'rem_0002', 'png').load_image()
Castle = Image(Castle_folder, 'Castle1', 'png').load_image()
Tree5 = Image(trees_05_folder, '_tree_05_{}0000'.format(random.randrange(0, 8)), 'png').load_image()
Tree3 = Image(trees_03_folder, '_tree_03_{}0000'.format(random.randrange(0, 8)), 'png').load_image()
Well = Image(Well_folder, 'Well_40000', 'png').load_image()
Hud = Image(backgrounds, 'HUD', 'png', image_size1=screen_width, image_size2=(screen_height/4)).load_image()
battle = Image(backgrounds, 'battle', 'jpg', image_size1=screen_width, image_size2=screen_height).load_image()


# does this make it worse? that the sizes are a little off

bg_map = Image(map_folder, 'Map_grid', 'png', image_size1=3281, image_size2=2481).load_image()
bg_map_rect = pygame.Rect(0, 0, 3281, 2481)

wall_picture_vert = wall_image
wall_picture_hor = wall_image

"""motions"""
#                  0      1      2       3       4         5        6        7
motion_sides = ['l_up', 'up', 'r_up', 'left', 'right', 'l_down', 'down', 'r_down']
animation_staying = []
animation_walking = []
animation_dying = []
animation_attacking = []

ak_staying = {}
ak_walking = {}
ak_dying = {}
ak_attacking = {}


def create_motion_images(motion_folder, motion, letter, side, dct):
    dct[side] = []
    for i in range(0,30,2):
        if i < 10:
            i = str(0) + str(i)
        filename = 'Orc_{}_{}00{}.png'.format(motion, letter, str(i))
        side_motion_folder = os.path.join(motion_folder, side)
        # i can make an object of the image here
        img = pygame.image.load(os.path.join(side_motion_folder, filename))
        img_resized = pygame.transform.scale(img, (tile_size, tile_size))
        dct[side].append(img_resized)


def create_all_sides(folder, motion, dct):
    create_motion_images(folder, motion, 'E', 'right', dct)
    create_motion_images(folder, motion, 'W', 'left', dct)
    create_motion_images(folder, motion, 'N', 'up', dct)
    create_motion_images(folder, motion, 'S', 'down', dct)
    create_motion_images(folder, motion, 'NE', 'r_up', dct)
    create_motion_images(folder, motion, 'NW', 'l_up', dct)
    create_motion_images(folder, motion, 'SE', 'r_down', dct)
    create_motion_images(folder, motion, 'SW', 'l_down', dct)


create_all_sides(staying_motion_folder, 'Staying', ak_staying)
create_all_sides(attacking_motion_folder, 'Attacking', ak_attacking)
create_all_sides(dying_motion_folder, 'Dying', ak_dying)
create_all_sides(walking_motion_folder, 'Walking', ak_walking)

turn_enemy_spawn = []

for turn in range(20, 300, 15):
    r = turn + random.randrange(5,10)
    turn_enemy_spawn.append(r)

for _ in range(0,10):
    delete = turn_enemy_spawn[random.randrange(1,len(turn_enemy_spawn))]
    turn_enemy_spawn.remove(delete)

print(turn_enemy_spawn)

if __name__ == '__main__':

    print(len(turn_enemy_spawn))
    print(turn_enemy_spawn)
