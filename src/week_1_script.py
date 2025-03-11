import os # added so that Github actions can run the script with test values 

# Check if running in Github Actions
is_ci = os.getenv("CI") == "true"
is_test = any(key.startswith("PYTEST_") for key in os.environ)  # ✅ Better way to detect pytest
print(f"Is Test: {is_test}")
print(f"Is CI: {is_ci}")


# This is Week 1 script. 

# This is Day 1 Script - It prints "Hello World!" to the console.
print("Hello World!")
print("My Name is Vikkas Arun Pareek")
print("I am learning Python Programming Language")
print("80-20 rule of learning, focus on essentions")
print("My Favourite Quote is: Rise and Shine")
print("Now I will show you ASCII Art")
print("   *   ")
print("  ***  ")
print(" ***** ")
print("*******")


# This is Day 2 Script - 

name = "Vikkas Arun Pareek"
age = 40
height = 5.11
weight = 85
is_married = True

print("Name: ", name)

if not (is_ci or is_test):
    name = input("Enter Your Name")
    print("Hello " +name+ "!")
else:
    name = "TestUser"
     
print("hello " +name+ "!, your age is ", age, 
      "years old, your hieght is ", height, ""
      "and your weight is ", weight, " kgs.")

print("Are you married? ", is_married)

#Task 1 - Create a Personal Info Program
 
if not (is_ci or is_test):
    name = input("Enter Your Name: ")
    age = input("Enter Your Age: ")
    color = input("Enter Your Favourite Color: ")
else:
    name, age, color = "TestUser", "25", "Blue"


print("Hello " +name+ "! Your age is", age, 
      " and your favourite color is ", color)

print("Hello " +name+ "! Your age is " +str(age)+ 
      " and your favourite color is " +str(color)+".")

print(f"Hello {name}! Your age is {age} and your favourite colour is {color}")

#Task 2 - Create a Simple Calculator

if not (is_ci or is_test):
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))    
else:
    num1, num2 = 5,8

sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

print(f"Sum of {num1} and {num2} is {sum_result}")
print(f"Difference of {num1} and {num2} is {difference_result}")
print(f"Product of {num1} and {num2} is {product_result}")


# This is Day 3 Script -

