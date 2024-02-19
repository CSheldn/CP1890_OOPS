from dataclasses import dataclass, field
from random import randint


@dataclass
class Die:
    value: int = 0

    def roll(self):
        self.value = randint(1, 6)

    @property
    def get_value(self):
        return self.value


@dataclass
class Game:
    __turn: int = 1
    __die: Die = field(default_factory=Die)
    __isGameOver: bool = False
    __isTurnOver: bool = False
    __score: int = 0
    __turnScore: int = 0

    def play(self):
        while not self.__isGameOver:
            self.take_turn()

    def take_turn(self):
        self.__isTurnOver = False
        print("\nTURN", self.__turn)
        while not self.__isTurnOver:
            user_input = input("Roll or hold (r/h): ")
            if user_input == "r":
                self.roll()
            elif user_input == "h":
                self.hold()
            else:
                print("Invalid input")
        print("Score for turn: ", self.__turnScore)
        print("Total score: ", self.__score)
        self.__turnScore = 0

    def roll(self):
        self.__die.roll()
        value = self.__die.get_value
        print("Die: ", value)
        if value == 1:
            self.__turnScore = 0
            self.__turn += 1
            self.__isTurnOver = True
        else:
            self.__turnScore += value

    def hold(self):
        self.__score += self.__turnScore
        self.__isTurnOver = True
        self.__turn += 1
        if self.__score > 21:
            self.__isGameOver = True
            print("\nYou finished in", self.__turn, "turns!")


