def find_missing_number(numbers):
    """Given a list of numbers from 1..n with one missing, return the missing one."""
    n = len(numbers) + 1
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(numbers)
if __name__ == "__main__":
    nums = [int(x) for x in input("Enter numbers (1..n, one missing): ").split()]
    print(find_missing_number(nums))