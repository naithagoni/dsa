# Find the sum of the Digits of a Number
# Time: O(d) where d = number of digits
# Space: O(d) (string conversion uses extra memory)
def sumOfDigits(n: int) -> int:
    total = 0
    for i in str(n):
        total += int(i)
    return total


# Time: O(d)
# Space: O(d) (recursive call stack)
def sumOfDigitsRec(n: int):
    if n == 0:
        return 0
    return (n % 10) + sumOfDigitsRec(n // 10)


# Time: O(d)
# Space: O(1)
def sumOfDigitsWhile(n: int) -> int:
    # Edge Case: Negative numbers
    n = abs(n)

    if n == 0:
        return n
    total = 0
    while n != 0:
        # Extracts last digit using n % 10
        digit = n % 10
        total += digit
        # Removes last digit using n // 10
        n = n // 10
    return total



print("sumOfDigits: ", sumOfDigits(123))
print("sumOfDigitsRec: ", sumOfDigitsRec(12345))
print("sumOfDigitsWhile: ", sumOfDigitsWhile(1234))