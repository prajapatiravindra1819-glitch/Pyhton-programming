import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("12_reverse_string")
reverse_string = _module.reverse_string
assert reverse_string("hello") == "olleh"
assert reverse_string("a") == "a"
assert reverse_string("") == ""
assert reverse_string("ab cd") == "dc ba"
assert reverse_string("12345") == "54321"
print("All test cases passed.")
