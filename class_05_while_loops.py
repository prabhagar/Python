"""Class 5: while loops.

Today you will learn:
1. How to repeat code with while
2. How a counter changes inside a loop
3. How a loop stops when a condition becomes false

How to learn from this file:
1. Run it
2. Read the output
3. Change the values
4. Run again and observe what changed
"""

print("=== Class 5: While Loops ===")

print("\n=== Example 1: Count from 1 to 5 ===")
number = 1

while number <= 5:
    print("Number:", number)
    number = number + 1

print("Loop finished.")

print("\n=== Example 2: Study tracker ===")
study_day = 1

while study_day <= 3:
    print("Day", study_day, ": 20 minutes of Python practice")
    study_day = study_day + 1

print("Nice work. You finished 3 study days.")

print("\n=== Example 3: Countdown ===")
countdown = 3

while countdown > 0:
    print("Starting in", countdown)
    countdown = countdown - 1

print("Start now!")

print("\n=== Your Practice ===")

# Exercise 1:
# Start with step = 1
# Use a while loop to print Step 1, Step 2, Step 3, Step 4
step = 1
while step <= 4:
    print("Step", step)
    step = step + 1

# Exercise 2:
# Start with bottles = 5
# Use a while loop to count down to 1
bottles = 5
while bottles >= 1:
    print("Bottles left:", bottles)
    bottles = bottles - 1

print("\n=== Extra Exercise: Save Money ===")

money = 1

while money <= 5:
    print("You saved", money, "dollar")
    money = money + 1

print("You saved 5 dollars in total.")

print("Class 5 complete. Change the numbers and run again.")

# Extra Exercise:
# Create a variable called coins and set it to 1.
# Use a while loop to print:
# I have 1 coin
# I have 2 coins
# I have 3 coins
# I have 4 coins
# I have 5 coins
# After the loop, print:
# I counted 5 coins.
coins = 1
while coins <= 5:
    print("I have", coins, "coin" if coins == 1 else "coins")
    coins = coins + 1

print("I counted 5 coins.")