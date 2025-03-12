import os # added so that Github actions can run the script with test values 

# Check if running in Github Actions
is_ci = os.getenv("CI") == "true"
is_test = any(key.startswith("PYTEST_") for key in os.environ)  # ✅ Better way to detect pytest
print(f"Is Test: {is_test}")
print(f"Is CI: {is_ci}")

'''
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


age = input("Enter Your Age: ") 

if int(age) < 21:
    print("You cant vote")
else:
    print("You can vote")   

for i in range(5): # Loops from 0 to 4
    print("Iterations:", i)    

for i in range(1,6): # Loops from 1 to 5
    print("Iterations:", i)    

count = 1 
while count <5:
    print("Count:",count)
    count += 1
''' 

#1️⃣ Task 1: Write a program that checks whether a number is positive, negative, or zero.


try:
   
   if not (is_ci or is_test):
        num = int(input("Enter a number: "))
   else: 
        num = 2

   if num > 0:
        print("Number is Positive")
   elif num < 0:
        print("Number is Negative")
   elif num == 0:
        print("Number is Zero")

except ValueError:
    print("Please enter a valid number")


#2️⃣ Task 2: Create a for loop that prints numbers from 1 to 10.

for i in range(1,11):
    print(i)

#3️⃣ Task 3: Create a while loop that keeps asking the user for input until they type "exit".

if not (is_ci or is_test):
    text = ""
    while text != "exit":
     text = input("Enter a text: ")
     print(text) 
else:
    text = "Test"

if not (is_ci or is_test):
    while True:
        text = input("Enter a text(type exit to stop): ")
        if text.lower() == "exit": 
            break
        print(text)
else:
    text = "Test"




# This is Day 4 Script -



