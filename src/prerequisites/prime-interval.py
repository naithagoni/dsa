# Find all prime numbers from 2 to n - Sieve of Eratosthenes (Optimized approach)
# Time: O(n²)
# Spce: O(1)
def primeNumbers(low: int, high: int):
    if high < 2:
        return []

    numbers = []

    for i in range(max(2, low), high + 1):
        isPrime = True

        for j in range(2, i):
            if i % j == 0:
                isPrime = False
                break

        if isPrime:
            numbers.append(i)

    return numbers

print("primeNumbers: ", primeNumbers(2, 10))


# Time: O(n√n)
# Spce: O(1)
def primeNumbersOpt(low: int, high: int):
    if high < 2:
        return []

    numbers = []

    for i in range(max(2, low), high + 1):
        isPrime = True

        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                isPrime = False
                break

        if isPrime:
            numbers.append(i)

    return numbers

print("primeNumbersOpt: ", primeNumbersOpt(2, 10))


# Time: O(n log log n)
# Spce: O(1)
def primeNumbsUsingSieve(a: int, b: int):
    if b < 2:
        return []

    # Step 1: Create a list for primes up to b
    # Create a list of numbers from 2 to n and mark all numbers as prime initially
    isPrime = [True] * (b + 1)
    isPrime[0] = isPrime[1] = False

    # Step 2: Sieve - Move to next unmarked number and repeat until √n
    for p in range(2, int(b**0.5) + 1):
        if isPrime[p]:
            # Mark all multiples of p (except p) as non-prime - p*p to b step p
            for multiples in range(p*p, b + 1, p):
                isPrime[multiples] = False
    # Step 2: Collect primes in the range [a, b]
    return [i for i in range(max(2, a), b +1) if isPrime[i]]