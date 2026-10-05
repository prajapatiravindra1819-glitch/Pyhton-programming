import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("18_missing_number")
find_missing_number = _module.find_missing_number
assert find_missing_number([1, 2, 4, 5]) == 3
assert find_missing_number([2, 3, 4, 5]) == 1
assert find_missing_number([1, 2, 3, 4]) == 5
assert find_missing_number([1]) == 2
assert find_missing_number([3, 1, 5, 2]) == 4
print("All test cases passed.")
