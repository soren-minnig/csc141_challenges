"""

1. You will ensure that you have left 3 comments at the top of your file
    # Your Name
    # Date
    # brief description of what this file does

2. For this program, you must prompt the user for a number between the 
    values of 1-100. If they give you a value outside of this range,
    your program should continue to ask for a value within range until
    the user has given the correct expected input. 

3. You will then print the correct Roman Numeral for the value that the
    user has given you. You should not be using a 100 branch conditional
    statement for each value. Attempt to find a smarter way to do this.

4. After completing above 3 steps, remove all comments in this file that are
    not your own and do not forget to rename this file to romanNumerals.py

"""


number = int(input("\nPlease enter a number 1-100 to exchange into a roman numeral: "))
while number > 100 or number <= 0:
    number = int(input("\nTry again, value outside of range. Enter a number 1-100 to exchange into a roman numeral: "))

tens = number // 10
ones = number % 10

numeralTens = ""
numeralOnes = ""


if number >= 101 :
    print("\nError, Try again\n")
    
elif tens == 1 :
    numeralTens = "X"

elif tens == 2 :
    numeralTens = "XX"

elif tens == 3 :
    numeralTens = "XXX"

elif tens == 4 :
    numeralTens = "XL"

elif tens == 5 :
    numeralTens = "L"

elif tens == 6 :
    numeralTens = "LX"

elif tens == 7 :
    numeralTens = "LXX"

elif tens == 8 :
    numeralTens = "LXXX"

elif tens == 9 :
    numeralTens = "XC"

elif tens >= 10 :
    numeralTens = "C\n"



if number <= 0:
    print("\nError, Try again\n")

elif ones == 1 :
    numeralOnes = "I\n"

elif ones == 2 :
    numeralOnes = "II\n"

elif ones == 3 :
    numeralOnes = "III\n"

elif ones == 4 :
    numeralOnes = "IV\n"

elif ones == 5 :
    numeralOnes = "V\n"

elif ones == 6 :
    numeralOnes = "VI\n"

elif ones == 7 :
    numeralOnes = "VII\n"

elif ones == 8 :
    numeralOnes = "VIII\n"

elif ones == 9 :
    numeralOnes = "IX\n"


print(numeralTens + numeralOnes)