"""Class 4: elif and multiple checks.

Today you will learn:
1. How to use if, elif, and else together
2. How to check a range with and
3. How to write small practical decisions

How to learn from this file:
1. Run it
2. Type answers
3. Read the output
4. Change values and run again
"""

print("=== Class 4: elif and Multiple Checks ===")

print("\n=== Example 1: Score message ===")
score_text = input("Enter your test score (0 to 100): ")
score = int(score_text)

if score >= 80:
    print("Great job. Your score is strong.")
elif score >= 50:
    print("Nice try. You passed. Keep practicing.")
else:
    print("Do not worry. Practice a bit more and try again.")

print("\n=== Example 2: Sleep check with and ===")
hours_text = input("How many hours did you sleep last night? ")
hours = int(hours_text)

if hours >= 7 and hours <= 9:
    print("Good range. Your sleep time is balanced.")
elif hours < 7:
    print("You may need more rest tonight.")
else:
    print("You slept a lot. Hope you feel fresh.")

print("\n=== Example 3: Weather and plan ===")
weather = input("Type weather: sunny, rainy, or cloudy: ")

if weather == "sunny":
    print("Plan: 20-minute walk.")
elif weather == "rainy":
    print("Plan: indoor Python practice.")
else:
    print("Plan: short stretch and study.")

print("\n=== Your Practice ===")

# Exercise 1:
# Ask for age.
# If age is 13 or more, print "You can create your own small project."
# Else, print "Start with tiny coding steps."
age_text = input("Enter your age: ")
age = int(age_text)

if age >= 13:
    print("You can create your own small project.")
else:
    print("Start with tiny coding steps.")

# Exercise 2:
# Ask for daily study minutes.
# If minutes >= 60: print "Excellent focus."
# Elif minutes >= 30: print "Good consistency."
# Else: print "Try to add 10 more minutes tomorrow."
study_minutes_text = input("How many minutes did you study today? ")
study_minutes = int(study_minutes_text)

if study_minutes >= 60:
    print("Excellent focus.")
elif study_minutes >= 30:
    print("Good consistency.")
else:
    print("Try to add 10 more minutes tomorrow.")

print("Class 4 complete. Change values and run again.")
