#Rock Paper Scissor
from random import randint

#moves for player
moves= ["rock","paper","scissors"]

while True:
    computer = moves[randint(0,2)]
    player = input("rock, paper, scissors? (or end the game)").lower()
    if player == "end the game":
        print("The game has ended!")
        break
    elif player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!",computer,"beats",player)
        else:
            print("You Win!",player,"beats",computer)
    elif player == "paper":
        if computer == "Scissors":
            print("You Lose!", computer,"beats",player)
        else:
            print("You Win!",player,"beats",computer)
    elif player == "scissors":
        if computer == "rock":
            print("You Lose!", computer,"beats",player)
        else:
            print("You Win!",player,"beats",computer)
    else:
        print("Check your spelling...")
