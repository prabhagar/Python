"""Class 1: Python baby steps.

Today you will learn:
1. print() to show output
2. Variables to store data
3. Text (string) vs numbers (int)
4. Changing values and running again

How to learn from this file:
1. Run it once
2. Read the output
3. Change values
4. Run again and observe what changed
"""

print("=== Class 1: Start ===")

# Step 1: print text
print("Hello, Python!")
print("I am learning one small step at a time.")

print("\n=== Step 2: Variables ===")

# A string is text inside quotes.
name = "Prabh"
city = "Melbourne"

# int means whole number.
age = 25
favorite_number = 7

print("My name is", name)
print("I live in", city)
print("My age is", age)
print("My favorite number is", favorite_number)

print("\n=== Step 3: Change values ===")

# We can replace old values with new values.
name = "YourName"
age = 18

print("Updated name:", name)
print("Updated age:", age)

print("\n=== Step 4: Numbers can do math ===")
next_year_age = age + 1
double_favorite = favorite_number * 2

print("Next year age:", next_year_age)
print("Double favorite number:", double_favorite)

print("\n=== Your Practice ===")

# Exercise 1:
# Create a variable called favorite_food and print it.
favorite_food = "Pizza"
print("My favorite food is", favorite_food)

# Exercise 2:
# Create a variable called hobby and print it.
hobby = "Reading"
print("My hobby is", hobby)

# Exercise 3:
# Change city and favorite_number to your real values, then run again.
city = "Sydney"
favorite_number = 42
print("Updated city:", city)
print("Updated favorite number:", favorite_number)

# Exercise 4:
# Create a number variable called daily_study_minutes.
# Print daily_study_minutes * 7 to see weekly study minutes.
daily_study_minutes = 30
weekly_study_minutes = daily_study_minutes * 7
print("Weekly study minutes:", weekly_study_minutes)

print("Class 1 complete. Edit values and run again.")