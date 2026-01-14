# Check Whether a Number is a Prime
def isPrime(n: int):
    # Step 1: 0 and 1 Prime numbers కాదు
    if n < 2:
        return False

    # Step 2: 2 Prime
    if n == 2:
        return True

    # Step 3: Even numbers Prime కాదు
    if n % 2 == 0:
        return False

    # Step 4: √n వరకు check చేయాలి
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2   # only odd numbers

    return True



# Time: O(√n)  -->  Checks only odd numbers, Total iterations ≈ √n / 2
# Space: O(1)  -->  Uses only a few variables (n, i), No arrays, no extra memory
def isPrime(n: int) -> bool:
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # Checking up to n is unnecessary
    # We only need to check up to √n
    # Anything beyond √n cannot be a new factor
    for i in range(3, int(n**0.5), 2):
        # Loop runs only up to √n
        # Loop checks only odd numbers
        if n % i == 0:
            return False
    return True

print("isPrime: ", isPrime(17))



# Optimized Code (6k ± 1)
# Time: O(√n)  -->  Checks only odd numbers, Total iterations ≈ √n / 2
# Space: O(1)  -->  Uses only a few variables (n, i), No arrays, no extra memory
def isPrime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True

    # eliminate multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    # check only 6k ± 1 values
    for i in range(5, int(n**0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True
