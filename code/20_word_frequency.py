import string
def word_frequency(sentence):
    """Return a dictionary with the count of each word (case-insensitive)."""
    freq = {}
    for word in sentence.lower().split():
        word = word.strip(string.punctuation)
        if word:
            freq[word] = freq.get(word, 0) + 1
    return freq
if __name__ == "__main__":
    s = input("Enter a sentence: ")
    print(word_frequency(s))