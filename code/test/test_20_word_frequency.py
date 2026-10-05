import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("20_word_frequency")
word_frequency = _module.word_frequency
assert word_frequency("the cat and the hat") == {"the": 2, "cat": 1, "and": 1, "hat": 1}
assert word_frequency("") == {}
assert word_frequency("Hello hello HELLO") == {"hello": 3}
assert word_frequency("Hi, there! Hi.") == {"hi": 2, "there": 1}
assert word_frequency("one") == {"one": 1}
print("All test cases passed.")