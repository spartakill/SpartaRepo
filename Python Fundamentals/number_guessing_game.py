# number guessing game

import random

game_random_number = random.randint(1, 100)
game_active = True

while game_active:
    game_start_message = "guess a number between 1 - 100"
    user_guess = int(input())
    if user_guess == game_random_number:
        print("you guessed correctly")
        game_active = False
    elif user_guess < game_random_number:
        print("guess higher")
    else:
        print("guess lower")