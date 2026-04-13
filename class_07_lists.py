"""Class 7: Lists.

Today you will learn:
1. What a list is
2. How to store multiple values in one variable
3. How to read one item from a list
4. How to loop through a list

How to learn from this file:
1. Run it
2. Read the output
3. Change the values
4. Run again and observe what changed
"""

print("=== Class 7: Lists ===")

print("\n=== Example 1: A simple list ===")

fruits = ["apple", "banana", "mango"]

print("My fruits:", fruits)

print("\n=== Example 2: Read one item ===")

# Items in a list are numbered starting from 0.
# 0 = first item, 1 = second item, 2 = third item

print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Third fruit:", fruits[2])

print("\n=== Example 3: Loop through a list ===")

cities = ["Melbourne", "Sydney", "Brisbane"]

for city in cities:
    print("City:", city)

print("\n=== Example 4: A list of numbers ===")

scores = [10, 20, 30, 40, 50]

for score in scores:
    print("Score:", score)

print("\n=== Your Practice ===")

# Exercise 1:
# Create a list called colors with 3 colors you like.
# Print the whole list.
colors = ["blue", "green", "black"]
print("My colors:", colors)

# Exercise 2:
# Print only the first color using colors[0]
print("First color:", colors[0])

# Exercise 3:
# Loop through colors and print each one.
for color in colors:
    print("Color:", color)

print("Class 7 complete. Add your own items to the lists and run again.")

days =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days);

print("Working days:")
for i, day in enumerate(days[:5], start=1):
    print("Day:", i, day)