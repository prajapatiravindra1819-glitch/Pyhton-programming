def check_even_odd(number):
    """Return 'Even' if number is even, otherwise 'Odd'."""
    if number % 2 == 0:
        return "Even"
    return "Odd"
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(check_even_odd(n))