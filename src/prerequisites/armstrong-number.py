# Time: O(d)
# Space: O(1)
def isArmstrong(n: int) -> bool:
    l = len(str(n))
    temp = n
    total = 0
    for i in range(l):
        digit = temp % 10
        total += digit**l
        temp //= 10
    return n == total

print(isArmstrong(1634))



# Time: O(d)
# Space: O(d)
def isArmstrongNumber(n: int) -> bool:
    s = str(n)
    l = len(s)
    total = 0
    for ch in s:
        total += int(ch) ** l
    return n == total

print(isArmstrongNumber(1634))


# Time: O(d)
# Space: O(d) - Recursive call stack grows once per digit
def isArmstrongRec(n: int, l: int):
    if n == 0:
        return 0
    return (n % 10) ** l + isArmstrongRec(n // 10, l)
n = 1634
print(n == isArmstrongRec(n, len(str(n))))