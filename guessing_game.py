import random


def guess(x):
    random_number = random.randint(1, x)
    guessed = 0
    while guessed != random_number:
        guessed = int(input(f'Guess a number between 1 and {x}: '))
        if guessed < random_number:
            print('Sorry, guess again. Too low.')
        elif guessed > random_number:
            print('Sorry, guess again. Too high')
    print(f'Yay, congrats. You have guessed the number {random_number} correctly.')


# guess(10)


def guess_color():
    color_options = ['black', 'blue', 'red', 'yellow', 'green', 'purple', 'grey', 'white', 'pink', 'brown', 'orange']
    random_color = random.choice(color_options)
    guessed = ''
    while guessed != random_color:
        guessed = input('Guess a color from black, blue, red, yellow, green, purple, grey, white, pink, brown, orange: ')
        print('Try again...')
    print(f'You have guessed the color {guessed} correctly.')


guess_color()
