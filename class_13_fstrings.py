"""Class 13: f-Strings (Formatted Strings)

Today you will learn:
1. What an f-string is
2. How to put variables directly inside text
3. How to do simple math inside an f-string
4. How to control decimal places

How to learn from this file:
1. Run it
2. Read the output
3. Try changing the values and run it again
"""

# -----------------------------------------------------------
# PART 1 — The old way vs the new way
# -----------------------------------------------------------
# You've been joining text and variables using commas in print().
# f-strings are a cleaner, easier way to do the same thing.

name = "Prabh"
city = "Melbourne"

# Old way
print("--- Part 1: Old way vs f-string ---")
print("My name is", name, "and I live in", city)

# New way — put an f before the quote, then use {} around variables
print(f"My name is {name} and I live in {city}")

# -----------------------------------------------------------
# PART 2 — Numbers inside f-strings
# -----------------------------------------------------------

age = 30
height = 1.75

print("\n--- Part 2: Numbers ---")
print(f"I am {age} years old and {height}m tall.")

# -----------------------------------------------------------
# PART 3 — Math inside f-strings
# -----------------------------------------------------------
# You can put simple expressions inside the curly braces.

price = 40
quantity = 3

print("\n--- Part 3: Math inside f-strings ---")
print(f"I bought {quantity} items at ${price} each.")
print(f"Total cost: ${price * quantity}")

# -----------------------------------------------------------
# PART 4 — Controlling decimal places
# -----------------------------------------------------------
# Use :.2f to show exactly 2 decimal places (useful for money).

score = 87.6666666

print("\n--- Part 4: Decimal places ---")
print(f"Your score is {score}")          # Lots of decimals
print(f"Your score is {score:.2f}")      # Rounded to 2 decimal places
print(f"Your score is {score:.0f}")      # Rounded to whole number

# -----------------------------------------------------------
# PART 5 — Putting it all together
# -----------------------------------------------------------

item = "tea"
unit_price = 4.50
cups = 5

print("\n--- Part 5: Summary ---")
print(f"You ordered {cups} cups of {item}.")
print(f"Price per cup: ${unit_price:.2f}")
print(f"Total: ${cups * unit_price:.2f}")

# -----------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------
# 1. Change `name` and `city` to your own details.
# 2. Change `price` and `quantity` to anything you like.
# 3. In Part 5, change `item` to something else (e.g. "tea") and run it.

flower = "rose"
print(f"I have a {flower} in my garden.")

food = "pizza"
unit_price = 12.99
orders = 2
print(f"I ordered {orders} {food}(s) that cost ${unit_price:.2f} each.")
print(f"After tax, it costs ${unit_price * orders * 1.1:.2f}.")
