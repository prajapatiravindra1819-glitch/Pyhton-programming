import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("10_sum_of_digits")
sum_of_digits = _module.sum_of_digits
assert sum_of_digits(123) == 6
assert sum_of_digits(0) == 0
assert sum_of_digits(9) == 9
assert sum_of_digits(99999) == 45
assert sum_of_digits(-45) == 9
print("All test cases passed.")
