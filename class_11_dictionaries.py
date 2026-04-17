"""Class 11: Dictionaries

Today you will learn:
1. What a dictionary is
2. How to create one
3. How to read values from it
4. How to add and change values

How to learn from this file:
1. Run it
2. Read the output
3. Try changing some values and run it again
"""

# -----------------------------------------------------------
# PART 1 — Creating a dictionary
# -----------------------------------------------------------
# A dictionary stores pairs: a KEY and a VALUE.
# Think of it like a real dictionary: word (key) → meaning (value).

person = {
    "name": "Prabh",
    "age": 30,
    "city": "Melbourne"
}

print("--- Part 1: My dictionary ---")
print(person)

# -----------------------------------------------------------
# PART 2 — Reading values by key
# -----------------------------------------------------------
# Use square brackets and the key name to get a value.

print("\n--- Part 2: Reading values ---")
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])

# -----------------------------------------------------------
# PART 3 — Changing a value
# -----------------------------------------------------------
# Just assign a new value to the key.

person["age"] = 31

print("\n--- Part 3: After changing age ---")
print("New age:", person["age"])

# -----------------------------------------------------------
# PART 4 — Adding a new key
# -----------------------------------------------------------
# You can add a brand new key at any time.

person["job"] = "Developer"

print("\n--- Part 4: After adding job ---")
print("Job:", person["job"])
print("Full dictionary now:", person)

# -----------------------------------------------------------
# PART 5 — Looping through a dictionary
# -----------------------------------------------------------
# .items() gives you both the key and value together.

print("\n--- Part 5: Printing all keys and values ---")
for key, value in person.items():
    print(key, "→", value)

# -----------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------
# 1. Change "name" to your own name.
# 2. Add a new key called "hobby" with any value you like.
# 3. Run the file and see the output change.
