# Soren Minnig
# 9/18/24
# This program prompts the user to input the speed limit and the speed they were
# driving at. It uses these values to calculate what qualifies as "excessive 
# speed" for the speed limit, how many mph over the speed limit they were going
# (if applicable), and the fine amount (if speeding, but not excessively).

# Speed inputs
speed_limit = int(input("\nWhat is the speed limit? "))
speed = int(input("How fast are you going? "))

# Speed calculations
over_speed = (speed) - (speed_limit)
excessive_speed = (speed_limit) + 30

# Fine calculations: in PA, the base fine is $35, but if the speed limit is over
# 65, it's $42.50. For each mile 5 mph over the speed limit, $2 are added.
if speed_limit >= 65:
    if over_speed > 5:
        fine_amount = 42.50 + 2*((over_speed)-5)
    else:
        fine_amount = 42.50
else:
    if over_speed > 5:
        fine_amount = 35 + 2*((over_speed)-5)
    else:
        fine_amount = 35

# Checking speed
if speed >= excessive_speed:
    print(f"\nEXCESSIVE SPEEDING: You went {speed} mph in a {speed_limit} mph "
          f"zone, which is over the speed limit by {over_speed}.")
    print("\nYour license is now SUSPENDED for 15 days.")
    print("You will either need to call a friend or a Lyft to get home.")
elif speed > speed_limit:
    print(f"\nSPEEDING: You went {speed} mph in a {speed_limit} mph zone, which "
          f"is over the speed limit by {over_speed}.")
    print("\nYou will receive a speeding ticket.")
    print(f"Additionally, you will receive a fine of ${fine_amount}.")
else:
    print(f"\nYou went {speed} mph in a {speed_limit} mph zone, which is not "
          "over the speed limit.")
    print("\nYou will face no consequences.")