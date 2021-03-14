# Rock Paper Scissors game against the computer where user inputs Rock, Paper or Scissors and either wins,loses,or ties.
from random import randint

# Create a list of options for the player to input.
t = ["Rock", "Paper", "Scissors"]

# Assign a random move to the computer.
computer = t[randint(0, 2)]

# Set player to false.
player = False

while not player:
    # Set player to true.
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
        # Adds an option for a tie.
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "crushes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "crushes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
        # Adds an option for if the player inputs an invalid move, and prompts them to re-enter their move.
    # Player was set to true, but it needs to be false so the loop continues.
    player = False
    computer = t[randint(0, 2)]
