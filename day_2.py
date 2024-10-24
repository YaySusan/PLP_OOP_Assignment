# VARIABLES AND DATA TYPES - Variables are like containers that store data. Python has various data types, such as integers, floats, strings, and booleans
# Let's store your favourite number
favourite_number = 3
print(f"My favourite number is {favourite_number}.")

# How about a word (string)?
greeting = "Hello there!"
print(greeting)

# And a true/false value (boolean)
is_python_fun = True
print(f"Is Python fun? {is_python_fun}")

# CONTROL FLOW (if, elif, else) - Control flow allows you to make decisions in your code using if, elif, and else statements. Think of control flow as if choosing your own adventure in a story. Depending on your choices, the story (or your code) takes a different path.
temperature = 30

if temperature > 25:
    print("It's hot outside! Wear shorts.")
elif temperature > 15:
    print("It'S warm. Maybe a light jacket.")
else:
    print("Brrr! It'S cold. Bundle up!")


#LOOPS - Loops allow you to repeat a block of code multiple times. for loops are used when you know the number of iterations, while while loops run until a condition is met. Loops are like a list of chores. You repeat the same action until you've completed all the chores (for loop) or until the house is clean (while loop).
# For loop example
for i in range(5):
    print(f"This is loop iteration {i}")

# While loop example
countdown = 5
while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1
print("Blast off!")


# FUNCTIONS - Functions are reusable blocks of code that perform a specific task. They help keep your code organized and avoid repetition. Think of functions like recipes. Once you have a recipe, you can make the same dish repeatedly without having to write it down each time.
# Defining a function
def greet(name):
    return f"Hello, {name}!"

# Using the function
print(greet("Alice"))
print(greet("Bob"))


# LISTS AND DICTIONARIES - Lists and dictionaries are ways to store collections of data. Lists are ordered and indexed by numbers, while dictionaries store data in key-value pairs. Imagine a list as your shopping list where each item has a specific position. Conversely, a dictionary is like a contact book where you look up people's numbers by their names.
# List example
fruits = ["apple", "banana", "cheery"]
print(f"My favourite fruit is {fruits[1]}.")

# Dictionary example
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678"
}

print(f"Alice's phone number is {contacts['Alice']}.")


# MODULES - Modules are files containing Python code (functions, variables, etc.) that you can import and use in your projects. They help keep your code organized and reusable. Think of modules as toolboxes. Each toolbox contains tools (functions, classes, variables) you can use in your project without building them from scratch.
# Let's use the built-in math module
import math

# Using a function from the math module
result = math.sqrt(16)
print(f"The square root of 16 is {result}.")

# Creating and using your own module
# Save this code in a file named my_module-py
# def greet(name):
#     return f"Hello, {name}!"

# Now in your main script, you can import and use it
import my_module

print(my_module.greet("Alice"))
print(my_module.greet("Susan"))



