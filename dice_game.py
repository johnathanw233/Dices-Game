import random


points = 5


def value_check():
    guess = int(input('Guess a number: '))
    print('You guessed %d' % guess)

    first_dice = random.randint(1, 3)
    second_dice = random.randint(1, 3)

    value = first_dice * second_dice

    print('You rolled a %d and a %d, which has the product of %d' % (first_dice, second_dice, value))

    global points
    if guess == value:
        print('Good guess! You get a point!')
        points = points + 1
        print('You now have %d points! \n' % points)
        if points == 5:
            print('Congratulations! You win the game!')
        else:
            value_check()

    else:
        while points == 0:
            print('You have no more points to lose!')
            print('Would you like to roll again?')
            answer = input('Enter yes or no: \n')
            if answer == "no":
                print("Better luck next time!")
                break

            else:
                points = 0
                value_check()

        else:
            print('Bad guess! You lose a point!')
            points = points - 1
            print('You now have %d points \n' % points)
            value_check()


def main():
    value_check()


main()
