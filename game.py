#game.py

import random

#customize player name

import os
import dotenv
dotenv.load_dotenv()
PLAYER_NAME = os.getenv("PLAYER_NAME", default = "Player One")
print("-------------------")
print(F"Welcome '{PLAYER_NAME}' to my Rock-Paper-Scissors game...")
print("-------------------")

#asking user for input

user_choice =input("Please choose either 'rock', 'paper', or 'scissors': ")
options = ["rock", "paper", "scissors"]

#print(x)

print("You chose:",user_choice)

user_choice = user_choice.lower()

if user_choice not in options:
    print("OOPS, please choose a valid option and try again!")
    exit()

#simulating a computer input

computer_choice = random.choice(options)
print(f"The computer chose: {computer_choice}")
print("-------------------")
    
#determining the winner
# adapted from Estelle's solution shared in the opim143 slack channel

if computer_choice == "paper" and user_choice == "scissors":
    print("Yay! You won!")
elif computer_choice == "rock" and user_choice == "paper":
    print("Yay! You won!")
elif computer_choice == "scissors" and user_choice == "rock":
    print("Yay! You won!")
elif computer_choice == user_choice:
    print("It's a tie!")
else:
    print("Oh, the computer won. It's ok.")

#ending message

print("-------------------")
print("Thanks for playing. Please play again!")
