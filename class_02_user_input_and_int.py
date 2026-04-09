"""Class 2: User input.

Today you will learn:
1. input() to ask the user for information
2. How to store answers in variables
3. Why input gives text
4. How to change text into a number with int()

How to learn from this file:
1. Run it
2. Type your answers
3. Read the output
4. Change the code and run again
"""

print("=== Class 2: User Input ===")

name = input("What is your name? ")
city = input("Which city do you live in? ")

print("Hello", name)
print("You live in", city)

print("\n=== Input is text by default ===")

age_text = input("How old are you? ")
print("You typed", age_text)

age = int(age_text)
next_year_age = age + 1

print("Next year you will be", next_year_age)

print("\n=== One more number example ===")

favorite_number_text = input("What is your favorite number? ")
favorite_number = int(favorite_number_text)

print("Double your favorite number is", favorite_number * 2)

print("\n=== Your Practice ===")

# Exercise 1:
# Ask the user for their favorite food.
# Store it in favorite_food and print it.
favorite_food = input("What is your favorite food? ")
print("Your favorite food is", favorite_food)


# Exercise 2:
# Ask the user for their hobby.
# Store it in hobby and print it.
hobby = input("What is your hobby? ")
print("Your hobby is", hobby)

# Exercise 3:
# Ask the user for daily study minutes.
# Change it to a number with int().
# Print weekly study minutes using * 7.
daily_study_minutes_text = input("How many minutes do you study daily? ")
daily_study_minutes = int(daily_study_minutes_text)
weekly_study_minutes = daily_study_minutes * 7
print("Your weekly study minutes are", weekly_study_minutes)

print("Class 2 complete. Add your practice code below.")