"""Class 8: changing lists.

Today you will learn:
1. How to add a new item to a list with append()
2. How to count items in a list with len()
3. How a list changes after you add something

How to learn from this file:
1. Run it
2. Read the output
3. Change the values
4. Run again and observe what changed
"""

print("=== Class 8: Changing Lists ===")

print("\n=== Example 1: Add one fruit ===")
fruits = ["apple", "banana"]

print("Before:", fruits)
fruits.append("mango")
print("After:", fruits)

print("\n=== Example 2: Count list items ===")
cities = ["Melbourne", "Sydney", "Brisbane"]

print("Cities:", cities)
print("Number of cities:", len(cities))

print("\n=== Example 3: Add and count ===")
tasks = ["study", "walk"]

print("Tasks before:", tasks)
tasks.append("read")
print("Tasks after:", tasks)
print("Number of tasks:", len(tasks))

print("\n=== Your Practice ===")

# Exercise 1:
# Create a list called foods with 2 foods.
# Print the list.
foods = ["rice", "pizza"]
print("Foods:", foods)

# Exercise 2:
# Add one more food with append().
# Print the list again.
foods.append("pasta")
print("Updated foods:", foods)

# Exercise 3:
# Print how many foods are in the list using len().
print("Number of foods:", len(foods))

print("Class 8 complete. Change the list items and run again.")