from game_concepts.Settings import *

black_tile_w_lst = []
black_tile_h_lst = []


def create_black_tile_lists():
    if not black_tile_w_lst:
        for bt_w in range(0, 1680, 80):
            black_tile_w_lst.append(bt_w)
    if not black_tile_h_lst:
        for bt_h in range(0, 800, 80):
            black_tile_h_lst.append(bt_h)


class Cutscenes:

    def __init__(self, text, background):
        self.active = True
        self.text = text
        self.background = background
        self.fade = False
        self.bl_t_w_counter = 0
        self.bl_t_h_counter = 0

    def set_start(self):
        self.active = True

    def set_end(self):
        self.active = False

    def wait(self, timer=500):
        pygame.time.delay(timer)

    def fade_on(self):
        self.fade = True

    def fade_start(self, screen):
        black_tile_under = pygame.Surface((1600, black_tile_w_lst[self.bl_t_h_counter]))
        black_tile_top = pygame.Surface(
            (black_tile_w_lst[self.bl_t_w_counter] + tile_size, black_tile_h_lst[self.bl_t_h_counter] + tile_size))
        black_tile_under.fill(black)
        black_tile_top.fill(black)
        screen.blit(black_tile_under, (0, 0))
        screen.blit(black_tile_top, (0, 0))

        if len(black_tile_w_lst) - 1 > self.bl_t_w_counter:
            self.bl_t_w_counter += 1

        elif len(black_tile_w_lst) - 1 == self.bl_t_w_counter and len(black_tile_h_lst) - 1 > self.bl_t_h_counter:
            self.bl_t_w_counter = 0
            self.bl_t_h_counter += 1

        else:
            self.wait()
            self.fade = False
            self.bl_t_w_counter = 0
            self.bl_t_h_counter = 0
            self.set_end()


text1 = ['Evil sorcerer \'Marar\' is brewing a spell '
         'that will cause tremendous terror upon this planet. You must stop him within 300 days (steps) '
         'Beware of his soldiers that will try to stop you. Gather better gear to increase your strength '
         'and defeat \'Marar\'']
text2 = ['You have been ambushed, prepare for battle!']

start_cutscene1 = Cutscenes(text1, sorcerer8bit)
battle_cutscene1 = Cutscenes(text2, battle)



if __name__ == '__main__':
    pass














