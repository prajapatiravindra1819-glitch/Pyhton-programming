def is_palindrome_number(n):
    """Return True if n reads the same forwards and backwards."""
    if n < 0:
        return False
    original = n
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return original == reversed_num
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Palindrome" if is_palindrome_number(n) else "Not palindrome")