import playsound
import random

class MusicBox:
    def __init__(self):
        self.variants = "correctincorrectABIUX" # возможные звуки
        self.score = 1
        self.sequence = random.choice(self.variants)

import playsound
import random

class MusicBox:
    def __init__(self):
        self.variants = "ABNTO"  # возможные звуки
        self.score = 0
        self.sequence = random.choice(self.variants)

    def __next(self):
        self.sequence += random.choice(self.variants)

    def check(self, user):
        if user == self.sequence:
            self.score += 1
            playsound.playsound("sounds/correct.wav")
            self.__next()

        else:
            playsound.playsound("sounds/incorrect.wav")
            self.score -= 0.5

    def play(self):
        for i in self.sequence:
            playsound.playsound(f"sounds/{i}.mp3")





