from dataclasses import dataclass, field
from random import randint


@dataclass
class Die:
    value: int = 1

    def roll(self):
        self.value = randint(1, 6)

    @property
    def get_value(self):
        return self.value


@dataclass
class Game:
    __turn: int = 1
    __turnScore: int = 0
    __isTurnOver: bool = False
    __totalScore: int = 0
    __isGameOver: bool = False
    __die: Die = field(default_factory=Die)

    def play(self):
        while not self.__isGameOver:
            self.take_turn()

    def take_turn(self):
        print("TURN ", self.__turn)
        while True:
            user_input = input("Roll or hold? (r/h): ")
            if user_input.lower() == 'r':
                self.roll_die()
            else:
                self.hold_turn()

    def roll_die(self):
        self.__die.roll()
        print("Die: ", self.__die.get_value)
        if self.__die.get_value == 1:
            self.__isTurnOver = True
            self.__turnScore = 0
            self.__turn += 1
            print("This turn is over, you lost your points. \n")
        else:
            self.__turnScore += self.__die.get_value

    def hold_turn(self):
        self.__totalScore += self.__turnScore
        print("Score for turn: ", self.__turnScore)
        print("Total score: ", self.__totalScore)
        print()
        if self.__totalScore > 20:
            self.__isGameOver = True
            print("You finished in 2 turns!")
        else:
            self.__turn += 1

