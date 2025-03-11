import sys
import os

# Add src/ to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


from src.week_1_script import sum_result, difference_result, product_result

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
 
