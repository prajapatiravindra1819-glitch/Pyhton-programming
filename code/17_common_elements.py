def common_elements(list1, list2):
    """Return the elements present in both lists (no repeats, order of list1)."""
    set2 = set(list2)
    result = []
    for item in list1:
        if item in set2 and item not in result:
            result.append(item)
    return result
if __name__ == "__main__":
    a = [int(x) for x in input("First list: ").split()]
    b = [int(x) for x in input("Second list: ").split()]
    print(common_elements(a, b))