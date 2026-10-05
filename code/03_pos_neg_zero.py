def check_number(number):
    """Return 'Positive', 'Negative' or 'Zero'."""
    if number > 0:
        return "Positive"
    if number < 0:
        return "Negative"
    return "Zero"
if __name__ == "__main__":
    n = float(input("Enter a number: "))
    print(check_number(n))