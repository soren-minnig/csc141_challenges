# Soren Minnig
# Date: 9/4/24
# This program prompts the user to input their name, age, and major. Then, it
# uses that input to create a personalized message.

print("To generate your introduction, I will need some information from you...")
name = input("What is your name? ")
age = input("How old are you? ")
major = input("What are you studying? ")

print(f"Hi, my name is {name.title()} and I am {age} years old. I am currently "
      f"studying {major.title()} at Albright.")