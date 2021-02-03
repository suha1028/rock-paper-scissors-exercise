#game.py

import random

print("Rock, Paper, Scissors, Shoot!")


print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for input

user_choice =input("Please choose either 'rock', 'paper', or 'scissors': ")
options = ["rock", "paper", "scissors"]
#print(x)

print("You chose:",user_choice)

user_choice.lower()

if user_choice not in options:
    print("OOPS, please choose a valid option and try again")
    exit()


#simulating a computer input

computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")





    
#determining the winner



print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")
print("Thanks for playing. Please play again!")
