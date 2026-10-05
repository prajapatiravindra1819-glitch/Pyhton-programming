import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("15_second_largest")
second_largest = _module.second_largest
assert second_largest([1, 2, 3, 4]) == 3
assert second_largest([4, 3, 2, 1]) == 3
assert second_largest([10, 10, 9]) == 9
assert second_largest([5, 5, 5]) is None
assert second_largest([7]) is None
assert second_largest([]) is None
assert second_largest([-1, -2, -3]) == -2
print("All test cases passed.")
