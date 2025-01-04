import random
import requests

def get_money_interval(difficulty):
    amount = random.randint(1, 100)
    response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    exchange_rate = response.json()["rates"]["ILS"]
    correct_value = amount * exchange_rate
    allowed_difference = 10 - difficulty
    return amount, correct_value - allowed_difference, correct_value + allowed_difference

def get_guess_from_user(amount):
    return float(input(f'Guess the value of {amount} USD in ILS: '))

def compare_results(lower_bound, upper_bound, user_guess):
    return lower_bound <= user_guess <= upper_bound

def play(difficulty):
    amount, lower_bound, upper_bound = get_money_interval(difficulty)
    user_guess = get_guess_from_user(amount)
    if compare_results(lower_bound, upper_bound, user_guess):
        print("You won!")
        return True
    else:
        print(f"You lost! The acceptable range was between {lower_bound:.2f} and {upper_bound:.2f}.")
        return False