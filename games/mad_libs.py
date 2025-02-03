from games.game_interface import GameInterface
from games.utility_functions import validated_input
import random

# Define the class with GameInterface as the base class
class MadLibs(GameInterface):
    def __init__(self):
        # Initialize word lists and templates
        self.nouns = ['dog', 'car', 'robot', 'ice cream']
        self.verbs = ['jump', 'swing', 'romp', 'pilot']
        self.adjectives = ['blue', 'strange', 'happy', 'fast']
        self.adverbs = ['quickly', 'mysteriously', 'joyfully', 'silently']
        self.templates = [
            "The {adjective} {noun} {adverb} {verb}s.",
            "When you {verb} the {noun}, it {adverb} becomes {adjective}.",
            "The {noun} has {verb}ed."
        ]

    def run(self):
        play_again = "y"
        while(play_again is "y"):
            # Get user inputs if necessary or use random words
            user_defined = self.get_user_inputs()
            # Generate a Mad Lib
            mad_lib = self.create_mad_lib(random.choice(self.templates), user_defined)
            print()
            print(mad_lib)
            print("Enter 'y' to create another, or 'q' to quit.")
            play_again = validated_input(["y", "q"])

    def get_name(self):
        # Return the name of the game
        return "Mad Libs"
    
    def get_help(self):
        # Provide help information about how to play the game
        return "Fill in the blanks to complete a fun, randomized story! You'll be asked to provide various types of words."

    def select_random_from_list(self, word_list):
        # Helper function to select a random word from a list
        return random.choice(word_list)

    def create_mad_lib(self, template, user_inputs={}):
        # Fill in the template using words from the lists or user inputs
        sentence = template.format(
            noun=self.select_random_from_list(self.nouns) if 'noun' not in user_inputs else user_inputs['noun'],
            verb=self.select_random_from_list(self.verbs) if 'verb' not in user_inputs else user_inputs['verb'],
            adjective=self.select_random_from_list(self.adjectives) if 'adjective' not in user_inputs else user_inputs['adjective'],
            adverb=self.select_random_from_list(self.adverbs) if 'adverb' not in user_inputs else user_inputs['adverb'],
        )
        return sentence

    def get_user_inputs(self):
        # Optionally get inputs from the user
        user_inputs = {}
        print("You can customize your Mad Lib or hit ENTER to use random words.")
        user_inputs['noun'] = input("Enter a noun (or hit ENTER to skip): ").strip() or None
        user_inputs['verb'] = input("Enter a verb (or hit ENTER to skip): ").strip() or None
        user_inputs['adjective'] = input("Enter an adjective (or hit ENTER to skip): ").strip() or None
        user_inputs['adverb'] = input("Enter an adverb (or hit ENTER to skip): ").strip() or None
        # Remove None entries to use defaults
        return {k: v for k, v in user_inputs.items() if v is not None}

# Example of creating and running the game
if __name__ == "__main__":
    mad_libs_game = MadLibs()
    mad_libs_game.run()
