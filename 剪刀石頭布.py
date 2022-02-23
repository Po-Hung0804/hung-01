# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 19:51:17 2022

@author: User
"""

from random import randint

choice=("stone" ,"paper","scissors")

computer= choice[randint(0,2)]


print("Welcome to the paper scissors stone\n")

player=input("Your choice: ")
print("computer choice: "+computer)

if computer==player:
    print("Draw")
elif computer == "stone" and player == "scissors":
    print("You lose")
elif computer == "stone" and player == "paper":
    print("You win")
elif computer == "paper" and player == "scissors":
    print("You win ")
elif computer == "paper" and player == "stone":
    print("You lose")
elif computer == "stone" and player == "scissors":
    print("You lose ")
elif computer == "stone" and player == "paper":
    print("You win")