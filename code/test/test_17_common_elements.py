import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("17_common_elements")
common_elements = _module.common_elements
assert common_elements([1, 2, 3, 4], [3, 4, 5]) == [3, 4]
assert common_elements([1, 2], [3, 4]) == []
assert common_elements([], [1, 2]) == []
assert common_elements([1, 1, 2], [1, 2, 2]) == [1, 2]
assert common_elements(["a", "b"], ["b", "c"]) == ["b"]
print("All test cases passed.")
