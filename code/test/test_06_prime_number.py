import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("06_prime_number")
is_prime = _module.is_prime
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(13) is True
assert is_prime(97) is True
assert is_prime(1) is False
assert is_prime(0) is False
assert is_prime(-7) is False
assert is_prime(9) is False
assert is_prime(100) is False
print("All test cases passed.")
