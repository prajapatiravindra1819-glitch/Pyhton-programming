def reverse_string(text):
    """Return text reversed, without using slicing."""
    result = ""
    for ch in text:
        result = ch + result
    return result
if __name__ == "__main__":
    s = input("Enter a string: ")
    print(reverse_string(s))