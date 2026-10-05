import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("05_fibonacci_series")
fibonacci_series = _module.fibonacci_series
assert fibonacci_series(0) == []
assert fibonacci_series(1) == [0]
assert fibonacci_series(2) == [0, 1]
assert fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
assert fibonacci_series(10)[-1] == 34
print("All test cases passed.")
