"""Class 3: If and else.

Today you will learn:
1. How a program makes a decision
2. How to use if
3. How to use else
4. How to compare values

How to learn from this file:
1. Run it
2. Type answers
3. Read the output
4. Change the values and run again
"""

print("=== Class 3: If and Else ===")

weather = input("Is the weather sunny? Type yes or no: ")

if weather == "yes":
    print("Great! You can go for a walk.")
else:
    print("You can stay inside and study Python.")

print("\n=== Number comparison ===")

study_minutes_text = input("How many minutes did you study today? ")
study_minutes = int(study_minutes_text)

if study_minutes >= 30:
    print("Nice work. You studied for 30 minutes or more.")
else:
    print("Good start. Try to reach 30 minutes tomorrow.")

print("\n=== Another example ===")

favorite_number_text = input("Type your favorite number: ")
favorite_number = int(favorite_number_text)

if favorite_number > 10:
    print("That is a big favorite number.")
else:
    print("That is a small favorite number.")

print("\n=== Your Practice ===")

# Exercise 1:
# Ask the user: "Are you feeling confident today?"
# If the answer is "yes", print "Keep going."
# Else, print "Small steps are fine."
FeelingConfident = input("Are you feeling confident today? Type yes or no: ")
if FeelingConfident == "yes":
    print("Keep going.")
else:
    print("Small steps are fine.")
# Exercise 2:
# Ask the user for their age.
# Change it to a number with int().
# If age is 18 or more, print "You are an adult."
# Else, print "You are under 18."
age_text = input("How old are you? ")
age = int(age_text)
if age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")


# Exercise 3:
# Ask the user how many hours they slept.
# Change it to a number with int().
# If the number is 8 or more, print "Good rest."
# Else, print "Try to rest more."
hours_slept_text = input("How many hours did you sleep? ")
hours_slept = int(hours_slept_text)
if hours_slept >= 8:
    print("Good rest.")
else:
    print("Try to rest more.")
print("Class 3 complete.")