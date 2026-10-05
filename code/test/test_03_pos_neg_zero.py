import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("03_pos_neg_zero")
check_number = _module.check_number
assert check_number(5) == "Positive"
assert check_number(-5) == "Negative"
assert check_number(0) == "Zero"
assert check_number(0.5) == "Positive"
assert check_number(-0.1) == "Negative"
print("All test cases passed.")
