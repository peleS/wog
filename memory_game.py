import random
import time
from utils import screen_cleaner

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    user_input = input(f'Please enter the {difficulty} numbers you saw, separated by spaces: ')
    return list(map(int, user_input.split()))

def is_list_equal(sequence, user_list):
    return sequence == user_list

def play(difficulty):
    sequence = generate_sequence(difficulty)
    print(f'Remember this sequence: {sequence}')
    time.sleep(0.7)
    screen_cleaner()
    user_list = get_list_from_user(difficulty)
    if is_list_equal(sequence, user_list):
        print("You won!")
        return True
    else:
        print("You lost!")
        return False