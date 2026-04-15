"""Class 10: function return values.

Today you will learn:
1. How to use return in a function
2. How to store the returned value
3. How to use the returned value in math

How to learn from this file:
1. Run it
2. Read the output
3. Change the values
4. Run again and observe what changed
"""

print("=== Class 10: Function Return Values ===")

print("\n=== Example 1: Return a greeting ===")


def build_greeting(name):
    message = "Hello " + name
    return message


text = build_greeting("Prabh")
print(text)

print("\n=== Example 2: Return a number ===")


def next_year_age(age):
    return age + 1


age_next_year = next_year_age(25)
print("Next year age:", age_next_year)

print("\n=== Example 3: Return total study minutes ===")


def weekly_minutes(daily_minutes):
    return daily_minutes * 7


total = weekly_minutes(30)
print("Weekly minutes:", total)

print("\n=== Your Practice ===")

# Exercise 1:
# Create a function called double_number.
# It takes one value and returns value * 2.
def double_number(value):
    return value * 2


result = double_number(8)
print("Double:", result)

# Exercise 2:
# Create a function called make_title.
# It takes one value called word.
# Return "My " + word
def make_title(word):
    return "My " + word


title = make_title("Notebook")
print(title)


def add_five(number):
    return number + 5

result = add_five(10)
print("Add five:", result)


def calculate_area(length, width):
    return length * width
area = calculate_area(5, 3)
print("Area:", area)

def name_length(name):
    return len(name)
length_of_name = name_length("Prabh")
print("Length of name:", length_of_name)


print("Class 10 complete. Change the values and run again.")