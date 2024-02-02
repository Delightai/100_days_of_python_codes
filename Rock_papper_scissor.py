rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


#Write your code below this line 👇

import random

option = [rock, paper, scissors]
option1 = ["rock","paper","scissors"]

User_choice = input("What are you chosen, ROCK, PAPER OR SCISSORS ?\n").lower()

computer_option_int = random.randint(0, len(option) -1)

computer_option_str = option[computer_option_int]



print("computer chose")
if computer_option_str == rock :
    print(rock)
elif computer_option_str == paper :
    print (paper)
else: 
    print (scissors)

print ("You chose")
if User_choice == "rock" :
    print (rock)
elif User_choice == "paper" :
    print (paper)
elif User_choice == "scissors" :
     print (scissors)
else: 
    print("You must have entered a wrong input")

if User_choice == "rock":
    if computer_option_str == rock :
        print ("You draw, Try again")
    elif computer_option_str == paper :
        print ("You win, You are amazing")
    else:
        print ("You win, you are amazing")
elif User_choice == "paper" :
    if computer_option_str == rock :
        print ("You lose !")
    elif computer_option_str == paper :
        print ("You draw, try again")
    else:
        print ("You lose !")
elif User_choice == "scissors" :
    if computer_option_str == rock :
        print("You lose !")
    elif computer_option_str == paper :
        print("You win, You are amazing")
    else: 
        print ("you draw, Try again")
        
