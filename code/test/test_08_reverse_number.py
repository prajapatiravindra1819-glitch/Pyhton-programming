import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("08_reverse_number")
reverse_number = _module.reverse_number
assert reverse_number(123) == 321
assert reverse_number(5) == 5
assert reverse_number(0) == 0
assert reverse_number(1200) == 21
assert reverse_number(-456) == -654
print("All test cases passed.")
