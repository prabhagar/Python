"""Class 6: for loops.

Today you will learn:
1. How to repeat code with for
2. How to use range()
3. How to print each value in a loop

How to learn from this file:
1. Run it
2. Read the output
3. Change the numbers
4. Run again and observe what changed
"""

print("=== Class 6: For Loops ===")

print("\n=== Example 1: Count from 1 to 5 ===")
for number in range(1, 6):
    print("Number:", number)

print("\n=== Example 2: Practice days ===")
for day in range(1, 4):
    print("Day", day, ": keep learning Python")

print("\n=== Example 3: Letters in a word ===")
word = "code"

for letter in word:
    print("Letter:", letter)

print("\n=== Your Practice ===")

# Exercise 1:
# Use a for loop to print Step 1, Step 2, Step 3, Step 4
for step in range(1, 5):
    print("Step", step)

# Exercise 2:
# Create a variable called food with a short word.
# Use a for loop to print each letter.
food = "rice"

for letter in food:
    print(letter)

print("Class 6 complete. Change the numbers and words and run again.")

vegetable = "carrot"

for letter in vegetable:
    print(letter)