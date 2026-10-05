import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("14_char_frequency")
char_frequency = _module.char_frequency
assert char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
assert char_frequency("") == {}
assert char_frequency("aaa") == {"a": 3}
assert char_frequency("a b a") == {"a": 2, " ": 2, "b": 1}
assert char_frequency("Aa") == {"A": 1, "a": 1}
print("All test cases passed.")
