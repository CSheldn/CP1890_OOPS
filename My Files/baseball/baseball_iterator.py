from dataclasses import dataclass


@dataclass
class Player:
    firstName: str = ''
    lastName: str = ''
    position: str = ''
    atBats: int = 0
    hits: int = 0

    @property
    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    def BattingAvg(self):
        try:
            avg = self.hits / self.atBats
            return avg
        except ZeroDivisionError:
            return 0.0


class Lineup:
    __player_list: list

    def count(self):
        return len(self.__player_list)

    def addPlayer(self, player: Player):
        self.__player_list.append(player)

    def removePlayer(self, number):
        self.__player_list.pop(number-1)

    def __iter__(self):
        for player in self.__player_list:
            yield player


def main():
    lineup = Lineup()
    lineup.addPlayer(Player('Sheldon', 'Jacque', 'S', 450, 449))
    lineup.addPlayer(Player('Arun', 'Rameshbabu', 'S', 100, 100))

    for player in Lineup:
        print(f"Player: {player.fullName}")
        print(f"AVG: {player.BattingAvg()}")
        print()

    print('Done')


if __name__ == '__main__':
    main()
