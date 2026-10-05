import os
import sys
import importlib
# Make the Code/ folder importable (file names start with digits, so use importlib)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Code"))
_module = importlib.import_module("07_primes_in_range")
primes_in_range = _module.primes_in_range
assert primes_in_range(1, 10) == [2, 3, 5, 7]
assert primes_in_range(10, 20) == [11, 13, 17, 19]
assert primes_in_range(2, 2) == [2]
assert primes_in_range(14, 16) == []
assert primes_in_range(-5, 3) == [2, 3]
assert primes_in_range(10, 5) == []
print("All test cases passed.")
