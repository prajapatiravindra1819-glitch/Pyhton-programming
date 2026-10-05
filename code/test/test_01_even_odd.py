import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("01_even_odd")
check_even_odd = _module.check_even_odd
assert check_even_odd(4) == "Even"
assert check_even_odd(7) == "Odd"
assert check_even_odd(0) == "Even"
assert check_even_odd(-3) == "Odd"
assert check_even_odd(-8) == "Even"
print("All test cases passed.")
