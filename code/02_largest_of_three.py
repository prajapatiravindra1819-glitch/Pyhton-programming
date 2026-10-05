def largest_of_three(a, b, c):
    """Return the largest of three numbers."""
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    return c
if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    c = float(input("Enter third number: "))
    print("Largest:", largest_of_three(a, b, c))