def reverse_number(n):
    """Return the digits of n reversed (sign is kept)."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10
    return sign * reversed_num
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(reverse_number(n))