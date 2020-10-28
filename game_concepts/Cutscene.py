from game_concepts.Settings import *


class Cutscenes:

    def __init__(self, text, background, sequence_number, timer):
        self.sequence_number = sequence_number
        self.text = text
        self.background = background
        self.end = False
        self.timer = timer * 1000

    def set_end(self):
        self.end = True

    def wait(self):
        pygame.time.delay(self.timer)


text1 = ['Now, this is a story all about how. My life got flipped-turned upside down. And I\'d like to '
                    'take a minute Just sit right there I\'ll tell you how I became the the prince of a town called '
                    'Bel-Air. In West Philadelphia born and raised On the playground is where I spent most of my days '
                    'Chillin out maxin relaxin all cool And all shootin some b-ball outside of the school When a '
                    'couple of guys who were up to no good Started making trouble in my neighborhood I got in one '
                    'little fight and my mom got scared She said You\'re movin with your auntie and uncle in Bel Air']



cutscene1 = Cutscenes(text1, sorcerer8bit, 1, 5)

if __name__ == '__main__':
    print(cutscene1.text)















