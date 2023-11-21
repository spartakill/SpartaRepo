import random


class NumberGuessingKata:
    def __init__(self, upper_limit):
        self.upper_limit = upper_limit
        self.number_to_guess = random.randint(0, upper_limit)
        self.lives = 3

    def get_user_guess(self):
        return int(input(f"Enter a number between 0 and {upper_limit_input}: "))


    def play_game(self):
        while self.lives > 0:
            guess = self.get_user_guess()

            if guess < self.number_to_guess:
                print("Too Low Guess Higher!")
                self.lives -= 1
            elif guess > self.number_to_guess:
                print("Too High Guess Lower")
                self.lives -= 1
            else:
                print("Congratulations, you defeated me and guessed right!")
                break

            if self.lives > 0:
                print(f"You still have {self.lives} {'lives' if self.lives > 1 else 'life'} left")
            else:
                print("Out of lives. The correct number was:", self.number_to_guess)


upper_limit_input = int(input("Enter the upper limit of the number range: "))
game = NumberGuessingKata(upper_limit_input)
game.play_game()