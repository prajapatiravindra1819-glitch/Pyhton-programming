def char_frequency(text):
    """Return a dictionary with the count of every character in text."""
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
if __name__ == "__main__":
    s = input("Enter a string: ")
    print(char_frequency(s))