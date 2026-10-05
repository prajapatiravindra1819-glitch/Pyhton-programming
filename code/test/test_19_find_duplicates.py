import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("19_find_duplicates")
find_duplicates = _module.find_duplicates
assert find_duplicates([1, 2, 2, 3, 3, 3]) == [2, 3]
assert find_duplicates([1, 2, 3]) == []
assert find_duplicates([]) == []
assert find_duplicates([4, 4, 4, 4]) == [4]
assert find_duplicates(["a", "b", "a"]) == ["a"]
print("All test cases passed.")
