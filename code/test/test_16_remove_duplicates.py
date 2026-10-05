import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("16_remove_duplicates")
remove_duplicates = _module.remove_duplicates
assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
assert remove_duplicates([]) == []
assert remove_duplicates([5, 5, 5]) == [5]
assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
print("All test cases passed.")
