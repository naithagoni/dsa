# Find the Factors of a Number

# Time: O(n)
# Space: O(1)
def factorsOfNumber(n: int):
    if n <= 0: return 0
    it = 1
    while it <= n:
        if n % it == 0:
            print(it, end=" ")
        it += 1

print(factorsOfNumber(10))

# Better Approach
# Time: O(√n)
# Space: O(1)
def optimizedFactorsOfNumber(n: int):
    if n <= 0: return 0
    it = 1
    while it * it <= n:
        if n % it == 0:
            print(it, end=" ")
            if it != n // it:
                print(n // it, end=" ")
        it += 1

print(optimizedFactorsOfNumber(10))
# Explanation:
# To find factors of a number n, we only need to check up to √n.
# If i is a factor of n, then n/i is also a factor.
# This reduces the number of iterations significantly, leading to O(√n) time complexity.

# Note:
# The factors may not be printed in sorted order using the optimized method.
# For example, for n = 36, the output will be: 1 36 2 18 3 12 4 9 6
# To print factors in sorted order, we can store them in a list and sort them before printing.
# However, that would increase space complexity to O(k), where k is the number of factors
# and time complexity to O(k log k) due to sorting.
# If sorted order is not a requirement, the optimized method is more efficient.
print(optimizedFactorsOfNumber(36))
# For n = 36, the output will be: 1 36 2 18 3 12 4 9 6
# Factors of 36 are: 1, 2, 3, 4, 6, 9, 12, 18, 36
# The optimized method runs in O(√n) time and O(1) space.
# In contrast, the naive method runs in O(n) time and O(1) space.
# Thus, the optimized method is preferred for finding factors of a number.
# Note: The optimized method does not guarantee sorted order of factors.
