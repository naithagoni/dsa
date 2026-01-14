# Keep summing digits until a single digit remains (Digital root)
# Time: O(1)
# Space: O(1)
def digitalRoot(n: int) -> int:
    if n == 0:
        return 0
    return 1 + (n - 1) % 9

# Example: 987 → 9+8+7 = 24 → 2+4 = 6


# Time: O(d) - Digits processed only a few times
# Space: O(1) - Variables used: n, total, No arrays, no recursion
def digitalRoot(n: int) -> int:
    n = abs(n)

    while n >= 10:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        n = total

    return n


print("summing digits: ", digitalRoot(1234))

