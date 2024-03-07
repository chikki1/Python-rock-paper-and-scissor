import random

print("lets play rock, paper, and scissor")


list1 = ["rock", "paper", "scissor"]

scorePlayer = 0
scoreComputer = 0

while(True):
    player = input("Pick rock, paper, or scissor or to terminate the game, type the letter 'n': ")
    if(player == "n"):
        break
    rand = random.randint(0,2)
    computer = list1[rand]
    print("Computer: {} /t You: {}".format(computer, player))
    if player == "rock" and computer == "scissor" or player == "scissor" and computer == "paper" or player == "rock" and computer == "scissor":
        print("you win")
        scorePlayer += 1
    elif player == "rock" and computer == "rock" or player == "scissor" and computer == "scissor" or player == "rock" and computer == "rock":
        print("Tie")
    else:
        print("You lose")
        scoreComputer += 1



print("Your score is {} and the computer score is {}".format(scorePlayer, scoreComputer))
if scorePlayer < scoreComputer:
    print("the computer wins")
elif(scoreComputer == scorePlayer):
    print("tie")
else:
    print("you wind")



