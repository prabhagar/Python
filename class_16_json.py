"""Class 16: Working with JSON

Today you will learn:
1. What JSON is and why it's useful
2. How to save a dictionary to a JSON file
3. How to load it back
4. How to work with a list of dictionaries in JSON

How to learn from this file:
1. Run it
2. Open the .json files it creates in VS Code
3. Try changing the data and run it again
"""

import json  # This is a built-in Python module — no install needed

# -----------------------------------------------------------
# PART 1 — What is JSON?
# -----------------------------------------------------------
# JSON is a way to save structured data (like dictionaries and lists)
# to a file so you can load it back later.
# It's also the format websites use to send data between each other.

# A normal Python dictionary
person = {
    "name": "Prabh",
    "age": 30,
    "city": "Melbourne",
    "hobbies": ["coding", "reading", "coffee"]
}

print("--- Part 1: Our dictionary ---")
print(person)

# -----------------------------------------------------------
# PART 2 — Saving a dictionary to a JSON file
# -----------------------------------------------------------
# json.dump() writes the dictionary into a file as JSON.
# indent=4 makes it look neat and readable when you open the file.

print("\n--- Part 2: Saving to person.json ---")

with open("person.json", "w") as f:
    json.dump(person, f, indent=4)

print("person.json saved. Open it in VS Code to see it!")

# -----------------------------------------------------------
# PART 3 — Loading a JSON file back into Python
# -----------------------------------------------------------
# json.load() reads the file and gives you back a Python dictionary.

print("\n--- Part 3: Loading from person.json ---")

with open("person.json", "r") as f:
    loaded_person = json.load(f)

print(loaded_person)
print(f"Name: {loaded_person['name']}")
print(f"First hobby: {loaded_person['hobbies'][0]}")

# -----------------------------------------------------------
# PART 4 — A list of dictionaries (very common in real apps)
# -----------------------------------------------------------
# Imagine saving multiple people or products.

print("\n--- Part 4: Saving a list of people ---")

people = [
    {"name": "Prabh", "city": "Melbourne"},
    {"name": "Sara",  "city": "Sydney"},
    {"name": "James", "city": "Brisbane"}
]

with open("people.json", "w") as f:
    json.dump(people, f, indent=4)

print("people.json saved.")

# Load it back and loop through
with open("people.json", "r") as f:
    loaded_people = json.load(f)

print("\nAll people:")
for p in loaded_people:
    print(f"  {p['name']} lives in {p['city']}")

# -----------------------------------------------------------
# PART 5 — Converting to/from JSON string (no file needed)
# -----------------------------------------------------------
# json.dumps() converts a dictionary to a JSON string.
# json.loads() converts a JSON string back to a dictionary.

print("\n--- Part 5: JSON as a string ---")

data = {"item": "coffee", "price": 4.50}

json_string = json.dumps(data)
print(f"JSON string: {json_string}")
print(f"Type: {type(json_string)}")

back_to_dict = json.loads(json_string)
print(f"Back to dict: {back_to_dict}")
print(f"Price: {back_to_dict['price']}")

# -----------------------------------------------------------
# TRY IT YOURSELF
# -----------------------------------------------------------
# 1. Change the person dictionary to your own details.
# 2. Add a 4th person to the people list and run it again.
# 3. Open person.json and people.json in VS Code to see the files.
