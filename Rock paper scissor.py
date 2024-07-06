# Rock paper scissors
import random

options = ['rock','paper','scissor']

dicts = {
    "computer":0,
    "player":0
}

while True:
    
    player = input("\n\nChoose rock,paper or scissor : ")
    computer = random.choice(options)
    
    if player not in options:
        print("\n\nInvalid option!\n\nEnter correct option")
        continue
    
    if player==computer:
        print("player :",player)
        print("computer :",computer)
        print("Tie!")
        

    elif player == "paper" and computer == "rock":
        print("player :",player)
        print("computer :",computer)
        print()
        print("player wins!")
        dicts["player"]+=1
        print("Current score of player: ",dicts["player"])
        print("Current score of computer: ",dicts["computer"])
        
    elif player == "paper" and computer == "scissor":
        print("player :",player)
        print("computer :",computer)
        print()
        print("computer wins!")
        dicts["computer"]+=1
        print("Current score of player: ",dicts["player"])
        print("Current score of computer: ",dicts["computer"])
        
    elif player == "rock" and computer == "paper":
        print("player :",player)
        print("computer :",computer)
        print()
        print("computer wins!")
        dicts["computer"]+=1
        print("Current score of player: ",dicts["player"])
        print("Current score of computer: ",dicts["computer"])
        
    elif player == "rock" and computer == "scissor":
        print("player :",player)
        print("computer :",computer)
        print()
        print("player wins!")
        dicts["player"]+=1
        print("Current score of player: ",dicts["player"])
        print("Current score of computer: ",dicts["computer"])
        
    elif player == "scissor" and computer == "rock":
        print("player :",player)
        print("computer :",computer)
        print()
        print("computer wins!")
        dicts["computer"]+=1
        print("Current score of player: ",dicts["player"])
        print("Current score of computer: ",dicts["computer"])
    
    elif player == "scissor" and computer == "paper":
        print("player :",player)
        print("computer :",computer)
        print()
        print("player wins!")
        dicts["player"]+=1
        print("Current score of player: ",dicts["player"])
        print("Current score of computer: ",dicts["computer"])
    
    if dicts["computer"]==10 or dicts["player"]==10:
        break
    
print("\nplayer points",dicts["player"])
print("\ncomputer points",dicts["computer"])

if dicts["computer"]>dicts["player"]:
    print("\ncomputer won 10 points ")
else:
    print("\nplayer won 10 points")