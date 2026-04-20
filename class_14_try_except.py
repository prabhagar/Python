"""Class 14: Handling Errors with try / except

Today you will learn:
1. What happens when Python hits an error
2. How to catch errors so your program doesn't crash
3. How to show a helpful message instead
4. How to handle different types of errors

How to learn from this file:
1. Run it
2. Read the output
3. Try changing the values and run it again
"""

# -----------------------------------------------------------
# PART 1 — What a crash looks like (this is commented out)
# -----------------------------------------------------------
# If you divide by zero, Python crashes with an error.
# Uncomment the next two lines to see it crash, then comment them back.

# result = 10 / 0
# print(result)

# -----------------------------------------------------------
# PART 2 — Catching the error with try / except
# -----------------------------------------------------------
# Put the risky code inside "try".
# Put what to do if it fails inside "except".

print("--- Part 2: Catching a division error ---")

try:
    result = 10 / 0
    print(result)
except:
    print("Oops! Something went wrong.")

print("Program keeps running after the error.")

# -----------------------------------------------------------
# PART 3 — A real example: asking the user for a number
# -----------------------------------------------------------
# If the user types "abc" instead of a number, int() will crash.
# try/except saves us.

print("\n--- Part 3: Safe number input ---")

user_input = "abc"   # Pretend the user typed this

try:
    number = int(user_input)
    print(f"You entered: {number}")
except:
    print(f"'{user_input}' is not a valid number. Please enter digits only.")

# Now try with a valid input
user_input = "42"

try:
    number = int(user_input)
    print(f"You entered: {number}")
except:
    print(f"'{user_input}' is not a valid number.")

# -----------------------------------------------------------
# PART 4 — Naming the error to see what went wrong
# -----------------------------------------------------------
# Use "except Exception as e" to capture the error message.

print("\n--- Part 4: Seeing the error message ---")

try:
    result = 10 / 0
except Exception as e:
    print(f"Error caught: {e}")

try:
    number = int("hello")
except Exception as e:
    print(f"Error caught: {e}")

# -----------------------------------------------------------
# PART 5 — Using else and finally
# -----------------------------------------------------------
# else  → runs only if NO error happened
# finally → runs no matter what (error or not)

print("\n--- Part 5: else and finally ---")

try:
    result = 10 / 2
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Success! Result is {result}")
finally:
    print("This always runs.")

# -----------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------
# 1. In Part 2, change 0 to 2 and run it. Does it crash now?
# 2. In Part 3, change "abc" to your own name and run it.
# 3. In Part 3, change "abc" to "100" and run it. What changes?

value = "abc"
try:
    number = int(value)
    print(f"You entered: {number}")
except Exception as e:
    print(f"Error: {e}")
