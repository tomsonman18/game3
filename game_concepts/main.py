from game_concepts.Factions import *
import pygame

# current player needs to be set by the turns
current_player_turn.append(mob1)
players = [p1, p2, p3, p4]


class Game:

    def __init__(self):
        # initialize game window, etc
        pygame.init()
        # mixer is to play sounds
        pygame.mixer.init()
        pygame.font.init()
        pygame.display.set_caption("T&N Board Game")
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.camera = Camera(screen_width, screen_height)
        # all sprites need to be added to the group and then they are automatically rendered in draw section
        self.all_sprites = pygame.sprite.Group()
        # new group for walls
        self.obstacles = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        # creates list
        self.map_data = []
        self.map_obstacles = []
        # loads the map file
        self.load_map()
        # for setup cutscene
        self.text_cutscene = True
        # for text on hud
        self.counter = 1
        self.text_starter = [0]
        self.game_active = False
        self.spacebar = False
        self.cutoff = 140
        self.last_space = []
        self.text = []
        self.playing = True

    # order of run cycle
    def run(self):
        # game loop

        while self.playing:
            # self.clock.tick(FPS)
            self.clock.tick()
            self.events()
            self.update()
            self.setup()
            self.draw()

    def new(self):
        # start a new game
        instantiate_animations()
        # groups all sprites together
        self.all_sprites.add(p1)
        self.all_sprites.add(p2)
        self.all_sprites.add(p3)
        self.all_sprites.add(p4)
        self.all_sprites.add(mob1)

        # this creates a camera
        self.camera = Camera((tiles_amount_width * tile_size), (tiles_amount_height * tile_size))

        # run the game
        self.run()

    def show_start_screen(self):
        # game start screen
        pass

    def load_map(self):

        # opens file and reads it
        with open(os.path.join(game_folder, 'mapfile.txt'), 'rt') as mp:
            for line in mp:
                # adds each line to the map_data list
                self.map_data.append(line)

        # creates objects and sets it to the obstacle group
        for y, y_tiles in enumerate(self.map_data):
            for x, x_tiles in enumerate(y_tiles):
                if x_tiles == '1':
                    # self.all_sprites.add(Obstacle(y, x, vert_wall_image))
                    self.obstacles.add(Obstacle(x, y, wall_picture_vert))
                elif x_tiles == '2':
                    # self.all_sprites.add(Obstacle(y, x, hor_wall_image))
                    self.obstacles.add(Obstacle(x, y, wall_picture_hor))
                    # you could also add to all_sprites if wanted: self.all_sprites.add(Obstacle(y,x))
                elif x_tiles == '3':
                    self.obstacles.add(Obstacle(x, y, Tree3))
                elif x_tiles == '5':
                    self.obstacles.add(Obstacle(x, y, Tree5))
                elif x_tiles == '6':
                    self.obstacles.add(Obstacle(x, y, House))
                elif x_tiles == '7':
                    self.obstacles.add(Obstacle(x, y, Well))
                elif x_tiles == '8':
                    self.obstacles.add(Obstacle(x, y, Cart))
                elif x_tiles == '9':
                    self.obstacles.add(Obstacle(x, y, Castle))

        # saves all the obstacle tiles
        for o in self.obstacles:
            self.map_obstacles.append(o.get_tile_number())

    # events
    def events(self):
        # game loop events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                # quits the game
                self.playing = False
                # also the g.running loop needs to quit
                self.running = False

            # check for button pressed
            if event.type == pygame.KEYDOWN and current_player_turn[0].moving is False:
                # which key is to which direction
                if event.key == pygame.K_KP8: Game.direction(self, up, animation_walking[1])
                if event.key == pygame.K_KP2: Game.direction(self, down, animation_walking[6])
                if event.key == pygame.K_KP4: Game.direction(self, left, animation_walking[3])
                if event.key == pygame.K_KP6: Game.direction(self, right, animation_walking[4])
                if event.key == pygame.K_KP7: Game.direction(self, l_up, animation_walking[0])
                if event.key == pygame.K_KP9: Game.direction(self, r_up, animation_walking[2])
                if event.key == pygame.K_KP1: Game.direction(self, l_down, animation_walking[5])
                if event.key == pygame.K_KP3: Game.direction(self, r_down, animation_walking[7])

                if event.key == pygame.K_SPACE and self.spacebar is True:
                    if self.counter == len(self.text[0]):
                        self.game_active = True
                        self.text_cutscene = False
                    elif self.counter % self.cutoff == 0:
                        self.text_starter[0] = self.cutoff
                        self.counter += 1
                        self.last_space = []
                        self.cutoff = 140


                    self.spacebar = False

    def stop_motion(self):
        # to stop the walking motion from being infinite
        if animation_walking_ongoing[0] is not False and current_player_turn[0].moving is False:
            self.all_sprites.remove(animation_walking_ongoing[0])
            animation_walking_ongoing[0] = False
            current_player_turn[0].set_image(default_knight)

    # update
    def update(self):
        # game loop update

        # all the sprites update at once
        self.all_sprites.update()
        self.camera.update(current_player_turn[0])

        """This stops the animation for the characters, change here if you want the mob to also show an animation"""
        if current_player_turn[0] in players:
            self.stop_motion()

    def direction(self, where, animation, who=current_player_turn[0]):
        player_position = who.get_position()
        new_player_position = player_position + where

        # can't walk into obstacles
        if new_player_position in self.map_obstacles:
            print('Can\'t go there')

        # can't walk to top map limit
        elif new_player_position < 0:
            print('Can\'t go there')

        # can't walk to left map limit
        elif player_position % tiles_amount_width == 0 \
                and new_player_position % tiles_amount_width == tiles_amount_width - 1:
            print('Can\'t go there')

        # can't walk to right map limit
        elif player_position % tiles_amount_width == tiles_amount_width - 1 \
                and new_player_position % tiles_amount_width == 0:
            print('Can\'t go there')

        # can't walk to bottom map limit
        elif player_position >= (amount_tiles - tiles_amount_width) \
                and new_player_position >= amount_tiles:
            print('Can\'t go there')

        else:
            # go to the new position
            who.set_new_position(new_player_position)

            # show walking animation if current player is a player
            """This shows the animation for the characters, change here if you want the mob to also show an animation"""
            if current_player_turn[0] in players:
                self.all_sprites.add(animation)
                animation_walking_ongoing[0] = animation

    def setup(self):

        # starting the game moving mob to right
        if self.text_cutscene is False and mob1.position % tiles_amount_width != tiles_amount_width - 2:
            mob1.set_image(boss_right)
            Game.direction(self, right, animation_walking[4])
        elif self.text_cutscene is False and mob1.position % tiles_amount_width == tiles_amount_width - 2:
            mob1.set_image(boss_left)
            self.text_cutscene = True

    # draw
    def draw(self):

        # self.screen.fill(background)
        self.screen.blit(bg_map, self.camera.apply_rect(bg_map_rect))
        # game loop draw
        if self.game_active is True:

            self.draw_opa_tile()

            self.draw_map()

            # show FPS:
            self.draw_text('SNES', 50, 'FPS {}'.format(self.clock.get_fps()), 100, 0, white)

            # all sprites will be drawn
            for sprite in self.all_sprites:
                # for each sprite in the sprites it displays the image and it is captured in the camera
                # apply(sprite) does rect.move(self.camera.topleft) in the opposite of where the camera moves
                self.screen.blit(sprite.image, self.camera.apply(sprite))

        # to start the first screen
        elif self.game_active is False:


            self.text = ['Now, this is a story all about how. My life got flipped-turned upside down. And I\'d like to '
                    'take a minute Just sit right there I\'ll tell you how I became the the prince of a town called '
                    'Bel-Air. In West Philadelphia born and raised On the playground is where I spent most of my days '
                    'Chillin out maxin relaxin all cool And all shootin some b-ball outside of the school When a '
                    'couple of guys who were up to no good Started making trouble in my neighborhood I got in one '
                    'little fight and my mom got scared She said You\'re movin with your auntie and uncle in Bel Air']

            # if the list is not empty then search for last space and makes that the cutoff point
            if not self.last_space:

                # to find the last space in the sentence and add the loc it to a list
                self.last_space.append(self.text[0].rfind(' ', self.text_starter[0],
                                                          self.text_starter[0] + self.cutoff))

                if len(self.text[0]) > (self.text_starter[0] + self.cutoff):
                    self.cutoff = self.last_space[0]
                else:
                    self.cutoff = len(self.text[0])

            # to draw the message with hud
            self.draw_text('Zilla Slab', 30, self.text[0][self.text_starter[0]:self.counter], 100,
                           int(screen_height - (screen_height / 7)),
                           yellow, hudwindow=True)

            # to start the counter for the text
            if self.counter < len(self.text[0]) and self.counter % self.cutoff != 0:
                self.counter += 1

            # to cut it off at cutoff point and show spacebar text
            if self.counter <= len(self.text[0]) and self.counter % self.cutoff == 0:
                self.draw_text('Zilla Slab', 30, 'Press space to continue', 660,
                               int(screen_height - (screen_height / 16)),
                               yellow)
                self.spacebar = True

        # After drawing everything flip display
        pygame.display.flip()

    def draw_text(self, font, size, text, x, y, color, hudwindow=False):
        my_font = pygame.font.SysFont(font, size)
        text_surface = my_font.render(text, False, color)
        if hudwindow is True:
            self.screen.blit(Hud, (0, int(screen_height - (screen_height / 4))))
            self.screen.blit(text_surface, (x, y))
        else:
            self.screen.blit(text_surface, (x, y))

    def draw_grid(self):

        # I believe this is faster

        for square in range(amount_tiles):
            rect = tile[square].get_rect()
            rect = self.camera.apply_rect(rect)
            pygame.draw.rect(self.screen, grid_color, rect, 1)

        """
        # I believe this is slower
        for y in range(tiles_amount_height):
            for x in range(tiles_amount_width):
                rect = pygame.Rect(x*80, y*80, tile_size, tile_size)
                rect = self.camera.apply_rect(rect)
                pygame.draw.rect(self.screen, grid_color, rect, 1)
        """

        """
        for x in range(0, screen_width, tile_size):
            # pygame.draw.line(where, color, (each tile_size * x, endpoint line), (endpoint line, endpoint line))
            x_rect = (x, 0), (x, screen_height)
            x_rect = self.camera.apply_rect(x_rect)
            pygame.draw.line(self.screen, white, x_rect)
        for y in range(0, screen_height, tile_size):
            y_rect = (0, y), (screen_width, y)
            y_rect = self.camera.apply_rect(y_rect)
            pygame.draw.line(self.screen, white, y_rect)
        """

    def draw_opa_tile(self):
        # below is to show the opacity tile:
        if current_player_turn[0] is not mob1:
            opacity_tile = pygame.Surface((tile_size, tile_size))  # the size of your rect
            opacity_tile.set_alpha(75)  # alpha level, the lower the more transparent
            opacity_tile.fill((current_player_turn[0].get_color()))  # this fills the surface with the color
            opa_rect = tile[
                current_player_turn[0].new_position].get_rect()  # gets the rect in order to offset the camera
            if current_player_turn[0].moving is False:  # only if the player is standing still show the opa_tile
                self.screen.blit(opacity_tile, self.camera.apply_rect(opa_rect))

    def draw_map(self):
        # displays all the obstacles. Can also go under the all_sprites if needed
        for sprite in self.obstacles:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

    def show_game_over_screen(self):
        # game go screen
        pass


g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_game_over_screen()
pygame.quit()
