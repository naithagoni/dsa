# Find the Power of a Number

import math

# Time: O(1)
# Space: O(1)
base = 2
exp = 3
res1 = base**exp
print("Power of a number using operator: ", res1)


# Time: O(1)
# Space: O(1)
num1 = 2
num2 = 3
res2 = int(math.pow(num1, num2))
print("Power of a number using pow function: ", res2)


# Time: O(log n)
# Key line that decides the time complexity 🔑
# exp //= 2 or >> 1

# This line cuts the problem size in HALF every loop.

# That single line is why the time is O(log n).

# General rule (MEMORIZE THIS)
# If a loop divides the input by a constant factor (2, 3, etc.) each iteration,
# the time complexity is O(log n).

# Visual intuition 🧠
# O(n) loop
# 16 → 15 → 14 → ... → 1   (16 steps)
# O(log n) loop
# 16 → 8 → 4 → 2 → 1       (5 steps)

# Space: O(1)
def powerOptimized(base: int, exp: int) -> int:
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result

print("Optimized Power (Binary Exponentiation): ", powerOptimized(2, 10))  # 1024