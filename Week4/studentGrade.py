# Soren Minnig
# 9/19/24
# This program prompts the user to enter a grade. Then, it calculates the letter
# grade.

# Input
grade = float(input("Please enter a score: "))

# Conditional
if (grade >= 0 and grade < 60):
    print("\nYour grade is a 'F'!")
elif (grade >= 60 and grade < 70):
    print("\nYour grade is a 'D'!")
elif (grade >= 70 and grade < 80):
    print("\nYour grade is a 'C'!")
elif (grade >= 80 and grade < 90):
    print("\nYour grade is a 'B'!")
elif (grade >= 90 and grade <= 100):
    print("\nYour grade is a 'A'!")
else:
    print("Error!")