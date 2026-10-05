def primes_in_range(start, end):
    """Return a list of prime numbers between start and end (inclusive)."""
    primes = []
    for n in range(max(start, 2), end + 1):
        is_prime = True
        i = 2
        while i * i <= n:
            if n % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            primes.append(n)
    return primes
if __name__ == "__main__":
    start = int(input("Start: "))
    end = int(input("End: "))
    print(primes_in_range(start, end))