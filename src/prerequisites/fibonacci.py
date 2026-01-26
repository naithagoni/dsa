# Explain Fibonacci Series:
# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. The sequence typically begins as follows:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
# In mathematical terms, the Fibonacci sequence can be defined using the following recurrence relation:
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) for n > 1



# Find the Fibonacci Series up to Nth Term
# Time: O(n)
# Space: O(n) (storing series)
def fibonacci(n: int):
    if n <= 0:
        return []

    if n == 1:
        return [0]

    series = [0, 1]

    for i in range(2, n):
        series.append(series[i - 1] + series[i - 2])
    return series

print("Fibonacci up to Nth Term:", fibonacci(4))


# Time: O(n)
# Space: O(1) ⭐
def fibonacciOptimized(n: int):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        # Old-school way
        # temp = a # store old a
        # a = b # assign old b to a
        # b = temp + b # assign old a + old b to b

        # Python shorthand
        a, b = b, a + b
        # a, b = b, a + b
        # Python does the following internally:
        # 1️⃣ Evaluates the right-hand side first: rhs = (b, a + b) - Python takes old values of "a" and "b" and Creates a tuple with two elements: (old b, old a + old b)
        # 2️⃣ Assigns both values simultaneously: - a, b = rhs
        # - "a" gets first element (old b)
        # - "b" gets second element (old a + old b)
fibonacciOptimized(4)
print("")


# Time: O(2ⁿ) (exponential)
# 👉 Same subproblems are solved again and again
#  - f(3) → computed 2 times
# - f(2) → computed 3 times
# - f(1) → computed 5 times
# This is called overlapping subproblems.

# Space: O(n)
def fibonacciRecSingle(n: int):
    if n == 0: return 0
    if n == 1: return 1
    return fibonacciRecSingle(n - 1) + fibonacciRecSingle(n - 2)

n = 4
for i in range(n):
    print(fibonacciRecSingle(i), end=" ")
print("")



# Dynamic Programming
# Time: O(n)
# Space: O(n) (recursion stack + memo dictionary)
def fibonacciTopDown(n: int, memo={}):
  if n in memo: return memo[n]
  if n == 0: memo[0] = 0
  elif n == 1: memo[1] = 1
  else: memo[n] = fibonacciTopDown(n - 1, memo) + fibonacciTopDown(n - 2, memo)
  return memo[n]

num = 4
for i in range(num):
    print(fibonacciTopDown(i), end=" ")

print("")



# Time: O(log n)
# Space: O(log n)
# Bonus: Fast Doubling
# Explian Fast Doubling Method:
#  - The Fast Doubling method is an efficient algorithm to compute Fibonacci numbers using matrix exponentiation properties. It leverages the relationships between Fibonacci numbers to compute them in logarithmic time.
#  - The key formulas used in this method are:
#    F(2k) = F(k) * [2*F(k+1) - F(k)]
#    F(2k + 1) = F(k+1)^2 + F(k)^2
#  - By recursively applying these formulas, we can compute Fibonacci numbers in O(log n) time, which is significantly faster than the naive recursive or iterative approaches.
#  - This method is particularly useful for large Fibonacci numbers where efficiency is crucial.
#  - Here's how the Fast Doubling method can be implemented in Python:
# def fibonacciFastDoubling(n: int):
#     if n == 0:
#         return (0, 1)
#     else:
#         a, b = fibonacciFastDoubling(n // 2)
#         c = a * (2 * b - a)
#         d = a * a + b * b
#         if n % 2 == 0:
#             return (c, d)
#         else:
#             return (d, c + d)
# print("Fibonacci Fast Doubling:")
# for i in range(4):
#     print(fibonacciFastDoubling(i)[0], end=" ")
# print("")




# Find the Nth Term of a Fibonacci Series (single value)
def fibonacciNTerm(n: int):
    if n < 2: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
print("Fibonacci Nth Term:", fibonacciNTerm(4))
print("")

# Time: O(n)
# Space: O(n)
def fibonacciBottomUp(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Time: O(n)
# Space: O(n)
def fibonacciBottomUpTwo(n):
    if n == 0: return 0
    if n == 1: return 1

    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]

print("Bottom-Up One:", fibonacciBottomUp(4))
print("Bottom-Up Two:", fibonacciBottomUpTwo(4))

