import random

choice=["Rock","Paper","Scissor"]
computer=random.choice(choice)

print("Rock\n Paper\n Scissor")

user_choice=input("Choose the Rock,Paper Scissor")

print("User choice:",user_choice)
print("computer choice",computer)
attempt=5  
while attempt>0:
 if(user_choice==computer):
    print("Draw")
 elif(user_choice=="Rock" and computer=="Paper")or\
    (user_choice=="Scissor" and computer=="Paper")or\
    (user_choice=="Rock" and computer=="Scissor"):
    print("user wins")
 else:
    print("computer wins") 
      
    attempt-=1
    print("Attempt left:",attempt)
    
