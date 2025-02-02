import random
from games.game_interface import GameInterface

class NumberGuesser(GameInterface):
    def __init__(self):
        self.target_number = random.randint(1, 100)

    def run(self):
        print("Welcome to Number Guesser!")
        print("Guess the number between 1 and 100.")
        
        attempts = 0
        while True:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
                if guess < self.target_number:
                    print("Too low!")
                elif guess > self.target_number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number {self.target_number} correctly in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def get_name(self):
        return "Number Guesser"

    def get_help(self):
        return "Try to guess the randomly generated number between 1 and 100. Enter guesses as integers."
