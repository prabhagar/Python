"""Class 18: Tuples and Sets

Today you will learn:
1. What a tuple is — a list you cannot change
2. When to use a tuple
3. What a set is — a collection with NO duplicates
4. When sets are useful

How to learn from this file:
1. Read each part
2. Run the file and look at the output
3. Try the challenges at the bottom
"""

# -----------------------------------------------------------
# PART 1 — Tuples (a list that cannot be changed)
# -----------------------------------------------------------
# A tuple uses ( ) instead of [ ]
# Once created, you cannot add, remove, or change items.

print("--- Part 1: Tuples ---")

coordinates = (10, 20)
print("Coordinates:", coordinates)
print("X:", coordinates[0])
print("Y:", coordinates[1])

# Good uses for tuples: things that should never change
days_of_week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
print("Days:", days_of_week)
print("First day:", days_of_week[0])
print("Last day:", days_of_week[-1])

# You can loop over a tuple just like a list
print("Weekdays:")
for day in days_of_week[:5]:   # first 5
    print(" ", day)

# This would cause an error — tuples are locked!
# coordinates[0] = 99   # ← try uncommenting this to see the error

# -----------------------------------------------------------
# PART 2 — Sets (a collection with no duplicates)
# -----------------------------------------------------------
# A set uses { } (but no key:value pairs like a dictionary)
# It automatically removes duplicates.
# Items have no order — so you can't use an index like set[0].

print("\n--- Part 2: Sets ---")

# Imagine a sign-in sheet with repeat names
sign_ins = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
print("Raw sign-ins:", sign_ins)

# Convert to a set — duplicates are removed automatically
unique_visitors = set(sign_ins)
print("Unique visitors:", unique_visitors)
print("How many unique visitors:", len(unique_visitors))

# Create a set directly
my_set = {"apple", "banana", "mango"}
print("My set:", my_set)

# Add an item
my_set.add("grape")
print("After add:", my_set)

# Add a duplicate — nothing happens
my_set.add("apple")
print("After adding apple again:", my_set)  # still no duplicates

# Remove an item
my_set.remove("banana")
print("After remove:", my_set)

# Check if something is in a set (very fast!)
print("Is mango in set?", "mango" in my_set)
print("Is banana in set?", "banana" in my_set)

# -----------------------------------------------------------
# PART 3 — Sets: comparing two groups
# -----------------------------------------------------------
print("\n--- Part 3: Comparing sets ---")

team_a = {"Alice", "Bob", "Charlie", "Diana"}
team_b = {"Charlie", "Diana", "Eve", "Frank"}

# Who is in BOTH teams?
print("In both teams:", team_a & team_b)

# Who is in EITHER team (combined, no duplicates)?
print("All players:", team_a | team_b)

# Who is in team_a but NOT team_b?
print("Only in team A:", team_a - team_b)

# -----------------------------------------------------------
# PART 4 — Quick summary
# -----------------------------------------------------------
print("\n--- Summary ---")
print("List   [ ]  → ordered, can change, allows duplicates")
print("Tuple  ( )  → ordered, CANNOT change, allows duplicates")
print("Set    { }  → unordered, can change, NO duplicates")

# -----------------------------------------------------------
# CHALLENGE — Try it yourself
# -----------------------------------------------------------
print("\n--- Challenge ---")
# 1. Create a tuple with 3 of your favourite foods.
#    Print the second item.

# 2. You have this list of numbers with duplicates.
#    Use a set to find out how many unique numbers there are.
numbers = [4, 7, 2, 4, 9, 7, 1, 2, 4]
# Write your code below:

# 1. Create a tuple with 3 of your favourite foods.
#    Print the second item.
favourite_foods = ("pizza", "sushi", "chocolate")
print("Second favourite food:", favourite_foods[1])

# 2. You have this list of numbers with duplicates.
#    Use a set to find out how many unique numbers there are.
numbers = [4, 7, 2, 4, 9, 7, 1, 2, 4]
unique_numbers = set(numbers)
print("Number of unique numbers:", len(unique_numbers))
