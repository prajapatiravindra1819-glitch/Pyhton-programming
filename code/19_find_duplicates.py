def find_duplicates(items):
    """Return the elements that appear more than once (in order of first appearance)."""
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return [item for item, count in counts.items() if count > 1]
if __name__ == "__main__":
    nums = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
    print(find_duplicates(nums))