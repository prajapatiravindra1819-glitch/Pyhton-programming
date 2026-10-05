import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("09_palindrome_number")
is_palindrome_number = _module.is_palindrome_number
assert is_palindrome_number(121) is True
assert is_palindrome_number(1331) is True
assert is_palindrome_number(7) is True
assert is_palindrome_number(0) is True
assert is_palindrome_number(123) is False
assert is_palindrome_number(10) is False
assert is_palindrome_number(-121) is False
print("All test cases passed.")
