# Soren Minnig
# 9/12/24
# This file creates a list of every odd number from 1 to 1,000,000. Then, it
# displays statistics for the list.

numbers = list(range(1, 1_000_000, 2))
mean = (sum(numbers))/(len(numbers))

print("The Min number is: " + str(min(numbers)))
print("The Max number is: " + str(max(numbers)))
print("The Sum is: " + str(sum(numbers)))
print("The Length is: " + str(len(numbers)))
print(f"The Mean is: {mean}")