def remove_duplicates(items):
    """Return a new list without duplicates, keeping the original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
if __name__ == "__main__":
    nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    print(remove_duplicates(nums))