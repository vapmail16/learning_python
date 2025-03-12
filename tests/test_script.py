import sys
import os

# Manually add `src/` to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# Import without `src.`
from week_1_script import sum_result, difference_result, product_result, num, i, text  # ✅ Corrected import

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

assert num > 0 # ✅ Should pass for positive numbers

assert list(range(1, 11)) == [1,2,3,4,5,6,7,8,9,10]  # ✅ Ensure correct range

assert text == "Test"  # ✅ Ensure correct value of text for testing 



# Run the test using the following command:
# pytest tests/test_script.py
#
# The output should look like this:
# ============================= test session starts ==============================      
# platform linux -- Python 3.8.5, pytest-6.2.2, pluggy-0.13.1
# rootdir: /home/runner/Python-Programming-101
# collected 3 items
#
# tests/test_script.py ...                                                  [100%]
#
# ============================== 3 passed in 0.01s =============================== 
 
