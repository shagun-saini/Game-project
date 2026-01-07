# Mastermind game

import random

play1=random.randrange(100,500)
play2=int(input("Enter the guessing num"))
print("Player1 guessing number",play1) #print the guessing number
print("Player2 guessing number",play2) #print the guessing number

if(play1==play2): #Check the condition
    print("Great! You guess the corect number")
else:
    print("Incorrect guess the number")

num=0
while(play2!=play1): #this conditon is not equal to match the number or play1 and play 2
    print("Sorry, You guess the second time incorect number")
    num+=1 #store the count of incorrect number

    count=0  #count the times or guess the number

    play1=str(play1) #explicitly conversion of integer to string
    play2=str(play2) #explicitly conversion of integer to string
 
    correct=['x']*3


    for i in range(0,3):

     if(play2[i]==play1[i]):
      print("You guess the correct number")

      count+=1
     
      correct[i]=play2[i]

     else:
      continue

    print(f"You did get the {count} digits correct")

    play2= int(input("Enter your next choice of numbers: "))

    if(play2[i]==play1[i]):
        num+=1
        print("You are a mastermind")
        print("It took you only", num, "tries.")