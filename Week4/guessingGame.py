# Soren Minnig
# 9/19/24
# This program generates a random number from 1-20 and asks the user to guess
# the number using 5 attempts. If the guess is incorrect, it provides feedback
# on whether the guess was too low or too high.

import random

# Variables
num = random.randint(1, 20)
attempts = 0

# Introduction
name = input("\nWelcome! What is your name? ")
print(f"Hello, {name}! I'm thinking of a number between 1-20.")
print("Your task is to guess this number.")

# Number guessing
while attempts < 5:
    attempts = (attempts)+1
    guess = int(input("\nEnter a number: "))
    if guess == num:
        print(f"The number {num} is correct! Good job!")
        print(f"You guessed the number in {attempts} tries.")
        quit()
    elif guess < num:
        print(f"The number {guess} is too low, try again!")
    elif guess > num:
        print(f"The number {guess} is too high, try again!")
