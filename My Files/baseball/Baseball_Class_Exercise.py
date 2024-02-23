from datetime import datetime
from Baseball_encapsulation import Player

POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')


def separator():
    return '='*64


def disp_title():
    print('\t\t\t\tBaseball Team Manager')


def date():
    current_date = datetime.now().date()

    print('CURRENT DATE:\t', current_date)

    game_date = datetime.fromisoformat(input('GAME DATE:\t\t ')).date()
    days = game_date - current_date
    print('DAYS UNTIL GAME:', days.days)


def menu_opt():
    print('MENU OPTIONS')
    print('1 - Display Lineup')
    print('2 - Add player')
    print('3 - Remove player')
    print('4 - Move player')
    print('5 - Edit player position')
    print('6 - Edit player stats')
    print('7 - Exit program')


def positions():
    print('POSITIONS')
    print(', '.join(POSITIONS))


def add_player(players):
    fname = input('First name: ')
    lname = input('Last name: ')
    position = input('Position: ')
    bats = input('At Bats: ')
    hits = input('Hits: ')

    player = Player(fname, lname, position, bats, hits)
    players.append(player)
    print(f'Player {player.full_name} was added.\n')


def get_player_pos():
    while True:
        position = input('Position: ').upper()
        if position in POSITIONS:
            return position
        else:
            print('Invalid position. Please enter correctly.')
            print('Possible options:', POSITIONS)


def get_at_bats(at_bats):
    while True:
        try:
            at_bats = int(input(''))
        except ValueError:
            print('Invalid integer. Please enter correctly.')
            continue

    if at_bats < 0 or at_bats > 500:
        print('Invalid entry. Must be between 0 and 500')


def get_hits(at_bats):
    while True:
        try:
            hits = int(input('Hits: '))
        except ValueError:
            print('Invalid integer. Please try again.')
            continue

    if hits < 0 or hits > at_bats:
        print(f'Invalid entry. Must be between 0 and {at_bats}')
    else:
        return hits


def get_lineup(players):
    if players == None:
        print('No players in the lineup.')
    else:
        print(f"{'':3}{'Player':40}{'POS':6}{'AB':>6}{'H':>6}{'AVG':>8}")
        print('-'*80)
        for i, player in enumerate(players):
            print(f'{i:>3d}{player.full_name:40}{player.position:6}{player.atBats:6d}{player.hits:6d}{player.battingAvg:8}')
        print()


def main():
    separator()
    disp_title()
    menu_opt()
    positions()
    separator()

    players = []

    while True:
        try:
            choice = int(input('Menu Option: '))
        except ValueError:
            choice = -1

        if choice == 1:
            get_lineup(players)
        elif choice == 2:
            add_player(players)

if __name__ == '__main__':
    main()

