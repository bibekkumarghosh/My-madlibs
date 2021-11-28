import random

#these parts are where the user makes the guess and the computer tells if the guess is correct or not...
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


#guess_color()


#this part is where the computer makes the guesses and the user answers whether the guesses made are correct or no.
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guessed = 0
    while feedback != 'c':
        if low != high:
            guessed = random.randint(low, high)
        else:
            guessed = low
        feedback = input(f'Is {guessed} too high (H), too low (L), or correct (C)??').lower()
        if feedback == 'h':
            high = guessed - 1
        elif feedback == 'l':
            low = guessed + 1

    print(f'Ysy! The computer guessed your number, {guessed}, correctly!')


computer_guess(1000)
