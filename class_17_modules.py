"""Class 17: Using Built-in Modules

Today you will learn:
1. What a module is
2. How to use the 'random' module (pick random numbers and items)
3. How to use the 'math' module (useful math tools)
4. How to use the 'datetime' module (today's date and time)

How to learn from this file:
1. Read each part
2. Run the file and look at the output
3. Try changing the values and run it again
"""

# A module is a file full of ready-made tools that come with Python.
# You just use: import module_name — and it's ready to use.

# -----------------------------------------------------------
# PART 1 — random module
# -----------------------------------------------------------
import random

print("--- Part 1: random ---")

# Pick a random whole number between 1 and 10
number = random.randint(1, 10)
print("Random number:", number)

# Pick a random item from a list
fruits = ["apple", "banana", "mango", "grape"]
pick = random.choice(fruits)
print("Random fruit:", pick)

# Shuffle a list (mix it up in place)
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print("Shuffled cards:", cards)

# -----------------------------------------------------------
# PART 2 — math module
# -----------------------------------------------------------
import math

print("\n--- Part 2: math ---")

# Round a number UP to the nearest whole number
print("Ceiling of 4.2:", math.ceil(4.2))

# Round a number DOWN
print("Floor of 4.9:", math.floor(4.9))

# Square root
print("Square root of 16:", math.sqrt(16))

# The value of pi
print("Pi is:", math.pi)

# -----------------------------------------------------------
# PART 3 — datetime module
# -----------------------------------------------------------
from datetime import datetime  # Import just the part we need

print("\n--- Part 3: datetime ---")

# Get the current date and time
now = datetime.now()
print("Right now:", now)

# Show just parts of it
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)

# Format the date nicely as a string
formatted = now.strftime("%d %B %Y")   # e.g. 26 April 2026
print("Formatted date:", formatted)

# -----------------------------------------------------------
# PART 4 — Try it yourself
# -----------------------------------------------------------
print("\n--- Part 4: Mini game ---")

# Simple number guessing game using random
secret = random.randint(1, 5)
guess = int(input("Guess a number between 1 and 5: "))

if guess == secret:
    print("Correct! Lucky you!")
else:
    print(f"Nope! The number was {secret}.")


secret_fruit = random.choice(fruits)
guess_fruit = input("Guess a fruit (apple, banana, mango, grape): ")

if guess_fruit == secret_fruit:
    print("Correct! Lucky you!")
else:
    print(f"Nope! The fruit was {secret_fruit}.")
