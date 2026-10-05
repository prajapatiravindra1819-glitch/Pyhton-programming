import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("04_factorial")
factorial = _module.factorial
assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(10) == 3628800
try:
    factorial(-1)
    assert False, "Expected ValueError for negative input"
except ValueError:
    pass
print("All test cases passed.")
