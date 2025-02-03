import random
from games.game_interface import GameInterface
from games.utility_functions import validated_input

class RockPaperScissors(GameInterface):
    def __init__(self):
        self.moves = ["rock", "paper", "scissors"]

    def win_check(self, move_a, move_b):
        return (    move_a == "rock" and move_b == "scissors" or
                    move_a == "scissors" and move_b == "paper" or
                    move_a == "paper" and move_b == "rock")

    def run(self):
        play_again = "y"
        while(play_again == "y"):
            computer_move = self.moves[random.randint(0,2)]
            print("Enter: rock, paper, or scissors")
            player_move = validated_input(self.moves)
            if self.win_check(computer_move, player_move):
                print("Computer Wins!")
                print(f"{computer_move} beats {player_move}")
            elif player_move == computer_move:
                print(f"{computer_move} ties {player_move}")
                print("Rematch.")
                continue
            else:
                print("Player Wins!")
                print(f"{player_move} beats {computer_move}")
            print("Enter 'y' to play again or 'q' to quit.")
            play_again = validated_input(["y", "q"])
        

    def get_name(self):
        return "Rock Paper Scissors"
    
    def get_help(self):
        return super().get_help()
