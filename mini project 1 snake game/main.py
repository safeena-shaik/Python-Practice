import random
""""
-1 for water
0 for gun 
1 for snake
"""""
computer = random.choice([-1,0,1]) #computer chooses to play
yourstr = input("Enter the choice:") #The user chooses to play
youdict = {"s":1,"w":-1,"g":0}
reversedict = {1:"Snake",-1:"water",0:"gun"}
you = youdict[yourstr]
print(f"You choose {reversedict[you]} \nComputer chose{reversedict[computer]}")
 #conditions/Rules of the game
if(computer==you):
    print("It's a draw")
else:
    if(computer==1 and you==-1):
        print("Computer wins")
    elif(computer==1 and you==0):
        print("You wins")
    elif(computer==-1 and you==0):
        print("Computer wins")
    elif(computer==-1 and you==1):
        print("You wins")
    elif(computer==0 and you==1):
        print("You wins")
    elif(computer==0 and you==-1):
        print("Computer Wins")
    else:
        print("Something went wrong")
 
 