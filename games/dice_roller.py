from games.utility_functions import validated_input
from games.game_interface import GameInterface
import random

class DiceRoller(GameInterface):
    def __init__(self):
        self.validNumberOfSides = [str(i) for i in range(2, 21)]  # Valid dice sides as strings for input validation

    def run(self):
        self.dice = []
        print("How many sides? Enter [2 - 20]")
        number_of_sides = validated_input(self.validNumberOfSides)
        self.dice.append(int(number_of_sides))
        while True:
            print("Enter [2 - 20] to add another die, or 'r' to roll.")
            number_of_sides = validated_input(self.validNumberOfSides + ["r"])
            if number_of_sides == "r":
                break
            self.dice.append(int(number_of_sides))

        while True:
            total = 0
            for d in self.dice:
                result = random.randint(1, d)
                total += result
                print(f"Rolled a {d}-sided die: {result}")
            print(f"Total of all rolls: {total}")
            print("Enter 'r' to reroll, or 'q' to quit.")
            choice = validated_input(["r", "q"])
            if(choice == "q"):
                return

    def get_name(self):
        return "Dice Roller"
    
    def get_help(self):
        return "Enter the number of sides for each die, add as many dice as you like, then roll them."
