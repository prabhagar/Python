"""Class 15: Reading and Writing Files

Today you will learn:
1. How to write text to a file
2. How to read text back from a file
3. How to add more text to an existing file
4. How to read a file line by line

How to learn from this file:
1. Run it
2. Check the new files it creates in your folder
3. Try changing the text and run it again
"""

# -----------------------------------------------------------
# PART 1 — Writing to a file
# -----------------------------------------------------------
# open() opens a file.
# "w" means write mode — it creates the file if it doesn't exist.
# If the file already exists, "w" will overwrite it.
# with ... as f: is the safe way to work with files — it closes
# the file automatically when you're done.

print("--- Part 1: Writing to a file ---")

with open("my_notes.txt", "w") as f:
    f.write("Hello from Python!\n")
    f.write("This is my first file.\n")
    f.write("Writing files is easy.\n")

print("File written successfully.")

# -----------------------------------------------------------
# PART 2 — Reading from a file
# -----------------------------------------------------------
# "r" means read mode.
# .read() loads the entire file content as one big string.

print("\n--- Part 2: Reading the file ---")

with open("my_notes.txt", "r") as f:
    content = f.read()

print(content)

# -----------------------------------------------------------
# PART 3 — Appending (adding to a file without deleting it)
# -----------------------------------------------------------
# "a" means append mode — it adds to the end without erasing.

print("--- Part 3: Appending to the file ---")

with open("my_notes.txt", "a") as f:
    f.write("This line was added later.\n")

print("Line appended.")

# Read the file again to see the new line
with open("my_notes.txt", "r") as f:
    content = f.read()

print(content)

# -----------------------------------------------------------
# PART 4 — Reading line by line
# -----------------------------------------------------------
# .readlines() gives you a list — one item per line.

print("--- Part 4: Reading line by line ---")

with open("my_notes.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines, start=1):
    print(f"Line {i}: {line.strip()}")

# -----------------------------------------------------------
# PART 5 — Writing a list of items to a file
# -----------------------------------------------------------

print("\n--- Part 5: Saving a list to a file ---")

fruits = ["apple", "banana", "mango", "grape"]

with open("fruits.txt", "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")

print("fruits.txt created.")

# Read it back
with open("fruits.txt", "r") as f:
    print(f.read())

# -----------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------
# 1. Change the text in Part 1 to your own notes and run it.
# 2. Open my_notes.txt in VS Code to see the file directly.
# 3. In Part 5, add more fruits to the list and run it again.


food = ["pizza", "burger",
        "pasta",
        "sambar",
        "dosa"]

with open("food.txt", "w") as f:
    for item in food:
        f.write(item + "\n")

with open("food.txt", "r") as f:
    print(f.read())
