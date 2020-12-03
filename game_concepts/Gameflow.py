from game_concepts.Factions import *
from game_concepts.Cutscene import *


"""
Game idea
Boss is in the castle but very strong you have 100 turns to destroy him
You need to gather gear first to be able to defeat him
On the field there are several chests that you have to go to
Along the way you will randomly encounter enemies (like pokemon also battle is the same as pokemon)
Some enemies are weak vs for example a shield etc
If you got your shield you will do critical damage against the foe
once you think you are ready go to the boss and try to defeat him
"""

cutscenes = []

cutscenes.append(start_cutscene1)
cutscenes.append(battle_cutscene1)


def change_player(player):
    current_player_turn[0] = player


# starting the game moving mob to right
def chapter1(entity, Game):
    # entity is the self run game, renamed it so its not a class keyword but can rename it back to self doesn't matter
    if entity.boss_setup_complete is False and mob1.position % tiles_amount_width != tiles_amount_width - 2:
        mob1.set_image(boss_right)
        Game.direction(entity, right, animation_walking[4], current_player_turn[0])

    elif entity.boss_setup_complete is False and mob1.position % tiles_amount_width == tiles_amount_width - 2:
        mob1.set_image(boss_left)
        entity.boss_setup_complete = True
        # problem lays here this is going to happen everytime
        start_cutscene1.fade_on()

    if start_cutscene1.active is False and entity.boss_setup_complete is True:
        change_player(p1)
        entity.chapter1_complete = True
        del cutscenes[0]
        print('chapter1 complete')






def soldier_battle():
    # spawns soldier after random amount of steps
    if turn_enemy_spawn and current_player_turn[0].step_count == turn_enemy_spawn[0]:
        battle_cutscene1.fade_on()
        if battle_cutscene1.active is False:
            del turn_enemy_spawn[0]
            return True



"""
Chapter 1 (Intro)
1. first a welcome screen for couple seconds - x
2. then the hud with text with background story - V
3. than maybe a fade out - x
4. boss animation goes to his castle - v
5. potentially hud again?
6. camera moves to player 1
7. highlight a help button? for first time?
8. turn start notification
"""


"""
Chapter 2 (Game starts)

"""

if __name__ == "__main__":
    pass