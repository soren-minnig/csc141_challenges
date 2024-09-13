# Soren Minnig
# Date: 9/10/24
# This program calculates the amount of money spent on lunch over a span of five
# days. It displays the tax per meal and the total spent with/without tax.

# Original values
PA_TAX = 0.06
PRICE_OF_MEAL = 12.49

# Calculations
meal_tax = (PRICE_OF_MEAL)*(PA_TAX)
total_without_tax = (PRICE_OF_MEAL)*5
total_with_tax = (total_without_tax)+(meal_tax)*5

# Display
print("| Lunch Spending Habits |")
print("-------------------------")
print(f"Tax per meal: {meal_tax}")
print(f"Total without tax: {total_without_tax}")
print(f"Total with tax: {total_with_tax}")
print("-------------------------")