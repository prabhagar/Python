"""Class 20: enumerate and zip

Today you will learn:
1. enumerate — loop over a list AND get the position number
2. zip — loop over two lists at the same time

How to learn from this file:
1. Read each part
2. Run the file
3. Try the challenges at the bottom
"""

# -----------------------------------------------------------
# PART 1 — The problem with normal loops
# -----------------------------------------------------------
print("--- Part 1: The old way ---")

fruits = ["apple", "banana", "mango"]

# You want to print: 1. apple, 2. banana, 3. mango
# Old way — manually track the number
count = 1
for fruit in fruits:
    print(count, fruit)
    count += 1

# This works, but it's clunky. enumerate() fixes this.

# -----------------------------------------------------------
# PART 2 — enumerate
# -----------------------------------------------------------
print("\n--- Part 2: enumerate ---")

# enumerate gives you the index AND the item at the same time
for i, fruit in enumerate(fruits):
    print(i, fruit)

# Output:
# 0 apple
# 1 banana
# 2 mango

# By default it starts at 0. You can start at 1:
print()
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

# Output:
# 1 apple
# 2 banana
# 3 mango

# Real use: print a numbered menu
print()
menu = ["Pizza", "Burger", "Pasta", "Salad"]
print("Today's menu:")
for i, item in enumerate(menu, start=1):
    print(f"  {i}. {item}")

# -----------------------------------------------------------
# PART 3 — zip
# -----------------------------------------------------------
print("\n--- Part 3: zip ---")

# zip lets you loop over TWO lists at the same time, side by side
names  = ["Alice", "Bob", "Charlie"]
scores = [88, 92, 75]

for name, score in zip(names, scores):
    print(name, "scored", score)

# It pairs them up:
# Alice  → 88
# Bob    → 92
# Charlie → 75

# Another example — match items to prices
print()
items  = ["apple", "banana", "mango"]
prices = [1.00, 0.50, 2.00]

for item, price in zip(items, prices):
    print(f"{item} costs ${price}")

# -----------------------------------------------------------
# PART 4 — Combining both
# -----------------------------------------------------------
print("\n--- Part 4: enumerate + zip together ---")

students = ["Alice", "Bob", "Charlie"]
grades   = ["A", "B+", "A-"]

for i, (student, grade) in enumerate(zip(students, grades), start=1):
    print(f"{i}. {student} — {grade}")

# -----------------------------------------------------------
# CHALLENGE — Try it yourself
# -----------------------------------------------------------
print("\n--- Challenge ---")

# 1. Use enumerate (starting at 1) to print this list
#    with numbers in front:
tasks = ["Buy groceries", "Call doctor", "Read book"]
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
# Expected output:
# 1. Buy groceries
# 2. Call doctor
# 3. Read book

# 2. Use zip to pair these two lists and print each line like:
#    "Alice lives in Paris"
people = ["Alice", "Bob", "Diana"]
cities = ["Paris", "Tokyo", "London"]

# Write your answers below:
for person, city in zip(people, cities):
    print(f"{person} lives in {city}")
