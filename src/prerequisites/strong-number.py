# A strong number is a special type of number in mathematics where the sum of the factorials of its digits is equal to the number itself. For example, the number 145 is considered a strong number because:1! + 4! + 5! = 1 + 24 + 120 = 145.
# Strong numbers are relatively rare, and they are often studied in number theory.
# The concept is similar to that of Armstrong numbers, but instead of raising digits to a power, we take the factorial of each digit.
# The known strong numbers are 1, 2, 145, and 40585.

# FASTEST - Precompute is faster because it avoids doing the same work again and again.
# Instead of recalculating factorials repeatedly, you look them up in O(1) time.

# Time: O(d)
# Space: O(1)
# Precompute factorials of digits 0–9
# ----------------------------------
# WHY:
# Digits in any number are only from 0 to 9.
# Instead of recalculating factorial(digit) again and again,
# we compute all possible digit factorials ONCE.
# This turns repeated computation into constant-time lookup.

fact = [1] * 10 # O(1) space: fixed size array (always 10 elements)
for i in range(2, 10):
  fact[i] = fact[i - 1] * i
  # WHY faster:
  # - This loop runs only 8 times (2 → 9)
  # - Cost is paid once, not per digit or per input

def isStrongNumber(n: int) -> bool:
    total = 0 # Constant space
    temp = n # Copy to avoid modifying original n
    while temp > 0:
        total += fact[temp % 10] # Extract last digit → O(1) lookup
        # WHY this is the key optimization:
        # - Array access is O(1)
        # - No loops
        # - No recursion
        # - No repeated multiplication
        #
        # Compared to:
        # factorial(digit) → multiple multiplications every time
        temp //= 10 # Remove last digit → O(1)
    return total == n

print(isStrongNumber(145))  # True



def factorialDigit(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
# Time: O(d)
# Space: O(1)
def is_strong_number(num):
    original_num = num
    sum_of_factorials = 0
    while num > 0: # Process each digit of the number
        digit = num % 10 # Get the last digit
        sum_of_factorials += factorialDigit(digit)
        num //= 10 # Remove the last digit
    return sum_of_factorials == original_num
print(is_strong_number(145)) # True


# Using Simple iteration
# Time: O(d)
# Space: O(1)
def isStrongNumberSimple(n: int) -> bool:
    total = 0
    for ch in str(n):
        val = int(ch)
        fact = 1
        for i in range(2, val + 1):
            fact *= i
        total += fact
    return total == n
print("Simple: ", isStrongNumberSimple(145))


# Refactored iterative code
def factorial(n: int):
  if n == 0 or n == 1: return 1
  fact = 1
  for i in range(2, n + 1):
      fact *= i
  return fact
# Time: O(d)
# Space: O(1)
def isStrongNumberIter(n: int) -> bool:
    total = 0
    for ch in str(n):
        total += factorial(int(ch))
    return total == n

print(isStrongNumberIter(145))


# Using Recursion
def factorialRec(n: int):
    if n == 0 or n == 1: return 1
    return n * factorialRec(n - 1)
# Time: O(d)
# Space: O(d)
def isStrongNumberRec(n: int) -> bool:
    total = 0
    for ch in str(n):
        total += factorialRec(int(ch))
    return total == n

print(isStrongNumberRec(145))