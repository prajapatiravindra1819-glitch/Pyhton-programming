import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("11_vowels_consonants")
count_vowels_consonants = _module.count_vowels_consonants
assert count_vowels_consonants("hello") == (2, 3)
assert count_vowels_consonants("AEIOU") == (5, 0)
assert count_vowels_consonants("xyz") == (0, 3)
assert count_vowels_consonants("") == (0, 0)
assert count_vowels_consonants("Hello, World! 123") == (3, 7)
print("All test cases passed.")
