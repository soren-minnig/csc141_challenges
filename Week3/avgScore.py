# Soren Minnig
# 9/12/24
# This program asks the user how many scores they would like to average, then
# prompts them to input those scores. Finally, it finds the average.

# Title
print("\n-----------------------")
print("Calculate average score")
print("-----------------------\n")

# Amount of scores
amount = int(input("How many scores would you like to average? "))
scores = []

# Score input
for i in range(int(amount)):
    score = float(input("Enter a score: "))
    scores.append(score)

# Averaging
average = sum(scores)/len(scores)
print(f"\nYour average score is {average} points.")