from game_concepts.Board import *
import pygame


class Knights(pygame.sprite.Sprite):

    def __init__(self, color, name, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.name = 'Sir {}'.format(name)
        # is the self.image
        self.image = image
        self.alive = True
        # defines the rectangle of the image
        self.rect = self.image.get_rect()
        self.rect.center = (tile[position].get_coordinates()[0] + half_tile_size,
                            tile[position].get_coordinates()[1] + half_tile_size)
        self.position = position
        self.new_position = position
        self.moving = False

    def set_image(self, new_image):
        self.image = new_image

    def get_color(self):
        return self.color

    def get_position(self):
        return self.position

    def set_new_position(self, new_tile):
        self.new_position = new_tile

    def game_over(self):
        self.alive = False

    def get_status(self):
        return self.alive

    def move(self, side, x=True, y=True, xplus=True, yplus=True):
        # if self.direction(side) is true it will move the player to the values that have been given in
        if self.new_position == self.position + side:
            # now starts the movement
            self.moving = True
            self.set_image(clear_image)
            # if x is True than horizontal movement
            if x:
                if xplus:
                    self.rect.x += moving_speed
                else:
                    self.rect.x -= moving_speed
            # if y is True than vertical movement
            if y:
                if yplus:
                    self.rect.y += moving_speed
                else:
                    self.rect.y -= moving_speed

    def moving_logic(self):
        # see if current_position is different than the new_position
        if self.position != self.new_position:
            # if the moving center equals the new_position center it stops and exits the loop
            if self.rect.center == (tile[self.new_position].get_coordinates()[0] + half_tile_size,
                                    tile[self.new_position].get_coordinates()[1] + half_tile_size):
                self.position = self.new_position
                self.moving = False
            else:
                # see the direction it needs to move
                #   l_up   |      up      |    r_up
                #   left   |      X       |    right
                #   l_down |     down     |    r_down

                # self.move(left, x=True, y=False, xplus=False, yplus=False)
                # is the same as:
                # if self.direction(left):
                #    self.rect.x -= moving_speed
                #    self.moving = True

                self.move(left, x=True, y=False, xplus=False, yplus=False)
                self.move(up, x=False, y=True, xplus=False, yplus=False)
                self.move(right, x=True, y=False, xplus=True, yplus=False)
                self.move(down, x=False, y=True, xplus=False, yplus=True)
                self.move(l_up, x=True, y=True, xplus=False, yplus=False)
                self.move(r_up, x=True, y=True, xplus=True, yplus=False)
                self.move(l_down, x=True, y=True, xplus=False, yplus=True)
                self.move(r_down, x=True, y=True, xplus=True, yplus=True)

    def update(self):
        self.moving_logic()



class Mob(pygame.sprite.Sprite):

    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = boss_left
        self.color = red
        self.rect = self.image.get_rect()
        self.position = position
        self.new_position = position
        self.moving = False
        self.rect.center = (tile[position].get_coordinates()[0] + half_tile_size,
                            tile[position].get_coordinates()[1] + half_tile_size)

    def get_color(self):
        return self.color

    def set_image(self, new_image):
        self.image = new_image

    def get_position(self):
        return self.position

    def set_new_position(self, new_tile):
        self.new_position = new_tile

    def move(self, side, x=True, y=True, xplus=True, yplus=True):
        # if self.direction(side) is true it will move the player to the values that have been given in
        if self.new_position == self.position + side:
            # now starts the movement
            self.moving = True
            # if x is True than horizontal movement
            if x:
                if xplus:
                    self.rect.x += moving_speed
                else:
                    self.rect.x -= moving_speed
            # if y is True than vertical movement
            if y:
                if yplus:
                    self.rect.y += moving_speed
                else:
                    self.rect.y -= moving_speed

    def moving_logic(self):
        # see if current_position is different than the new_position
        if self.position != self.new_position:
            # if the moving center equals the new_position center it stops and exits the loop
            if self.rect.center == (tile[self.new_position].get_coordinates()[0] + half_tile_size,
                                    tile[self.new_position].get_coordinates()[1] + half_tile_size):
                self.position = self.new_position
                self.moving = False
            else:
                # see the direction it needs to move
                #   l_up   |      up      |    r_up
                #   left   |      X       |    right
                #   l_down |     down     |    r_down

                # self.move(left, x=True, y=False, xplus=False, yplus=False)
                # is the same as:
                # if self.direction(left):
                #    self.rect.x -= moving_speed
                #    self.moving = True

                self.move(left, x=True, y=False, xplus=False, yplus=False)
                self.move(up, x=False, y=True, xplus=False, yplus=False)
                self.move(right, x=True, y=False, xplus=True, yplus=False)
                self.move(down, x=False, y=True, xplus=False, yplus=True)
                self.move(l_up, x=True, y=True, xplus=False, yplus=False)
                self.move(r_up, x=True, y=True, xplus=True, yplus=False)
                self.move(l_down, x=True, y=True, xplus=False, yplus=True)
                self.move(r_down, x=True, y=True, xplus=True, yplus=True)

    def update(self):
        self.moving_logic()


class Animation(pygame.sprite.Sprite):
    def __init__(self, side, dct):
        pygame.sprite.Sprite.__init__(self)
        self.side = side
        self.image = dct[self.side][0]
        self.dct = dct
        self.rect = self.image.get_rect()
        self.rect.center = current_player_turn[0].rect.center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = animation_frame_rate

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.dct[self.side]):
                # infinite anim set this as self.frame = 0
                self.frame = 0
                self.rect.center = current_player_turn[0].rect.center
            else:
                # this updates the player center
                center = current_player_turn[0].rect.center
                self.image = self.dct[self.side][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# instead of making each var with side the fill_motion_lists makes a list for all animations with numbers
# example:
# animation_walking_r = Animation(current_player_turn[0].rect.center, 'right', ak_walking)
# animation_walking[0] = Animation(who.rect.center, 'lst_walking[0]', ak_walking)
# if later animations needed to be made for other characters it can be changed with the who

def instantiate_animations():
    def fill_motion_lists(motion_lst, dct):
        for side in range(8):
            motion_lst.append(Animation(motion_sides[side], dct))

    fill_motion_lists(animation_staying, ak_staying)
    fill_motion_lists(animation_walking, ak_walking)
    fill_motion_lists(animation_dying, ak_dying)
    fill_motion_lists(animation_attacking, ak_attacking)


"""
    |   Instantiation of Knight objects   |

        - Knights have a color
        - Knights have a name
        - Knights have an image
        - Knights have a start position

"""
p1 = Knights(blue, name1, default_knight, tile_start_players[0])
p2 = Knights(black, name2, default_knight, tile_start_players[1])
p3 = Knights(red, name3, default_knight, tile_start_players[2])
p4 = Knights(yellow, name4, default_knight, tile_start_players[3])

mob1 = Mob(tile_start_mob[0])

if __name__ == "__main__":

    print(p1.rect)
    print(len(ak_staying['right']))