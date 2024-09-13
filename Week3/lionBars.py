# Soren Minnig
# 9/12/24
# This program prompts the user to enter in the weight of each Lion Bar (oz) and
# the anount produced that month. Then, it calculates and prints the total
# weight in lbs and oz.

# Input
weight = float(input("\nPlease enter the weight of each Lion Bar "
                     "(in ounces): "))
amount = int(input("How many Lion Bars were produced this month? "))

# Calculations
total_oz_weight = (weight)*(amount)
total_lbs_weight = int((total_oz_weight)/16)
remainder = ((total_oz_weight)%16)

# Report
print("\nLion Bars Production Report")
print("-------------------------------")
print(f"Monthly production = {amount} Lion Bars @ {weight} oz per bar.\n")
print(f"Total weight produced = {total_oz_weight} oz, which is "
      f"{total_lbs_weight} lb(s), and {remainder} oz.\n")