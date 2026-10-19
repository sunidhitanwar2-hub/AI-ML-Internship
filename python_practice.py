

# 1. Variables and data types
name = "Sunidhi"
age = 20
percentage = 85.5
is_learning_python = True

print("Name:", name)
print("Age:", age)
print("Percentage:", percentage)
print("Learning Python:", is_learning_python)

print("\n--- Conditional Statements ---")

# 2. If-else
marks = 75

if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")

print("\n--- For Loop ---")

# 3. For loop
for number in range(1, 6):
    print(number)

print("\n--- While Loop ---")

# 4. While loop
count = 1
while count <= 3:
    print("Count:", count)
    count += 1

print("\n--- Functions ---")

# 5. Function
def greet(person):
    return f"Hello, {person}! Welcome to Python."

print(greet(name))

def add(a, b):
    return a + b

print("Sum:", add(10, 20))

print("\n--- User Input ---")

# 6. User input
user_name = input("Enter your name: ")
print(f"Welcome, {user_name}!")
