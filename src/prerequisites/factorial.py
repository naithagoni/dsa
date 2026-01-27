# A factorial is a mathematical operation that multiplies a given positive integer by all the positive integers less than it. It is denoted by an exclamation mark (!). For example, the factorial of 5 (written as 5!) is calculated as follows:
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# The factorial of 0 is defined to be 1 (0! = 1). Factorials are commonly used in permutations, combinations, and other areas of mathematics and computer science.
# 0! = 1, 1! = 1

# Time: O(n)
# Space: O(1)
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print("Factorial:", factorial(5))  # Output: 120

# Time: O(n)
# Space: O(n)
def factorialRec(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorialRec(n - 1)
print("Factorial (recursive):", factorialRec(7))  # Output: 5040