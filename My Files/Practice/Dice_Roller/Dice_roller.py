from Dice_roller_classes import Die, Dice


def main():
    print("The Dice Roller program\n")

    while True:
        try:
            amount = int(input('Enter the number of dice to roll: '))
            break
        except ValueError:
            print('Enter a valid integer.\n')

    dice = Dice()
    for i in range(amount):
        die = Die()
        dice.addDie(die)

    while True:
        dice.rollAll()
        print('YOUR ROLL: ', end='')
        for die in dice.die_list:
            print(die.get_value, end=' ')
        print()

        user_input = input('\nRoll again? (y/n): ')
        if user_input.lower() != 'y':
            break

    print('Bye!')

main()
