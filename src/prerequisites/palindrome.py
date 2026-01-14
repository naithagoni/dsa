# Strings
# Time: O(n)
# Space: O(n) - s[::-1] creates a new string copy of length n.
def isPalindrome(s: str) -> bool:
    return s == s[::-1]

# Time: O(n)
# Space: O(n) - "reversed(s)"" → iterator (O(1)), "".join(...) → allocates a new string of size n
def isPalindromeReversed_1(s: str) -> bool:
    reverse = "".join(reversed(s))
    return True if s == reverse else False

# Time: O(n²) - Strings are immutable, Each "reverse += ch" copies the entire string, Cost: 1 + 2 + 3 + ... + n → O(n²)
# Space: O(n)
def isPalindromeReversed_2(s: str) -> bool:
    reverse = ''
    for ch in reversed(s):
        reverse += ch
    return True if s == reverse else False

# Time: O(n²) - Strings are immutable, Each "reverse += s[i]" copies the entire string, Cost: 1 + 2 + 3 + ... + n → O(n²)
# Space: O(n)
def isPalindromeIndexed(s: str) -> bool:
    reverse = ''
    for i in range(len(s) - 1, -1, -1):
        reverse += s[i]
    return True if s == reverse else False



# Time: O(n)
# Space: O(1)
def isPalindromeTwoPointer(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        print("Left: ", left)
        print("Right: ", right)
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True



print(isPalindrome("1221"))
print(isPalindromeReversed_1("1221"))
print(isPalindromeReversed_2("1221"))
print(isPalindromeIndexed("1221"))
print(isPalindromeTwoPointer("1221"))



# Numbers
# Time: O(d)
# Space: O(1)
def isPalindromeNumber(n: int) -> bool:
    reverse = 0
    temp = n
    while temp > 0: # temp != 0
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp =  temp // 10
    return True if n == reverse else False


# Time: O(d)
# Space: O(d) - str(n) allocates a string, "slicing" allocates another string
def isPalindromeNumSlice(n: int) -> bool:
    reverse = int(str(n)[::-1])
    return True if n == reverse else False

print(isPalindromeNumber(1221))
print(isPalindromeNumSlice(1221))




