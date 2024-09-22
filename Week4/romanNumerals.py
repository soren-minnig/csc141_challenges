# Soren Minnig
# 9/20/24
# This program prompts the user to enter a number from 1-100 and converts it to
# a roman numeral.

# Defining roman numerals
o = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
t = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']

# Loop
while True:
    number = int(input("\nPlease enter a number between 1-100 to exchange for "
                       "a roman numeral: "))
    
    # Checking if the input is within range
    if (number < 1 or number > 100):
        print("Value outside of range; enter a valid number.")
    else:
        if number == 100:
            print("C")
        else:
            # Calculating the roman numeral
            tens = t[(number % 100) // 10]
            ones = o[number % 10]

            numeral = tens + ones
            print(numeral)
        quit()