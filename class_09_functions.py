"""Class 9: functions.

Today you will learn:
1. How to create a function with def
2. How to call a function
3. How to give one value to a function

How to learn from this file:
1. Run it
2. Read the output
3. Change the values
4. Run again and observe what changed
"""

print("=== Class 9: Functions ===")

print("\n=== Example 1: A simple function ===")


def say_hello():
    print("Hello from the function.")


say_hello()
say_hello()

print("\n=== Example 2: A function with one value ===")


def greet(name):
    print("Hello", name)


greet("Prabh")
greet("Friend")

print("\n=== Example 3: A study message function ===")


def show_study_message(minutes):
    print("You studied for", minutes, "minutes today.")


show_study_message(20)
show_study_message(45)

print("\n=== Your Practice ===")

# Exercise 1:
# Create a function called say_bye.
# Inside it, print "Bye for now."
# Then call it two times.
def say_bye():
    print("Bye for now.")


say_bye()
say_bye()

# Exercise 2:
# Create a function called show_food.
# Give it one value called food.
# Inside it, print "I like" and the food.
# Then call it with two different foods.
def show_food(food):
    print("I like", food)


show_food("pizza")
show_food("rice")

def show_age(age):
    print("I am", age, "years old.")

age = input("Enter your age: ")
show_age(age)

print("Class 9 complete. Change the function names and values and run again.")
