def print_games():
    print('1. Memory Game - a sequence of numbers will appear for 1 second and you have to remember what it was')
    print('2. Guess Game - guess a number and see if you chose like the computer.')
    print('3. Currency Roulette - try and guess the value of a random amount of USD in ILS')



def welcome():
    name = input('Please enter your name:')
    print(f'Hi {name} and welcome to the World of Games: The Epic Journey')

def start_play():
    selected = False
    print_games()
    while not selected:
        try:
            choice = int(input('Please choose a game to play (1-3): '))
            if choice == 1:
                selected = True
                print('Memory Game - a sequence of numbers will appear for 1 second and you have to remember what it was.')
            elif choice == 2:
                selected = True
                print('Guessing Game - guess a number and see if it matches the one selected by the computer.')
            elif choice == 3:
                selected = True
                print('Currency Roulette - try and guess the value of a random amount of USD in ILS.')
            else:
                print('Error: Selection is incorrect - please choose one of the available options (1-3).')
        except ValueError:
            print('Error: Invalid input. Please enter a number between 1 and 3.')

    difficulty_selected = False

    while not difficulty_selected:
        try:
            difficulty = int(input('Please select a difficulty setting (1-5): '))
            if 1 <= difficulty <= 5:
                difficulty_selected = True
                print(f'You selected difficulty level {difficulty}. Good luck!')
            else:
                print('Error: Difficulty setting must be between 1 and 5.')
        except ValueError:
            print(f'Error: Invalid input. you chose {difficulty} Please enter a number between 1 and 5.')