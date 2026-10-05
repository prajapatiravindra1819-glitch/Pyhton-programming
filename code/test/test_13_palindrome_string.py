import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("13_palindrome_string")
is_palindrome_string = _module.is_palindrome_string
assert is_palindrome_string("madam") is True
assert is_palindrome_string("Racecar") is True
assert is_palindrome_string("A man, a plan, a canal: Panama") is True
assert is_palindrome_string("") is True
assert is_palindrome_string("hello") is False
assert is_palindrome_string("ab") is False
print("All test cases passed.")
