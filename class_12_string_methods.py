"""Class 12: String Methods

Today you will learn:
1. How to change the case of text
2. How to check what's inside a string
3. How to clean up messy text
4. How to replace words in a string
5. How to split a sentence into a list

How to learn from this file:
1. Run it
2. Read the output
3. Try changing the text and run it again
"""

# -----------------------------------------------------------
# PART 1 — Changing case
# -----------------------------------------------------------

name = "prabh singh"

print("--- Part 1: Changing case ---")
print(name.upper())       # All capitals
print(name.lower())       # All lowercase
print(name.title())       # First letter of each word is capital

# -----------------------------------------------------------
# PART 2 — Checking what's inside
# -----------------------------------------------------------

sentence = "I live in Melbourne"

print("\n--- Part 2: Checking content ---")
print(sentence.startswith("I"))        # Does it start with "I"?
print(sentence.endswith("Sydney"))     # Does it end with "Sydney"?
print("Melbourne" in sentence)         # Is "Melbourne" anywhere inside?

# -----------------------------------------------------------
# PART 3 — Cleaning up messy text
# -----------------------------------------------------------
# Users often accidentally type extra spaces. .strip() removes them.

messy = "   hello world   "

print("\n--- Part 3: Cleaning spaces ---")
print("Before strip:", messy)
print("After strip: ", messy.strip())

# -----------------------------------------------------------
# PART 4 — Replacing words
# -----------------------------------------------------------

greeting = "Good morning, Prabh!"

print("\n--- Part 4: Replacing text ---")
new_greeting = greeting.replace("morning", "evening")
print(new_greeting)

# -----------------------------------------------------------
# PART 5 — Splitting a string into a list
# -----------------------------------------------------------
# .split() breaks a string apart wherever it finds a space (or any separator).

fruits = "apple,banana,mango,grape"

print("\n--- Part 5: Splitting ---")
fruit_list = fruits.split(",")
print(fruit_list)
print("First fruit:", fruit_list[0])
print("Last fruit: ", fruit_list[-1])



name = "prabh chetty"
print(name.upper())
print(name.lower())
print(name.title())

food = "pizza, burger, pasta, sambar, dosa"
food_list = food.split(", ")
print(food_list)
print("First food:", food_list[0])
print("Last food: ", food_list[-1])

