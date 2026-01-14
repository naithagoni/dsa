# Find the Reverse of a Number
# Time: O(d)
# Space: O(d)
def reverseDigit(n: int) -> int:
    revNumber = []
    while n != 0:
        digit = n % 10
        revNumber.append(str(digit))
        n //= 10
    return int("".join(revNumber))


# Time: O(d)
# Space: O(1)
def reverseDigitFormula(n: int) -> int:
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = (reverse * 10) + digit
        n //= 10
    return reverse


# Time: O(d)
# Space: O(d)
def reverseDigitFor(n: int) -> int:
    rev = ""

    for ch in str(n):
        rev = ch + rev   # prepend
    return int(rev)

print("Reverse a digit: ", reverseDigitFormula(1234))


# Time: O(d)
# Space: O(d) - string copy + reversed string
num = 1234
print("Reverse a digit simple: ", str(num)[::-1])




