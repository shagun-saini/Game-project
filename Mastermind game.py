# Mastermind game

import random

play1=random.randrange(100,500)
play2=int(input("Enter the guessing num"))
print("Player1 guessing number",play1) #print the guessing number
print("Player1 guessing number",play2) #print the guessing number

if(play1==play2): #Check the condition
    print("Great! You guess the corect number")
else:
    print("Incorrect guess the number")

try_again=True/False 
print("1.Yes")
print("2.No")

choice=input("Choose the yes/no")

if choice==1:
    True
    print("Yes")
elif choice==2:
    False
    print("No")
else:
    print("Invalid choice")    







