from dataclasses import dataclass
from random import randint


class Dice:

    def __init__(self):
        self.die_list = []

    def addDie(self, die):
        self.die_list.append(die)

    def rollAll(self):
        for die in self.die_list:
            die.roll()


@dataclass
class Die:
    value: int = 1

    def roll(self):
        self.value = randint(1, 6)

    @property
    def get_value(self):
        return self.value
