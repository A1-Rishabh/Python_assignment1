# student_Detail.py

# Name: Rishabh Bhardwaj
# Roll No: 2501060109
# Course: BCA
# Semester: 1st
# Subject: Problem Solving with Python
# Assignment: Unit-1 Project
# Title: Student Profile Console App
# Date: 13/11/20254

# ========================================
# Task 1: Setup & Introduction
# ========================================

print("========================================")
print("     STUDENT PROFILE CONSOLE APP")
print("========================================")
print("Welcome! This tool will collect and display your basic profile details.")
print("It also demonstrates fundamental Python concepts like I/O, Operators, and Strings.")
print("----------------------------------------")




# ========================================
# Task 2: Input & Variables
# ========================================

# Get student profile information
print("\n--- Profile Data Input ---")
student_full_name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")
program = input("Enter Program (e.g., BCA): ")
university_name = input("Enter University Name: ")
city = input("Enter City: ")
hobby = input("Enter Hobby: ")
age = int(input("Enter your age: "))

# printing input 
print("NAME: ",student_full_name)
print("ROLL NO: ",roll_number)
print("PROGRAM: ",program)
print("UNIVERSITY NAME: ",university_name)
print("CITY: ",city)
print("HOBBY: ",hobby)
print("Age: ",age)
print("--- Input Complete ---")




# ========================================
# Task 3: Operators Demonstration
# ========================================

print("\n--- Operator Demonstration ---")
# Get two numbers for arithmetic/comparison demonstration
while True:
    try:
        num1_str = input("Enter the first number (Num1): ")
        num2_str = input("Enter the second number (Num2): ")
        num1 = float(num1_str) # Use float to handle decimal inputs easily
        num2 = float(num2_str)
        break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# 1. Arithmetic Operators
print("\n[1] Arithmetic Operators:")
print(f"  Addition (Num1 + Num2): {num1 + num2}")
print(f"  Subtraction (Num1 - Num2): {num1 - num2}")
print(f"  Multiplication (Num1 * Num2): {num1 * num2}")
print(f"  Division (Num1 / Num2): {num1 / num2}")
print(f"  Modulus (Num1 % Num2): {num1 % num2}")
print(f"  Exponentiation (Num1 ** 2): {num1 ** 2}")
print(f"  Floor Division (Num1 // Num2): {num1 // num2}")

# 2. Assignment Operators (Demonstrating on a temporary variable 'x')
x = 10
print("\n[2] Assignment Operators (Starting x=10):")
x += 5
print(f"  x += 5  -> x is now: {x}") # x is now 15
x -= 3
print(f"  x -= 3  -> x is now: {x}") # x is now 12
x *= 2
print(f"  x *= 2  -> x is now: {x}") # x is now 24

# 3. Comparison Operators
print("\n[3] Comparison Operators (Num1={num1}, Num2={num2}):")
print(f"  Num1 == Num2: {num1 == num2}")
print(f"  Num1 > Num2: {num1 > num2}")
print(f"  Num1 <= Num2: {num1 <= num2}")

# 4. Logical Operators (Using comparison results)
is_major = age >= 18
is_roll_numeric = roll_number.isdigit() # Check if roll number is purely numeric
print("\n[4] Logical Operators (Is Major: {is_major}, Roll Numeric: {is_roll_numeric}):")
print(f"  Is Major AND Roll Numeric: {is_major and is_roll_numeric}")
print(f"  Is Major OR Roll Numeric: {is_major or is_roll_numeric}")
print(f"  NOT Is Major: {not is_major}")

# 5. Identity Operators
a = [1, 2]
b = [1, 2]
c = a
print("\n[5] Identity Operators (a=[1, 2], b=[1, 2], c=a):")
print(f"  a is c: {a is c} (True, they point to the same object)")
print(f"  a is b: {a is b} (False, even if content is same, they are different objects)")
print(f"  a is not b: {a is not b}")

# 6. Membership Operators
print("\n[6] Membership Operators:")
print(f"  'BCA' in Program '{program}': {'BCA' in program}")
print(f"  'University' in University Name '{university_name}': {'University' in university_name}")
print(f"  'z' not in Hobby '{hobby}': {'z' not in hobby}")




# ========================================
# Task 4: Python Strings & Formatting
# ========================================

print("\n--- String Operations Demo ---")

# 1. String Concatenation
greeting_message = "Hello, " + student_full_name + "! Welcome to Python Assignment 1."
print(f"Concatenation: {greeting_message}")

# 2. f-string and Escape Characters
# \t for tab, \n for newline, \" for double quote
f_string_demo = f"Profile Summary:\n\t- Name: \"{student_full_name}\"\n\t- Program: {program}"
print("f-string with Escape Chars:")
print(f_string_demo)

# 3. At least 5 String Methods
print("\nString Methods Demonstration:")

# Method 1: .upper()
name_upper = student_full_name.upper()
print(f"  Upper Case Name: {name_upper}")

# Method 2: .title()
hobby_title = hobby.title()
print(f"  Title Case Hobby: {hobby_title}")

# Method 3: .strip() (using City as an example, assuming user might have leading/trailing spaces)
city_stripped = city.strip()
print(f"  City (stripped of spaces): '{city_stripped}'")

# Method 4: .replace()
roll_replaced = roll_number.replace('BCA', 'bca')
print(f"  Roll No (BCA replaced with bca): {roll_replaced}")

# Method 5: .count()
name_count_a = student_full_name.lower().count('a')
print(f"  Count of 'a' in Name: {name_count_a}")




# =============================================
# Task 5: Final Output — Student Profile Card
# =============================================

print("\n" + "="*40)
print(" "*8 + "STUDENT PROFILE SYSTEM")
print("="*40)

# The :<20 format specifier ensures that the label takes up 20 characters, left-aligned.
print(f"Name:{'':<14}{student_full_name}")
print(f"Roll No:{'':<11}{roll_number}")
print(f"Course:{'':<12}{program.upper()}")
print(f"University:{'':<8}{university_name.title()}")
print(f"City:{'':<14}{city.title()}")
print(f"Age:{'':<15}{age}")
print(f"Hobby:{'':<13}{hobby.title()}")

print("="*40)
print("Welcome to Python Programming!")
print("="*40)



# ========================================
# Task 6: Bonus Task (Extra Credit)
# ========================================

save_profile = input("\nDo you want to save your profile? (yes/no): ").lower().strip()

if save_profile == 'yes':
    file_name = "student_profile.txt"
    try:
        # Open the file in write mode ('w')
        with open(file_name, 'w') as file:
            file.write("--- STUDENT PROFILE LOG ---\n")
            file.write(f"Name: {student_full_name}\n")
            file.write(f"Roll No: {roll_number}\n")
            file.write(f"Course: {program.upper()}\n")
            file.write(f"University: {university_name.title()}\n")
            file.write(f"City: {city.title()}\n")
            file.write(f"Age: {age}\n")
            file.write(f"Hobby: {hobby.title()}\n")
            file.write("---------------------------\n")

        print(f"\n✅ Profile successfully saved to '{file_name}' in the current folder.")
    except Exception as e:
        print(f"\n❌ An error occurred while saving the file: {e}")

else:
    print("\nProfile not saved. Thank you for using the app!")

# ========================================
# End of Program
# ========================================
