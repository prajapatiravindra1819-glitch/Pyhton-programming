import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("02_largest_of_three")
largest_of_three = _module.largest_of_three
assert largest_of_three(1, 2, 3) == 3
assert largest_of_three(9, 2, 3) == 9
assert largest_of_three(1, 8, 3) == 8
assert largest_of_three(5, 5, 5) == 5
assert largest_of_three(-1, -5, -3) == -1
assert largest_of_three(7, 7, 2) == 7
print("All test cases passed.")
