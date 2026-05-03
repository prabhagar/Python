"""Class 19: List and Dictionary Comprehensions

Today you will learn:
1. What a comprehension is
2. How to build a list in one line
3. How to add a condition (filter) to it
4. How to do the same with a dictionary

How to learn from this file:
1. Read each part — compare the "old way" vs the "new way"
2. Run the file
3. Try the challenges at the bottom
"""

# -----------------------------------------------------------
# PART 1 — The old way vs the new way
# -----------------------------------------------------------
print("--- Part 1: The old way ---")

# Old way — loop to build a list of squares
squares = []
for n in range(1, 6):
    squares.append(n * n)
print("Squares (old way):", squares)

# New way — list comprehension (same result, one line)
print("\n--- New way: List Comprehension ---")

squares = [n * n for n in range(1, 6)]
print("Squares (new way):", squares)

# How to read it:
# [  n * n          for n in range(1, 6)  ]
#   ↑ what to keep    ↑ where to get items

# -----------------------------------------------------------
# PART 2 — Adding a condition (filter)
# -----------------------------------------------------------
print("\n--- Part 2: Filtering with a condition ---")

# Only keep even numbers from 1 to 10
evens = [n for n in range(1, 11) if n % 2 == 0]
print("Even numbers:", evens)

# Only keep words longer than 4 letters
words = ["cat", "banana", "dog", "elephant", "kiwi", "strawberry"]
long_words = [w for w in words if len(w) > 4]
print("Long words:", long_words)

# Make all words uppercase — no filter, just transform
upper_words = [w.upper() for w in words]
print("Uppercase:", upper_words)

# -----------------------------------------------------------
# PART 3 — Dictionary Comprehension
# -----------------------------------------------------------
print("\n--- Part 3: Dictionary Comprehension ---")

# Old way — build a dictionary with a loop
fruits = ["apple", "banana", "mango"]
fruit_lengths = {}
for fruit in fruits:
    fruit_lengths[fruit] = len(fruit)
print("Lengths (old way):", fruit_lengths)

# New way — dictionary comprehension
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print("Lengths (new way):", fruit_lengths)

# How to read it:
# { fruit : len(fruit)   for fruit in fruits }
#   ↑ key   ↑ value         ↑ where to get items

# Another example — square each number as a dict
number_squares = {n: n * n for n in range(1, 6)}
print("Number squares dict:", number_squares)

# With a filter — only include numbers where the square is > 10
big_squares = {n: n * n for n in range(1, 6) if n * n > 10}
print("Big squares only:", big_squares)

# -----------------------------------------------------------
# PART 4 — Real-world style example
# -----------------------------------------------------------
print("\n--- Part 4: Real example ---")

# You have a list of prices. Apply a 10% discount to each.
prices = {"apple": 1.00, "banana": 0.50, "mango": 2.00, "grape": 3.00}

discounted = {item: round(price * 0.9, 2) for item, price in prices.items()}
print("Original prices:", prices)
print("After 10% discount:", discounted)

# -----------------------------------------------------------
# CHALLENGE — Try it yourself
# -----------------------------------------------------------
print("\n--- Challenge ---")

# 1. Use a list comprehension to get all numbers from 1 to 20
#    that are divisible by 3.
#    Expected: [3, 6, 9, 12, 15, 18]

# 2. You have this list of names.
#    Use a dict comprehension to create a dictionary
#    where each name maps to its length.
names = ["Alice", "Bob", "Charlie", "Diana"]
# Expected: {'Alice': 5, 'Bob': 3, 'Charlie': 7, 'Diana': 5}

# Write your answers below:
numbers_div_by_3 = [n for n in range(1, 21) if n % 3 == 0]
name_lengths = {name: len(name) for name in names}
