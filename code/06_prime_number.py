def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Prime" if is_prime(n) else "Not prime")