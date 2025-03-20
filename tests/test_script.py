import sys
import os
import pytest

# Manually add `src/` to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# Import without `src.`
from week_1_script import sum_result, difference_result, product_result, num, i, text, movies, colour, person, multiply, is_even, get_student_info  # ✅ Corrected import

# ✅ Task 1: Testing Mathematical Operations

# Test the sum, difference, and product results

def test_sum():
    assert sum_result == 13

def test_fail_sum():
    assert sum_result != 10

def test_difference():
    assert difference_result == -3

def test_fail_diff():
    assert difference_result != -2

def test_product():
    assert product_result == 40

def test_fail_product():
    assert product_result != 20 

# ✅ Task 2: Ensure number is positive

def test_positive_number():
    assert num > 0 # ✅ Should pass for positive numbers


# ✅ Task 3: Ensure list has correct values
def test_movies():
    assert movies[0] == "The Shawshank Redemption"


def test_colours():  
    assert colour[0] == "Red"

# ✅ Task 4: Ensure dictionary values are correct
def test_student_data():
    assert person["grade"] == "B"


# ✅ Task 5: Ensure while loop assigns "Test" in test mode
def test_while_loop():
    assert text == "Test"  # ✅ Ensure correct value of text for testing


# ✅ Task 6: Ensure `for` loop range is correct
def test_for_loop():
    assert list(range(1, 11)) == [1,2,3,4,5,6,7,8,9,10]  # ✅ Ensure correct range



# ✅ Task 7: Ensure `multiply` function is correct

def test_multiply():
    assert multiply(5,8) == 40


# ✅ Task 8: Ensure is_even(n) that returns True if n is even, else False.

def test_iseven():
    assert is_even(2) == True
    assert is_even(3) == False 


# ✅ Task 9: Ensure get_student_info(name, age, course="Python") returns a formatted string.
def test_get_student_info():
    assert get_student_info("TestUser", 25) == "Hello TestUser, You are 25 years old and you are learning Python Programming."
    

# ✅ Task 10: Ensure file operations work correctly

# ✅ Setup: Create sample.txt if it doesn't exist

def setup_file():
    print("🔹 Creating sample.txt before running tests...")
    with open("sample.txt", "w") as file:
        file.write("Hello, this is my first file in Python!\n")

setup_file()


#✅ Does the file exist after writing?

def test_file_exists():
    assert os.path.exists("sample.txt") # ✅ File should exist after writing   



#✅ Is the file content correct after writing?

def test_file_reading():
    with open("sample.txt", "r") as file:
        content = file.read()
        assert "Hello, this is my first file in Python!" in content # ✅ Check expected text


#✅ Does appending work correctly (without erasing content)?

def test_file_append():
    with open("sample.txt", "a") as file:
        file.write("This is the fourth line in the file.\n")
    
    with open("sample.txt", "r") as file:
         content = file.read()
    
    assert "This is the fourth line in the file." in content # ✅ Check if new content exists

#✅ Does deleting the file work properly?

def test_file_delete():
    if os.path.exists("sample.txt"):
        os.remove("sample.txt")
        assert not os.path.exists("sample.txt") # ✅ Check if file is deleted
    else:
        assert True

#✅ Test Handling of Missing Files

def test_missing_file():
    filename = "sample.txt"

    # ✅ Ensure the file is deleted before testing
    if os.path.exists(filename):
        os.remove(filename)

    # ✅ Now test if FileNotFoundError is raised
    try:
        with open(filename, "r") as file:
            content = file.read()
    except FileNotFoundError:
        assert True  # ✅ Pass because file is missing
    else:
        assert False  # ❌ Fail if no exception was raised



        

