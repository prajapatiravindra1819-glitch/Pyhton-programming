def second_largest(numbers):
    """Return the second largest distinct number, or None if it does not exist."""
    largest = None
    second = None
    for x in numbers:
        if largest is None or x > largest:
            second = largest
            largest = x
        elif x != largest and (second is None or x > second):
            second = x
    return second
if __name__ == "__main__":
    nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    print(second_largest(nums))