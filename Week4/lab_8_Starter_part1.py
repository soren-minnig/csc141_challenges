"""

1. You will ensure that you have left 3 comments at the top of your file
    # Your Name
    # Date
    # brief description of what this file does

2. For this program, you must ask the user for their name and print a hello 
    message using their name along with a brief statement on how to play
    this game. Then, using a while loop, continue to ask the user to guess
    a number until they either guess the number correctly or run out of tries. 
    Your loop should end as soon as either of these conditions are met.
    Additionally, let the user know if their guess is too low or too high.

    *** The user is only allowed 5 attempts ***

3. Before your program ends, it should either print a message stating if the 
    user won when they have won along with the number of guesses it took for 
    them to win, or a message stating they have lost after 
    running out of attempts along with the number the user failed to guess

4. After completing above 3 steps, remove all comments in this file that are
    not your own and do not forget to rename this file to guessingGame.py

"""

# This is a library that is common amongst programming
# languages in which it allows the use of random number generation
import random

# Each time the program is ran, a random number is generated 
# between the values of 1-20 inclusive, meaning that 1 and 20
# are possible outcomes to the random number
num = random.randint(1, 20)
