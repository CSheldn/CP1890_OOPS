from datetime import date

POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')


def title():
    print('='*64)
    print('\t\t\t\tBaseball Team Manager')
    print('CURRENT DATE:', date.today())
    print("GAME DATE:")


def menu():
    print("MENU OPTIONS")
    print("1 - Display Lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")


def display_pos():
    print('POSITIONS')
    print(', '.join(POSITIONS))


display_pos()

