"""

1. You will ensure that you have left 3 comments at the top of your file
    # Your Name
    # Date
    # brief description of what this file does

2. For this program, you must ask the user for their name and print a hello 
    message using their name along with a brief statement on how to play
    this game. Then, using a while loop, continue to ask the user to guess
    a number until they either guess the number correctly or run out of tries. 
    Your loop should end as soon as either of these conditions are met

    *** The user is only allowed 5 attempts ***

3. Before your program ends, it should either print a message stating if the 
    user won when they have won along with the number of guesses it took for 
    them to win, or a message stating they have lost after 
    running out of attempts along with the number the user failed to guess

4. After completing above 3 steps, remove all comments in this file that are
    not your own and do not forget to rename this file to guessingGame.py

"""

# This is a library that is common amongst programming
# languages that allow the use of random number generation
import random

# Each time the program is ran, a random number is generated 
# between the values of 1-20 inclusive, meaning that 1 and 20
# are possible outcomes to the random number
num = random.randint(1, 20)

name = input ("\nWelcome!, What is your name? ")

print(f'''
Hello {name}, I am thinking of a number between 1 and 20.
Your task is to guess the number. 
      ''')

count = 5
guessCount = 0

while count > 0 :

    count = count - 1
    guess = int(input("Make a guess: "))
    guessCount = guessCount + 1


    if guess > num :
     print("Your guess is too high.\n")

    elif guess < num :
        print("Your guess is too low.\n")

    else :
        count = 0 # This ends the loop


if guess == num :
    print(f"\nHooray, you win! \nYou guessed the number in {guessCount} guesses.\n")

else :
    print(f"\nBummer, You lost! \nThe chosen number was {num}.\n")